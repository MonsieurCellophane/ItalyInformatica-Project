#!/bin/bash

USAGE="Usage; $0 user password [baseurl]"
U=$1
P=$2
[[ x$U != x ]] || { echo $USAGE 1>&2 ; exit 1 ; }
[[ x$P != x ]] || { echo $USAGE 1>&2 ; exit 1 ; }

BASE=$3

[[ x$BASE == x ]] && BASE=http://localhost:8000

token=$( http -b POST $BASE/api/auth/token/ username="$U" password="$P" | fgrep token | awk -F: '{print $2}' | sed -e 's/["}]//g' )

if [[ x$token != x ]]; then
    echo "****************"
    echo "* Obtain token *"
    echo "****************"
    http POST $BASE/api/auth/token/ username="$U" password="$P"
    echo "****************"
    echo "* Verify token *"
    echo "****************"
    http POST $BASE/api/auth/verify/ token=$token    
else
    echo "************************"
    echo "* CANNOT Obtain token! *"
    echo "************************"

    http POST $BASE/api/auth/token/ username="$U" password="$P"
    http POST $BASE/api/auth/verify/ token=$token    
fi
																 
