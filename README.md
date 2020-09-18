# Gradient-Descent-for-Hawkes-Process

使用梯度下降法估计 Hawkes 参数。参考文献 Ozaki. Maximum likelihood estimation of Hawkes’ self-exciting point processes

# 模拟
`python simulation.py`：给定 Hawkes 过程参数，生成符合该参数的一组时间序列。

# 参数估计
`python gradient.py`：使用梯度下降法估计 Hawkes 过程的参数。
`refractory.py`：添加了绝对不应期的修正。

# 数据
`/data` 目录下存放有序列数据，每行的格式如下：

arrival_time channel

修改`gradient.py`主程序中的文件路径和通道编号，可以对其他数据进行估计。

# 作图
`draw.py` 定义了一些作图函数，可以绘制时间序列图以及 λ-t 图。
