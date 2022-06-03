# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        - Get the numbers from two linked list
            - traverse the linked list and generate the numbers
            - insert new items in the first index of the array
        - Get the two numbers and add it
        - return the number as a linked list
        """
        added_number = self.traverseAndReturnTheList(l1) + self.traverseAndReturnTheList(l2)
        new_linked_list = None
        added_number = str(added_number)[::-1]

        for item in added_number:
            # print(self.insert_into_linked_list(new_linked_list, int(item)))
            new_linked_list = self.insert_into_linked_list(new_linked_list, int(item))

        return new_linked_list

    def traverseAndReturnTheList(self, givenlist: ListNode):
        current = givenlist
        temp = ""
        while current:
            temp = f'{current.val}{temp}'
            current = current.next
        return int(temp)

    def insert_into_linked_list(self, givenlist: Optional[ListNode], value: int):

        current = givenlist
        if not current:

            givenlist = ListNode(value)

        else:

            while current.next:
                current = current.next
            current.next = ListNode(value)

        print(givenlist)

        return givenlist
