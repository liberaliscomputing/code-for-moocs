Q. How would you create and use a component called Message that accepts a string variable  `msg` and renders it inside of a `div`? (Hint: This component can be created with a single line arrow function)

A.  
```
const Message = (props) => <div>{props.msg}</div>;
<Message msg="Hello World!" />
```