from pymediator import Event, EventHandler, Mediator


def test_base_event():
    assert Event.EVENT_NAME is ''


def test_base_event_handler():
    handler = EventHandler()
    res = handler.handle(Event())
    assert res is None


def test_mediator_register_event():
    test_event_name = 'test_event'
    test_mediator = Mediator()
    test_mediator.on(test_event_name)(EventHandler)
    assert test_event_name in test_mediator.handlers
    assert test_mediator.handlers[test_event_name] is not None


def test_mediator_emit_event():
    test_event_name = 'test_event'
    test_mediator = Mediator()
    test_mediator.on(test_event_name)(EventHandler)
    assert test_event_name in test_mediator.handlers
    assert test_mediator.handlers[test_event_name] is not None


def test_mediator_handle_event():
    mediator = Mediator()

    @mediator.on(Event.EVENT_NAME)
    class BaseEventHandler(EventHandler):
        def handle(self, event: Event):
            return None

    event = Event()
    res = mediator.emit(event)
    assert res is None


def test_mediator_simple_event():
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

    event = SimpleEvent('some text')
    res = mediator.emit(event)

    assert res is not None
    assert res == 'some text'
