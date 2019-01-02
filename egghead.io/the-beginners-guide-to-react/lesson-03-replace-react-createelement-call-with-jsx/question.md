Q. Convert this to the JavaScript (`React.createElement`) equivalent:  
```
<div id='greeting' className='active'>Hello {user.name}</div>
```

A.  
```
React.createElement(
  'div',
  { id: 'greeting', className: 'active' },
  'Hello ',
  user.name,
);
```