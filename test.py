import os

# convert ipynb to md
nb_path = "testfiles/epl_bets_pred.ipynb"
os.system(f"jupyter nbconvert {nb_path} --to markdown")

fname = f"{nb_path.split('.')[0]}.md"

line_numbers = []
img_calls = []
for l_number, l in enumerate(open(fname, "r").readlines(), start=1):
    if l.startswith("```"):
        # append l_number to line_numbers
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


def insert_images(code_cells, image_calls, include_code=True):
    """

    :param code_cells:
    :param image_calls:
    :param include_code: Whether to include code cells associated with the plots or not
                         defaults to True
    :return: a string document with all contents(plots and their associated code) that
             will be exported as markdown
    """

    document = """<h1 style="text-align: center;">Plots</h1>\n\n-----\n\n"""

    if include_code:
        for code_cell, img_call in zip(code_cells, image_calls):
            document += ('```python\n' + code_cell + "\n" + img_call + "\n")
    else:
        for img_call in image_calls:
            document += ("\n" + img_call + "\n")

    return document


# Applying functions to md file
cells = get_codeCells(line_numbers=line_numbers)
doc = insert_images(cells, image_calls=img_calls, include_code=True)


# export document
with open("testfiles/test.md", "w") as output_file:
    output_file.write(doc)
    output_file.close()