import typer
from Generators.code39 import app as code39

app = typer.Typer()
app.add_typer(code39, name="code39")

app()