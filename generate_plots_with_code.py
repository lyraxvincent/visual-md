fname = "epl_bets_pred.md"

line_numbers = []
image_calls = []
for l_number, l in enumerate(open(fname, "r").readlines(), start=1):
    if l.startswith("```"):
        # append l_number to line_numbers
        line_numbers.append(l_number)
    elif l.startswith("![png]"):
        image_calls.append(l)

# grab line number pairs in which between them is a code cell
code_cells = []
for idx in range(len(line_numbers)-1):

    code_cell = open(fname, "r").readlines()[line_numbers[idx]:line_numbers[idx+1]]
    code_cell = ''.join(code_cell)

    if ('plt.' in code_cell) or ('sns.' in code_cell) and ('import' not in code_cell):
        code_cells.append(code_cell)

# document string to export as markdown file
document = """<h1 style="text-align: center;">Plots</h1>\n\n-----\n\n"""

# inserting images
for img_call, code_cell in zip(image_calls, code_cells):
    document += ('```python\n' + code_cell + "\n" + img_call + "\n")

# export document
with open("plots_with_their_code.md", "w") as output_file:
    output_file.write(document)
    output_file.close()
