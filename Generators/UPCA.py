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
def single(data: str, output: str = "."):
    res = genBarcode(data, output)
    if res == 1:
        print(f"{Fore.RED}ERROR: Make shure your data is only numeric and 12 digits long!{Fore.WHITE}")        
    else:
        print(f"{Fore.CYAN}{data.replace(' ', '_')}.jpg{Fore.WHITE}")

def genBarcode(data, outfolder):
    if len(data) == 12 and data.isdigit():
        code = barcode.UPCA(data, writer=ImageWriter())
        path = os.path.join(outfolder, data.replace(" ", "_"))
        code.save(path)
        return 0
    else: 
        return 1
    

