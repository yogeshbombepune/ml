import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2.*np.pi, 2.*np.pi, 100)
y = np.sin(x)

# plt.plot(x, y)
# plt.show()

y = np.cos(x)

plt.plot(x, y)
# plt.show()
plt.savefig('myplt.pdf')