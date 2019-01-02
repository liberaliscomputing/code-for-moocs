Q. Using the raw React API (i.e. JavaScript, not JSX), how would you create a `div` React element with a class of `'container'` that contains the text 'Hello World!'?

A.  
```
const element = React.createElement('div', { className: 'container' }, 'Hello World!'});
```