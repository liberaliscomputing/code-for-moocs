Q. What is a technique to avoid displaying a "No Results" message before an HTTP request has been made with `axios`?

A. Set an initial state of `{loaded: false}` , and inside of the `.then()` after the request with  `axios` resolves, call `setState({loaded: true})`.