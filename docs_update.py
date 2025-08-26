import os
from collections import namedtuple


TextSwap = namedtuple("TextSwap", ["old", "new"])

swaps = list()
# adjusting paths
swaps.append(TextSwap('"/build/', '"build/'))
swaps.append(TextSwap('import "build/manifest', 'import "/build/manifest'))
swaps.append(TextSwap('"build/root', '"/build/root'))
swaps.append(TextSwap('"build/routes', '"/build/routes'))
swaps.append(TextSwap('"build/entry', '"/build/entry'))
swaps.append(TextSwap('"/myst-theme.css"', '"myst-theme.css"'))
# remove made with myst
swaps.append(TextSwap("Made with MyST", ""))

file_path = os.path.join("docs", "index.html")

with open(file_path, "r") as f:
    data = f.read()

for swap in swaps:
    data = data.replace(swap.old, swap.new)

with open(file_path, "w") as f:
    f.write(data)
