# PyMCL

PyMCL is a set of Python bindings to the [C++ MCL library](https://github.com/herumi/mcl) by [Herumi](https://github.com/herumi/).

## Available curves

Seven different curves are currently available in this wrapper:

Curve name  | CurveType value | Supporty pairings |
------------|-----------------|-------------------|
BN160       | MCL_BN160       | True              |
BN254       | MCL_BN254       | True              |
BN381_1     | MCL_BN381_1     | True              |
BN381_2     | MCL_BN381_2     | True              |
BLS12_381   | MCL_BLS12_381   | True              |
BN_SNARK1   | MCL_BN_SNARK1   | True              |
SECP192K1   | MCL_SECP192K1   | False             |
SECP224K1   | MCL_SECP224K1   | False             |
SECP256K1   | MCL_SECP256K1   | False             |
SECP384R1   | MCL_SECP384R1   | False             |
NIST_P192   | MCL_NIST_P192   | False             |
NIST_P224   | MCL_NIST_P224   | False             |
NIST_P256   | MCL_NIST_P256   | False             |
SECP160K1   | MCL_SECP160K1   | False             |
P160_1      | MCL_P160_1      | False             |

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

For now, a couple of global setting calls as well as Lagrange calls
are missing (and may be added in the future).

Fp6 and Fp12 types were not added becaose it didn't seem like they
were needed.

## Compatibility

For now, this binding set only supports Linux operating systems.
The library was tested with MCL v1.52

## Contributions

If you have any problems with this wrapper, please let me know and
I'll try to fix them as soon as possible.
