### Hexlet tests and linter status:
[![Actions Status](https://github.com/sidnnov/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/sidnnov/python-project-50/actions)
[![my-ci-app](https://github.com/sidnnov/python-project-50/actions/workflows/my-check.yml/badge.svg)](https://github.com/sidnnov/python-project-50/actions/workflows/my-check.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/156003457597319ffd99/maintainability)](https://codeclimate.com/github/sidnnov/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/156003457597319ffd99/test_coverage)](https://codeclimate.com/github/sidnnov/python-project-50/test_coverage)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Tutorial:
-------------------------------
<!-- Эта утилита позволяет выявлять отличия у файлов формата .json и .yaml, а так же выводить результат в удобном формате.
На выбор есть формат: 'stylish', 'plain', 'json'. По умолчанию выбран формат 'stylish'. -->
This utility allows you to detect exceptions for .json and .yaml files, as well as display the result in a convenient format.
There is a format to choose from: 'stylish', 'plain', 'json'. The default format is 'stylish'.

### Launch example:
```
gendiff -f json puthfile1.json puthfile2.json
```
### Installation:
-----------------------

python 3.8+ is required to install hexlet-code. And also need poetry for the assembly of the project.

```
$ git clone git@github.com:sidnnov/python-project-50.git
```
```
$ poetry build

$ python3 -m pip install --user dist/*.whl
```

### Make commands:
```
make install     # poetry install

make build       # poetry build

package-install  # python3 -m pip install --user dist/*.whl
```

### Work examples:
-----------------------

#### Diff json:
[![asciicast](https://asciinema.org/a/537298.svg)](https://asciinema.org/a/537298)

#### Diff yaml:
[![asciicast](https://asciinema.org/a/537787.svg)](https://asciinema.org/a/537787)

#### Diff format 'stylish':
[![asciicast](https://asciinema.org/a/540338.svg)](https://asciinema.org/a/540338)

#### Diff format 'plain':
[![asciicast](https://asciinema.org/a/541326.svg)](https://asciinema.org/a/541326)

#### Diff format 'json':
[![asciicast](https://asciinema.org/a/541494.svg)](https://asciinema.org/a/541494)