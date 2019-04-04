# Class Practice _ Calculator
numOne = int(input("First Number: "))
numTwo = int(input("Second Number: "))

class FourCal:
    def setdata(self, numOne, numTwo):
        self.numOne = numOne
        self.numTwo = numTwo

    def sum(self):
        result = numOne + numTwo
        return result

    def mul(self):
        result = numOne * numTwo
        return result

    def sub(self):
        result = numOne - numTwo
        return result

    def div(self):
        result = numOne / numTwo
        return result

a = FourCal()
print(a.sum())
print(a.mul())
print(a.sub())
print(a.div())