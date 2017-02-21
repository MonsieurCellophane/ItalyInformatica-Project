#! /usr/bin/env python
from sys import argv
import sys
import getopt
from getopt import getopt, gnu_getopt,GetoptError
import os

import prolog
from django.contrib.auth.models import User


(VERSION,AUTHOR,NAME)=("0.1",'Alessandro Forghieri <alf@orion.it>',os.path.basename(__file__))

def  usage():
    sys.stderr.write( """
    %s %s %s
    Usage: %s [-f] [-p] [-r] [substring]
	        -d   debug
	        -v   verbose
                -h   print help
	        -f   print user fields
	        -p   print profile fields
	        -r   print registration fields
	sustring: partial username (all users if omitted)
	
    Lists user(s) and details

	See also: django
""" %(NAME,VERSION,AUTHOR,NAME))
    sys.exit(1)

(ops,opl)=('fprdvh',['full','profile','registration','verbose','help','debug'])
(DEBUG,opt_v,opt_h,opt_f,opt_p,opt_r)=(0,False,False,False,False,False);

def vbs (*args):
    if not opt_v: return
    sys.stderr.write(''.join(args))

def d0 (*args):
    if not DEBUG: return
    sys.stderr.write(''.join(args))

def dN (level,*args):
    if  not DEBUG or DEBUG<level : return
    sys.stderr.write(''.join(args))

def  brk(level=1):
    if DEBUG and DEBUG>=level:
        import pdb; pdb.set_trace()

#(options, rest) = getopt(argv[1:],
try:
    (opts,rest) = gnu_getopt(argv[1:],ops,opl)
except GetoptError,e:
    sys.stderr.write("Error: %s\n"%str(e))
    usage()

for opt, arg in opts:
    if opt in ('-f', '--full'):
        opt_f=True
    if opt in ('-p', '--profile'):
        opt_p=True
    if opt in ('-r', '--registration'):
        opt_r=True
    elif opt in ('-v', '--verbose'):
        opt_v = True
    elif opt in ('-d', '--debug'):
        DEBUG += 1
    elif opt in ('-h', '--help'):
        opt_h=True
        

#from django.db.models.fields.related_descriptors import RelatedObjectDoesNotExist
#uflds=[x.name for x in User._meta.get_fields()]
#uflds=['logentry', 'profile', u'registration', u'id', 'password', 'last_login', 'is_superuser', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'date_joined', 'groups', 'user_permissions']
uflds=[u'id','first_name', 'last_name', 'email','is_superuser','is_staff', 'is_active', 'date_joined']

if len(rest) > 0:
    qs=User.objects.filter(username__contains=rest[0])
else:
    qs=User.objects.all()
    
for u in qs :
    sys.stdout.write('%s'%u.username)
    if opt_f:
        for field  in uflds:
            sys.stdout.write(':%s=%s'%(field,str(getattr(u,field,None))))
    #profile
    if opt_p:
        sys.stdout.write('|')
        try:
            # assumes a suitable iterator; see Profile
            for field,val in u.profile:
                if field == 'bio' and val is not None: val=val[:10]
                if field == 'owner' and val is not None: val=val.id
                sys.stdout.write('%s=%s:'%(field,str(val)))
        except AttributeError as e :
            sys.stderr.write(e.message)
    #registration
    if opt_r:
        sys.stdout.write('|')
        try:
            # assumes a suitable iterator; see registration
            reg=u.registration
            for field,val in u.registration:
                if field == 'bio' and val is not None: val=val[:10]
                if field == 'owner' and val is not None: val=val.id
                sys.stdout.write('%s=%s:'%(field,str(val)))
        except AttributeError as e :
            sys.stderr.write(e.message)
        
    print
    
    

