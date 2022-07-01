import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# parameters
omega = 1.4
T = 2 * np.pi / omega

def duffing(u, t, A, B, C, D, E):
    x, v = u
    a = - 4 * A * (x**3) + 2 * B * x - C * v + D * np.cos(E * t)
    return v, a

r0 = [0, 0]

t = np.arange(0, 25000 * T, T)
r_t = odeint(duffing, r0, t, args=(0.25, 0.5, 0.1, 0.39, omega))

x = r_t[:, 0]
v = r_t[:, 1]

plt.scatter(x, v, marker = '.')
plt.xlabel('x(t)')
plt.ylabel('v(t)')
plt.show()
