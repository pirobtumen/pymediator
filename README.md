# PyMediator

Simple but powerful python mediator pattern library.

## Installation

```shell script
python -m pip install git+https://github.com/pirobtumen/pymediator.git@v0.1.0\#egg\=pymediator
```

## Usage

```python
from pymediator import Event, EventHandler, Mediator

mediator = Mediator()

class SimpleEvent(Event):
    EVENT_NAME = 'simple_event'

    def __init__(self, text):
        self._text = text

    def get_text(self):
        return self._text

@mediator.on(SimpleEvent.EVENT_NAME)
class SimpleEventHandler(EventHandler):
    def handle(self, event: SimpleEvent):
        return event.get_text()


if __name__ == "__main__":
    event = SimpleEvent('some text')
    res = mediator.emit(event)
    print(res)
```
