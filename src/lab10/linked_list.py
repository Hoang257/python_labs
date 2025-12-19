class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"Node({self.value})"


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self._size = 0
        self._tail = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node

        self._size += 1

    def prepend(self, value):
        new_node = Node(value, self.head)
        self.head = new_node

        if self._tail is None:
            self._tail = new_node

        self._size += 1

    def insert(self, idx, value):
        if idx < 0:
            raise IndexError("Индекс меньше нуля")
        if idx > self._size:
            raise IndexError("Индекс больше длины коллекции")

        if idx == 0:
            self.prepend(value)
            return

        if idx == self._size:
            self.append(value)
            return

        curr = self.head
        for _ in range(idx - 1):
            curr = curr.next

        new_node = Node(value, next=curr.next)
        curr.next = new_node
        self._size += 1

    def get(self, idx):
        if idx < 0 or idx >= self._size:
            raise IndexError("Индекс вне диапазона")

        curr = self.head
        for _ in range(idx):
            curr = curr.next

        return curr.value

    def remove_at(self, idx):
        if idx < 0 or idx >= self._size:
            raise IndexError("Индекс вне диапазона")

        if idx == 0:
            value = self.head.value
            self.head = self.head.next
            self._size -= 1

            if self.head is None:
                self._tail = None

            return value

        curr = self.head
        for _ in range(idx - 1):
            curr = curr.next

        value = curr.next.value
        curr.next = curr.next.next

        if curr.next is None:
            self._tail = curr

        self._size -= 1
        return value

    def remove(self, value):

        if self.head is None:
            return False

        if self.head.value == value:
            self.head = self.head.next
            self._size -= 1

            if self.head is None:
                self._tail = None

            return True

        curr = self.head
        while curr.next is not None and curr.next.value != value:
            curr = curr.next

        if curr.next is None:
            return False

        curr.next = curr.next.next
        self._size -= 1

        if curr.next is None:
            self._tail = curr

        return True

    def find(self, value):

        curr = self.head
        idx = 0

        while curr is not None:
            if curr.value == value:
                return idx
            curr = curr.next
            idx += 1

        return -1

    def clear(self):

        self.head = None
        self._tail = None
        self._size = 0

    def is_empty(self):

        return self._size == 0

    def __iter__(self):

        curr = self.head
        while curr:
            yield curr.value
            curr = curr.next

    def __len__(self):

        return self._size

    def __str__(self):

        if self.head is None:
            return "None"

        return " -> ".join(f"[{value}]" for value in self) + " -> None"

    def __repr__(self):

        vals = list(self)
        return f"SinglyLinkedList({vals})"

    def __getitem__(self, idx):
        return self.get(idx)


if __name__ == "__main__":
    lst = SinglyLinkedList()
    print(f"Пустой список: {lst}")
    print(f"Длина: {len(lst)}")

    lst.append(10)
    lst.append(20)
    lst.append(30)
    print(f"После append 10,20,30: {lst}")
    print(f"Длина: {len(lst)}")

    lst.prepend(5)
    print(f"После prepend 5: {lst}")
    print(f"Длина: {len(lst)}")

    lst.insert(2, 15)
    print(f"После insert 15 на позицию 2: {lst}")
    print(f"Длина: {len(lst)}")

    print("Итерация по списку:")
    for item in lst:
        print(f"  {item}")

    print(f"repr: {repr(lst)}")
