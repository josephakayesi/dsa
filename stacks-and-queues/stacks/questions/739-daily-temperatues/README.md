# Daily Temperatures

## Question

[Leetcode - Daily Temperatures](https://leetcode.com/problems/daily-temperatures/)

Given a string containing only the characters `()[]{}`, determine if the string is valid. A string is valid if:

1. Open brackets are closed by the same type of brackets.
2. Open brackets are closed in the correct order.

---

## Thought Process

---

## Post-Mortem

**Date:** August 22, 2025

### Approaches Tried

### Was the Final Solution Optimal?

### Time

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
