import os
from collections import namedtuple


TextSwap = namedtuple("TextSwap", ["old", "new"])

swaps = list()
swaps.append(TextSwap("/build/_shared/", "build/_shared/"))
swaps.append(TextSwap("/build/_assets/", "build/_assets/"))

file_path = os.path.join("docs", "index.html")

with open(file_path, "r") as f:
    data = f.read()

for swap in swaps:
    data = data.replace(swap.old, swap.new)

with open(file_path, "w") as f:
    f.write(data)
