import numpy as np

from transforms import rotz


def main():
    theta = np.pi / 4

    print("Rotation matrix around Z axis:")
    print(rotz(theta))


if __name__ == "__main__":
    main()