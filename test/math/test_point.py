#!/usr/bin/env python

import unittest
from roslibpy.math import Point


class PointTests(unittest.TestCase):
    def test_defaults(self):
        p = Point()
        self.assertEqual(p.x, 0)
        self.assertEqual(p.y, 0)
        self.assertEqual(p.z, 0)
