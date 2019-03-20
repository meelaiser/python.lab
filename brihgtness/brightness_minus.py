#!/usr/bin/env python3
import subprocess
with open("/home/deric/Public/brihgtness/brightness") as f:
    b = int(f.read()) - 5
if b > 4:
    with open("/home/deric/Public/brihgtness/brightness", 'w') as f:
        b = str(b) 
        f.write(b)
        subprocess.call(["xcalib", "-c"])
        subprocess.call(["xcalib", "-co", b, "-a", "-d", ":0", "/home/deric/Public/B156HAN04.3.icm"])
