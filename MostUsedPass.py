import Node
import linkedList

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

# Main method in charge of sending the linked list as a parameter to sort list.
def main():

    passwords = linkedList()
    read_file(passwords)
    length = length_linked_list(passwords)
    mergeSort(passwords, 0, length)
    print_list(passwords)

# Reading the passwrds.txt file 
def read_file(passwords):

    with open('passwords.txt', 'r') as f:
        f_contents = f.read()
        print(f_contents)

# Length of the list 
def length_linked_list(passwords):
    temp = list.head
    count = 0

    while temp:
        count += 1
        temp = temp.next
    return count

# Printing the top 20 passwords 
def print_list(passwords):

    node = passwords.head

    for i in range(20):
        print(node.item)
        node = node.next

# Time complexity of sorting O(nlogn)
def mergeSort(head):
    
    if(head.val == -1):
        return    
    if(head is None or head.next is None):
        return head
    
    # Partitioning the list to half 
    list1, list2 = divideList(head)
    # Sorting individual portion of the list 
    list1 = mergeSort(list1)
    list2 = mergeSort(list2)
    head = merge(list1, list2)
    return head

 # Helper method for the merge sort    
def divideList(head):
    slow = head
    fast = head
    
    if fast and fast.val != -1:
        fast = fast.next
    while fast and fast.val != -1:
        fast = fast.next
        if fast:
            fast = fast.next
            slow = slow.next
    mid = slow.next
    slow.next = None
    return head, mid

# Merging two lists 
def merge(l1, l2):     
    temp = None
    if(l1 is None):        
        return l2
    if(l2 is None):
         return l1
     
    if(l1.val <= l2.val):
        temp = l1
        temp.next = merge(l1.next, l2)
    else:
         temp = l2
         temp.next = merge(l1, l2.next)
    return temp
   
