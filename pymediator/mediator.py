from typing import Type, Dict

from .event import Event


class Mediator:
    def __init__(self):
        self.handlers: Dict = {}

    def _register_handler(self, event_name: str, event_handler_class: Type[Event]):
        self.handlers[event_name] = event_handler_class()

    def on(self, event_name: str):
        def _wrap(event_handler_class: Type[Event]):
            self._register_handler(event_name, event_handler_class)
            return event_handler_class

        return _wrap

    def emit(self, event: Event):
        handler = self.handlers[event.EVENT_NAME]
        return handler.handle(event)
