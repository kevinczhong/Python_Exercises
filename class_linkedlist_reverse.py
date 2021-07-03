import ListNode

class Solution:
    def Reverse(self, head):
        curr = None
        while head != None:
            temp = head.next
            head.next = curr
            curr = head
            head = temp
        return curr

s_head = ListNode.ListNode(1)
s_head.next = ListNode.ListNode(2)
s_head.next.next = ListNode.ListNode(3)

print("here is the input")
input = s_head
while input != None:
    print(input.value)
    input = input.next

s = Solution()
result = s.Reverse(s_head)
print("reverse the list")
while result != None:
    print(result.value)
    result = result.next 