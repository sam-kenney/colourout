# colourout

A Python package for printing coloured text to the terminal.

## Installation

Install this package using pip:

    pip install colourout


## API

The `colourout` package provides two functions, and an `Enum` for the available colours.

### `printc`

The `printc` utilises the builtin `print` function to print coloured text to the terminal.

```python
from colourout import printc

printc("Hello, World!", styles=["BLUE", "UNDERLINE"])
>>> \033[34m\033[4mHello, World!\033[0m
```


### `eprintc`

The `eprintc` function is the same as `printc`, but prints to `stderr` instead of `stdout`.

```python
from colourout import eprintc

eprintc("Hello, World!", styles=["RED", "BOLD"])
>>> \033[31m\033[1mHello, World!\033[0m
```


### `Styles`

The `Styles` enum provides a list of available styles.

```python
from colourout import Styles, printc

printc(
    "Hello, World!",
    styles=[Styles.BLUE, Styles.UNDERLINE],
)

>>> \033[34m\033[4mHello, World!\033[0m
```


## Contributing

Fork the repository and clone it locally.

Make any changes you want and then submit a pull request.

Ensure all tests are passing and that you have added tests for any new functionality.

Run testing, formatting, and linting by using `nox`.

You can run individual sessions by using the `-s` flag with nox.
For example:

    nox -s test
    nox -s lint

Code is formatted and linted upon commit using the `pre-commit` tool.

Make sure to install the `pre-commit` config using `pre-commit install` once you have installed the `requirements-dev.txt` dependencies.

You can check that everything is passing by running `pre-commit` after `git add`-ing your files to a commit.

> **_NOTE:_** Tests are not run with `pre-commit` due to performance issues, please ensure to run `nox` to validate tests.


## Authors

* Sam Kenney - *Initial release* - [sam-kenney](https://github.com/sam-kenney)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
