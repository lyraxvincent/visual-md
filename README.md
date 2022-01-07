<h1 align="center">visual-md</h1>

<img style="display: block; margin-left: auto; margin-right: auto; width: 80%;" src="assets/visual-md.gif" alt="gif"/>

-----

From your jupyter notebooks to a static dashboard made in pure markdown.  
Visual-md features a python commandline tool to extract plots from a jupyter notebook to a markdown file.

### **Usage**
The tool takes a jupyter notebook as input and returns a markdown file as output.  
Run the script on terminal specifying the jupyter notebook path and the filename 
you wish to give your markdown output file in the following format (without the square brackets) 
and in that specific order:

```python
python generate_dashboard.py [input_notebook.ipynb] [output_file.md]
```

Add the following argument to include code associated with the plots (code that generates specific 
plots from the notebook):

```python
python generate_dashboard.py [input_notebook.ipynb] [output_file.md] --include-code
```

## **License**
This project is provided under the MIT License.