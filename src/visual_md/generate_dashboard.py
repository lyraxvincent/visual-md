import os
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]
try:
    include_code = sys.argv[3]
except:
    include_code = ''

# convert jupyter notebook(ipynb) to markdown(md)
os.system(f"jupyter nbconvert {input_file} --to markdown")

fname = f"{input_file.split('.')[0]}.md"

line_numbers = []
img_calls = []

for l_number, l in enumerate(open(fname, "r").readlines(), start=1):
    if l.startswith("```"):
        line_numbers.append(l_number)
    elif l.startswith("![png]"):
        img_calls.append(l)


def get_codeCells(line_numbers):
    """

    :param line_numbers:
    :return: list of code cells with their associated code in the form:

                ```python

                >>> python code
                >>> more python code

                ```
    """

    code_cells = []
    for idx in range(len(line_numbers)-1):

        code_cell = open(fname, "r").readlines()[line_numbers[idx]:line_numbers[idx+1]]
        code_cell = ''.join(code_cell)

        if ('plt.' in code_cell) or ('sns.' in code_cell) and ('import' not in code_cell):
            code_cells.append(code_cell)

    os.remove(fname)
    return code_cells


def insert_images(code_cells, image_calls, include_code=str(include_code)):
    """

    :param code_cells:
    :param image_calls:
    :param include_code: Whether to include code cells associated with the plots or not
                         defaults to True
    :return: a string document with all contents(plots and their associated code) that
             will be exported as markdown
    """

    document = """<h1 align="center">Plots</h1>\n\n-----\n\n"""

    if include_code == "--include-code":
        for code_cell, img_call in zip(code_cells, image_calls):

            # centered image
            img_call_centered = f"""\n<p align="center">\n\t<img src='{img_call.split(']')[-1].strip().strip(')').strip('(')}', alt='plot'/>\n</p>\n"""

            document += ('```python\n' + code_cell + "\n" + img_call_centered + "\n")
    else:
        for img_call in image_calls:
            img_call_centered = f"""\n<p align="center">\n\t<img src='{img_call.split(']')[-1].strip().strip(')').strip('(')}', alt='plot'/>\n</p>\n"""
            document += ("\n" + img_call_centered + "\n")

    return document


# Applying functions to md file
cells = get_codeCells(line_numbers=line_numbers)
doc = insert_images(cells, image_calls=img_calls, include_code=include_code)


# export document
with open(output_file, "w") as out_file:
    out_file.write(doc)
    out_file.close()