# ユーザにリストを用意させない（直感的に使用できるようにする）
# プログラマはクラス（Addなど）を実装しやすくするために基底クラスを修正

import numpy as np

class Function:
    def __call__(self, *inputs):
        xs = [x.data for x in inputs]
        ys = self.forward(*xs) # 修正1. リストのアンパック
        if not isinstance(ys, tuple): # 修正2. タプルではない時の追加対応
            ys = (ys,)
        outputs = [Variable(as_array(y)) for y in ys]

        for output in outputs:
            output.set_creator(self)
        self.inputs = inputs
        self.outputs = outputs
        return outputs if len(outputs) > 1 else outputs[0]
    
    def forward(self, xs):
        raise NotImplementedError()

    def backward(self, gys):
        raise NotImplementedError()

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

class Add(Function):
    def forward(self, x0, x1):
        y = x0 + x1
        return y

x0, x1 = Variable(np.array(2)), Variable(np.array(3))
f = Add()
y = f(x0, x1)
print('クラスの結果: ', y.data)

# AddクラスをPythonの関数として使う
def add(x0, x1):
    return Add()(x0, x1)

y = add(x0, x1)
print('関数の結果: ', y.data)