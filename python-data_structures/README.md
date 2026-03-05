# Python - Data Structures: Lists, Tuples

This project is part of the **ALU Higher Level Programming** curriculum. It covers the fundamentals of Python data structures, focusing on lists and tuples.

## Learning Objectives

- What are lists and how to use them
- What are the differences and similarities between strings and lists
- What are the most common methods of lists and how to use them
- How to use lists as stacks and queues
- What are list comprehensions and how to use them
- What are tuples and how to use them
- When to use tuples versus lists
- What is a sequence
- What is tuple packing and sequence unpacking
- What is the `del` statement and how to use it

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All files are interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.8.5)
- All files end with a new line
- The first line of all files is `#!/usr/bin/python3`
- Code uses the `pycodestyle` style (version 2.8.*)
- No modules are imported unless stated otherwise

## Files

| File | Description |
|------|-------------|
| `0-print_list_integer.py` | Prints all integers of a list, one per line using `str.format()` |
| `1-element_at.py` | Retrieves an element from a list by index; returns `None` for invalid index |
| `2-replace_in_list.py` | Replaces an element at a specific position in a list (modifies original) |
| `3-print_reversed_list_integer.py` | Prints all integers of a list in reverse order using `str.format()` |
| `4-new_in_list.py` | Replaces an element at a specific position in a copy of a list |
| `5-no_c.py` | Removes all occurrences of `c` and `C` from a string |
| `6-print_matrix_integer.py` | Prints a matrix of integers using `str.format()` |
| `7-add_tuple.py` | Adds 2 tuples element-wise and returns a tuple of 2 integers |
| `8-multiple_returns.py` | Returns a tuple with the length of a string and its first character |
| `9-max_integer.py` | Finds the biggest integer in a list without using `max()` |
| `10-divisible_by_2.py` | Returns a list of booleans indicating which elements are divisible by 2 |
| `11-delete_at.py` | Deletes an item at a specific position in a list without using `pop()` |
| `12-switch.py` | Switches the values of two variables `a` and `b` in exactly 5 lines |

## Usage Examples

### 0. Print a list of integers
```python
my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)
# Output: 1 / 2 / 3 / 4 / 5 (one per line)
```

### 1. Secure access to an element in a list
```python
my_list = [1, 2, 3, 4, 5]
element_at(my_list, 3)   # → 4
element_at(my_list, -1)  # → None
element_at(my_list, 10)  # → None
```

### 2. Replace element
```python
my_list = [1, 2, 3, 4, 5]
replace_in_list(my_list, 3, 9)
# my_list → [1, 2, 3, 9, 5]
```

### 3. Print a list of integers in reverse
```python
my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)
# Output: 5 / 4 / 3 / 2 / 1 (one per line)
```

### 4. Replace in a copy
```python
my_list = [1, 2, 3, 4, 5]
new_list = new_in_list(my_list, 3, 9)
# new_list → [1, 2, 3, 9, 5]
# my_list  → [1, 2, 3, 4, 5]  (unchanged)
```

### 5. Remove all `c` and `C` from a string
```python
no_c("Best School")  # → "Best Shool"
no_c("Chicago")      # → "hiago"
no_c("C is fun!")    # → " is fun!"
```

### 6. Print a matrix of integers
```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print_matrix_integer(matrix)
# Output:
# 1 2 3
# 4 5 6
# 7 8 9
```

### 7. Tuples addition
```python
add_tuple((1, 89), (88, 11))  # → (89, 100)
add_tuple((1, 89), (1,))      # → (2, 89)
add_tuple((1, 89), ())        # → (1, 89)
```

### 8. More returns!
```python
multiple_returns("At school, I learnt C!")  # → (22, 'A')
multiple_returns("")                         # → (0, None)
```

### 9. Find the max
```python
max_integer([1, 90, 2, 13, 34, 5, -13, 3])  # → 90
max_integer([])                               # → None
```

### 10. Only by 2
```python
divisible_by_2([0, 1, 2, 3, 4, 5, 6])
# → [True, False, True, False, True, False, True]
```

### 11. Delete at
```python
my_list = [1, 2, 3, 4, 5]
delete_at(my_list, 3)
# → [1, 2, 3, 5]
```

### 12. Switch
```python
# Switches values of a and b in exactly 5 lines
# a=10 - b=89
```

## Repository

- **GitHub repository:** `alu-higher_level_programming`
- **Directory:** `python-data_structures`

## Author

Built as part of the ALU Higher Level Programming curriculum.