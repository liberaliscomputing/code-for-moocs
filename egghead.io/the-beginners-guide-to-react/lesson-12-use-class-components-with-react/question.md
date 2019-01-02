Q. Why should we use arrow functions as instance methods inside of class components?

A. Arrow functions have their own lexical `this`. When we use arrow functions, we don't have to manually bind them to the class.