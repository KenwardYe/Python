import random


class Queue:
    def __init__(self):
        self.items = []

    def dequeue(self):
        return self.items.pop()

    def enqueue(self, item):
        self.items.insert(0, item)

    def isempty(self):
        return self.items == []

    def size(self):
        return len(self.items)


def hotpotato(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)
    while simqueue.size() > 1:
        for i in range(num):
            temp = simqueue.dequeue()
            simqueue.enqueue(temp)
            print(temp)
        print('out: ', simqueue.dequeue())
    return simqueue.dequeue()


class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0

    def tick(self):
        if self.currentTask is not None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):
        if self.currentTask is not None:
            return True
        else:
            return False

    def startnext(self, newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getpages() * 60 / self.pagerate


class Task:
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)

    def getstamp(self):
        return self.timestamp

    def getpages(self):
        return self.pages

    def waittime(self, currenttime):
        return currenttime - self.timestamp


def simulation(numseconds, pagesperminute):
    labprinter = Printer(pagesperminute)
    printqueue = Queue()
    waitingtimes = []
    for currentSecond in range(numseconds):
        if newprinttask():
            task = Task(currentSecond)
            printqueue.enqueue(task)
        if (not labprinter.busy()) and (not printqueue.isempty()):
            nexttask = printqueue.dequeue()
            waitingtimes.append(nexttask.waittime(currentSecond))
            labprinter.startnext(nexttask)
        labprinter.tick()
    averagewait = sum(waitingtimes) / len(waitingtimes)
    print("Average Wait %6.2f secs %3d tasks remaining." %
          (averagewait, printqueue.size()))


def newprinttask():
    num = random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False


class Deque:
    def __init__(self):
        self.items = []

    def isempty(self):
        return self.items == []

    def addfront(self, item):
        self.items.append(item)

    def addrear(self, item):
        self.items.insert(0, item)

    def removefront(self):
        return self.items.pop()

    def removerear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


def palchecker(astring):
    chardeque = Deque()
    for ch in astring:
        chardeque.addrear(ch)
    stillequal = True
    while chardeque.size() > 1 and stillequal:
        first = chardeque.removefront()
        last = chardeque.removerear()
        if first != last:
            stillequal = False

    return stillequal
