import os
import stat
import subprocess
import sys

try:
    st = os.stat('qa.sh')
    os.chmod('qa.sh', st.st_mode | stat.S_IEXEC)
except OSError as err:
    print('ERROR: Could not make file executable. %s!' % err)
    sys.exit(1)


try:
    subprocess.check_call(["pyenv", "install", "--skip-existing", "3.8.3"])
except subprocess.CalledProcessError as err:
    print('ERROR: pyenv exited with %s!' % err)


try:
    subprocess.check_call(["pyenv", "local", "3.8.3"])
except subprocess.CalledProcessError as err:
    print('ERROR: pyenv exited with %s!' % err)


try:
    subprocess.check_call(["poetry", "update"])
except subprocess.CalledProcessError as err:
    print('ERROR: poetry exited with %s!' % err)
