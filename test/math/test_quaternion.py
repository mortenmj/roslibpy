#!/usr/bin/env python

import unittest
from roslibpy.math import Quaternion


class QuaternionTests(unittest.TestCase):
    def test_defaults(self):
        q = Quaternion()
        self.assertEqual(q.x, 0)
        self.assertEqual(q.y, 0)
        self.assertEqual(q.z, 0)
        self.assertEqual(q.w, 1)

    def test_value_x(self):
        x, y, z, w = 1, 0, 0, 0

        q = Quaternion(x, y, z, w)
        self.assertEqual(q.x, x)
        self.assertEqual(q.y, y)
        self.assertEqual(q.z, z)
        self.assertEqual(q.w, w)

    def test_value_y(self):
        x, y, z, w = 0, 1, 0, 0

        q = Quaternion(x, y, z, w)
        self.assertEqual(q.x, x)
        self.assertEqual(q.y, y)
        self.assertEqual(q.z, z)
        self.assertEqual(q.w, w)

    def test_value_z(self):
        x, y, z, w = 0, 0, 1, 0

        q = Quaternion(x, y, z, w)
        self.assertEqual(q.x, x)
        self.assertEqual(q.y, y)
        self.assertEqual(q.z, z)
        self.assertEqual(q.w, w)

    def test_value_w(self):
        x, y, z, w = 0, 0, 0, 1

        q = Quaternion(x, y, z, w)
        self.assertEqual(q.x, x)
        self.assertEqual(q.y, y)
        self.assertEqual(q.z, z)
        self.assertEqual(q.w, w)

    def test_conjunction(self):
        x, y, z, w = 1.1, 2.2, 3.3, 4.4

        q = Quaternion(x, y, z, w)
        r = q.conjugate
        self.assertEqual(r.x, -x)
        self.assertEqual(r.y, -y)
        self.assertEqual(r.z, -z)
        self.assertEqual(r.w, w)

    def test_norm(self):
        x, y, z, w = 2, 2, 2, 2

        q = Quaternion(x, y, z, w)
        norm = q.norm
        self.assertEqual(norm, 4)

    def test_normalize(self):
        x, y, z, w = 2, 2, 2, 2

        q = Quaternion(x, y, z, w)
        r = q.normalized
        self.assertEqual(r.x, 0.5)
        self.assertEqual(r.y, 0.5)
        self.assertEqual(r.z, 0.5)
        self.assertEqual(r.w, 0.5)
