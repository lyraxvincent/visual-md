<h1></h1>

<p align="center">
<img src="assets/visual-md.gif" width="600" height="350" alt="gif"/>
</p>


-----

From your jupyter notebooks to a static dashboard (visualization page) made in pure markdown.  
Visual-md features a python commandline tool to extract plots from a jupyter notebook to a markdown file.

## **Usage**
The tool takes a jupyter notebook as input and returns a markdown file as output.  
### As a CLI tool :
- install visual_md using pip:  
    ```pip install visual_md```
- run visual_md on your terminal specifying input and output files:  
    ```visual_md -i input.ipynb -o output.md```

To include code cells in your visualization page, add argument `--include-code`:  

```visual_md -i input.ipynb -o output.md --include-code```

### Using the python script : 
Get the script under  `src/visual_md/`:  

```python
python generate_dashboard.py [input_notebook.ipynb] [output_file.md]
```

Add the following argument to include code associated with the plots (code that generates specific 
plots from the notebook):

```python
python generate_dashboard.py [input_notebook.ipynb] [output_file.md] --include-code
```
