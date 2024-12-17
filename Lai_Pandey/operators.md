### what are operators in python?
- operators in python are set of symbols and works that have very strict and specific meaning and perform fixed operation
- Operation like 
  - addition, subtraction, multiplication, division, conditional checks, logic dates, binary operation etc.

## types of operators in python
1. Arithmetic Operators
2. Assignment Operators
3. Conditional operators
4. Logical Operators
5. Binary operator
6. Membership operators


#### Arithmetic Operators
1. Addition (+) 
2. Subtraction (-)
3. multiplication (*)
4. Normal division (/)
5. Floor division (//)
6. modulus (%)
7. exponent (**)


#### Assignment Operators
```python
var1 = 12

## combine with arithmatic operator
var1 += 10 # var1 -> 22
# similar to
var1 = var1 + 10


var1 -= 10
var1 *= 10
var1 /= 10
var1 //=10
var1 %= 18
var1 **= 12
```

# NOTE: Auto type casting
- In python the datatype precedence is supported, i.e. if we have any kind of operation where one of the value is of (say `float`) and other is (say `int`) the output is going to be `float`
##### possible
```python
var1 = 12
var2 = 10.0
res = var1 + var2
print(res)
```

```terminal
22.0
```

##### not possible
```python
var1 = "12"
var2 = 10.0
print(var1 + var2)
```
```terminal
Traceback (most recent call last):
  File "E:\python5tutor\Lai_Pandey\operators.py", line 13, in <module>
    print(var1 + var2)
TypeError: can only concatenate str (not "float") to str
```