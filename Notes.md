### Python operator precedence (important)
Python evaluates boolean operators from highest to lowest precedence:
1. `not`
2. `and`
3. `or`

Examples:
```py
print(
    not False and True,      # (not False) and True -> True
    True or False and False, # True or (False and False) -> True 

    not (False and True),     #  True
    (True or False) and False # False 
)
```