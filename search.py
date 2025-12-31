class search:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next
    def __str__(self):
        return str(self.val)
head=search(1)
a=search(2)
b=search(3)
head.next=a 
a.next=b
def searchHead(head,val):
    curr=head
    while curr:
        if val==head.val:
            return True
        curr=curr.next
    return False
print(searchHead(head,5))