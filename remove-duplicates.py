class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        current = head

        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next  # skip duplicate
            else:
                current = current.next  # move forward

        return head

def build_list(values):
    dummy = ListNode()
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


def print_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    print(res)


head = build_list([1, 1, 2, 3, 3])
solution = Solution()
print_list(solution.deleteDuplicates(head))  # [1, 2, 3]