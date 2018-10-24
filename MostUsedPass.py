# Write a program that determines the 20 most used passwords
import Node
import linkedList


def main():

    passwords = linkedList()
    read_file(passwords)
    length = length_linked_list(passwords)
    sort(passwords, 0, length)
    print_list(passwords)


def read_file(passwords):

    with open('passwords.txt', 'r') as f:
        f_contents = f.read()
        print(f_contents)


def length_linked_list(passwords):
    temp = list.head
    count = 0

    while temp:
        count += 1
        temp = temp.next
    return count


def print_list(passwords):

    node = passwords.head

    for i in range(20):
        print(node.item)
        node = node.next


def partition(passwords, first, last):
        pivot = len(passwords)//2
        part_index = first - 1

        i = first
        for i in range(last):
            if passwords(i) <= pivot:
                part_index += 1

                # Swaps if its lesser than the pivot
                temp = passwords[part_index]
                passwords[part_index] = passwords[i]
                passwords[i] = temp

        # Swap pivot element at partition index
        temp = passwords[part_index + 1]
        passwords[part_index + 1] = passwords[last]
        passwords[last] = temp
        part_index += 1
        return part_index


# Sorting the Linked List
def sort(passwords, first, last):

    if passwords is None or len(passwords) == 0:
        return passwords

        # if the segment is invalid and if there is only one element
    if first < last:

        part_index = partition(passwords, first, last)

        # Recursive call to sort the segment left to the partition index
        sort(passwords, first, part_index - 1)
        # Recursive call to sort the segment right to the partition index
        sort(passwords, part_index + 1, last)

        return passwords
