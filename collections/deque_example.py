from collections import deque

class TicketQueue(object):
    def __init__(self):
        self.deque = deque()

    def add_person(self, name):
        self.deque.append(name)
        print(f"{name} added to queue")

    def service_person(self, name):
        name = self.deque.popleft()
        print(f"{name} has been serviced")

    def bypass_queue(self, name):
        self.deque.appendleft(name)
        print(f"{name} has been bypassed")

ticket_queue = TicketQueue()
ticket_queue.add_person("MM")
ticket_queue.service_person("MM")
ticket_queue.bypass_queue("MM")
