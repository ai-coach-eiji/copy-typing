# 3つの改善
# 1. Pythonの関数として利用（関数内でクラスのインスタンス化を行い、作業の手間を省く）
# 2. 逆伝播の簡略化（dy=1 を省略するためにbackwardメソッドに np.ones_like を使用）
# 3. ndarrayだけを扱う（ためにVariableクラスの初期化メソッドに isinstance を使用）
# 3の変更に伴い、0次元のndarrayには注意する（numpy.float64になってしまうため、便利関数でndarrayに変換する）

class Variable:
    def __init__(self, data):
        if data is not None:
            if not isinstance(data, np.ndarray):
                raise TypeError(f"{type(data)} is not supported")

        self.data = data
        self.grad = None
        self.creator = None

    def set_creator(self, func):
        self.creator = func
    
    def backward(self):
        if self.grad is None:
            self.grad = np.ones_like(self.data) # 同じ形状かつ同じデータ型で、要素が1のndarrayインスタンス

        funcs = [self.creator]
        while funcs:
            f = funcs.pop()
            x, y = f.input, f.output
            x.grad = f.backward(y.grad)

            if x.creator is not None:
                funcs.append(x.creator)

def as_array(x):
    if np.isscalar(x):
        return np.array(x)
    return x

class Function:
    def __call__(self, input):
        x = input.data
        y = self.forward(x)
        output = Variable(as_array(y))
        output.set_creator(self)
        self.input = input 
        self.output = output
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

def square(x):
    f = Square()
    return f(x)

def exp(x):
    f = Exp()
    return f(x)

import numpy as np

x = Variable(np.array(0.5))
# x = Variable(0.5) # データ型がndarrayではないため例外を発生（TypeError: <class 'float'> is not supported）

y = square(exp(square(x)))
y.backward()
print("x grad: ", x.grad)

