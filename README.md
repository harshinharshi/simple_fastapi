# simple_fastapi
a project to learn how docker works


neccesary knowlage of UV :
$ pip install uv

check if it is working 
$ uv

$ uv init

uv init will crate readme.md, main.py, pyproject.toml, .python-version, .gitignore (if any of the file is present it will skip that file from creation )

$ uv run main.py 

uv run wll crate .venv folder and uv.lock file

$ uv add requests 

this will add the dependencies to the pyproject.toml file

To remove a package, you can use uv remove:
$ uv remove requests
