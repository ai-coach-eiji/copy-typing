# "不確かさ"に立ち向かうために「確率」を使う（完全な予測は難しいので）
# 確率変数: 取り得る値が確率的に変わるもの（サイコロの場合は取り得る値は1 ~ 6）
# 確率分布: 起こり得る全ての値に対してその確率が示されたもの（サイコロの場合 p(1)= 1/6）
# 一様分布: 取り得る確率が全て同じである確率分布（サイコロの場合、各目の出る確率は1/6）

# p(x)が表すもの: 離散型の確率変数の場合は「確率」, 連続型の場合は「確率密度」

import numpy as np
import matplotlib.pyplot as plt

def normal(x, mu=0, sigma=1):
    y = 1 / (np.sqrt(2 * np.pi) * sigma) * np.exp(-(x - mu)**2 / (2 * sigma**2))
    return y

x = np.linspace(-5, 5, 100)
y = normal(x)

plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.show()