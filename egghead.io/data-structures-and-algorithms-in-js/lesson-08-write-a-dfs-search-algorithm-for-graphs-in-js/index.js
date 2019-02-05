const SearchGraph = require('./search-graph');


const searchGraph = new SearchGraph(directed = true);
const nodes = [1, 2, 3, 4, 5, 6];
const edges = [
  [1, 2],
  [1, 3],
  [1, 4],
  [2, 3],
  [2, 5],
  [3, 6],
];

nodes.map(node => searchGraph.addNode(node));
edges.map(edge => searchGraph.addEdge(...edge));

searchGraph.breadthFirstSearch(1, node => {
  console.log(node.key); // logs 1 => 2 => 3 => 4 => 5 => 6
});

searchGraph.depthFirstSearch(1, node => {
  console.log(node.key); // logs 1 => 2 => 3 => 6 => 5 => 4
});