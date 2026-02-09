from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Iterable, List, Optional

from autobusiness.modules import ModuleInfo


@dataclass
class ModuleState:
    info: ModuleInfo
    enabled: bool = True


class ModuleRegistry:
    def __init__(self, modules: Iterable[ModuleInfo]) -> None:
        self._modules: Dict[str, ModuleState] = {
            module.module_id: ModuleState(info=module) for module in modules
        }

    def list_all(self) -> List[ModuleState]:
        return list(self._modules.values())

    def get(self, module_id: str) -> Optional[ModuleState]:
        return self._modules.get(module_id)

    def enable(self, module_id: str) -> None:
        state = self._require(module_id)
        state.enabled = True

    def disable(self, module_id: str) -> None:
        state = self._require(module_id)
        state.enabled = False

    def _require(self, module_id: str) -> ModuleState:
        if module_id not in self._modules:
            raise KeyError(f"Unknown module '{module_id}'")
        return self._modules[module_id]
