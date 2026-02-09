from unified_platform import (
    EventBus,
    ModuleRegistry,
    load_unified_15_modules,
)
from unified_platform.subscription import SubscriptionManager, build_default_plans


def bootstrap() -> tuple[ModuleRegistry, EventBus, SubscriptionManager]:
    registry = ModuleRegistry()
    registry.register_many(load_unified_15_modules())
    bus = EventBus()
    subscriptions = SubscriptionManager(bus=bus)
    subscriptions.add_plans(
        build_default_plans(module.key for module in registry.all().values())
    )
    return registry, bus, subscriptions


if __name__ == "__main__":
    registry, _bus, _subscriptions = bootstrap()
    print(f"Modules chargés: {len(registry.all())}")
