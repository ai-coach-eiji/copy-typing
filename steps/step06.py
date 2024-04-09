# "y" の各変数に関する微分を求める: dy/dy, dy/db, dy/da, dy/dx

# 積の性質上, 出力から入力方向の順番で表現するのは問題ない

# この順で計算するのは "y" を重要視するため: 
# 損失関数の各パラメータ（変数）を微小な値だけ変化させた時に y がどのくらい変化するか知りたい
# つまり, （合成関数を構成する各局所関数の積で使用される）全てのパラメータの変化量を求める必要がある

class Variable:
    def __init__(self, data):
        self.data = data
        self.grad = None

class Function:
    def __call__(self, input):
        x = input.data
        y = self.forward(x)
        output = Variable(y)
        self.input = input # 入力を保持（勾配の計算時に使用するため）
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

y.grad = np.array(1.0)
b.grad = C.backward(y.grad)
a.grad = B.backward(b.grad)
x.grad = A.backward(a.grad)

print('x.grad: ', x.grad)