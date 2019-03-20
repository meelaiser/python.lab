#!/usr/bin/env python3
import subprocess
with open("/home/deric/Public/brihgtness/brightness") as f:
    b = f.read()
subprocess.call(["xcalib", "-co", b, "-a", "-d", ":0", "/home/deric/Public/B156HAN04.3.icm"])

