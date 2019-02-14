def quick_sort(array):
  if len(array) < 2: return array

  pivot_index = len(array) - 1
  pivot = array[pivot_index]
  pred, succ = [], []

  for i in range(pivot_index):
    curr = array[i]
    if curr < pivot: pred.append(curr)
    else: succ.append(curr)

  sorted_array = (
    quick_sort(pred) 
    + [pivot] 
    + quick_sort(succ)
  )
  print(sorted_array)

  return sorted_array