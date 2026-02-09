"""Unified platform package for the 25-module suite."""

from unified_platform.registry import ModuleRegistry
from unified_platform.bus import EventBus
from unified_platform.modules import load_default_modules

__all__ = ["ModuleRegistry", "EventBus", "load_default_modules"]
