# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr, prev = head, None
        # print(node, prev)

        # node의 값이 없을때 까지 반복문을 통해
        while curr:
            # 현재 노드에 저장된 next 값은 변수에 할당해둔 채
            next = curr.next
            # 현재 노드의 next 값에 이전 노드 할당
            curr.next = prev

            # 반복적으로 위의 로직을 이루기 위해 prev 를 curr로 업데이트
            prev = curr

            # 현재 노드를 next node가 넘어가서  현재 노드가 None 상태가 될때 까지 계속 반복
            curr = next

        return prev