"""
Contains task automations and syntactic sugar for Jepedia.
"""

from invoke import task


PTY: bool = True


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

    c.run("mkdocs serve", pty=PTY)


@task
def lab(c):
    """
    Runs the JupyterLab server.
    """

    c.run("jupyter lab", pty=PTY)
