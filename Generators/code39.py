import typer
import os

import barcode
from barcode.writer import ImageWriter

app = typer.Typer()

@app.command()
def batch(inputF: str, output: str = "."):
    with open(inputF, "r") as inf:
        lines = inf.readlines()
    for line in lines:
        genBarcode(line, output)

def genBarcode(data, outfolder):
    code = barcode.Code39(data, writer=ImageWriter(), add_checksum=False)
    path = os.path.join(outfolder, data.replace(" ", "_"))
    code.save(path)

@app.command()
def single(data: str, outputPath: str = "."):
    code = barcode.Code39(data, add_checksum=False, writer=ImageWriter())
    path = os.path.join(outputPath, data.replace(" ", "_"))
    code.save(path)