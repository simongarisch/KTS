#!/usr/bin/bash

# which distro
cat /etc/os-release

# running in github codespaces which has Python installed by default
# ensure that jupyterbook is installed from requirements.txt
python --version # 3.12.1
pip install -r requirements.txt

# install kotlin lang
sdk install kotlin
kotlinc -version
