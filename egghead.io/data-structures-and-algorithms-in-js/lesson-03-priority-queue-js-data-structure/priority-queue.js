const CustomQueue = require('../lesson-02-queue-data-structure-in-js/custom-queue');


class PriorityQueue {
  constructor() {
    this.highPriorityQueue = new CustomQueue();
    this.lowPriorityQueue = new CustomQueue();
  }

  enqueue(item, isHighPriority = false) {
    isHighPriority 
      ? this.highPriorityQueue.enqueue(item) 
      : this.lowPriorityQueue.enqueue(item);
  }

  dequeue() {
    !this.highPriorityQueue.isEmpty() 
      ? this.highPriorityQueue.dequeue() 
      : this.lowPriorityQueue.dequeue();
  }

  peek() {
    return !this.highPriorityQueue.isEmpty() 
      ? this.highPriorityQueue.peek() 
      : this.lowPriorityQueue.peek();
  }

  get size() {
    return this.highPriorityQueue.size 
      + this.lowPriorityQueue.size;
  }

  isEmpty() {
    return this.highPriorityQueue.isEmpty()
      && this.lowPriorityQueue.isEmpty();
  }
}

module.exports = PriorityQueue;
