#!/usr/bin/env python

from collections import namedtuple

from .point import Point
from .quaternion import Quaternion


class Transform(namedtuple('Transform', ('translation', 'rotation'))):
    def __init__(self, translation: Point, orientation: Quaternion):
        self.__translation = translation
        self.__orientation = orientation
