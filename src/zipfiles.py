import os
import subprocess
import sys

a = "myplugins/unique fix/about.txt"
changed = str(sys.argv)
print("'"+a+"' vs '"+ changed +"'" )
plugins = set()
for f in changed.split("%%%"):
    if not "myplugins" in f:
        continue
    path = f.split(os.sep)
    index = path.index("myplugins") + 1
    if index >= len(path):
        continue
    plugins.add(path[index])
if plugins:
    print("The following plugins have changed:")
    for p in plugins:
        print(p)
        os.chdir('myplugins/')
        x = p.replace(" ", ".")
        subprocess.run(["zip", "-r", "../" + x + ".zip", p], stdout=subprocess.DEVNULL)
        os.chdir('../')
else:
    print("No plugin changes have been detected.")