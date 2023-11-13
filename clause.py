from event import Event


class Clause:
    def __init__(self, head:Event, body:list) -> None:
        self.head = head
        self.body = body