const BinaryTree = require('./binary-tree');


const binaryTree = new BinaryTree(10);
const b = binaryTree.root.addNode(6);
const c = binaryTree.root.addNode(14);
const d = b.addNode(4);
const e = b.addNode(8);
const f = d.addNode(1);
const g = d.addNode(5);
const h = e.addNode(7);
const i = c.addNode(16);

const print = (node) => {
  console.log(node.data);
}

console.log('==In-order traversal==');
binaryTree.traverse(binaryTree.root, print, 'in');

console.log('==Pre-order traversal==');
binaryTree.traverse(binaryTree.root, print, 'pre');

console.log('==Post-order traversal==');
binaryTree.traverse(binaryTree.root, print, 'post');
