import numpy as np
from matplotlib import pyplot as plt
import utils


l1 = 1.0
l2 = 2.17
l3 = 2.067
l4 = 2.31
l5 = 5.4
l6 = 0

theta1 = 102
w2 = 1


def slider_theta_w4_from_theta(theta):
    theta4, theta3 = utils.vector_loop(l1, l2, l3, l4, np.radians(theta))
    slider_theta2 = theta4 - np.radians(theta1)
    _, w4 = utils.velocity_analysis(l2, l3, w2, np.radians(theta), theta3, theta4)
    return slider_theta2, w4


def slider_pos_from_theta(theta):
    slider_theta2, _ = slider_theta_w4_from_theta(theta)
    slider_pos, _ = utils.slider_crank_vector_loop(l4, l5, l6, slider_theta2)
    return slider_pos


def f(theta):
    slider_theta2, w4 = slider_theta_w4_from_theta(theta)
    _, v_c = utils.slider_crank_velocity_analysis(l4, l5, l6, w4, slider_theta2)
    return -v_c


print("Percent deviation from constant velocity:")
print(f"\t240 to 270 degrees: {utils.percent_dev_from_constant(f, 240, 270):.2f}%")
print(f"\t190 to 316 degrees: {utils.percent_dev_from_constant(f, 190, 316):.2f}%")

plt.subplot(211)
utils.plot(f, title="Problem 4: Velocity by Theta_2", xlabel="Angle (deg)", ylabel="Slider Velocity (units/s)", colors=["purple"])
plt.subplot(212)
utils.plot(f, xfun=slider_pos_from_theta, title="Problem 4: Velocity by Slider Position", xlabel="Slider Position (units)", ylabel="Slider Velocity (units/s)", colors=["red"])
plt.tight_layout()
plt.show()
