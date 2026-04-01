def calculate(a,b):
    def add():
        return (a+b)
    def sub():
        return (a-b)
    def mul():
        return (a*b)
    return add(), sub(), mul()

res=calculate(10,5)
print("\n".join(str(r) for r in res))