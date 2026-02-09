from unified_platform import EventBus, ModuleRegistry, load_default_modules


def bootstrap() -> tuple[ModuleRegistry, EventBus]:
    registry = ModuleRegistry()
    registry.register_many(load_default_modules())
    bus = EventBus()
    return registry, bus


if __name__ == "__main__":
    registry, _bus = bootstrap()
    print(f"Modules chargés: {len(registry.all())}")
