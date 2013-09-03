#! /usr/bin/ruby

require 'rubygems'
require 'json'

# session and csrf are stored in the firefox cookie jar
COOKIE_JAR="~/.mozilla/firefox/8b22l8b2.default/cookies.sqlite"

# the course that I am uploading to
COURSERA_COURSE="sequence-001"

# load the cookies from the jar
COOKIES=`sqlite3 #{COOKIE_JAR} 'select name, value from moz_cookies where baseDomain="coursera.org" and path="/'#{COURSERA_COURSE}'";' | tr '|' '=' | tr '\n' ';' | sed 's/;/; /g'`
MORE_COOKIES=`sqlite3 #{COOKIE_JAR} 'select name, value from moz_cookies where baseDomain="coursera.org";' | tr '|' '=' | tr '\n' ';' | sed 's/;/; /g'`

sections = JSON.parse(`curl -e https://class.coursera.org/#{COURSERA_COURSE}/admin/ --cookie "#{COOKIES} #{MORE_COOKIES}" "https://class.coursera.org/#{COURSERA_COURSE}/admin/api/sections?course_id=#{COURSERA_COURSE}&full=1&draft=1"`)

hash = Hash.new

for section in sections
  for item in  section["items"]
    if item["item_type"] == "lecture" and not item["source_video"].nil?
      my_name = item["source_video"].split('.')[0]
      coursera_id = item["id"]
      hash[my_name] = coursera_id
    end
  end
end

f = File.open("videos.json","w")
f.puts hash.to_json
f.close
