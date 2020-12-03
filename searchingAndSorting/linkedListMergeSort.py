def merge(S1, S2, S): 
  # Merges S1 and S2 into empty queue S
  
  
  while not S1.is_empty() and not S2.is_empty():
    if S1.first() < S2.first():
      S.enqueue(S1.dequeue())
    else:
      S.enqueue(S2.dequeue())
      
  while not S1.is_empty(): # Move remainder of S1 onto S
    S.enqueue(S1.dequeue())
    
  while not S2.is_empty(): # Move remainder of S2 onto S
    S.enqueue(S2.dequeue())
    
def merge_sort(S):
  # Sorts elements of queue S using merge-sort


  n = len(S) # list is already sorted
  if n < 2:
    return
  
  S1 = LinkedQueue()
  S2 = LinkedQueue() 
  
  while len(S1) < n//2: # Move the first n//2 elements to S1
    S1.enqueue(S.dequeue())
  while not S.is_empty(): # Move the rest to S2
    S2.enqueue(S.dequeue())
  
  merge_sort(S1) # Sorts first half
  merge_sort(S2) # Sorts second half 
  
  merge(S1, S2, S) # Merge sorted halves back to S 
