import time
import sys

print time.asctime()

if sys.argv[1] == '-n' and len(sys.argv) == 4:
    print(int(sys.argv[2]) + int(sys.argv[3]))
else:
    # python modules.py <arg>
    print sys.argv[1]


