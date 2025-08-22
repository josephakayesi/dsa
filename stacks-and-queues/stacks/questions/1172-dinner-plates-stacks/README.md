### Dinner Plates Stacks (Revisit)

### Question

[Leetcode – Dinner Plate Stacks](https://leetcode.com/problems/dinner-plate-stacks/)

### Thought Process

I will maintain a collection of stacks, stored inside a `setOfStacks` array. Each individual stack can hold elements up to a fixed capacity.

- **Insertion (Push):**
  For the naive approach, whenever an item needs to be inserted, I will loop over the stacks in `setOfStacks` and check each stack’s capacity. Once I find a stack that isn’t full, I insert the element there. If all stacks are full, I create a new stack and append it to `setOfStacks`.

- **PopAt (Pop from a specific stack):**
  I will access the stack at the given index in `setOfStacks`. If the stack has elements, I pop from it. If the stack is empty or the index is invalid, I return `-1`.

---

### Post-Mortem

#### Date:

August 22, 2025

#### Approaches Tried:

#### Was the Final Solution Optimal?:

#### Time to Design Algorithm (min):

#### Time to Write Complete Code (min):

#### Total Time (min):

#### Rubric Rating (self-assessment):

#### What Could I Have Done Differently?:

#### Triggers or Mid-Problem Insights:

#### Key Takeaways:

Use a heap to keep track of avaialble stacks to push

#### Additions to My Study Sheet:

#### Bugs Encountered (for bug list):

---

Would you like me to also **add time/space complexity analysis** into the “Thought Process” section (so you capture it for future reference)?
