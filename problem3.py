import numpy as np
from matplotlib import pyplot as plt
import utils


theta1 = 135

l2 = 105
l3 = 172
l4 = 27
r_in = 301


def f(theta):
    return utils.slider_crank_mechanical_advantage(l2, l3, l4, np.radians(theta), r_in)


utils.plot(f, xmin=15, xmax=60, xstep=0.1, title="Problem 3", xlabel="Theta_AC (deg)", ylabel="Mechanical Advantage")
plt.show()
