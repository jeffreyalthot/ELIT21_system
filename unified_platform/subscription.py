from dataclasses import dataclass, field
from datetime import datetime, timedelta
from enum import Enum
from typing import Dict, Iterable, Optional, Set

from unified_platform.bus import Event, EventBus


class SubscriptionStatus(str, Enum):
    ACTIVE = "active"
    CANCELED = "canceled"
    PAST_DUE = "past_due"


@dataclass(frozen=True)
class SubscriptionPlan:
    key: str
    name: str
    monthly_price_eur: int
    module_keys: Set[str]
    trial_days: int = 0


@dataclass
class Subscription:
    user_id: str
    plan_key: str
    status: SubscriptionStatus
    started_at: datetime
    ends_at: Optional[datetime]
    module_keys: Set[str] = field(default_factory=set)

    def is_active(self, now: Optional[datetime] = None) -> bool:
        reference = now or datetime.utcnow()
        if self.status != SubscriptionStatus.ACTIVE:
            return False
        if self.ends_at is None:
            return True
        return reference <= self.ends_at

    def can_access(self, module_key: str, now: Optional[datetime] = None) -> bool:
        return self.is_active(now=now) and module_key in self.module_keys


class SubscriptionManager:
    def __init__(self, bus: Optional[EventBus] = None) -> None:
        self._plans: Dict[str, SubscriptionPlan] = {}
        self._subscriptions: Dict[str, Subscription] = {}
        self._bus = bus

    def add_plan(self, plan: SubscriptionPlan) -> None:
        if plan.key in self._plans:
            raise ValueError(f"Plan '{plan.key}' already registered")
        self._plans[plan.key] = plan

    def add_plans(self, plans: Iterable[SubscriptionPlan]) -> None:
        for plan in plans:
            self.add_plan(plan)

    def subscribe(self, user_id: str, plan_key: str) -> Subscription:
        plan = self._plans.get(plan_key)
        if plan is None:
            raise ValueError(f"Unknown plan '{plan_key}'")
        now = datetime.utcnow()
        trial_delta = timedelta(days=plan.trial_days)
        ends_at = None
        if plan.trial_days > 0:
            ends_at = now + trial_delta
        subscription = Subscription(
            user_id=user_id,
            plan_key=plan.key,
            status=SubscriptionStatus.ACTIVE,
            started_at=now,
            ends_at=ends_at,
            module_keys=set(plan.module_keys),
        )
        self._subscriptions[user_id] = subscription
        self._publish(
            "subscription.activated",
            {
                "user_id": user_id,
                "plan_key": plan.key,
                "trial_days": plan.trial_days,
            },
        )
        return subscription

    def cancel(self, user_id: str) -> None:
        subscription = self._subscriptions.get(user_id)
        if subscription is None:
            raise ValueError(f"No subscription found for '{user_id}'")
        subscription.status = SubscriptionStatus.CANCELED
        subscription.ends_at = datetime.utcnow()
        self._publish(
            "subscription.canceled",
            {"user_id": user_id, "plan_key": subscription.plan_key},
        )

    def subscription_for(self, user_id: str) -> Optional[Subscription]:
        return self._subscriptions.get(user_id)

    def can_access(self, user_id: str, module_key: str) -> bool:
        subscription = self._subscriptions.get(user_id)
        if subscription is None:
            return False
        return subscription.can_access(module_key)

    def _publish(self, name: str, payload: dict) -> None:
        if self._bus is None:
            return
        self._bus.publish(Event(name=name, payload=payload))


def build_default_plans(module_keys: Iterable[str]) -> list[SubscriptionPlan]:
    modules = set(module_keys)
    return [
        SubscriptionPlan(
            key="starter",
            name="Starter",
            monthly_price_eur=49,
            module_keys=modules,
            trial_days=7,
        ),
        SubscriptionPlan(
            key="pro",
            name="Pro",
            monthly_price_eur=99,
            module_keys=modules,
            trial_days=14,
        ),
    ]
