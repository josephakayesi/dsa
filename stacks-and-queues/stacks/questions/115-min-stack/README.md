### Stack Min

### Question

[Leetcode – Min Stack](https://leetcode.com/problems/min-stack/)

---

### Thought Process

To efficiently retrieve the minimum element from the stack at any time, we maintain an **auxiliary stack** (`min_stack`) alongside the regular stack (`stack`).

- **Push operation**:

  - If the stack is empty, we push the value onto both `stack` and `min_stack`.
  - If the new value is less than or equal to the top of `min_stack`, we also push it onto `min_stack`.
  - Otherwise, we only push to `stack`.

- **Pop operation**:

  - Remove the top element from `stack`.
  - If the popped value is equal to the top of `min_stack`, we also pop from `min_stack`.

- **Top operation**:

  - Simply return the last element of `stack`.

- **Get Min operation**:

  - Return the top of `min_stack`, which always holds the current minimum.

This ensures that at any time, `min_stack` mirrors the minimums of `stack`.

---

### Implementation

```python
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
            self.min_stack.append(val)
            return

        current_min = self.min_stack[-1]

        if val <= current_min:
            self.min_stack.append(val)

        self.stack.append(val)

    def pop(self) -> None:
        top = self.stack.pop()
        if top == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
```

---

### Complexity Analysis

- **Time Complexity**:

  - `push()`: **O(1)**
  - `pop()`: **O(1)**
  - `top()`: **O(1)**
  - `getMin()`: **O(1)**

- **Space Complexity**:

  - In the worst case, every pushed element could be smaller (or equal) than the previous ones, meaning all elements end up in both `stack` and `min_stack`.
  - Thus, total space usage is **O(n)**, where `n` is the number of elements in the stack.

---
