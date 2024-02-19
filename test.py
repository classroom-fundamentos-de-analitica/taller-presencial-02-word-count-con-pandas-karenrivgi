"""GitHub Classroom autograding script."""

import os

import pandas as pd
from word_count import run

run("input/", "output.txt")

#
# Retorna error si la carpeta output/ no existe
if not os.path.exists("output.txt"):
    raise FileNotFoundError("File 'output.txt' not found")

#
# Lee el contenido del archivo output.txt
dataframe = pd.read_csv(
    "output.txt", delimiter="\t", header=None, names=["word", "count"]
)
dataframe = dataframe.set_index("word")
series = dataframe["count"]


assert series["analytics"] == 5
assert series["business"] == 7
assert series["by"] == 3
assert series["algorithms"] == 2
assert series["analysis"] == 4
