I've historically kept small "sandbox" environments for testing out various things in the language I'm working with.  I've decided to commit to using Python as a general purpose language, so this repo is the random stuff I try out.

Lots of it is boring interview prep stuff and this isn't intended to be a resume item or anything (I'm a sucker for the Github contributions visualization, though, so here we are).

# Installation
```sh
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt -e .
```

# Running Tests
```sh
pytest --cov=src --cov-report=html tests/
```