class CustomStack {
  constructor() {
    this.stack = [];
  }

  push(item) {
    this.stack.push(item);
  }

  pop() {
    this.stack.pop();
  }

  peek() {
    return this.stack[this.size - 1];
  }

  get size() {
    return this.stack.length;
  }

  isEmpty() {
    return this.size === 0;
  }
}

module.exports = CustomStack;
