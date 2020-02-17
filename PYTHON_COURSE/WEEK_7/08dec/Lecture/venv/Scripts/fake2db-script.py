#!c:\users\administrateur\onedrive\bureau\di_python_course\week_7\08dec\lecture\venv\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'fake2db==0.5.4','console_scripts','fake2db'
__requires__ = 'fake2db==0.5.4'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('fake2db==0.5.4', 'console_scripts', 'fake2db')()
    )
