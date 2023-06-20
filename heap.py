import heapq

class Heap:
    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def min_heap_insert(self, val):
        heapq.heappush(self.min_heap, val)

    def max_heap_insert(self, val):
        heapq.heappush(self.max_heap, -val)

    def min_heap_pop(self):
        return heapq.heappop(self.min_heap)

    def max_heap_pop(self):
        return -heapq.heappop(self.max_heap)
    
    def print_min_heap(self):
        print([elem for elem in self.min_heap])
        
    def print_max_heap(self):
        print([-elem for elem in self.max_heap])  # Remember we stored the elements negated

# Example usage:
heap = Heap()

heap.max_heap_insert(6)
heap.max_heap_insert(12)
heap.max_heap_insert(13)
heap.max_heap_insert(4)
heap.max_heap_insert(8)
heap.max_heap_insert(14)
heap.max_heap_insert(5)
heap.print_max_heap()  # Output: [3, 2, 1]
