# pymbend

-----

**Table of Contents**

- [Description)(#description)
- [Installation](#installation)
- [License](#license)

## Description

[`mbend`](https://github.com/nilforooshan/mbend) is an "R package for bending non-positive-definite matrices to positive-definite".
This is a simple port of `mbend` to Python, with the goal of improving computation time.

Some naive timings are below:

| Method | Matrix size | Time [s] |
| --- | ---: | ---: |
| `mbend` | 100 | 0.89 |
| `mbend` | 200 | 13.8 |
| `mbend` | 500 |  |
| `pymbend` | 100 | 0.85 |
| `pymbend` | 200 | 4.4 |
| `pymbend` | 500 | 36.7 |


## Installation

```console
pip install git+https://github.com/zietzm/pymbend
```

## License

`pymbend` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
