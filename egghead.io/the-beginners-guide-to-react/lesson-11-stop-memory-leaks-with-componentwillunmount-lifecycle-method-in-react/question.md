Q. When is `componentWillUnmount` called and when should it be used?

A. It's called before the component is removed from the page. It should be used when your component has things running which need to be cleaned up, especially asynchronous tasks like `setTimeout`, `setInterval`, or ajax requests.