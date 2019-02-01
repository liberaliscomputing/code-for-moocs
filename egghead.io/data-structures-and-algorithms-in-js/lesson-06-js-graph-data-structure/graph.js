const Node = require('./node');


class Graph {
  constructor(directed = false) {
    this.directed = directed;
    this.nodes = [];
    this.edges = [];
  }

  addNode(key) {
    this.nodes.push(new Node(key));
  }

  getNode(key) {
    return this.nodes.find(node => node.key === key);
  }

  addEdge(key1, key2) {
    const node1 = this.getNode(key1);
    const node2 = this.getNode(key2);

    node1.addNeighbor(node2);
    this.edges.push(`${key1}-${key2}`);

    if (!this.directed) {
      node2.addNeighbor(node1);
    }
  }

  print() {
    return this.nodes.map(({ key, neighbors }) => {
      return { [key]: neighbors };
    });
  }
}

module.exports = Graph;
