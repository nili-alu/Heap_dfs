class BinaryHeap:
   def __init__(self,list=[]):
       self.heap=[0]

       #looping through the list to get element from it, so that it can heapify the list
       for nbr in list:
           self.heap.append(nbr)
           self.__siftUp(len(self.heap) - 1)

   # adding new item into the list
   def insert (self,data):
       self.heap.append(data)
       self.__siftUp(len(self.heap) - 1)

   # swapping the elements of the list to follow the heap properties
   def __swap(self,i,j):
      self.heap[i], self.heap[j]= self.heap[j],self.heap[i]

   # swaping up function
   def __siftUp(self,index):
        parent = index // 2
        if index <= 1:
            return

        # if the element on certain index less than element on parent index swap
        elif self.heap[index] < self.heap[parent]:
            self.__swap(index,parent)
            self.__siftUp(parent)

   # graph organisation
   def __graphOrganisation(self,index):
        left = index * 2
        right = index * 2
        smallest = index
        if len(self.heap) > left and self.heap[smallest] < self.heap[left]:
            smallest = left
        if len(self.heap) > right and self.heap[smallest] < self.heap[right]:
            smallest = right

        if smallest != index:
            self.__swap(index,smallest)

   def __str__(self):
        return str(self.heap)

# calling functions
val = BinaryHeap([5,9,11,14,18,19,21,33,17,27])
print("origin list before adding 12: \n" + str(val) +"\n")
val.insert(12)
print("final list after adding 12:\n" + str(val))

