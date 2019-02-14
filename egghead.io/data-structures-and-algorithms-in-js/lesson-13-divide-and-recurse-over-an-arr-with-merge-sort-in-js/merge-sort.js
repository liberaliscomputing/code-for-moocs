const mergeSort = (array) => {
  if (array.length < 2) return array;

  const cent = Math.floor(array.length / 2);
  const pred = array.slice(0, cent);
  const succ = array.slice(cent);

  return merge(mergeSort(pred), mergeSort(succ));
};

const merge = (pred, succ) => {
  const sorted = [];

  while (pred.length && succ.length) {
    sorted.push(pred[0] <= succ[0] 
      ? pred.shift() 
      : succ.shift()
    );
  }

  const merged = [...sorted, ...pred, ...succ];
  console.log(merged);
  
  return merged;
};

module.exports = mergeSort;
