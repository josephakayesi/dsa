from stack import Stack

if __name__ == "__main__":
    stack = Stack()
    stack.push(2)
    stack.push(4)
    stack.push(8)

    assert stack.pop() == 8
    assert stack.pop() == 4
    assert stack.size() == 1
    assert stack.pop() == 2
    assert stack.size() == 0

    try:
        stack.pop()
        assert False, "Expected an exception but none was raised"
    except Exception as e:
        assert str(e) == "cannot pop from empty stack"