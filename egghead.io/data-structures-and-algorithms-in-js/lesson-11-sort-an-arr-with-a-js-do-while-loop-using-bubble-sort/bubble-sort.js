const bubbleSort = (array) => {
  let isSwapped;

  do {
    isSwapped = false;

    array.forEach((value, index, array) => {
      console.log(array);

      if (value > array[index + 1]) {
        const curr = value;
        array[index] = array[index + 1];
        array[index + 1] = curr;
        isSwapped = true; 
      }
    });

  } while (isSwapped);

  return array;
}

module.exports = bubbleSort;
