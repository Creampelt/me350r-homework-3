import numpy as np
from matplotlib import pyplot as plt
import utils


theta1 = 135

o2_a = 70
o2_c = 138
ab = 35
o4_b = 34
o4_d = 82
o2_o4 = 48


def theta_ab_from_theta_2(theta):
    _, theta3 = utils.vector_loop(o2_o4, o2_a, ab, o4_b, np.radians(theta1 - theta), crossed=True)
    return (135 - np.degrees(theta3)) % 180


def f(theta):
    return utils.mechanical_advantage(o2_o4, o2_a, ab, o4_b, np.radians(theta1 - theta), o2_c, o4_d, crossed=True)


utils.plot(f, xfun=theta_ab_from_theta_2, xmin=90, xmax=120, xstep=0.1, title="Problem 2", xlabel="Theta_AB (deg)", ylabel="Mechanical Advantage")
plt.show()
