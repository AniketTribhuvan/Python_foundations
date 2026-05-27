# Control Flow

Control flow is used to control how a program executes step by step.

Using control flow we can:
- make decisions
- repeat tasks
- execute different blocks of code
- improve program logic

# if-else

## if statement

if statement is used to check a condition.

If condition is true then code inside if block executes.

Example :

```python
age = 18

if age >= 18:
    print("Adult")
```

Output :

```python
Adult
```

## if-else

if-else is used when we want two possible outputs.

If condition is true then if block runs.
If condition is false then else block runs.

Example :

```python
age = 16

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

Output :

```python
Minor
```

## if-elif-else

if-elif-else is used when we have multiple conditions.

Example :

```python
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
else:
    print("Grade C")
```

Output :

```python
Grade B
```

## nested if-else

Nested if-else means using if-else inside another if-else.

Example :

```python
a = 100
b = 1000
c = 120

if a > b:
    if a > c:
        print("a is greater")
    else:
        print("c is greater")
else:
    if b > c:
        print("b is greater")
    else:
        print("c is greater")
```

Output :

```python
b is greater
```

# match-case

match-case is used when we have many cases to check.

It is similar to switch-case in C language.

If a case matches then that block executes.
If no case matches then default case (`case _`) executes.

Example :

```python
day = 2

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Invalid day")
```

Output :

```python
Tuesday
```

# Loops 

## while loop

while loop runs until the condition becomes false.

Example :

```python
i = 1

while i <= 5:
    print(i)
    i += 1
```

Output :

```python
1
2
3
4
5
```

## for loop

for loop is used for iteration.

It is commonly used with range().

Example :

```python
for i in range(5):
    print(i)
```

Output :

```python
0
1
2
3
4
```

## emulated do-while loop

Python does not have a built-in do-while loop.

But we can emulate it using while loop.

In do-while loop code executes at least one time.

Example :

```python
while True:
    num = int(input("Enter a number : "))

    if num > 0:
        break
```

In above example loop runs at least one time before checking condition.

## break statement

break statement is used to terminate the loop immediately.

When break executes, loop stops and control comes outside the loop.

Example :

```python
for i in range(0,10):

    if(i == 6):
        break

    print(i)
```

Output :

```python
0
1
2
3
4
5
```

In above example loop terminates when value of i becomes 6.

## continue statement

continue statement is used to skip current iteration.

It does not terminate the loop.

Example :

```python
for i in range(0,10):

    if(i == 6):
        continue

    print(i)
```

Output :

```python
0
1
2
3
4
5
7
8
9
```

In above example when i becomes 6 current iteration gets skipped.

# Important Points

- if statements are used for decision making
- else executes when condition becomes false
- elif is used for multiple conditions
- nested if improves complex condition handling
- match-case makes code cleaner for many cases
- while loop works on conditions
- for loop is best for iteration
- Python has no direct do-while loop