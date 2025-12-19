from collections import deque
from typing import Any, Optional


class Stack:
    def __init__(self):
        self._data = []

    def push(self, item: Any) -> None:
        self._data.append(item)

    def pop(self) -> Any:
        if self.is_empty():
            raise IndexError("Стек пустой")
        return self._data.pop()

    def peek(self) -> Optional[Any]:
        if self.is_empty():
            return None
        return self._data[-1]

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def size(self) -> int:
        return len(self._data)

    def __repr__(self) -> str:
        return f"Stack({self._data})"

    def __str__(self) -> str:
        return f"Stack(вершина ->{self._data[-1] if self._data else 'пусто'})"

    def __len__(self) -> int:
        return len(self._data)


class Queue:
    def __init__(self):
        self._data = deque()

    def enqueue(self, item: Any) -> None:
        self._data.append(item)

    def dequeue(self) -> Any:
        if self.is_empty():
            raise IndexError("Пустая очередь")
        return self._data.popleft()

    def peek(self) -> Optional[Any]:
        if self.is_empty():
            return None
        return self._data[0]

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def size(self) -> int:
        return len(self._data)

    def __repr__(self) -> str:
        return f"Queue({list(self._data)})"

    def __str__(self) -> str:
        return f"Queue(начало -> {self._data[0] if self._data else 'пусто'})"

    def __len__(self) -> int:
        return len(self._data)


if __name__ == "__main__":

    print("Тестирование Stack")
    stack = Stack()

    stack.push(10)
    stack.push(20)
    stack.push(30)

    print(f"Длина стека: {len(stack)}")
    print(f"Верхний элемент: {stack.peek()}")

    popped = stack.pop()
    print(f"Извлеченный элемент: {popped}")
    print(f"Длина после pop: {len(stack)}")
    print(f"Пустой ли стек: {stack.is_empty()}")

    stack.pop()
    stack.pop()
    print(f"Пустой ли стек после очистки: {stack.is_empty()}")

    try:
        stack.pop()
    except IndexError as e:
        print(f"Ошибка при pop из пустого стека: {e}")

    print()

    print("Тестирование Queue")
    queue = Queue()

    queue.enqueue("первый")
    queue.enqueue("второй")
    queue.enqueue("третий")

    print(f"Длина очереди: {len(queue)}")
    print(f"Первый элемент: {queue.peek()}")

    dequeued = queue.dequeue()
    print(f"Извлеченный элемент: {dequeued}")
    print(f"Длина после dequeue: {len(queue)}")
    print(f"Пустая ли очередь: {queue.is_empty()}")

    queue.dequeue()
    queue.dequeue()
    print(f"Пустая ли очередь после очистки: {queue.is_empty()}")

    try:
        queue.dequeue()
    except IndexError as e:
        print(f"Ошибка при dequeue из пустой очереди: {e}")
