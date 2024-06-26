class Variable:
    def __init__(self, data):
        self.data = data

class Function:
    def __call__(self, input): # callメソッドの役割: Variableからデータを取り出し, 結果をVariableに詰める
        x = input.data
        y = self.forward(x)
        output = Variable(y)
        return output

    def forward(self, x):
        raise NotImplementedError()

class Square(Function):
    def forward(self, x):
        return x ** 2

import numpy as np

x = Variable(np.array(10))
f = Square()
y = f(x)

print("type(y): ", type(y))
print("y.data: ", y.data)