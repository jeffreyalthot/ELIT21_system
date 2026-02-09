from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from typing import Any, Callable, DefaultDict, Dict, Iterable, List, Type

EventHandler = Callable[["Event"], None]
CommandHandler = Callable[["Command"], Any]


@dataclass(frozen=True)
class Event:
    name: str
    payload: Dict[str, Any]


@dataclass(frozen=True)
class Command:
    name: str
    payload: Dict[str, Any]


class EventBus:
    """Simple event bus for pub/sub communication between modules."""

    def __init__(self) -> None:
        self._subscribers: DefaultDict[str, List[EventHandler]] = defaultdict(list)

    def subscribe(self, event_name: str, handler: EventHandler) -> None:
        self._subscribers[event_name].append(handler)

    def publish(self, event: Event) -> None:
        for handler in self._subscribers.get(event.name, []):
            handler(event)

    def subscribers(self, event_name: str) -> Iterable[EventHandler]:
        return list(self._subscribers.get(event_name, []))


class CommandBus:
    """Command dispatcher to orchestrate module actions."""

    def __init__(self) -> None:
        self._handlers: Dict[str, CommandHandler] = {}

    def register(self, command_name: str, handler: CommandHandler) -> None:
        self._handlers[command_name] = handler

    def dispatch(self, command: Command) -> Any:
        if command.name not in self._handlers:
            raise KeyError(f"No handler registered for command '{command.name}'")
        return self._handlers[command.name](command)

    def handlers(self) -> Dict[str, CommandHandler]:
        return dict(self._handlers)
