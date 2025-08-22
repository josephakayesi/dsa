# Queue via Stacks

## Question

[CTCI – Chapter 3, Question 3.4]()

Implement a `MyQueue` class which implements a queue using two stacks.

---

## Thought Process

Maintain two stacks:

- `push_stack` – used for incoming elements.
- `pop_stack` – used for outgoing elements.

**Push Operation:**

- Add the new element to `push_stack`.

**Pop Operation:**

- If `pop_stack` is empty, move all elements from `push_stack` into `pop_stack`.
- Pop the top element from `pop_stack`.

This ensures **FIFO (First In, First Out)** behavior.

---

## Post-Mortem

**Date:** August 22, 2025

### Approaches Tried

- Created two stacks: `push_stack` and `pop_stack`.
- Push all elements into `push_stack`.
- To pop:
  - If `pop_stack` is not empty, pop directly.
  - If `pop_stack` is empty, transfer all elements from `push_stack` to `pop_stack` and then pop.

### Was the Final Solution Optimal?

Yes.

### Time

- Time to Design Algorithm: 10 min
- Time to Write Complete Code: 20 min
- Total Time: 30 min

### Rubric Rating (Self-Assessment)

- **Problem-Solving:** 4/5

  - Missed an edge case: initially moved all elements from `push_stack` to `pop_stack` based on `self.__size`. After repeated pops, `pop_stack` might already have elements, causing `IndexError`.

- **Coding:** 4/5

  - The bug with `__size` handling would fail some edge cases.

- **Verification:** 5/5

  - Successfully tested normal queue operations.

- **Communication:** 0/5
  - Did not practice explaining the solution aloud.

### What Could I Have Done Differently?

- Pay closer attention to edge cases.

### Triggers or Mid-Problem Insights

- Only transfer elements to `pop_stack` if it’s empty.

### Key Takeaways

- Always verify edge cases carefully.

### Additions to My Study Sheet

- Queue implementation using two stacks.
- Proper handling of `pop_stack` refill.

### Bugs Encountered

```python
class QueueStack:
    def __init__(self):
        self.push_stack = []
        self.pop_stack = []
        self.__size = 0

    def push(self, value):
        self.__size += 1
        self.push_stack.append(value)

    def pop(self):
        if not self.pop_stack:
            # Only transfer if pop_stack is empty
            while self.push_stack:
                self.pop_stack.append(self.push_stack.pop())

        if not self.pop_stack:
            return None  # Queue is empty

        self.__size -= 1
        return self.pop_stack.pop()

    def size(self):
        return self.__size
```
