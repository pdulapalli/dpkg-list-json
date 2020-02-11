# Contributing to dpkg_list_json

## Testing the package
    virtualenv venv
    . venv/bin/activate
    pip install --editable .

## New version to PyPi?
### 1. Build
```
rm -rf dist/ dpkg_list_json.egg-info/
python setup.py sdist
```

### 2. Push
```
twine upload dist/*
```
