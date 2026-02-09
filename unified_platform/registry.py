from dataclasses import dataclass
from typing import Dict, Iterable, List, Optional


@dataclass(frozen=True)
class Module:
    key: str
    name: str
    description: str
    category: str


@dataclass
class ModuleState:
    module: Module
    enabled: bool = True


class ModuleRegistry:
    def __init__(self) -> None:
        self._modules: Dict[str, ModuleState] = {}

    def register(self, module: Module) -> None:
        if module.key in self._modules:
            raise ValueError(f"Module '{module.key}' already registered")
        self._modules[module.key] = ModuleState(module=module)

    def register_many(self, modules: Iterable[Module]) -> None:
        for module in modules:
            self.register(module)

    def all(self) -> Dict[str, Module]:
        return {key: state.module for key, state in self._modules.items()}

    def states(self) -> Dict[str, ModuleState]:
        return dict(self._modules)

    def list_all(self) -> List[ModuleState]:
        return list(self._modules.values())

    def get(self, key: str) -> Optional[ModuleState]:
        return self._modules.get(key)

    def enable(self, key: str) -> None:
        state = self._require(key)
        state.enabled = True

    def disable(self, key: str) -> None:
        state = self._require(key)
        state.enabled = False

    def by_category(self, category: str) -> List[ModuleState]:
        return [state for state in self._modules.values() if state.module.category == category]

    def _require(self, key: str) -> ModuleState:
        if key not in self._modules:
            raise KeyError(f"Unknown module '{key}'")
        return self._modules[key]
