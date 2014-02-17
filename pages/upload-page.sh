#! /bin/bash
#
# download-pages.sh - Download all pages from a Coursera course to HTML files
# 
# (c) 2013, Jim Fowler.
#

# session and csrf are stored in the firefox cookie jar
COOKIE_JAR=~/.mozilla/firefox/8b22l8b2.default/cookies.sqlite

# the course that I am uploading to
COURSERA_COURSE=sequence-002

# load the cookies from the jar
COOKIES=$(sqlite3 $COOKIE_JAR 'select name, value from moz_cookies where baseDomain="coursera.org" and path="/'$COURSERA_COURSE'";' | tr '|' '=' | tr '\n' ';' | sed 's/;/; /g')
MORE_COOKIES=$(sqlite3 $COOKIE_JAR 'select name, value from moz_cookies where baseDomain="coursera.org";' | tr '|' '=' | tr '\n' ';' | sed 's/;/; /g')

CSRF_TOKEN=$(sqlite3 $COOKIE_JAR 'select value from moz_cookies where baseDomain="coursera.org" and path="/'$COURSERA_COURSE'" and name="csrf_token";' | tr '|' '=' | tr -d '\n' | sed 's/;/; /g')

PAGE=$1

PAGE_CODE=$(curl -L -e https://class.coursera.org/$COURSERA_COURSE/wiki/all --cookie "$COOKIES $MORE_COOKIES" https://class.coursera.org/sequence-002/wiki/$PAGE | grep /admin/coursepages/ | sed 's/.*\/admin\/coursepages\///;s/".*//')

CSRF2_COOKIE=$(echo $COOKIES $MORE_COOKIES | tr ';' '\n' | grep -m1 csrf2 | sed 's/^ //g' | cut -f 1 -d '=')
CSRF2_TOKEN=$(echo $COOKIES $MORE_COOKIES | tr ';' '\n' | grep -m1 csrf2 | sed 's/^ //g' | cut -f 2 -d '=')

cat $PAGE.html | python -c "import json,sys; print('{\"content\":' + json.dumps(sys.stdin.read())+\"}\")" | curl --cookie "$COOKIES $MORE_COOKIES" -H "Host: class.coursera.org" -H "User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:26.0) Gecko/20100101 Firefox/26.0" -H "Content-Type: application/json; charset=utf-8" -H "If-Match: 44" -H "X-HTTP-Method-Override: PATCH" -H "X-CSRF-Token:$CSRF_TOKEN" -H "X-CSRF2-Cookie: $CSRF2_COOKIE" -H "X-CSRF2-Token: $CSRF2_TOKEN" -H "X-Requested-With: XMLHttpRequest" -H "Referer: https://class.coursera.org/sequence-002/admin/coursepages/$PAGE_CODE"  --data @- "https://class.coursera.org/$COURSERA_COURSE/admin/api/pages/$PAGE_CODE?fields=content"
