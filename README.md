# PyMCL

PyMCL is a set of Python bindings from the [C++ MCL library](https://github.com/herumi/mcl) by [Herumi](https://github.com/herumi/).

## Installation

1.  Clone, build and install the MCL library (instructions are provided in the [MCL repo](https://github.com/herumi/mcl))
1.  Make sure that the `MCL_PATH` environmental variable is set properly (i.e. it points to where MCL was built/installed)
1.  Run the following commands in any folder you'd like:
```
git clone https://github.com/alex-zaplik/pymcl.git
cd pymcl
sudo python3 setup.py install
```
4.  Done!

## Usage

If MCL and these bindings were installed properly, examples given in `samples/` should run properly if started as follows:
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
