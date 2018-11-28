# Node class
class Node(object):
    password = ""
    count = -1
    next = None

    def __init__(self, password, count, next):
        self.password = password
        self.count = count
        self.next = next

# Linked list class
class LinkedList:
    def __init__(self):
        self.head = None


# This method reads the file where the passwords are stored
def read_passwords_ll(password_list):
    with open('file.txt', 'r') as infile:
        for line in infile:
            line = line.split()
            if len(line) > 1:
                add_password_ll(password_list, line[1])

# This method reads the file where passwords are stored
def read_passwords_dict(password_list, my_dict):
    with open('file.txt', 'r') as infile:
        for line in infile:
            credentials = line.split()
            if len(credentials) > 1:
                add_password_dict(credentials[1], my_dict)


# This method adds all passwords to a linked list
def add_password_ll(password_list, password):
    node = password_list.head
    while node is not None:
        if node.password == password:
            node.count += 1
            return
        node = node.next
    password_list.head = Node(password, 1, password_list.head)


# This method adds every password to a dictionary
def add_password_dict(password, my_dict):
    if password in my_dict:
        my_dict[password] += 1
    else:
        my_dict[password] = 1
   


# This method gets the size of the linked list
def get_list_size(password_list):
    node = password_list.head
    linked_list_size = 0
    while node is not None:
        linked_list_size += 1
        node = node.next
    return linked_list_size


# O(n^2)
# This method runs the bubble sort algorithm
def bubble_sort(password_list, linked_list_size):
    for i in range(linked_list_size):
        cur_node = password_list.head
        nxt_node = cur_node.next

        for j in range(linked_list_size - 1):
            if cur_node.count < nxt_node.count:
                tmp_count = cur_node.count
                cur_node.count = nxt_node.count
                nxt_node.count = tmp_count
                tmp_pass = cur_node.password
                cur_node.password = nxt_node.password
                nxt_node.password = tmp_pass

            cur_node = nxt_node
            nxt_node = nxt_node.next

"""
def mergeSort(x):
    if x is None or x.next is None:
        return x

    leftHalf, rightHalf = splitTheList(x)

    left = mergeSort(leftHalf)
    right = mergeSort(rightHalf)

    return mergeTheLists(left, right)

#Splits the linked list into two
def splitTheList(x):
    if x == None or x.next == None:
        leftHalf = x
        rightHalf = None

        return leftHalf, rightHalf

    else:
        mid = x
        head = x.next

        while head != None:
            head = head.next

            if head != None:
                head = head.next
                midPointer = mid.next

    leftHalf = x
    rightHalf = mid.next
    midPointer.next = None

    return leftHalf, rightHalf

#Merges the two list once it is sorted
def mergeTheLists(leftHalf, rightHalf):
    head = Node(None)
    curr = head

    while leftHalf and rightHalf:
        if leftHalf.count < rightHalf.count:
            curr.next = leftHalf
            leftHalf = leftHalf.next

        else:
            curr.next = rightHalf
            rightHalf = rightHalf.next

        curr = curr.next

    if leftHalf == None:
        curr.next = rightHalf

    elif rightHalf == None:
        curr.next = leftHalf

    return head.next
"""

# This method inserts all components into a linked list
def into_linked_list(password_list, my_dict):
    for password in my_dict:
        node = Node(password, my_dict[password], password_list.head)
        password_list.head = node



# This method displays the passwords
def print_list(password_list):
    node = password_list.head
    limit = 0
    while node is not None and limit < 20:
        print(node.password + ":", node.count)
        node = node.next
        limit += 1

# Main method
def main():

    print(" Solution A -- Linked List ")
    password_list = LinkedList()
    read_passwords_ll(password_list)
    linked_list_size = get_list_size(password_list)
    bubble_sort(password_list, linked_list_size)
    #merge(linked_list)
    print_list(password_list)
    print("List size:", linked_list_size)

    print(" Solution B -- Dictionary ")
    linked_list_size = 0
    my_dict = {}
    password_list = LinkedList()
    read_passwords_dict(password_list, my_dict)
    into_linked_list(password_list, my_dict)
    linked_list_size = len(my_dict)
    bubble_sort(password_list, linked_list_size)
    print_list(password_list)
    print("List size:", linked_list_size)

main()
