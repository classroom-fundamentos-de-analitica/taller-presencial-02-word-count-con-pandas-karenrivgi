"""Taller evaluable"""

import glob

import pandas as pd


def load_input(input_directory):
    """Load text files in 'input_directory/'"""
    #
    # Lea los archivos de texto en la carpeta input/ y almacene el contenido en
    # un DataFrame de Pandas. Cada línea del archivo de texto debe ser una
    # entrada en el DataFrame.
    #

    filenames = glob.glob(input_directory + "/*.*")
    dataframes = [
        # Asume que la primera fila es el nombre de las columnas, cambiamos esto con names
        pd.read_csv(filename, sep=";", names=['text']) for filename in filenames
    ]

    # Permite tener varios datafranes en una lista, uno debajo del otro
    # Se espera que tengan las mismas columnas, si no, las agrega y rellena con NaN
    dataframe = pd.concat(dataframes).reset_index(drop=True)
    return dataframe



def clean_text(dataframe):
    """Text cleaning"""
    #
    # Elimine la puntuación y convierta el texto a minúsculas.
    #

     # Copia el dataframe para no modificar el original
    dataframe = dataframe.copy()
    dataframe.text = dataframe.text.str.lower()
    dataframe.text = dataframe.text.str.replace(',', '').str.replace('.', '')
    return dataframe


def count_words(dataframe):
    """Word count"""

    dataframe = dataframe.copy()

    # Cada fila es una lista de palabras
    dataframe.text = dataframe.text.str.split()

    # Transforma cada registro que es lista en una fila, un registro por palabra
    dataframe = dataframe.explode('text').reset_index(drop=True)

    # Renombra la columna text a word y agrega una columna count con valor 1
    dataframe = dataframe.rename(columns={'text': 'word'})
    dataframe['count'] = 1

    # Agrupa por palabra y suma la columna valor, el elemento agrupador queda como índice
    # (anulamos esto último con el reset_index o con as_index=False en groupby()
    conteo = dataframe.groupby(['word'], as_index=False).agg({'count': 'sum'})

    return conteo



def save_output(dataframe, output_filename):
    """Save output to a file."""

    dataframe.to_csv(output_filename, index=False)


#
# Escriba la función job, la cual orquesta las funciones anteriores.
#
def run(input_directory, output_filename):
    """Call all functions."""
    dataframe = load_input(input_directory)
    dataframe = clean_text(dataframe)
    dataframe = count_words(dataframe)
    save_output(dataframe, output_filename)


if __name__ == "__main__":
    run(
        "input",
        "output.txt",
    )
