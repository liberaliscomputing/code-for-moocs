def insertion_sort(array):
  for i in range(1, len(array)):
    for j in range(0, i):
      print(array)

      if array[j] > array[i]:
        curr = array[i]
        array.remove(curr)
        array.insert(j, curr)
  
  return array