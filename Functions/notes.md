# Python Functions

A function is a block of code that performs a specific task whenever it is called. In bigger programs, where we have large amounts of code, it is advisable to create or use existing functions that make the program flow organized and neat.

There are two types of functions:

1. Built-in functions
2. User-defined functions

# Built-in functions:
These functions are defined and pre-coded in python. Some examples of built-in functions are as follows:

min(), max(), len(), sum(), type(), range(), dict(), list(), tuple(), set(), print(), etc.

# User-defined functions:
We can create functions to perform specific tasks as per our needs. Such functions are called user-defined functions.

Syntax:
def function_name(parameters):
  pass

## Code and Statements

Rules to naming function are similar to that of naming variables.
Any statements and other code within the function should be indented.

## Calling a function:
We call a function by giving the function name, followed by parameters (if any) in the parenthesis.

Example:

def name(fname, lname):
    print("Hello,", fname, lname)

name("Ram", "Yadav")
Output:

Hello, Ram Yadav

# Function Arguments

We must pass all the required arguments while calling the function.

If values are missing, python gives an error.

Example:

```python
def student(name, age):
    print(name)
    print(age)

student("Ram", 17)
```

## Default Arguments

We can provide default values to parameters while defining the function.

If no value is passed during function call, the default value is used.

Example:

```python
def country(name = "India"):
    print("Country:", name)

country()
country("Japan")
```

Output:

```python
Country: India
Country: Japan
```

## Keyword Arguments

In keyword arguments, we pass values using parameter names.

This improves readability and order does not matter.

Example:

```python
def intro(name, age):
    print(name)
    print(age)

intro(age = 17, name = "Aniket")
```

## Return Statement

The return statement is used to send value back from the function.

Functions without return usually give `None`.

Example:

```python
def square(num):
    return num * num

result = square(4)

print(result)
```

Output:

```python
16
```

## Variable-length Arguments

Variable-length argument functions can accept any number of arguments.

There are two types of variable-length arguments:

1. Arbitrary Arguments
2. Keyword Arbitrary Arguments

## Arbitrary Arguments

Use `*` before parameter name while defining function.

Arguments are stored in tuple form.

Example:

```python
def average(*nums):

    print("Type of nums is :", type(nums))

    sum = 0

    for i in nums:
        sum = sum + i

    print("Average is:", sum / len(nums))

average(1, 2, 3, 4)
```

Output:

```python
Type of nums is : <class 'tuple'>
Average is: 2.5
```

## Keyword Arbitrary Arguments

Use `**` before parameter name while defining function.

Arguments are stored in dictionary form.

Example:

```python
def name(**name):

    print("Type of nums is :", type(name))

    print("Name is", name["fname"], name["lname"])

name(fname = "John", lname = "David")
```

Output:

```python
Type of nums is : <class 'dict'>
Name is John David
```