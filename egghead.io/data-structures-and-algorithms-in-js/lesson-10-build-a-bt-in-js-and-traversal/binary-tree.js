const Node = require('./node');


class BinaryTree {
  constructor(data) {
    this.root = new Node(data);
  }

  traverse(node, func, order) {
    if (node !== null) {
      switch (order) {
        case 'in': {
          this.traverse(node.prev, func, 'in'); 
          func(node);
          this.traverse(node.next, func, 'in');
          break;
        }
        case 'pre': {
          func(node);
          this.traverse(node.prev, func, 'pre');
          this.traverse(node.next, func, 'pre');
          break;
        }
        case 'post': {
          this.traverse(node.prev, func, 'post');
          this.traverse(node.next, func, 'post');
          func(node);
          break;
        }

        // no default
      }
    }
  }
}

module.exports = BinaryTree;
