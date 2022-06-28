import typer
import os
from colorama import Fore
import barcode
from barcode.writer import ImageWriter

app = typer.Typer()

@app.command()
def multi(datafile: str, output = "."):
    with open(datafile, "r") as inf:
        lines = inf.readlines()
    total = 0
    print(f"Generating {Fore.GREEN}{len(lines)}{Fore.WHITE} Files!")
    with typer.progressbar(lines) as progress:
        for val in progress:
            genBarcode(val.strip(), output)
            total += 1
    print(f"Generated {Fore.GREEN}{total}{Fore.WHITE} Files!")
    print(f"Saved to {Fore.CYAN}{output}{Fore.WHITE}!")
    

@app.command()
def single(data: str, outputPath: str = "."):
    genBarcode(data, outputPath)
    print(f"{Fore.CYAN}{data.replace(' ', '_')}.jpg{Fore.WHITE}")

def genBarcode(data, outfolder):
    code = barcode.Code128(data, writer=ImageWriter())
    path = os.path.join(outfolder, data.replace(" ", "_"))
    code.save(path)

