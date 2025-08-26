import os

file_path = os.path.join("docs", "index.html")
old_string = "/build/_shared/"
new_string = "build/_shared/"

with open(file_path, "r") as f:
    data = f.read()

data = data.replace(old_string, new_string)

with open(file_path, "w") as f:
    f.write(data)
