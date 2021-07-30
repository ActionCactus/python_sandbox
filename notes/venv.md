[Official Documentation](https://docs.python.org/3.8/library/venv.html?highlight=venv#module-venv)

Used to create virtual environments containing external dependencies, including the Python version used in creating the project.

```sh
python3 -m venv .venv
source .venv/bin/activate
echo $VIRTUAL_ENV
deactivate
```