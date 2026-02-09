from unified_platform import EventBus, ModuleRegistry, ModuleRunner, load_unified_15_modules
from unified_platform.subscription import SubscriptionManager, build_default_plans


def bootstrap() -> tuple[ModuleRegistry, EventBus, SubscriptionManager, ModuleRunner]:
    registry = ModuleRegistry()
    registry.register_many(load_unified_15_modules())
    bus = EventBus()
    subscriptions = SubscriptionManager(bus=bus)
    subscriptions.add_plans(
        build_default_plans(module.key for module in registry.all().values())
    )
    runner = ModuleRunner(registry=registry, subscriptions=subscriptions, bus=bus)
    return registry, bus, subscriptions, runner


if __name__ == "__main__":
    registry, _bus, _subscriptions, _runner = bootstrap()
    print(f"Modules chargés: {len(registry.all())}")
