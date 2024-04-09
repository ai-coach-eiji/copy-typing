# コンピュータは極限を扱えないため, hを（1e-4で）近似する数値微分で計算

# 数値微分の問題点: 
# 1. 桁落ちによる誤差
# 2. 計算コストが大きい（変数ごとに微分するため）
# これを解決するために誤差逆伝播を使う

class Variable:
    def __init__(self, data):
        self.data = data

class Function:
    def __call__(self, input):
        x = input.data
        y = self.forward(x)
        output = Variable(y)
        return output

    def forward(self, x):
        raise NotImplementedError()

class Square(Function):
    def forward(self, x):
        return x ** 2

class Exp(Function):
    def forward(self, x):
        return np.exp(x)

def numerical_diff(f, x, eps=1e-4):
    x0 = Variable(x.data - eps)
    x1 = Variable(x.data + eps)
    y0 = f(x0)
    y1 = f(x1)
    return (y1.data - y0.data) / (2 * eps) # 中心差分近似: ( f(x+h) - f(x-h) ) / 2h

import numpy as np

f = Square()
x = Variable(np.array(2.0))
dy = numerical_diff(f, x)
print('x^2の微分 dy: ', dy)

def f(x):
    A = Square()
    B = Exp()
    C = Square()
    return C(B(A(x)))

x = Variable(np.array(0.5))
dy = numerical_diff(f, x)
print('合成関数 dy: ', dy) # output: 3.297（xを0.5から微小なだけ値を変化させるとyは3.297倍だけ変化する）
