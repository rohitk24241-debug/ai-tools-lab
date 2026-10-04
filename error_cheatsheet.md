

# Python Error Cheat-Sheet

## 1. IndexError

**Error:** `IndexError: list index out of range`

**Cause:**  
A list index was accessed outside the valid range of the list.

**Fix:**  
Use a valid index or check the list length before accessing an element.

Example:
```python
numbers = [10, 20, 30]
print(numbers[2])


---

## 2. KeyError

**Error:** `KeyError: 'marks'`

**Cause:**
A KeyError occurs when a program tries to access a dictionary key that does not exist in the dictionary. In our example, the dictionary contains `name` and `age`, but the program tries to access `marks`.

**Fix:**
Use an existing key or add the required key to the dictionary.

Example:
```python
student = {
    "name": "Rohit",
    "age": 21
}

print(student["name"])


---

## 3. TypeError

Error: TypeError: unsupported operand type(s) for +: 'int' and 'str'

Cause:
An integer and a string were used together with the + operator. Python cannot directly add these two different data types.

Fix:
Convert the string into an integer before performing the addition.

Example:

number = 10
text = "5"

print(number + int(text))



---

## 4. RecursionError

Error: RecursionError: maximum recursion depth exceeded

Cause:
A recursive function keeps calling itself without reaching a stopping condition. This causes Python to exceed its maximum recursion depth.

Fix:
Add a base case that stops the recursive function when a specific condition is reached.

Example:

def count_down(n):
    if n <= 0:
        return
    return count_down(n - 1)

count_down(5)




---

## 5. AttributeError

Error: AttributeError: 'str' object has no attribute 'append'

Cause:
An AttributeError occurs when a program tries to use a method or attribute that the object does not have. In this example, the object is a string, and strings do not have an append() method.

Fix:
Use an operation or method that is supported by the object's data type.

Example:

name = "Rohit"

print(name + " Kumar")

Output:
Rohit Kumar
