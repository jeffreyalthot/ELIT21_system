from __future__ import annotations

from autobusiness.bus import Command, CommandBus, Event, EventBus
from autobusiness.modules import MODULES
from autobusiness.registry import ModuleRegistry


def bootstrap() -> tuple[CommandBus, EventBus, ModuleRegistry]:
    command_bus = CommandBus()
    event_bus = EventBus()
    registry = ModuleRegistry(MODULES)

    def handle_list_modules(_: Command) -> list[dict[str, str]]:
        return [
            {
                "id": state.info.module_id,
                "name": state.info.name,
                "category": state.info.category,
                "enabled": str(state.enabled),
            }
            for state in registry.list_all()
        ]

    def handle_publish_event(command: Command) -> None:
        event = Event(name=command.payload["event"], payload=command.payload.get("data", {}))
        event_bus.publish(event)

    command_bus.register("list_modules", handle_list_modules)
    command_bus.register("publish_event", handle_publish_event)

    return command_bus, event_bus, registry


if __name__ == "__main__":
    bus, _, _ = bootstrap()
    result = bus.dispatch(Command(name="list_modules", payload={}))
    for entry in result:
        print(entry)
