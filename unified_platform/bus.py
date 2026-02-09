from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Callable, Dict, List
from uuid import uuid4


@dataclass(frozen=True)
class Event:
    name: str
    payload: Dict[str, Any]
    event_id: str = field(default_factory=lambda: str(uuid4()))
    occurred_at: datetime = field(default_factory=datetime.utcnow)
    metadata: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "event_id": self.event_id,
            "name": self.name,
            "payload": self.payload,
            "occurred_at": self.occurred_at.isoformat(),
            "metadata": self.metadata,
        }


@dataclass(frozen=True)
class Command:
    name: str
    payload: Dict[str, Any]
    command_id: str = field(default_factory=lambda: str(uuid4()))
    issued_at: datetime = field(default_factory=datetime.utcnow)
    metadata: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "command_id": self.command_id,
            "name": self.name,
            "payload": self.payload,
            "issued_at": self.issued_at.isoformat(),
            "metadata": self.metadata,
        }


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
