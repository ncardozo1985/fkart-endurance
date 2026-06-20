import sys
p = 'public/index.html'
with open(p,'w') as f:
    f.write(sys.stdin.read())
import os
print('OK',os.path.getsize(p),'bytes')
