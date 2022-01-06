fname = "testfiles/epl_bets_pred.md"

line_numbers = []
img_calls = []
for l_number, l in enumerate(open(fname, "r").readlines(), start=1):
    if l.startswith("```"):
        # append l_number to line_numbers
        line_numbers.append(l_number)
    elif l.startswith("![png]"):
        img_calls.append(l)

# grab line number pairs in which between them is a code cell
def get_codecells(line_numbers):

    code_cells = []
    for idx in range(len(line_numbers)-1):

        code_cell = open(fname, "r").readlines()[line_numbers[idx]:line_numbers[idx+1]]
        code_cell = ''.join(code_cell)

        if ('plt.' in code_cell) or ('sns.' in code_cell) and ('import' not in code_cell):
            code_cells.append(code_cell)

    return code_cells


# inserting images
def insert_images(code_cells, image_calls):
    # document string to export as markdown file
    document = """<h1 style="text-align: center;">Plots</h1>\n\n-----\n\n"""

    for img_call, code_cell in zip(image_calls, code_cells):
        document += ('```python\n' + code_cell + "\n" + img_call + "\n")

    return document


# Applying functions to md file
cells = get_codecells(line_numbers=line_numbers)
doc = insert_images(cells, image_calls=img_calls)


# export document
with open("testfiles/test.md", "w") as output_file:
    output_file.write(doc)
    output_file.close()
