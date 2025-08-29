# KTS

Notebooks for Kotlin.

The [new Jupyter Book](https://next.jupyterbook.org/upgrade/) has a single configuration file myst.yml.

## setup.sh ##

```bash
chmod +x setup.sh
./setup.sh
```

## init your book ##

See the Jupyter book [docs](https://next.jupyterbook.org/start/init/)

```bash
jupyter book init
```

## build the book ##

```bash
jupyter book init --write-toc
jupyter book build --all
jupyter book build --html
```

## serving ##

```bash
python -m http.server -d _build/html
```

## github pages ##

See the [jupyterbook docs on publishing](https://jupyterbook.org/en/stable/start/publish.html).

```
jupyter-book build --html
pip install ghp-import
ghp-import -n -p -f _build/html
```
