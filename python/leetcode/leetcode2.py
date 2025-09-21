from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_list = []
        l2_list = []
        while l1:
            l1_list.append(l1.val)
            l1 = l1.next
        while l2:
            l2_list.append(l2.val)
            l2 = l2.next
        sum_str = str(int(''.join(map(str, reversed(l1_list)))) + int(''.join(map(str, reversed(l2_list)))))
        reversed_sum_list = [int(sum_str[i]) for i in reversed(range(len(sum_str)))]
        print(reversed_sum_list)
        head = ListNode(val=reversed_sum_list[0])
        curr = head
        for i in range(len(reversed_sum_list) - 1):
            curr.next = ListNode(val=reversed_sum_list[i + 1])
            curr = curr.next
        return head

l1_1 = ListNode(2)
l1_2 = ListNode(4)
l1_3 = ListNode(3)
l1_1.next = l1_2
l1_2.next = l1_3

l2_1 = ListNode(5)
l2_2 = ListNode(6)
l2_3 = ListNode(4)
l2_1.next = l2_2
l2_2.next = l2_3

print(Solution().addTwoNumbers(l1_1, l2_1).val)




