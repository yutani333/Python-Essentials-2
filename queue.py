class QueueError(IndexError):  # Choose base class for the new exception.
    pass

class Queue:
    def __init__(self):
        self.q_list = []

    def put(self, elem):
        print("putting [" + str(elem) + "]")
        self.q_list.insert(0, elem)

    def get(self):
        if len(self.q_list):
            elem = self.q_list[-1]
            del self.q_list[-1]
            return elem
        else:
            raise QueueError

    def reveal(self):
        print(self.q_list)

class SuperQueue(Queue):
    def __init__(self):
        Queue.__init__(self)

    def isempty(self):
        if len(self.q_list):
            return False
        return True
    
act = input("Activate Super Queue:")

if not (act == 'yes'):
    que = Queue()
    que.put(1)
    que.put("dog")
    que.put(False)
    try:
        for i in range(4):
            print(que.get())
    except IndexError:
        print("Queue error")


que = SuperQueue()
que.put(1)
que.put("cat")
que.put(False)
for i in range(4):
    que.reveal()
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")
