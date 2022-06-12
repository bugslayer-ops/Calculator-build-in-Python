import functools

class basic_method:
    def add(self):
        # x = int(input("Enter Value: "))
        # y = int(input("Enter Value: "))
        num = []
        x = ""
        while x !='q':
            x = input("Enter Value: ")
            if x == 'q':
                break
            num.append(x)
        num = list(map(int, num))
        result  = functools.reduce(lambda x,y: x+y,num)
        return result
    def subtract(self):
        num = []
        x = ""
        while x != 'q':
            x = input("Enter Value: ")
            if x == 'q':
                break
            num.append(x)
        num = list(map(int,num))
        result = functools.reduce(lambda x,y: x-y,num)
        return result
    def multiply(self):
        num = []
        x = ""
        while x != 'q':
            x  = input("Enter Value: ")
            if x == 'q':
                break
            num.append(x)
        num = list(map(int,num))
        result = functools.reduce(lambda x,y: x*y,num)
    def divide(self):
        x = int(input("Enter Value: "))
        y = int(input("Enter Value: "))
        return x/y

    
