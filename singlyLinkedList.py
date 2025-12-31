class singlyLinkedList:
  def __init__(self,val,next=None):
    self.val=val
    self.next=next
  def __str__(self):
    return str(self.val)
Head=singlyLinkedList(1)
a=singlyLinkedList(2)
b=singlyLinkedList(3)
Head.next=a
a.next=b
curr=Head
while curr:
  print(curr)
  curr= curr.next