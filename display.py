class display:
    def __init__(self,val, next=None):
        self.val=val
        self.next=next
    def __str__(self):
        return str(self.val)
Head=display(1)
a=display(2)    
b=display(3)
Head.next=a
a.next=b
curr=Head
ele=[]
while curr:
    ele.append(str(curr.val))
    curr= curr.next
print("".join(ele))