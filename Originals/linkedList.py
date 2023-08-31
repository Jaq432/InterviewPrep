# Individual pieces' type
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# List type
class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    # Add to the end of the list
    def append(self, data):
        new_node = Node(data)
        # Make the first head
        if self.isEmpty():
            self.head = new_node
        # Add to the end of the list
        else:
            current = self.head
            # Iterate through all of the nodes for the last
            while current.next is not None:
                current = current.next
            # Add to the end
            current.next = new_node

    # Add to the beginning of the list
    def prepend(self, data):
        new_node = Node(data)
        # Create a copy of the head and make a copy as the second position
        # It looks like: 1 -> 1 -> 2
        new_node.next = self.head
        # Overwrite the first to be the new data
        # It looks like: new -> 1 -> 2
        self.head = new_node

    def delete(self, data):
        # Return early
        if self.isEmpty():
            return

        # Remove the current position that matches the data 
        # and assign the current head to the next data
        if self.head.data == data:
            self.head = self.head.next
            return

        # Go through each one to find the one that matches the data
        # if the next one is what we want to delete, set next to the next's next
        current = self.head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    # Returns if the node exists
    def search(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                return True
            current = current.next
        return False

    # Shows all of the elements in the LinkedList
    def display(self):
        elements = []
        current = self.head
        while current is not None:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements))


# Example

# Create a new linked list
my_list = LinkedList()

# Append some elements
my_list.append(5)
my_list.append(10)
my_list.append(15)

# Prepend an element
my_list.prepend(2)

# Display the linked list
my_list.display()  # Output: 2 -> 5 -> 10 -> 15

# Delete an element
my_list.delete(10)

# Search for an element
print(my_list.search(5))  # Output: True
print(my_list.search(10))  # Output: False