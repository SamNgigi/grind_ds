import nbformat as nbf

ntbk = nbf.read("old_notebook.ipynb", nbf.NO_CONVERT)
new_ntbk = ntbk
new_ntbk.cells = [cell for cell in ntbk.cells if cell.cell_type = "markdown"]
nbf.write(new_ntbk, "new_md_only_notebook.ipynb", version=nbf.NO_CONVERT)