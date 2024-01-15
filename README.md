# pymbend

## Description

[`mbend`](https://github.com/nilforooshan/mbend) is an "R package for bending non-positive-definite matrices to positive-definite".
This is a simple port of `mbend` to Python, with the goal of improving computation time.

Some naive timings are below:

| Matrix size | `mbend` time [s] | `pymbend` time [s] |
| --- | ---: | ---: |
| 100 | 0.89 | 0.85|
| 200 | 13.8 | 4.4 |
| 500 | 1370.6 | 36.7 |

These were made on a 2021 Intel MacBook Pro.


In addition, it adds the ability to bend a matrix ($A$) to satisfy a generalized Rayleigh quotient inequality:
$$0 \leq \frac{\beta^\intercal A \beta}{\beta^\intercal B \beta} \leq 1$$


## Installation

```console
pip install git+https://github.com/zietzm/pymbend
```

## License

`pymbend` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
