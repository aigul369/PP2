#1
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
#2
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

#3
print(bool("Hello"))
print(bool(15))

#4
x = "Hello"
y = 15

print(bool(x))
print(bool(y))

#5
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])