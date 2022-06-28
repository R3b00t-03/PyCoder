import typer
import barcode
from barcode.writer import ImageWriter
import os

from Generators.code39 import app as code39

app = typer.Typer()
app.add_typer(code39, name="code39")

app()