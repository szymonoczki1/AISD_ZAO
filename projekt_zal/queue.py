class minHeap:
    def __init__(self, heap=[]):
        self.heap = heap

    def left(self, i):
        return 2*i + 1
    
    def right(self, i):
        return 2*i + 2

    def parent(self, i):
        return (i-1)//2

    def min_heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        smallest = i

        if l < len(self.heap) and self.heap[l].number < self.heap[smallest].number:
            smallest = l
        if r < len(self.heap) and self.heap[r].number < self.heap[smallest].number:
            smallest = r
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.min_heapify(smallest)

    def build_heap(self):
        #od rodzica ostatniego elementu
        for i in range(self.parent(len(self.heap)-1),-1,-1):
            self.min_heapify(i)

    def heap_insert(self,x):
        self.heap.append(x)
        i = len(self.heap)-1

        while i>0:
            if self.heap[self.parent(i)].number > self.heap[i].number:
                self.heap[self.parent(i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]
                i = self.parent(i)
            else:
                break

    def heap_remove(self, irm=0):
        self.heap[irm], self.heap[-1] = self.heap[-1], self.heap[irm]
        removed_element = self.heap.pop()

        if irm < len(self.heap):
            self.min_heapify(irm)

        return removed_element
    
    def print_heap(self):
        for node in self.heap:
            print((node.name,node.number))


        