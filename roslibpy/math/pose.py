#!/usr/bin/env python

from collections import namedtuple

from .point import Point
from .quaternion import Quaternion
from .transform import Transform


class Pose(namedtuple('Pose', ('position', 'orientation'))):
    def __new__(cls,
                position: Point=Point(),
                orientation: Quaternion=Quaternion()):
        return super(Pose, cls).__new__(cls, position, orientation)

    def transform(self, tf: Transform):
        self.position = self.__position.rotate(tf.rotation)
        self.position += tf.translation
        self.orientation = tf.rotation
