class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self) -> bool:
        """
        Проверяет стек на пустоту

        Выводной параметр:
        True - стек пустой, False - наоборот
        """
        return len(self.items) == 0

    def push(self, item) -> None:
        """
        Добавляет элемент в вершину стека
        """
        self.items.append(item)

    def pop(self) -> str:
        """
        Удаляет верхний элемент из стека и возвращает его

        Выводной параметр:
        верхний элемент измененного стека
        """
        if not self.is_empty():
            return self.items.pop()

    def peek(self) -> str:
        """
        Возвращает верхний элемент стека, но не удаляет его

        Выводной параметр:
        верхний элемент неизмененного стека
        """
        if not self.is_empty():
            return self.items[-1]

    def size(self) -> int:
        """
        Возвращает количество элементов в стеке

        Выводной параметр:
        количество элементов в стеке
        """
        return len(self.items)


def is_balanced(expression: str) -> str:
    """
    Проверяет сбалансированность скобок

    Выводной параметр:
    "Сбалансированно" - скобки сбалансированы, "Несбалансированно" - наоборот
    """

    stack = Stack()
    opening_brackets = "([{"
    closing_brackets = ")]}"
    bracket_pairs = {')': '(', ']': '[', '}': '{'}

    for char in expression:
        if char in opening_brackets:
            stack.push(char)
        elif char in closing_brackets:
            if stack.is_empty():
                return "Несбалансированно"
            if stack.peek() == bracket_pairs[char]:
                stack.pop()
            else:
                return "Несбалансированно"

    if stack.is_empty():
        return "Сбалансированно"
    else:
        return "Несбалансированно"


if __name__ == '__main__':

    expressions = [
        "(((([{}]))))",
        "[([])((([[[]]])))]{()}",
        "{{[()]}}",
        "}{}",
        "{{[(])]}}",
        "[[{())}]"
    ]

    # Проверка работы функции is_balanced
    for my_expression in expressions:
        print(my_expression, ' => ', is_balanced(my_expression))
