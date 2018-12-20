Q. Given this `<SayHello />` component:  
```
function SayHello(props) {
  return (
    <div>
      Hello {props.firstName} {props.lastName}!
    </div>
  )
}
```
How could you validate that the `firstName` and `lastName` props are each a string (and required) using `PropTypes` from the `prop-types` package?

A.  
```
SayHello.propTypes = {
  firstName: PropTypes.string.isRequired,
  lastName: PropTypes.string.isRequired,
};
```