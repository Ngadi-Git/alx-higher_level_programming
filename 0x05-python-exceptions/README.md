# Python - Exceptions

In this project, I learned handling errors and exceptions in Python with `try`
and `except`.

## Function Prototypes :floppy_disk:

Prototypes for functions written in this project:

| File                             | Prototype                                               |
| -------------------------------- | ------------------------------------------------------- |
| `0-safe_print_list.py`           | `def safe_print_list(my_list=[], x=0):`                 |
| `1-safe_print_integer.py`        | `def safe_print_integer(value):`                        |
| `2-safe_print_list_integers.py`  | `def safe_print_list_integers(my_list=[], x=0):`        |
| `3-safe_print_division.py`       | `def safe_print_division(a, b):`                        |
| `4-list_division.py`             | `def list_division(my_list_1, my_list_2, list_length):` |
| `5-raise_exception.py`           | `def raise_exception():`                                |
| `6-raise_exception_msg.py`       | `def raise_exception_msg(message=""):`                  |
| `100-safe_print_integer_err.py`  | `def safe_print_integer_err(value):`                    |
| `101-safe_function.py`           | `def safe_function(fct, *args):`                        |
| `102-magic_calculation.py`       | `def magic_calculation(a, b);`                          |
| `103-python.c`                   | <ul><li>`void print_python_list(PyObject *p);`</li><li>`void print_python_bytes(PyObject *p);`</li><li>`void print_python_float(PyObject *p);`</li></ul> |

## Tasks :page_with_curl:

* **0. Safe list printing**
  * [0-safe_print_list.py](./0-safe_print_list.py): Python function that prints `x` elements
  of a list on the same line, followed by a new line.
  * The parameter `x` represents the number of elements to print - can be
  bigger than the length of `my_list`.
  * Returns the real number of elements printed.
  * Without importing modules or using `len()`.

* **1. Safe printing of an integers list**
  * [1-safe_print_integer.py](./1-safe_print_integer.py): Python function that prints an integer in `"{:d}".format()` format.
  * The parameter `value` can be any type.
  * Returns `True` if `value` was printed correctly (ie. was an integer),
  `False` otherwise.

