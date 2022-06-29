import typer
from Generators.code39 import app as code39
from Generators.code128 import app as code128
from Generators.UPCA import app as upca

app = typer.Typer()
app.add_typer(code39, name="code39")
app.add_typer(code128, name="code128")
app.add_typer(upca, name="upca")


app()
