from collections import defaultdict
from typing import Callable, Dict, List


class EventBus:
    """
    A high-performance event bus for decoupled communication between services and systems.
    Allows for 0-coupling between components.
    """

    def __init__(self):
        self._subscribers: Dict[str, List[Callable]] = defaultdict(list)

    def subscribe(self, event_type: str, callback: Callable):
        self._subscribers[event_type].append(callback)

    def emit(self, event_type: str, **kwargs):
        for callback in self._subscribers[event_type]:
            callback(**kwargs)


# Global instance for easy access, though dependency injection is preferred
event_bus = EventBus()
