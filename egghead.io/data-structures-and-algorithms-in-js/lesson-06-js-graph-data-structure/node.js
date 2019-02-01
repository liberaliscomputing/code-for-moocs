class Node {
  constructor(key) {
    this.key = key;
    this.neighbors = [];
  }

  addNeighbor(node) {
    this.neighbors.push(node)
  }
}

module.exports = Node;
