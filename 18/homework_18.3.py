
class MyStr(str):
    def __str__(self):
        return super().__str__().upper()

my_str = MyStr('test')
print(my_str)