import os
import stat
import subprocess
import sys

try:
    subprocess.check_call(["git", "init"])
except subprocess.CalledProcessError as err:
    print('ERROR: git exited with %s!' % err)


try:
    st = os.stat("qa.sh")
    os.chmod("qa.sh", st.st_mode | stat.S_IEXEC)
except OSError as err:
    print("ERROR: Could not make file executable. %s!" % err)
    sys.exit(1)


try:
    os.symlink("../../qa.sh", ".git/hooks/pre-commit")
except OSError as err:
    print("ERROR: Could not symlink git pre-commit hook. %s!" % err)
    sys.exit(1)


try:
    subprocess.check_call(["pyenv", "install", "--skip-existing", "3.8.3"])
except subprocess.CalledProcessError as err:
    print("ERROR: pyenv exited with %s!" % err)
    sys.exit(1)


try:
    subprocess.check_call(["pyenv", "local", "3.8.3"])
except subprocess.CalledProcessError as err:
    print("ERROR: pyenv exited with %s!" % err)
    sys.exit(1)


try:
    subprocess.check_call(["poetry", "update"])
except subprocess.CalledProcessError as err:
    print("ERROR: poetry exited with %s!" % err)
    sys.exit(1)
