const Node = require('./node');


class LinkedList {
  constructor() {
    this.head = null;
    this.tail = null;
    this.size = 0;
  }

  push(value) {
    const node = new Node(value);

    if (this.head === null) {
      this.head = node;
      this.tail = node;
      this.size++;

      return node;
    }

    this.tail.next = node;
    this.tail = node;
    this.size++;

    return node;
  }

  pop() {
    if (this.isEmpty()) {
      return null;
    }

    const node = this.tail;

    if (this.head === this.tail) {
      this.head = null;
      this.tail = null;
      this.size--;

      return node;
    }

    let curr = this.head;
    let penultimate;
    while (curr) {
      if (curr.next === this.tail) {
        penultimate = curr;
        break;
      }

      curr = curr.next;
    }

    penultimate.next = null;
    this.tail = penultimate;
    this.size--;

    return node;
  }

  get(index) {
    if (index < 0 || index > this.size - 1) {
      return null;
    }

    if (index === 0) {
      return this.head;
    }

    let curr = this.head;
    let i = 0;

    while (i < index) {
      curr = curr.next;
      i++;
    }

    return curr;
  }

  delete(index) {
    if (index < 0 || index > this.size - 1) {
      return null;
    }

    let curr = this.head;
    
    if (index === 0) {
      this.head = this.head.next;
      this.size--;

      return curr;
    }

    let prev;
    let i = 0;

    while (i < index) {
      prev = curr;
      curr = curr.next;
      i++;
    }

    prev.next = curr.next;

    if (prev.next === null) {
      this.tail = prev;
    }

    this.size--;

    return curr;
  }

  isEmpty() {
    return this.size === 0;
  }

  print() {
    const values = [];
    let curr = this.head;

    while (curr) {
      values.push(curr.value);
      curr = curr.next;
    }

    return values.join(' => ');
  }
}

module.exports = LinkedList;
