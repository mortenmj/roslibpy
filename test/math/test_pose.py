#!/usr/bin/env python

import unittest
from roslibpy.math import Pose, Point, Quaternion


class PoseTests(unittest.TestCase):
    def test_defaults(self):
        p = Pose()
        self.assertEqual(p.position, Point())
        self.assertEqual(p.orientation, Quaternion())
