from unified_platform import EventBus, ModuleRegistry, load_unified_15_modules
from unified_platform.bus import Command, CommandBus, Event
from unified_platform.subscription import Subscription, SubscriptionManager, build_default_plans


def bootstrap() -> tuple[ModuleRegistry, EventBus, SubscriptionManager]:
    registry = ModuleRegistry()
    registry.register_many(load_unified_15_modules())
    bus = EventBus()
    subscriptions = SubscriptionManager(bus=bus)
    subscriptions.add_plans(
        build_default_plans(module.key for module in registry.all().values())
    )
    return registry, bus, subscriptions


def bootstrap_with_commands() -> tuple[ModuleRegistry, EventBus, SubscriptionManager, CommandBus]:
    registry, bus, subscriptions = bootstrap()
    command_bus = CommandBus()

    def handle_list_modules(command: Command) -> list[dict[str, str]]:
        category = command.payload.get("category")
        modules = registry.list_all() if category is None else registry.by_category(category)
        return [
            {
                "key": state.module.key,
                "name": state.module.name,
                "category": state.module.category,
                "enabled": str(state.enabled),
            }
            for state in modules
        ]

    def handle_publish_event(command: Command) -> None:
        event = Event(
            name=command.payload["event"],
            payload=command.payload.get("data", {}),
            metadata=command.payload.get("metadata", {}),
        )
        bus.publish(event)

    def handle_set_module_state(command: Command) -> None:
        key = command.payload["key"]
        enabled = bool(command.payload.get("enabled", True))
        if enabled:
            registry.enable(key)
        else:
            registry.disable(key)

    def handle_subscribe(command: Command) -> dict[str, object]:
        subscription = subscriptions.subscribe(
            user_id=command.payload["user_id"],
            plan_key=command.payload["plan_key"],
        )
        return _serialize_subscription(subscription)

    def handle_can_access(command: Command) -> bool:
        return subscriptions.can_access(
            user_id=command.payload["user_id"],
            module_key=command.payload["module_key"],
        )

    command_bus.register("list_modules", handle_list_modules)
    command_bus.register("publish_event", handle_publish_event)
    command_bus.register("set_module_state", handle_set_module_state)
    command_bus.register("subscribe", handle_subscribe)
    command_bus.register("can_access", handle_can_access)

    return registry, bus, subscriptions, command_bus


def _serialize_subscription(subscription: Subscription) -> dict[str, object]:
    return {
        "user_id": subscription.user_id,
        "plan_key": subscription.plan_key,
        "status": subscription.status.value,
        "started_at": subscription.started_at.isoformat(),
        "ends_at": subscription.ends_at.isoformat() if subscription.ends_at else None,
        "module_keys": sorted(subscription.module_keys),
    }


if __name__ == "__main__":
    registry, _bus, _subscriptions = bootstrap()
    print(f"Modules chargés: {len(registry.all())}")
