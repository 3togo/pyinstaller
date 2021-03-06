# LD_LIBRARY_PATH set by bootloader should not contain ./
#
# This test assumes the LD_LIBRARY_PATH is not set before running the test.
# If you experience that this test fails, try to unset the variable and
# rerun the test.
#
# This is how it is done in bash:
#
#  $ cd buildtests
#  $ unset LD_LIBRARY_PATH
#  $ ./runtests.py basic/test_absolute_ld_library_path.py

import os
import sys

# For Linux, Solaris, AIX only

libpath = os.path.normpath(os.path.abspath(os.path.dirname(sys.executable)))
libpath += '/'

# The name of the environment variable used to define the path where the
# OS should search for dynamic libraries.
if sys.platform.startswith('aix'):
    libpath_var_name = 'LIBPATH'
else:
    libpath_var_name = 'LD_LIBRARY_PATH'

print('LD_LIBRARY_PATH expected: ' + libpath)

libpath_from_env = os.environ.get(libpath_var_name)
print('LD_LIBRARY_PATH  current: ' + libpath_from_env)
assert libpath == libpath_from_env
