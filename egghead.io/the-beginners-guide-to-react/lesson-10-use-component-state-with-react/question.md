Q. Create a stateful counter component called `Counter` that renders a button with a number that represents the times that button has been clicked. When the button is clicked, the count should be incremented by one.

A.  
```
class Counter extends React.Component {
  state = { count: 0 };

  increase = () => {
    this.setState((state) => {
      return { count: state.count + 1 };
    });
  }

  render() {
    return (
      <div style={{ textAlign: 'center' }}>
        <button onClick={this.increase} style={{ fontSize: '2em'}}>{this.state.count}</button>
      </div>
    )
  }
}
```