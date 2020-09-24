"""
Contains task automations and syntactic sugar for Jepedia.
"""

import os
from pathlib import Path

from invoke import task

PTY: bool = True

ROOT_DIR = os.path.dirname(__file__)
ROOT_PATH = Path(ROOT_DIR)

JUPYTERLAB_EXTENSIONS = [
    "jupyterlab-drawio",
    # "nbgather",
    # "@krassowski/jupyterlab-lsp",
    "@jupyterlab/git",
    "@jupyterlab/toc",
    # "@jupyterlab/mathjax3-extension",
    "@aquirdturtle/collapsible_headings",
    "./jupyterlab-jepedia"
]


@task(name="list")
def list_(c):
    """
    Lists the available commands.
    """

    c.run("inv --list", pty=PTY)


@task(name="help")
def help_(c, command):
    """
    Prints help information for a given command.
    """

    c.run(f"inv --help {command}", pty=PTY)


@task()
def install_jupyterlabs_ext(c):
    """Installs the JupyterLab Extensions."""

    with c.cd(ROOT_DIR):
        c.run(
            f"jupyter labextension install {' '.join(JUPYTERLAB_EXTENSIONS)} ", pty=PTY
        )


@task
def build(c):
    """
    Builds the documentation site.
    """

    c.run(
        """
    jupyter nbconvert\
    --to markdown *.ipynb\
    --output-dir build\
    --TagRemovePreprocessor.remove_cell_tags='{"remove_cell"}'\
    --TagRemovePreprocessor.remove_input_tags='{"remove_input"}'\
    --template=templates/to_markdown.tpl
    """,
        pty=PTY,
    )


@task
def docs(c):
    """
    Serves to mkdocs documentation site.
    """

    with c.cd(ROOT_DIR):
        c.run("mkdocs serve", pty=PTY)


@task
def lab(c):
    """
    Runs the JupyterLab server.
    """

    with c.cd(ROOT_DIR):
        c.run("jupyter lab", pty=PTY)
