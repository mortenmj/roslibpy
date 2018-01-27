#!/usr/bin/env python

from collections import namedtuple
from math import sqrt


class Quaternion(namedtuple('Quaternion', ('x', 'y', 'z', 'w'))):
    def __new__(cls, x=0, y=0, z=0, w=1):
        return super(Quaternion, cls).__new__(cls, x, y, z, w)

    @property
    def conjugate(self):
        """
        Return the conjugate of the Quaternion
        """
        return Quaternion(self.x * -1, self.y * -1, self.z * -1, self.w)

    @property
    def norm(self) -> float:
        """
        Return the norm of the Quaternion
        """
        return sqrt(sum([x**2 for x in self]))

    @property
    def normalized(self):
        """
        Return a normalized Quaternion
        """
        n = self.norm
        if n is 0:
            x, y, z, w = 0, 0, 0, 1
            return Quaternion(x, y, z, w)
        else:
            n = 1/n
            x, y, z, w = self.x * n, self.y * n, self.z * n, self.w * n
            return Quaternion(x, y, z, w)

    @property
    def inverse(self):
        """
        Return the inverse of the Quaternion
        """
        return self.conjugate.normalize
