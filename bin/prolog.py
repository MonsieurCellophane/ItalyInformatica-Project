#!/usr/bin/python
# This snippet:
# 1) finds where it (or importing file) lives - even across symlinks
# 2) assuming its real location is in a subdir of the django project dir, finds Django manage.py script 
# 3) extracts form manage.py the correct DJANGO_SETTINGS_MODULE value and sets it (using regexp/eval)
# 4) prepends manage.py's location to sys.path.
#
# By importing this, scripts living int he same dir have access to all the django modules, plus all those installed in a
# project
import os
import os.path
import sys
import re

#find our own real location: shoudl 
_pdir=os.path.dirname(os.path.abspath(os.path.realpath(__file__)))
#find DJANGO_DIR
_cdir=os.path.dirname(_pdir)
_pth=os.path.join(_cdir,"manage.py")

#tell django where settings.py is
#os.environ.setdefault['DJANGO_SETTINGS_MODULE']='settings'
# search in manage.py

if not os.path.isfile(_pth): raise IOError("Cannot find manage.py as %s"%_pth)
fn=re.compile('(os\.environ\.setdefault\("DJANGO_SETTINGS_MODULE",.*\))')
mng=open(_pth,"r")
for l in mng.readlines():
    m=fn.search(l)
    if m:
        eval(m.groups()[0])
        break
mng.close()

sys.path.insert(0,_cdir)
# try it ...
#__import__( os.environ["DJANGO_SETTINGS_MODULE"] )
try:
    import django
except ImportError:
    raise ImportError(
        "Couldn't import Django. Are you sure it's installed and "
        "available on your PYTHONPATH environment variable? Did you "
        "forget to activate a virtual environment?"
    )
django.setup()


if __name__ == '__main__':
    sys.stderr.write ("Living in %s, DJANGO_DIR:%s, SETTINGS %s\n"%(_pdir,_cdir,os.environ["DJANGO_SETTINGS_MODULE"]))
