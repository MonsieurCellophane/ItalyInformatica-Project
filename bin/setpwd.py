#! /usr/bin/env python
import prolog
import sys
from django.contrib.auth.models import User

if len(sys.argv) != 3:
    sys.stderr.write("Usage: %s username password\n"%sys.argv[0])
    sys.exit(1)

try:
    u=User.objects.get(username=sys.argv[1])
    u.set_password(sys.argv[2])
except User.DoesNotExist:
    sys.stderr.write("User %s does not exist\n"%sys.argv[1])
    

    



