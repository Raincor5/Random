class Node:
    def __init__(self, data):
        self.data = data  # Initialize the node with the provided data.
        self.next = None  # Initialize the next pointer to None.

class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the linked list with an empty head node.

    def insert_at_beginning(self, data):
        """
        Inserts a new node with the given data at the beginning of the linked list.
        """
        new_node = Node(data)  # Create a new node with the provided data.
        new_node.next = self.head  # Point the new node's next pointer to the current head.
        self.head = new_node  # Update the head to the newly inserted node.

    def delete_at_beginning(self):
        """
        Deletes the node at the beginning of the linked list.
        """
        if self.head:  # Check if the linked list is not empty.
            temp = self.head  # Store the current head node.
            self.head = self.head.next  # Move the head to the next node.
            temp.next = None  # Disconnect the original head node.
            del temp  # Delete the original head node.

    def insert_at_position(self, data, position):
        """
        Inserts a new node with the given data at the specified position in the linked list.
        """
        if position <= 0:
            print("Invalid position")  # Print an error message for invalid position.
            return
        new_node = Node(data)  # Create a new node with the provided data.
        if position == 1:  # If the position is 1 (insert at the beginning),
            new_node.next = self.head  # Point the new node's next pointer to the current head.
            self.head = new_node  # Update the head to the newly inserted node.
        else:
            current = self.head  # Start from the head of the linked list.
            count = 1  # Initialize a count variable for position tracking.
            while count < position - 1 and current:
                current = current.next  # Traverse the list until the desired position.
                count += 1
            if current:  # If the position is valid within the list,
                new_node.next = current.next  # Point the new node's next to the next node of the current node.
                current.next = new_node  # Update the current node's next to the new node.
            else:
                print("Invalid position")  # Print an error message for invalid position.

    def delete_at_position(self, position):
        """
        Deletes the node at the specified position in the linked list.
        """
        if position <= 0 or not self.head:
            print("Invalid position")  # Print an error message for invalid position or empty list.
            return
        if position == 1:  # If the position is 1 (delete the beginning node),
            temp = self.head  # Store the current head node.
            self.head = self.head.next  # Move the head to the next node.
            temp.next = None  # Disconnect the original head node.
            del temp  # Delete the original head node.
        else:
            current = self.head  # Start from the head of the linked list.
            count = 1  # Initialize a count variable for position tracking.
            while count < position - 1 and current.next:
                current = current.next  # Traverse the list until the node before the desired position.
                count += 1
            if current.next:  # If the position is valid within the list,
                temp = current.next  # Store the node to be deleted.
                current.next = current.next.next  # Update the current node's next pointer.
                temp.next = None  # Disconnect the node to be deleted.
                del temp  # Delete the node to be deleted.

    def search(self, target):
        """
        Searches for a node with the given target data in the linked list.
        """
        current = self.head  # Start from the head of the linked list.
        while current:  # Traverse the list until the end.
            if current.data == target:  # If the current node's data matches the target,
                return True  # Return True indicating the target is found.
            current = current.next  # Move to the next node.
        return False  # Return False if the target is not found in the list.

    def reverse(self):
        """
        Reverses the linked list.
        """
        prev = None  # Initialize a pointer to the previous node (initially None).
        current = self.head  # Start from the head of the linked list.
        while current:  # Traverse the list until the end.
            next_node = current.next  # Store the next node in the original list.
            current.next = prev  # Reverse the next pointer of the current node.
            prev = current  # Move the previous pointer to the current node.
            current = next_node  # Move to the next node in the original list.
        self.head = prev  # Update the head to the last node, which becomes the first node after reversal.
