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

First copy html build to docs folder

```bash
chmod +x docs_update.sh
./docs_update.sh
python -m http.server -d docs
```

Go to repository settings -> pages -> github pages build and deployment.
