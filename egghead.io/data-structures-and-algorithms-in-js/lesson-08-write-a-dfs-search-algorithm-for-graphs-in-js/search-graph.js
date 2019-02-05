const Graph = require('../lesson-06-js-graph-data-structure/graph');
const CustomQueue = require('../lesson-02-queue-data-structure-in-js/custom-queue');


class SearchGraph extends Graph {
  breadthFirstSearch(key, func) {
    const head = this.getNode(key);
    const hist = this.nodes.reduce((acc, node) => {
      acc[node.key] = false;
      return acc;
    }, {});
    const customQueue = new CustomQueue();
    customQueue.enqueue(head);

    while (!customQueue.isEmpty()) {
      const curr = customQueue.dequeue();

      if (!hist[curr.key]) {
        func(curr);
        hist[curr.key] = true;
      }

      curr.neighbors.map(neighbor => {
        if (!hist[neighbor.key]) {
          customQueue.enqueue(neighbor);
        }
      })
    }
  }

  depthFirstSearch(key, func) {
    const head = this.getNode(key);
    const hist = this.nodes.reduce((acc, node) => {
      acc[node.key] = false;
      return acc;
    }, {});

    function traverse(node) {
      if (hist[node.key]) {
        return
      }

      func(node);
      hist[node.key] = true;

      node.neighbors.map(neighbor => traverse(neighbor));
    }

    traverse(head);
  }
}

module.exports = SearchGraph;
