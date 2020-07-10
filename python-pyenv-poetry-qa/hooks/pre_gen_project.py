import re
import sys


MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'
package_slug = '{{ cookiecutter.package_slug }}'
if not re.match(MODULE_REGEX, package_slug):
    print('ERROR: %s is not a valid Python package name!' % package_slug)
    sys.exit(1)
