def bubble_sort(array):
  while True:
    is_swapped = False

    for i in range(len(array) - 1):
      print(array)
      
      if array[i] > array[i + 1]:
        curr = array[i]
        array[i] = array[i + 1]
        array[i + 1] = curr
        is_swapped = True

    if not is_swapped: break

  return array