from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any, Callable, Dict, Optional

from unified_platform.bus import Event, EventBus
from unified_platform.registry import ModuleRegistry
from unified_platform.subscription import SubscriptionManager


ModuleHandler = Callable[[str, dict[str, Any]], dict[str, Any]]


@dataclass(frozen=True)
class ModuleExecution:
    user_id: str
    module_key: str
    started_at: datetime
    finished_at: Optional[datetime]
    status: str
    output: Optional[dict[str, Any]] = None
    error: Optional[str] = None


class ModuleRunner:
    def __init__(
        self,
        registry: ModuleRegistry,
        subscriptions: SubscriptionManager,
        bus: Optional[EventBus] = None,
    ) -> None:
        self._registry = registry
        self._subscriptions = subscriptions
        self._bus = bus
        self._handlers: Dict[str, ModuleHandler] = {}

    def register_handler(self, module_key: str, handler: ModuleHandler) -> None:
        if module_key in self._handlers:
            raise ValueError(f"Handler already registered for '{module_key}'")
        self._handlers[module_key] = handler

    def run(self, user_id: str, module_key: str, payload: dict[str, Any]) -> ModuleExecution:
        if module_key not in self._registry.all():
            raise ValueError(f"Unknown module '{module_key}'")
        if not self._subscriptions.can_access(user_id, module_key):
            self._publish(
                "module.run.denied",
                {"user_id": user_id, "module_key": module_key},
            )
            now = datetime.utcnow()
            return ModuleExecution(
                user_id=user_id,
                module_key=module_key,
                started_at=now,
                finished_at=now,
                status="denied",
            )

        handler = self._handlers.get(module_key, self._default_handler)
        started_at = datetime.utcnow()
        self._publish(
            "module.run.started",
            {"user_id": user_id, "module_key": module_key, "payload": payload},
        )
        try:
            output = handler(user_id, payload)
        except Exception as exc:  # noqa: BLE001 - surface module failure
            finished_at = datetime.utcnow()
            self._publish(
                "module.run.failed",
                {
                    "user_id": user_id,
                    "module_key": module_key,
                    "error": str(exc),
                },
            )
            return ModuleExecution(
                user_id=user_id,
                module_key=module_key,
                started_at=started_at,
                finished_at=finished_at,
                status="failed",
                error=str(exc),
            )

        finished_at = datetime.utcnow()
        self._publish(
            "module.run.completed",
            {
                "user_id": user_id,
                "module_key": module_key,
                "output": output,
            },
        )
        return ModuleExecution(
            user_id=user_id,
            module_key=module_key,
            started_at=started_at,
            finished_at=finished_at,
            status="completed",
            output=output,
        )

    def _default_handler(self, user_id: str, payload: dict[str, Any]) -> dict[str, Any]:
        return {
            "user_id": user_id,
            "message": "Module handler not implemented yet.",
            "payload": payload,
        }

    def _publish(self, name: str, payload: dict[str, Any]) -> None:
        if self._bus is None:
            return
        self._bus.publish(Event(name=name, payload=payload))
