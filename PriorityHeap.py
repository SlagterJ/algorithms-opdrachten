class PriorityHeap:
    def __init__(self, max_size=31):
        # Initialiseer een lijst met None-waarden voor de heap
        # Index 0 wordt niet gebruikt om berekeningen te vereenvoudigen
        self.heap = [None] * (max_size + 1)
        self.size = 0
        self.max_size = max_size

    def _parent(self, index):
        """Retourneert de index van de ouder"""
        return index // 2

    def _left_child(self, index):
        """Retourneert de index van het linker kind"""
        return 2 * index

    def _right_child(self, index):
        """Retourneert de index van het rechter kind"""
        return 2 * index + 1

    def _swap(self, index1, index2):
        """Verwisselt twee elementen in de heap"""
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def _heapify_up(self, index):
        """Recursieve functie om een element omhoog te bubelen"""
        if index <= 1:
            return

        parent_idx = self._parent(index)
        if self.heap[parent_idx] is not None and self.heap[index] > self.heap[parent_idx]:
            self._swap(index, parent_idx)
            self._heapify_up(parent_idx)

    def _heapify_down(self, index):
        """Recursieve functie om een element naar beneden te bubelen"""
        largest = index
        left = self._left_child(index)
        right = self._right_child(index)

        if (left <= self.size and self.heap[left] is not None and 
            self.heap[left] > self.heap[largest]):
            largest = left

        if (right <= self.size and self.heap[right] is not None and 
            self.heap[right] > self.heap[largest]):
            largest = right

        if largest != index:
            self._swap(index, largest)
            self._heapify_down(largest)

    def insert(self, value):
        """Voegt een element toe aan de heap"""
        if self.size >= self.max_size:
            raise Exception("Heap is vol")

        self.size += 1
        self.heap[self.size] = value
        self._heapify_up(self.size)

    def remove_max(self):
        """Verwijdert en retourneert het grootste element (root)"""
        if self.size < 1:
            raise Exception("Heap is leeg")

        max_value = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.heap[self.size] = None
        self.size -= 1
        
        if self.size > 0:
            self._heapify_down(1)

        return max_value

    def __str__(self):
        """String representatie van de heap"""
        return str([x for x in self.heap[1:self.size + 1]])


# Maak een nieuwe heap
heap = PriorityHeap()

# Test insert
heap.insert(50)
heap.insert(30)
heap.insert(20)
heap.insert(15)
heap.insert(10)
heap.insert(8)
heap.insert(16)
print("Heap na initiële inserts:", heap)

# Test insert van 97
heap.insert(97)
print("Heap na toevoegen van 97:", heap)

# Test remove_max
max_value = heap.remove_max()
print(f"Verwijderd maximum ({max_value}), nieuwe heap:", heap)