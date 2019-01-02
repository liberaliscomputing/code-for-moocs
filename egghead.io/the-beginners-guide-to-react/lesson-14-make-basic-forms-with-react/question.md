Q. Inside of an event handler, how would you access the `username` inside of this form?  
```
handleSubmit = (event) => {

}

render() {
  return (
    <form onSubmit={this.handleSubmit}>
      <label>
        Name:
        <input type="text" name="username" />
      </label>
      <button type="submit">Submit</button>
    </form>
  )
}
```

A.  
```
doSomething(event.target.elements.username.value);
```