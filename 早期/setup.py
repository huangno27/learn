#!c:\users\13436\appdata\local\programs\python\python37-32\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'setuptools==39.2.0','console_scripts','easy_install'
__requires__ = 'setuptools==39.2.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('setuptools==39.2.0', 'console_scripts', 'easy_install')()
    )
