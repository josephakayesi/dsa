# Valid Parentheses

## Question

[Leetcode - Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)

Given a string containing only the characters `()[]{}`, determine if the string is valid. A string is valid if:

1. Open brackets are closed by the same type of brackets.
2. Open brackets are closed in the correct order.

---

## Thought Process

- Use a **dictionary** to store matching pairs of parentheses.
- Iterate through each character in the string:
  - If the stack is not empty and the top of the stack matches the current closing bracket, **pop** the top.
  - Otherwise, **push** the current character onto the stack.
- Return `True` if the stack is empty at the end (all brackets matched), otherwise return `False`.

---

## Post-Mortem

**Date:** August 22, 2025

### Approaches Tried

- Created a dictionary `pairs` containing valid parentheses pairs.
- Used a stack to keep track of unmatched opening brackets.
- Iterated through the string and applied the pair matching logic.

### Was the Final Solution Optimal?

Yes. Using a stack is the standard and optimal solution for this problem.

### Time

- Time to Design Algorithm: 3 min
- Time to Write Complete Code: 2 min
- Total Time: 5 min

### Rubric Rating (Self-Assessment)

- **Problem-Solving:** 4/5

  - Missed skipping the `append` operation when a pair is matched in early attempts.

- **Coding:** 5/5

  - Code is clean and handles all edge cases.

- **Verification:** 5/5

  - Correctly tested multiple valid and invalid cases.

- **Communication:** 4/5
  - Explained logic in comments, but could practice verbal explanation.

### What Could I Have Done Differently?

- Carefully control the loop to **avoid appending characters after a successful match**.
- Add more explicit comments for clarity.

### Triggers or Mid-Problem Insights

- Using `stack and stack[-1] == pairs.get(char)` is a concise way to check for a match.

### Key Takeaways

- Stack-based approaches are very effective for matching nested structures.
- Always consider edge cases like empty strings or strings starting with a closing bracket.

### Additions to My Study Sheet

- Stack usage for valid parentheses problems.
- Dictionary-based pair matching.

### Bugs Encountered

- Initially forgot to `continue` after a successful match, which caused the character to be appended unnecessarily.

---

## Final Solution

```python
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pairs = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        stack = []

        for char in s:
            # If current char is a closing bracket and matches the top of stack
            if stack and stack[-1] == pairs.get(char):
                stack.pop()
                continue

            # Otherwise, push the current char onto the stack
            stack.append(char)

        # If stack is empty, all brackets matched
        return not stack
```
