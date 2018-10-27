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


class Vertex:
    def __init__(self, key, distance=0, predecessor=None, color='white'):
        self.id = key
        self.distance = distance
        self.setpred = predecessor
        self.color = color
        self.connectedTo = {}

    def setcolor(self, color):
        self.color = color

    def getcolor(self):
        return self.color

    def setdistance(self, distance):
        self.distance = distance

    def getdistance(self):
        return self.distance

    def setpred(self, predecessor):
        self.setpred = predecessor

    def getpred(self):
        return self.setpred

    def addneighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getconnections(self):
        return self.connectedTo.keys()

    def getid(self):
        return self.id

    def getweight(self, nbr):
        return self.connectedTo[nbr]


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addvertex(self, key):
        self.numVertices = self.numVertices + 1
        newvertex = Vertex(key)
        self.vertList[key] = newvertex
        return newvertex

    def getvertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertList

    def addedge(self, f, t, cost=0):
        if f not in self.vertList:
            nv = self.addvertex(f)
        if t not in self.vertList:
            nv = self.addvertex(t)
        self.vertList[f].addneighbor(self.vertList[t], cost)

    def getvertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())


def buildgraph(wordfile):
    d = {}
    g = Graph()
    wfile = open(wordfile, 'r')
    # create buckets of words that differ by one letter
    for line in wfile:
        word = line[:-1]
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i + 1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]
    # add vertices and edges for words in the same bucket
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addedge(word1, word2)
    return g


def bfs(g, start):
    start.setdistance(0)
    start.setpred(None)
    vertqueue = Queue()
    vertqueue.enqueue(start)
    while vertqueue.size() > 0:
        currentvert = vertqueue.dequeue()
        for nbr in currentvert.getconnections():
            if nbr.getcolor() == 'white':
                nbr.setcolor('gray')
                nbr.setdistance(currentvert.getdistance() + 1)
                nbr.setpred(currentvert)
                vertqueue.enqueue(nbr)
        currentvert.setcolor('black')


def traverse(y):
    x = y
    while x.getpred():
        print(x.getid())
        x = x.getpred()
    print(x.getid())


def knightgraph(bdsize):
    ktgraph = Graph()
    for row in range(bdsize):
        for col in range(bdsize):
            nodeid = postonodeid(row, col, bdsize)
            newpositions = genlegalmoves(row, col, bdsize)
            for e in newpositions:
                nid = postonodeid(e[0], e[1], bdsize)
                ktgraph.addedge(nodeid, nid)
    return ktgraph


def postonodeid(row, column, board_size):
    return (row * board_size) + column


def genlegalmoves(x, y, bdsize):
    newmoves = []
    moveoffsets = [(-1, -2), (-1, 2), (-2, -1), (-2, 1), (1, -2), (1, 2), (2, -1), (2, 1)]
    for i in moveoffsets:
        newx = x + i[0]
        newy = y + i[1]
        if legalcoord(newx, bdsize) and legalcoord(newy, bdsize):
            newmoves.append((newx, newy))
    return newmoves


def legalcoord(x, bdsize):
    if 0 <= x <= bdsize:
        return True
    else:
        return False


def orderbyavail(n):
    reslist = []
    for v in n.getconnections():
        if v.getcolor() == 'white':
            c = 0
            for w in v.getconnections():
                if w.getcolor() == 'white':
                    c = c + 1
            reslist.append((c, v))
    reslist.sort(key=lambda x: x[0])
    return [y[1] for y in reslist]


def knighttour(n, path, u, limit):
    u.setcolor('gray')
    path.append(u)
    if n < limit:
        nbrlist = orderbyavail(u)
        i = 0
        done = False
        while i < len(nbrlist) and not done:
            if nbrlist[i].getcolor() == 'white':
                done = knighttour(n + 1, path, nbrlist[i], limit)
            i = i + 1
        if not done:  # prepare to backtrack
            path.pop()
            u.setcolor('white')
    else:
        done = True
    return done


class DFSGraph(Graph):
    def __init__(self):
        super().__init__()
        self.time = 0

    def dfs(self):
        for avertex in self:
            avertex.setcolor('white')
            avertex.setpred(-1)
        for avertex in self:
            if avertex.getcolor() == 'white':
                self.dfsvisit(avertex)

    def dfsvisit(self, startvertex):
        startvertex.setcolor('gray')
        self.time += 1
        startvertex.setdiscovery(self.time)
        for nextvertex in startvertex.getconnections():
            if nextvertex.getcolor() == 'white':
                nextvertex.setpred(startvertex)
                self.dfsvisit(nextvertex)
        startvertex.setcolor('black')
        self.time += 1
        startvertex.setfinish(self.time)
