from event import Event


class Clause:
    def __init__(self, head:Event, body:list[Event]) -> None:
        self.head = head
        self.body = body