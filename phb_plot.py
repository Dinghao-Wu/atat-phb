import numpy as np
import matplotlib.pyplot as plt

# 读取 phb 输出
data = np.loadtxt('phase_645_40.out')
T = data[:, 0]
x1 = 200/(5 + data[:, 2])
x2 = 200/(5 + data[:, 3])

# 画图（限制浓度范围）
plt.plot(x1, T, 'o-', label='x1 (phase α)')
plt.plot(x2, T, 'o-', label='x2 (phase β)')
plt.xlabel('Concentration x')
plt.ylabel('Temperature / K')
plt.title('Phase diagram from phb')
plt.xlim(40, 45)
 # ← 这里设置为论文的浓度范围
plt.ylim(200, max(T)*1.05)
plt.legend()
plt.grid(True)
plt.show()
