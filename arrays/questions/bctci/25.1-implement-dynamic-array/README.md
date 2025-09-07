## Example: Dynamic Array Implementation in Python

Below is a simplified implementation of a **Dynamic Array**, which resizes automatically as elements are added or removed:

```python
class DynamicArray:
    def __init__(self, capacity=10):
        """Initialize a dynamic array with a given initial capacity."""
        self.capacity = capacity
        self.array = [None] * capacity
        self._size = 0

    def _is_index_valid(self, i):
        """Check if an index is within the bounds of the array."""
        if i < 0 or i >= self._size:
            raise IndexError("Index out of bounds")

    def _is_full(self):
        """Return True if the array is at full capacity."""
        return self._size == self.capacity

    def _expand(self):
        """Double the array capacity when full and copy existing elements."""
        self.capacity *= 2
        new_array = [None] * self.capacity
        for i in range(self._size):
            new_array[i] = self.array[i]
        self.array = new_array

    def _contract(self):
        """Halve the array capacity when underutilized to save memory."""
        self.capacity //= 2
        new_array = [None] * self.capacity
        for i in range(self._size):
            new_array[i] = self.array[i]
        self.array = new_array

    def append(self, x):
        """Add an element to the end of the array, resizing if necessary."""
        if self._is_full():
            self._expand()
        self.array[self._size] = x
        self._size += 1

    def get(self, i):
        """Retrieve the element at index `i`."""
        self._is_index_valid(i)
        return self.array[i]

    def set(self, i, x):
        """Set the element at index `i` to `x`."""
        self._is_index_valid(i)
        self.array[i] = x

    def size(self):
        """Return the current number of elements in the array."""
        return self._size

    def pop_back(self):
        """Remove and return the last element, shrinking capacity if sparse."""
        if self._size == 0:
            return None
        if self._size / self.capacity < 0.25 and self.capacity > 10:
            self._contract()
        data = self.array[self._size - 1]
        self.array[self._size - 1] = None
        self._size -= 1
        return data

    def pop(self, i):
        """Remove and return the element at index i, shifting elements left."""
        self._is_index_valid(i)
        value = self.array[i]
        # Shift elements left in one slice assignment
        self.array[i:self._size - 1] = self.array[i + 1:]
        self.array[self._size - 1] = None
        self._size -= 1
        return value

    def contains(self, x):
        """
        Return index of first occurrence of x, or -1 if not found.
        """
        for i in range(self._size):
            if self.array[i] == x:
                return i
        return -1

    def insert(self, i, x):
        """Insert element x at index i, shifting elements to the right."""
        if i < 0 or i > self._size:  # allow inserting at the end
            raise IndexError("Index out of bounds")
        if self._is_full():
            self._expand()

        # Shift elements right using slice assignment
        self.array[i + 1 : self._size + 1] = self.array[i : self._size]
        self.array[i] = x
        self._size += 1


    def show(self):
        """Return a string representation of the array contents."""
        print(self.array)

    def remove(self, x):
        """
        Remove first occurrence of element x.
        Returns removed element, or None if not found.
        """
        index = self.contains(x)
        if index == -1:
            return None
        return self.pop(index)

```

## Time & Space Complexity of `DynamicArray`

```python
class DynamicArray:
    ...
```

## Constructor & Helpers

### `__init__(capacity=10)`

- **Time Complexity:** O(n) — initializes an array of size `capacity`
- **Space Complexity:** O(n) — stores an array of `capacity` elements

### `_is_index_valid(i)`

- **Time Complexity:** O(1) — simple bounds check
- **Space Complexity:** O(1)

### `_is_full()`

- **Time Complexity:** O(1)
- **Space Complexity:** O(1)

### `_expand()`

- **Time Complexity:** O(n) — copies all elements into a new array (where `n = size`)
- **Space Complexity:** O(n) — new array with doubled capacity

### `_contract()`

- **Time Complexity:** O(n) — copies all elements into a new array
- **Space Complexity:** O(n)

## Core Methods

### `append(x)`

- **Time Complexity:**
  - O(1) amortized (most appends)
  - O(n) worst-case when expansion happens
- **Space Complexity:** O(1)

### `get(i)`

- **Time Complexity:** O(1) — direct access
- **Space Complexity:** O(1)

### `set(i, x)`

- **Time Complexity:** O(1)
- **Space Complexity:** O(1)

### `size()`

- **Time Complexity:** O(1)
- **Space Complexity:** O(1)

## Removal Methods

### `pop_back()`

- **Time Complexity:** O(1) — remove last element
  - O(n) if contraction occurs
- **Space Complexity:** O(1)

### `pop(i)`

- **Time Complexity:** O(n − i) ≈ O(n) — shifts elements left after removal
- **Space Complexity:** O(1)

### `remove(x)`

- **Time Complexity:**
  - O(n) to search via `contains`
  - O(n) for shifting (`pop`)
  - Overall: O(n)
- **Space Complexity:** O(1)

## 🔹 Search & Insertion

### `contains(x)`

- **Time Complexity:** O(n) — linear search
- **Space Complexity:** O(1)

### `insert(i, x)`

- **Time Complexity:** O(n − i) ≈ O(n) — shifts elements right
  - O(n) worst-case when expansion occurs
- **Space Complexity:** O(1)

## Utility

### `show()`

- **Time Complexity:** O(n) — prints entire array
- **Space Complexity:** O(1) — ignoring print buffer

## Summary Table

| Operation      | Time Complexity            | Space Complexity |
| -------------- | -------------------------- | ---------------- |
| `get(i)`       | O(1)                       | O(1)             |
| `set(i, x)`    | O(1)                       | O(1)             |
| `size()`       | O(1)                       | O(1)             |
| `append(x)`    | O(1) amortized, O(n) worst | O(1)             |
| `insert(i, x)` | O(n)                       | O(1)             |
| `pop_back()`   | O(1), O(n) if contract     | O(1)             |
| `pop(i)`       | O(n)                       | O(1)             |
| `remove(x)`    | O(n)                       | O(1)             |
| `contains(x)`  | O(n)                       | O(1)             |
| `_expand()`    | O(n)                       | O(n)             |
| `_contract()`  | O(n)                       | O(n)             |
| `show()`       | O(n)                       | O(1)             |

##
