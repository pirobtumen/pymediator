import abc

from .event import Event


class EventHandler:
    @abc.abstractmethod
    def handle(self, event: Event):
        return
