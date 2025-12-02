def even_odd(n):
    if (n & 1)==0:
        return "even"
    else:
        return "odd"
if __name__=='__main__':
    n=int(input("enter the number: "))
    print(even_odd(n))