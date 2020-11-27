def merge(S1, S2, S):
"""Merge 2 sorted lists into list of size S"""
  i = j = 0
  while i + j < len(S): 
    if i == len(S2) or (i < len(S1) and S1[i] < S2[j]):
      S[i+j] = S1[i]
      i += 1
    else:
      S[i+j] = S2[i]
      j+= 1
 
 def mergeSort(S):
 """Divide elements until 0 or 1 using recursion""" 
  n = len(S)
  if n < 2:
    return
  
  mid = n // 2
  S1 = S[0:mid]
  S2 = S[mid:n]
  
  mergeSort[S1]
  mergeSort[S2]
  
  merge(S1, S2, S)
