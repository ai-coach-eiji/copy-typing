# "不確かさ"に立ち向かうために「確率」を使う（完全な予測は難しいので）

# 確率変数: 取り得る値が確率的に決まる変数（サイコロの場合、取り得る値は1 ~ 6）
# 確率分布: 起こり得る全ての値に対してその確率が示されたもの（サイコロの場合 p(1) = 1/6）
# 一様分布: 取り得る確率が全て同じである確率分布（サイコロの場合、各目の出る確率は1/6）

# p(x)が表すもの: 離散型の確率変数の場合は「確率」, 連続型の場合は「確率密度」

# 観測値: 確率分布から実際に得られるひとつひとつの値
# 期待値: 一回の観測で得られる値の平均値（サイコロの場合、21/6=3.5）

# --- 期待値（Expected Value）の定義式 ---
# 離散型確率分布の場合: E[x] = Σ{x_k * p(x_k)} (k=1からNまで)
# 連続型確率分布の場合: E[x] = ∮{x * p(x)}dx (-∞から∞まで)

# 分散: 確率変数の取る値が期待値μの周りにどの程度ばらつくかを表す
#（分散が小さい = 確率変数の取り得る値が期待値の周辺に集まる）

# --- 分散（Variance）の定義式 ---
# 離散型確率分布の場合: Var[x] = E[(x - μ)^2] = Σ{(x_k - μ)^2 * p(x_k)} (k=1からNまで)
# 連続型確率分布の場合: Var[x] = E[(x - μ)^2] = ∮{(x - μ)^2 * p(x)}dx (-∞から∞まで)

# パラメータ: 確率分布の形状を決めるもの（正規分布の場合、μとσ）
# パラメータを関数の引数に加えるときは、セミコロンの右側に書く（確率変数と区別するため）

# --- 正規分布（Normal Distribution）の定義式 ---
# N(x; μ, σ) = 1 / {(√2π) * σ} * exp(-(x-μ)^2 / 2σ^2)

# 標準正規分布: 平均が0、標準偏差が1の正規分布
# 平均0を中心に左右対称の山を形成し、曲線の形は釣り鐘（Bell Curve）とも呼ばれる
# N(x; μ=0, σ=1) = 1 / (√2π) * exp(-(x^2 / 2))


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

# パラメータの役割
# 1. σを固定してμの値を変化させる
# 形状は同じだが、確率密度の最大値（山のピーク = μの位置）が異なる

x = np.linspace(-10, 10, 1000)
y0 = normal(x, mu=-3)
y1 = normal(x, mu=0)
y2 = normal(x, mu=5)

plt.plot(x, y0, label="$\mu$=-3")
plt.plot(x, y1, label="$\mu$=0")
plt.plot(x, y2, label="$\mu$=5")

plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.show()

# 2. μを固定してσを変化させる
# 山の形状が変わる（σを大きくすると左右に広がる）

y0 = normal(x, mu=0, sigma=0.5)
y1 = normal(x, mu=0, sigma=1)
y2 = normal(x, mu=0, sigma=2)

plt.plot(x, y0, label="$\sigma$=0.5")
plt.plot(x, y1, label="$\sigma$=1")
plt.plot(x, y2, label="$\sigma$=2")

plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.show()
