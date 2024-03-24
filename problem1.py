import numpy as np
from matplotlib import pyplot as plt
import utils


l1 = np.sqrt(47.5 ** 2 + (76 - 12) ** 2)
l2 = 14.0
l3 = 80.0
l4 = 51.26
theta1 = np.degrees(np.arctan2(76 - 12, 47.5))
w2 = 10.0

theta2_static = 45.0
p1 = np.array([114.68, -33.19])
o4 = np.array([l1, 0.0])


def f(theta):
    xy_4p1 = p1 - o4
    theta_4p1_0 = np.arctan2(xy_4p1[1], xy_4p1[0])
    theta4_0 = utils.vector_loop(l1, l2, l3, l4, np.radians(180 - theta2_static - theta1))[0]
    theta_b4p1 = theta4_0 - theta_4p1_0
    theta4, theta3 = utils.vector_loop(l1, l2, l3, l4, np.radians(theta))
    w4 = utils.velocity_analysis(l2, l3, w2, np.radians(theta), theta3, theta4)[1]
    theta_4p1 = theta4 - theta_b4p1

    v_mag = w4 * np.linalg.norm(p1 - o4)
    v_theta = 90 - np.degrees(theta_4p1)
    return np.vstack([v_mag, v_theta]).T


utils.plot(f, title="Problem 1", xlabel="Theta_2 (deg)", labels=["Magnitude (units/s)", "Direction (deg)"],
           colors=["red", "blue"], sharex=True)
plt.show()
