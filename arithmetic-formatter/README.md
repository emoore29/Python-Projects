# Arithmetic Formatter

This is a [freeCodeCamp project](https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/arithmetic-formatter). It's a python program that takes a list of "problems", e.g. "122 + 3", and returns a string that formats the problems with operands right-aligned vertically. Forked from a [template](https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/arithmetic-formatter
) that includes tests. 

## Examples  
### Function call:   
arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])

### Output:    
![image](https://github.com/AthenasCode/python-arithmetic-formatter/assets/113172968/22414f0c-393e-40a8-ac4e-ebb7c563c321)


### Function call:
arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)

### Output:  
![image](https://github.com/AthenasCode/python-arithmetic-formatter/assets/113172968/ee9d6afd-bc83-4411-a557-dd5f5f5b5ca0)



## Rules:
- Max five problems
- Only accepts addition and subtraction operators
- Numbers must only contain digits and have a max of 4 digits (max number possible is 9999)
- Single space between operator and second operand
- Operands in order provided
- Numbers right-aligned
- Four spaces between each problem
- Dashes at the bottom of each problem
