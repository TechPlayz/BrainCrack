
# BrainCrack Syntax Documentation

BrainCrack is a fun and quirky language designed for playful scripting. Below are the main syntax rules and their uses.

## Variables
Variables are stored in a dictionary `vars` and can be assigned values using the `put` keyword:
```braincrack
put <variable_name> <value>
```
Example:
```braincrack
put x 10
```
This assigns `10` to `x`.

## Output
The `yap` keyword is used to print values to the console:
```braincrack
yap <value>
```
- The value can be a string (enclosed in quotes), a number, or a variable.
- If a variable is used, its value is printed.
```braincrack
yap "Hello, world!"
yap 42
yap x
```

## Error Handling
If a variable is used that hasn't been defined, an error is raised:
```braincrack
Error Bruhhhh: Undefined Variable: <variable_name>
```

## String Handling
Strings should be enclosed in double or single quotes. When printing, these quotes are removed:
```braincrack
yap "Hello"    # Prints Hello
```

## Arithmetic Operations
Addition is performed using the `stick` keyword followed by numbers:
```braincrack
stick <number1> <number2> ... <numberN>
```
This will output the sum of all the numbers provided.
Example:
```braincrack
stick 1 2 3 4 5  # Prints 15
```

## Notes
- Variables can be used after they are declared.
- Only integers and strings are supported in operations.
- Undefined variables in operations trigger an error.
