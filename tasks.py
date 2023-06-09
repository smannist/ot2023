from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/start_game.py", pty=True)

@task
def test(ctx):
    ctx.run("pytest src", pty=True)

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src", pty=True)

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html", pty=True)

@task
def open_report(ctx):
    ctx.run("xdg-open htmlcov/index.html")

@task
def lint(ctx):
    ctx.run("pylint src", pty=True)

@task
def pep8(ctx):
    ctx.run("autopep8 --in-place --recursive src", pty=True)
