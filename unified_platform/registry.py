from dataclasses import dataclass
from typing import Dict, Iterable


@dataclass(frozen=True)
class Module:
    key: str
    name: str
    description: str
    category: str


class ModuleRegistry:
    def __init__(self) -> None:
        self._modules: Dict[str, Module] = {}

    def register(self, module: Module) -> None:
        if module.key in self._modules:
            raise ValueError(f"Module '{module.key}' already registered")
        self._modules[module.key] = module

    def register_many(self, modules: Iterable[Module]) -> None:
        for module in modules:
            self.register(module)

    def all(self) -> Dict[str, Module]:
        return dict(self._modules)
