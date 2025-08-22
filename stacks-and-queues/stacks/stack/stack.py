class Stack:
    def __init__(self):
        self.__stack = [] 
        self.__size = 0

    def __is_empty(self):
        return self.__size == 0

    def push(self, value):
        self.__size += 1
        self.__stack.append(value)

    def pop(self):
        if self.__is_empty():
            raise Exception("cannot pop from empty stack")

        self.__size -= 1
        return self.__stack.pop() 

    def size(self):
        return self.__size
