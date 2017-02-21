#!/bin/bash

ver=0.1
author="Monsieur Cellophane <MrC3llophane@gmail.com>"
name=`basename $0`
BASE='http://127.0.0.1:8000'
METH='GET'

URL='/test/'

sa_usage () { 	echo "Usage: $name [-b base] [-m method] username password [abspath [args]]"; }
usage () {
	echo "$name $ver $author"
	echo
	echo $(sa_usage)
	echo
	echo "        -b   baseurl (default: $BASE)"
	echo "        -m   method (GET,POST...) (default: $METH)"
	echo " username: your username"
	echo " password: your password"
	echo " abspath : absolute path to browse (default: $URL)"
	echo " args    : additional args"
	echo 
	echo "tests an authenticated request"
	echo
	echo "See also: Django"
	echo
}

#http://stackoverflow.com/questions/3915040/bash-fish-command-to-print-absolute-path-to-a-file
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

#usage: if ask "Do you [y/n]" y; then this; else that; fi
# will write
#  Do you [y/n]?> 
# and return true if use enters y
function ask() {
    if [[ x$ASSUME_YES != x ]]; then /bin/true; return ; fi
    echo -n $1 "?> " 1>&2 
    read ans
    if [[ x$ans == x$2 ]]; then
	/bin/true
    else
	/bin/false
    fi
}

vbs() {
    [[ x$opt_v != x ]] && echo $1 1>&2
}

die() {
    echo $1 1>&2
    exit $2
}

warn() {
    echo $1 1>&2
}

token() {
    local flags
    [[ x$opt_v != x ]] && flags="$flags -v"

    http $flags -b POST $BASE/api/auth/token/ username="$1" password="$2" | fgrep '{"token":' | awk -F: '{print $2}' | sed -e 's/["}]//g'
}

tokenfmt() {
    echo $1 | awk -F, '{print $2;}' | base64 -d | sed -e s'/.*"usage": "//' -e 's/".$//'
}

request() {
    local header=$1
    shift
    local url=$1
    shift
    local flags
    [[ x$opt_v != x ]] && flags="$flags -v"
    
    http $flags $METH ${BASE}${url} "$header" $@
}

while getopts dvhb:m: opt ; do
	case "$opt" in
	        d) set -x ;;
		b) BASE="$OPTARG" ;;
		b) METH="$OPTARG" ;;
	        v) opt_v=1 ;;
		?) usage; exit ;;
	esac
done

shift `expr $OPTIND - 1`

U=$1
shift
P=$1
shift
[[ x$U == x ]] &&  die "$(sa_usage)" ; 
[[ x$P == x ]] &&  die "$(sa_usage)" ; 
[[ x$1 != x ]] && { URL=$1 ; shift ; }

token=$(token $U $P)
vbs "Acquired token: $token"
fmt=$(tokenfmt $token)
vbs "Token format: '$fmt'"
header=$(printf "$fmt" $token)
vbs "header: '$header'"

request "$header" "$URL" "$@"



