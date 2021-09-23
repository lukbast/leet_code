class Node:
    def __init__(self, data, next_node=None):
        """
        Create new instance of singly linked list node

        :param data: data to contain in newly created node
        :param next_node: pointer to next node in linked list
        """
        self.data = data
        self.next_node = next_node


class SinglyLinkedList:

    def __init__(self):
        """
        Create new instance of Singly Linked List
        """
        self.head = None
        self.tail = None

    def append(self, value: any) -> None:
        """
        Creates a new Node with provided value and appends it to the
        end of Linked List

        :param value: any - value to append to a Linked List
        :return: None
        """
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            value_to_add = Node(value)
            self.tail.next_node = value_to_add
            self.tail = value_to_add

    def append_node(self, node: Node) -> None:
        """
        Takes already created node and append it to an end of the
        Linked List

        :param node: Node - already created Linked list node
        :return: None
        """

        if self.head is None:
            self.head = node
            self.tail = self.head
        else:
            self.tail.next_node = node
            self.tail = node

    def insert(self, value: any, position: int):
        """
        Insert provided value into Linked List at specified position.
        Positions start at 0 and positions have to be continuous.

        If you want add value to the end of the Linked list insert()
        won't work. In that case use append()
        for better time complexity: append -> O(1), insert -> O(n)

        In case inserting to 0 position
        insert have time complexity O(1)

        :param value: any - Value to add to a Linked List
        :param position: int - position where new value should be added
        :return: Boolean - if value was inserted returns true, returns false otherwise
        """
        if position == 0:
            value_to_add = Node(value, self.head)
            self.head = value_to_add
            return True

        current = self.head
        current_position = 0
        while current:
            if current_position + 1 == position:
                value_to_add = Node(value, current.next_node)
                current.next_node = value_to_add
                return True
            current = current.next_node
        return False

    def display_values(self) -> None:
        """
        Prints all values with their positions in Linked List to the console

        :return: None
        """
        print("="*40)
        current = self.head
        current_position = 0
        while current:
            print(f'{current_position}: {current.data}')
            current_position += 1
            current = current.next_node
        print("="*40)

    def remove(self, value):
        """
        Iterates over linked list, and when encounters node with data
        that equals provided value remove it form linked list and
        returns True.

        If node that contains data matching provided value wasn't found
        returns False

        :param value: any - value to remove from linked list
        :return: Boolean - True if value was found and deleted, otherwise
          returns true
        """
        current = self.head
        while current:
            if current.next_node.data == value:
                current.next_node = current.next_node.next_node
                return True
            current = current.next_node
        return False

    def remove_with_position(self, position):
        """
        Iterates over linked list, and when encounters node with position
        that equals provided integer remove it form linked list and
        returns True.

        :param position: int - position to remove from Linked List
        :return: Boolean - True if node with provided position was
          deleted, False if otherwise
        """

        if position == 0:
            self.head = self.head.next_node
            return True

        current = self.head
        current_position = 0
        while current.next_node:
            if current_position + 1 == position:
                current.next_node = current.next_node.next_node
                return True
            current = current.next_node
            current_position += 1
        return False

    def length(self) -> int:
        """
        Returns number of records in the linked list

        :return: int - number of positions
        """

        length = 1
        current = self.head
        while current.next_node:
            length += 1
            current = current.next_node
        return length

    def find(self, value):
        """
        returns True if provided value is in Linked List, otherwise returns False

        :param value: value to find
        :return: boolean
        """
        current = self.head
        while current:
            if current.data == value:
                return True
            current = current.next_node
        return False

    def get(self, position: int) -> any:
        """
        Takes an position and returns value of node on that position

        Returns None if provided position don't exist on the list

        :return: any - value held in provided position
        """

        current = self.head
        current_position = 0
        while current:
            if current_position == position:
                return current.data
            current = current.next_node
            current_position += 1

    def append_head(self) -> None:
        """
        Remove head and append its as tail to the Linked List

        :return: None
        """

        current_node = self.head
        self.append_node(current_node)
        self.remove_with_position(0)
        current_node.next_node = None
        self.tail = current_node

    def reverse(self) -> None:

        """
        Reverse Linked List order
        :return: None
        """
        end_point = self.tail

        while end_point != self.head:
            if end_point.next_node:
                moved_node = self.head
                self.remove_with_position(0)
                moved_node.next_node = end_point.next_node
                end_point.next_node = moved_node
            else:
                self.append_head()


ll = SinglyLinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.display_values()

ll.reverse()

ll.display_values()

print(ll.get(2))
print(ll.get(0))
print(ll.get(4))
print(ll.get(666))

