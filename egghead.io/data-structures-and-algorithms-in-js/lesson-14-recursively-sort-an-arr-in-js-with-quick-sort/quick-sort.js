const quickSort = (array) => {
  if (array.length < 2) return array;

  const pivotIndex = array.length - 1;
  const pivot = array[pivotIndex];
  const pred = [];
  const succ = [];

  for (let i = 0; i < pivotIndex; i++) {
    const curr = array[i];
    curr < pivot
      ? pred.push(curr)
      : succ.push(curr);
  }

  const sorted = [
    ...quickSort(pred), 
    pivot, 
    ...quickSort(succ)
  ];
  console.log(sorted);

  return sorted;
};

module.exports = quickSort;
