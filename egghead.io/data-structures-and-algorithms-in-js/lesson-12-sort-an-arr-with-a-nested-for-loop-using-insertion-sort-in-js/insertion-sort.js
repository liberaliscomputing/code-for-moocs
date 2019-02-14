const insertionSort = (array) => {
  for (let i = 1; i < array.length; i++) {
    for (let j = 0; j < i; j++) {
      console.log(array);

      if (array[j] > array[i]) {
        const [curr] = array.splice(i, 1);
        array.splice(j, 0, curr);
      }
    }
  }

  return array;
};

module.exports = insertionSort;
