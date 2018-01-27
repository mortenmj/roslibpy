#!/usr/bin/env python

from collections import namedtuple
from .quaternion import Quaternion


class Point(namedtuple('Point', ('x', 'y', 'z'))):
    def __new__(cls, x=0, y=0, z=0):
        return super(Point, cls).__new__(cls, x, y, z)

    def rotate(self, q: Quaternion):
        ix = q.w * self.x + q.y * self.z - q.z * self.y
        iy = q.w * self.y + q.z * self.x - q.x * self.z
        iz = q.w * self.z + q.x * self.y - q.y * self.x
        iw = -q.x * self.x - q.y * self.y - q.z * self.z

        self.__x = ix * q.w + iw * -q.x + iy * -q.z - iz * -q.y
        self.__y = iy * q.w + iw * -q.y + iz * -q.x - ix * -q.z
        self.__z = iz * q.w + iw * -q.z + ix * -q.y - iy * -q.x
