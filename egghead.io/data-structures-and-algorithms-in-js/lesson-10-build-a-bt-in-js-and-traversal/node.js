class Node {
  constructor(data) {
    this.data = data;
    this.prev = null;
    this.next = null;
  }

  addNode(data) {
    const node = new Node(data);

    if (data < this.data) {
      this.prev = node;
    } else {
      this.next = node;
    }

    return node;
  }
}

module.exports = Node;
