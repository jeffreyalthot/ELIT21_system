from dataclasses import dataclass
from typing import Any, Callable, Dict, List


@dataclass(frozen=True)
class Event:
    name: str
    payload: Dict[str, Any]


@dataclass(frozen=True)
class Command:
    name: str
    payload: Dict[str, Any]


class EventBus:
    def __init__(self) -> None:
        self._handlers: Dict[str, List[Callable[[Event], None]]] = {}

    def subscribe(self, event_name: str, handler: Callable[[Event], None]) -> None:
        self._handlers.setdefault(event_name, []).append(handler)

    def publish(self, event: Event) -> None:
        for handler in self._handlers.get(event.name, []):
            handler(event)


class CommandBus:
    def __init__(self) -> None:
        self._handlers: Dict[str, Callable[[Command], Any]] = {}

    def register(self, command_name: str, handler: Callable[[Command], Any]) -> None:
        if command_name in self._handlers:
            raise ValueError(f"Command '{command_name}' already registered")
        self._handlers[command_name] = handler

    def dispatch(self, command: Command) -> Any:
        if command.name not in self._handlers:
            raise KeyError(f"No handler registered for command '{command.name}'")
        return self._handlers[command.name](command)

    def handlers(self) -> Dict[str, Callable[[Command], Any]]:
        return dict(self._handlers)
