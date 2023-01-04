<<<<<<< HEAD
"""
BOJ#11653 소인수분해
기본 수학 2
"""

import sys

n = int(sys.stdin.readline().rstrip())

cur = 2
while n != 1:
    if (n%cur) == 0:
        n = n//cur
        print(cur)    
    else:
        cur+=1

=======
"""
BOJ#11653 소인수분해
기본 수학 2
"""

import sys

n = int(sys.stdin.readline().rstrip())

cur = 2
while n != 1:
    if (n%cur) == 0:
        n = n//cur
        print(cur)    
    else:
        cur+=1

>>>>>>> 44eb9ab6eb732a550c37acd6f8bafd6100c82fab
