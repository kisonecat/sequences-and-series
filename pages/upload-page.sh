#! /bin/bash
#
# download-pages.sh - Download all pages from a Coursera course to HTML files
# 
# (c) 2013, Jim Fowler.
#

# session and csrf are stored in the firefox cookie jar
COOKIE_JAR=~/.mozilla/firefox/8b22l8b2.default/cookies.sqlite

# the course that I am uploading to
COURSERA_COURSE=sequence-001

# load the cookies from the jar
COOKIES=$(sqlite3 $COOKIE_JAR 'select name, value from moz_cookies where baseDomain="coursera.org" and path="/'$COURSERA_COURSE'";' | tr '|' '=' | tr '\n' ';' | sed 's/;/; /g')
MORE_COOKIES=$(sqlite3 $COOKIE_JAR 'select name, value from moz_cookies where baseDomain="coursera.org";' | tr '|' '=' | tr '\n' ';' | sed 's/;/; /g')

CSRF_TOKEN=$(sqlite3 $COOKIE_JAR 'select value from moz_cookies where baseDomain="coursera.org" and path="/'$COURSERA_COURSE'" and name="csrf_token";' | tr '|' '=' | tr -d '\n' | sed 's/;/; /g')

PAGE=$1

EDIT_REVISION=$(curl -L -e https://class.coursera.org/$COURSERA_COURSE/wiki/all --cookie "$COOKIES $MORE_COOKIES" https://class.coursera.org/$COURSERA_COURSE/wiki/edit?page=$PAGE | grep edit_revision | tr -dc 0-9)

PAGE_TITLE=$(curl -L -e https://class.coursera.org/$COURSERA_COURSE/wiki/all --cookie "$COOKIES $MORE_COOKIES" https://class.coursera.org/$COURSERA_COURSE/wiki/edit?page=$PAGE | grep page_title | grep value | sed 's/.*value="//g;s/".*//g')

curl -L -e https://class.coursera.org/$COURSERA_COURSE/wiki/edit?page=$PAGE --cookie "$COOKIES $MORE_COOKIES" -F page_title="$PAGE_TITLE" -F canonical_page_name=$PAGE -F visible=1 -F content=\<$PAGE.html -F wysihtml5_mode=1 -F __csrf-token=$CSRF_TOKEN -F edit_revision=$EDIT_REVISION -F submit=Save https://class.coursera.org/$COURSERA_COURSE/wiki/edit?page=$PAGE\&history=$EDIT_REVISION\&html=1
