
# BrainCrack Syntax Documentation

BrainCrack is a playful programming language with basic operations. Here's an overview of its syntax.

## Variables
Variables are stored in a dictionary named `vars`. They can be assigned using the `put` keyword:
```braincrack
put <variable_name> <value>
```
Example:
```braincrack
put x 10
```
This assigns `10` to the variable `x`.

## Output
The `yap` keyword is used to print values:
```braincrack
yap <value>
```
- The value can be a string (enclosed in quotes), a number, or a variable.
- If a variable is used, its value is printed.

Example:
```braincrack
yap "Hello, world!"
yap 42
yap x
```

### String Handling:
- Strings are enclosed in either single or double quotes (`" "` or `' '`).
- Printed strings will remove the enclosing quotes.

## Arithmetic Operations (Addition)
The `stick` keyword is used for addition:
```braincrack
stick <value1> <value2> ... <valueN>
```
It will output the sum of all values (numbers or variables).

Example:
```braincrack
stick 1 2 3 4  # Prints 10
```

### Variable Handling in Arithmetic:
- If a variable is used in an operation, its value is retrieved from `vars`.
- Undefined variables will raise an error.

## Error Handling
- Undefined variables result in an error:
```braincrack
Error Bruhhhh: Undefined Variable: <variable_name>
```

## Notes
- Variables can be of type `int` or `str` (string).
- Operations like addition only work with integers or variables that hold integers.
