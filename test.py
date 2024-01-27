def add(a,b,**kwargs):
    return a+b+kwargs["a"]

print(add(a=1, b=2, c=3, a=5))