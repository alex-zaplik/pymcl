import ctypes
import platform
import os

MCL_PATH = os.environ.get("MCL_PATH", "/usr/local/")

def load_lib(path, *args):
    try:
        return ctypes.CDLL(path, *args)
    except OSError:
        print(
f"""Failed to import mcl library from {MCL_PATH}.
Please set mcl installation directory to MCL_PATH and run again.

export MCL_PATH=<path>
""")

name = platform.system()
if name == 'Linux':
    load_lib(MCL_PATH + "lib/libmcl.so", ctypes.RTLD_GLOBAL)
    mcl = load_lib(MCL_PATH + "lib/libmclbn384_256.so")
else:
    raise RuntimeError(f'Not supported yet: {name}')
