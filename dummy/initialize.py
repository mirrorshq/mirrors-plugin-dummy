#!/usr/bin/python3
# -*- coding: utf-8; tab-width: 4; indent-tabs-mode: t -*-

import os
import sys
import json


dataDir = json.loads(sys.argv[1])["data-directory"]

# test file
with open(os.path.join(dataDir, "test.txt"), "w") as f:
    f.write("test\n")

# test directory and file
dn = os.path.join(dataDir, "test2")
if not os.path.exists(dn):
    os.mkdir(dn)
with open(os.path.join(dn, "test2.txt"), "w") as f:
    f.write("test2\n")
