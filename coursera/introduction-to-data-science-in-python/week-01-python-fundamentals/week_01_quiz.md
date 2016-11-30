## Week-01 Quiz
### 1. Python is an example of an
+ **Interpreted language**
+ Declarative language
+ Operating system language
+ Data science language
+ Low level language

### 2. Data Science is a
+ Branch of statistics
+ Branch of computer science
+ Branch of artificial intelligence
+ **Interdisciplinary, made up of all of the above**

### 3. Data visualization is not a part of data science.
+ True
+ **False**

### 4. Which bracketing style does Python use for tuples?
+ {}
+ **()**
+ []

### 5. In Python, strings are considered Mutable, and can be changed.
+ **False**
+ True

### 6. What is the result of the following code: ['a', 'b', 'c'] + [1, 2, 3]
+ **['a', 'b', 'c', 1, 2, 3]**
+ TypeError: Cannot convert list(int) to list(str)
+ ['a1', 'b2', 'c3'] 
+ [['a', 'b', 'c'], [1, 2, 3]]

### 7. String slice is
+ A way to make string mutable in python
+ A way to reduce the size on disk of strings in python
+ **A way to make a substring of a string in python**

### 8. When you create a lambda, what type is returned? E.g. type(lambda x: x+1) returns
+ **<class 'function'>**
+ <class 'type'>
+ <class 'int'>
+ <class 'object'>

### 9. The epoch refers to
+ January 1, year 0
+ **January 1, year 1970**
+ January 1, year 1980
+ January 1, year 2000

### 10. This code, [x ** 2 for x in range(10)] , is an example of a
+ **List comprehension**
+ Sequence comprehension
+ Tuple comprehension
+ List mjltiplication

### 11. Given a 6x6 NumPy array r, which of the following options would slice the shaded elements?
```python
[[ **0**,  1,  2,  3,  4,  5],
 [ 6,  **7**,  8,  9, 10, 11],
 [12, 13, **14**, 15, 16, 17],
 [18, 19, 20, **21**, 22, 23],
 [24, 25, 26, 27, **28**, 29],
 [30, 31, 32, 33, 34, **35**]]
```
+ 
```
**r.reshape(36)[::7]**
```
+ 
```
r[::7]
```
+ 
```
r[:,::7]
```
+ 
```
r[0:6,::-7]
```
### 12. Given a 6x6 NumPy array r, which of the following options would slice the shaded elements?
```python
[[ 0,  1,  2,  3,  4,  5],
 [ 6,  7,  8,  9, 10, 11],
 [12, 13, **14**, **15**, 16, 17],
 [18, 19, **20**, **21**, 22, 23],
 [24, 25, 26, 27, 28, 29],
 [30, 31, 32, 33, 34, 35]]
```
+ **`r[[2,3],[2,3]]`**
+
```
r[2::2,2::2]
```
+
```
r[::2,::2]
```
+
```
**r[2:4,2:4]**
```
