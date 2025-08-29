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

[You'll need subtree](https://codeengineered.com/blog/how-to-install-git-subtree/)

We can then [deploy a sub-folder](https://gist.github.com/cobyism/4730490)

Also see [git releases](https://www.kernel.org/pub/software/scm/git/)

```
jupyter-book build --html
git version
sudo apt update
sudo apt install git=<full_version_string>
git subtree push --prefix _build/html origin gh-pages
```
