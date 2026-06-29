import textwrap
string="ABCDEFGHIJKLIMNOQRSTUVWXYZ"
width=4

def text_wrap(string,width):
    res=textwrap.fill(string, width)
    return res

print(text_wrap(string,width))