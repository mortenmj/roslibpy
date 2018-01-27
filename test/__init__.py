#!/usr/bin/env python
import subprocess
import os

global proc

def setUpModule():
    my_env = os.environ.copy()
    my_env['ROS_MASTER_URI'] = 'http://localhost:11311'
    proc = subprocess.Popen('roscore', env=my_env)

def tearDownModule():
    proc.terminate()
