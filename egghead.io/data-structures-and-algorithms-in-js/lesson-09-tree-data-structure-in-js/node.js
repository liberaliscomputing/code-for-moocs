class Node {
  constructor(key) {
    this.key = key;
    this.children = [];
  }

  addChild(key) {
    const child = new Node(key);
    this.children.push(child);
    
    return child;
  }
}

module.exports = Node;
