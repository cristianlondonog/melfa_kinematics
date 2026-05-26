import numpy as np


def rotz(theta):
    """
    Rotation matrix around Z axis.
    Angle must be provided in radians.
    """

    return np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta),  np.cos(theta), 0],
        [0,              0,             1]
    ])