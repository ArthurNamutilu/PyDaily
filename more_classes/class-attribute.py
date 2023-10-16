class GgClass:
    a = "This is a class attribute!"


x = GgClass()
y = GgClass()

print(x.a)
GgClass.a = "New instance"  # changing the class attribute
print(x.a)
print(y.a)
