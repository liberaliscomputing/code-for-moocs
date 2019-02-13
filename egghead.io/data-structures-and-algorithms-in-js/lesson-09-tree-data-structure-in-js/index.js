const Tree = require('./tree');


const dom = new Tree('html');
const head = dom.root.addChild('head');
const body = dom.root.addChild('body');
const title = head.addChild('title');
const header = body.addChild('header');
const main = body.addChild('main');
const footer = body.addChild('footer');

/**
 * html
 *   head
 *     title
 *   body
 *     header
 *     main
 *     footer
 */
dom.print();
