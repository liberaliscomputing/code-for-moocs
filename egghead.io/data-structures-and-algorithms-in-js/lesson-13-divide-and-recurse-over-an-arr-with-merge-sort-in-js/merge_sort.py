import math


def merge_sort(array):
  if len(array) < 2: return array
  
  cent = math.floor(len(array) / 2)
  pred, succ = array[:cent], array[cent:]
  
  return merge(merge_sort(pred), merge_sort(succ))

def merge(pred, succ):
  sorted_array = []

  while len(pred) and len(succ):
    sorted_array.append(pred.pop(0) 
      if pred[0] <= succ[0] 
      else succ.pop(0)
    )

  merged_array = sorted_array + pred + succ
  print(merged_array)

  return merged_array