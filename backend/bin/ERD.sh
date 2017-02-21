#!/bin/bash

abspath() {
    curdir=$(pwd)
    if [[ -d "$1" ]]; then
	retval=$( cd "$1" ; pwd )
    else 
	retval=$( cd $( dirname "$1" ); pwd )/$(basename "$1")
    fi
    cd $curdir
    echo $retval
}

usage="$0 outfile.pdf"

[[ x$APPS == x ]] && APPS="accounts schema swt registration  auth"
[[ x$1 == x    ]] && { echo $usage 1>&2 ; exit 1 ; }

MANAGE=$(dirname $(dirname $(abspath $0)))/manage.py
python  $MANAGE graph_models -v 3 $APPS | dot -Tpdf > $1

