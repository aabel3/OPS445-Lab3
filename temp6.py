#!/usr/bin/env python3
# OPS445 - Lab 3
# lab3a.py
# Author: Avraham Abel

import os
import subprocess

# ~os.system('ls -l')
# ~os.system('ipconfig')

p = subprocess.Popen(['date'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
output = p.communicate()
stdout = output[0].decode('utf-8').strip()
print(stdout)

