# 逆伝播の自動化
# Define-by-Run: 計算（で使用される変数や関数）のつながり（生みの親）をその計算が行われるタイミングで作る仕組み
# ここでは変数（Variable）につながりを記録している

class Variable:
    def __init__(self, data):
        self.data = data
        self.grad = None
        self.creator = None

    def set_creator(self, func):
        self.creator = func

class Function:
    def __call__(self, input):
        x = input.data
        y = self.forward(x)
        output = Variable(y)
        output.set_creator(self) # 生みの親として自身を設定する
        self.input = input 
        self.output = output # 次のステップで使用
        return output
    
    def forward(self, x):
        raise NotImplementedError()

    def backward(self, gy):
        raise NotImplementedError()

class Square(Function):
    def forward(self, x):
        y = x ** 2
        return y
    
    def backward(self, gy):
        x = self.input.data
        gx = 2 * x * gy
        return gx

class Exp(Function):
    def forward(self, x):
        y = np.exp(x)
        return y
    
    def backward(self, gy):
        x = self.input.data
        gx = np.exp(x) * gy
        return gx


import numpy as np

A = Square()
B = Exp()
C = Square()

x = Variable(np.array(0.5))
a = A(x)
b = B(a)
y = C(b)

# 逆向きに計算グラフのノードを辿る
assert y.creator == C
assert y.creator.input == b 
assert y.creator.input.creator == B
assert y.creator.input.creator.input == a
assert y.creator.input.creator.input.creator == A
assert y.creator.input.creator.input.creator.input == x

y.grad = np.array(1.0)

C = y.creator
b = C.input
b.grad = C.backward(y.grad)
B = b.creator
a = B.input
a.grad = B.backward(b.grad)
A = a.creator
x = A.input
x.grad = A.backward(a.grad)
print("x grad: ", x.grad)