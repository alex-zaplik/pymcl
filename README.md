# PyMCL

PyMCL is a set of Python bindings from the [C++ MCL library](https://github.com/herumi/mcl) by [Herumi](https://github.com/herumi/).

## Available curves

Four different curves are currently available in this wrapper:

Curve name  | CurveType value |
------------|-----------------|
BN160       | MCL_BN160       |
BN254       | MCL_BN254       |
BLS12_381   | MCL_BLS12_381   |
BN_SNARK1   | MCL_BN_SNARK1   |

## Installation

1.  Clone, build and install the MCL dynamic library (instructions are provided in the [MCL repo](https://github.com/herumi/mcl))
1.  Make sure that the `MCL_PATH` environmental variable is set properly (it should point to a folder containing MCL `lib` and `include` folders)
1.  Run the following commands in any folder you'd like:
```
git clone https://github.com/alex-zaplik/pymcl.git
cd pymcl
sudo python3 setup.py install
```
4.  Done!

## Usage

If MCL and these bindings were installed properly, examples given in `samples/` should run properly if started in the following way:
```
python3 <path_to_sample>.py
```

## Missing parts of the API

For now, only BLS12_381 is supperted and a couple of global
setting calls as well as Lagrange calls are missing (and
may be added in the future).

Fp6 and Fp12 types were not added becaose it didn't seem like they
were needed.

## Compatibility

For now, this binding set only supports Linux operating systems.
The library was tested with MCL v1.52

## Contributions

If you have any problems with this wrapper, please let me know and
I'll try to fix it as soon as possible.
