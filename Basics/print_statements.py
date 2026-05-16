"""
print() is a built-in function used to display output on the screen.

Comments are lines that Python ignores while executing the program.
They are mainly used to explain the code.
"""

print("Hello World")


"""
In Python, print() has some special parameters that control
how the output appears.

Important parameters:

sep   - separator between values
end   - what comes at the end of output
file  - where the output is sent
flush - forces output immediately
"""

print("Hello", 6, 7, sep="  ")
# sep adds spaces or symbols between values.

print("Hello", end="\n")
# end decides what comes after the output.

print("Hello")

# Output
# Hello World
# Hello  6  7
# Hello
# Hello