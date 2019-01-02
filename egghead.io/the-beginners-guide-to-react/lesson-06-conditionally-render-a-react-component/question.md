Q. Given the outline of this `Message` component, how would you implement a ternary expression to display the `message` inside of a div, or “No Message” if the `message` prop wasn't supplied?  
```
function Message({ message }) {
  return (
    <div>
      // Your Code Here
    </div>
  )
}
```

A.  
```
function Message({ message }) {
  return (
    <div>
      {message ? (
        <div>{message}</div>
      ) : (
        <div>No Message!</div>
      )}
    </div>
  )
}
```