Q. How would you update this `input` tag to call a function `this.update` every time a key is pressed in the input form?  
```
<input
  type="text"
  name="username"
/>
```

A.  
```
<input
  onChange={this.update}
  type="text"
  name="username"
/>
```