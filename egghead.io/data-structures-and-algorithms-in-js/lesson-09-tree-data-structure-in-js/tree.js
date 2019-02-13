const Node = require('./node');


class Tree {
  constructor(key) {
    this.root = new Node(key);
  }

  print() {
    function traverse(node, func, depth) {
      func(node, depth);

      if (node.children.length) {
        node.children.map(child => traverse(child, func, depth + 1));
      }
    }

    function indent(node, depth) {
      console.log(depth === 0
        ? node.key
        : `${' '.repeat(depth * 2)}${node.key}`
      );
    } 

    traverse(this.root, indent, 0);
  }
}

module.exports = Tree;
