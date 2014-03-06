require 'rubygems'
require 'json'
require 'date'

COURSE_NAME="sequence-002"
WEEK_COUNT = 6
COURSE_START = Date.civil(2014, 3, 1)

MAX_ATTEMPTS_PER_HOMEWORK = 999
POINTS_PER_HOMEWORK = 20
EXAM_MAX_ATTEMPTS="twice"
EXAM_POINTS = 180
CERTIFICATE_PERCENTAGE = 70
CERTIFICATE_WITH_DISTINCTION_PERCENTAGE = 90
TOTAL_POINTS = POINTS_PER_HOMEWORK * WEEK_COUNT + EXAM_POINTS

WEEK_STARTS = (0...WEEK_COUNT).collect{ |i| COURSE_START + 7*i }
WEEK_ENDS = (0...WEEK_COUNT).collect{ |i| COURSE_START + 7 + 7*i }

COURSERA_COURSE='sequence-002'

def wikipedia(article,title)
  html =<<EOF
<a href="http://en.wikipedia.org/wiki/#{article}"><i class="icon-external-link"></i>&nbsp;#{title}</a>
EOF

  return html.strip
end

def linkto_week(week)
  return '#' if week <= 0 or week > WEEK_COUNT

  return "/#{COURSE_NAME}/wiki/view?page=week#{week}"
end

$videos = JSON.parse(File.open("../identifiers/videos.json").read)
def linkto_video(video,title)
  raise "Missing video #{video}" unless $videos.keys.include?(video)

  html = <<EOF
<a href="/#{COURSE_NAME}/lecture/#{$videos[video]}"><i class="icon-film"></i>&nbsp;#{title}</a>
EOF

  return html.strip
end

$textbook = "https://d396qusza40orc.cloudfront.net/sequence%2Ftextbook%2Fsequences-and-series.pdf"
$labels = {}
for line in File.open('../textbook/textbook.aux').readlines
  if line.match( /^\\newlabel\{([^\}]+)\}\{\{([^\}]+)\}\{([^\}]+)\}/ )
    $labels[$1] = [$2, $3]
  end
  if line.match( /^\\newlabel\{([^\}]+)\}\{\{([^\}]+\{[^\}]+\})\}\{([^\}]+)\}/ )
    $labels[$1] = [$2.gsub( '{', '' ).gsub( '}', '' ), $3]
  end
end

def linkto_textbook(label)
  raise "Missing label #{label}" unless $labels.keys.include?(label)

  kinds = {}
  kinds['fig'] = 'Figure'
  kinds['section'] = 'Section'
  kinds['chapter'] = 'Chapter'
  kinds['subsection'] = 'Subsection'
  kinds['thm'] = 'Theorem'
  kinds['example'] = 'Example'

  kind_code = label.split(":")[0]
  kind = kinds[kind_code]
  name = $labels[label][0]
  page = $labels[label][1]
  link = "#{kind} #{name} on Page #{page} of the Textbook"

  html = <<EOF
<a href="#{$textbook}#page=#{page}"><i class="icon-book"></i>&nbsp;#{link}</a>
EOF

  return html.strip
end

def breadcrumbs(title)
  return <<EOF
<ul class="breadcrumb">
  <li><a href="/#{COURSE_NAME}/class/index">Home</a> <span class="divider">/</span></li>
  <li class="active">#{title}</li>
</ul>
EOF
end

def week_breadcrumbs(week)
  return <<EOF
<ul class="breadcrumb">
  <li><a href="/#{COURSE_NAME}/class/index">Home</a> <span class="divider">/</span></li>
  <li><a href="/#{COURSE_NAME}/wiki/view?page=syllabus">Syllabus</a> <span class="divider">/</span></li>
  <li class="active">Week #{week}</li>
</ul>
EOF
end

def week_title(number,title)
  title =<<EOF
<h3><span style="float: right; color: #888; font-size: 60%; font-weight: normal;">#{WEEK_STARTS[number-1].strftime('%e %B %Y').strip}&ndash;#{WEEK_ENDS[number-1].strftime('%e %B %Y').strip}</span>
<span id=\"week-title\">#{title}</span>
</h3>
EOF

  return week_breadcrumbs(number) + title
end


def week_pager(week)
  previous_disabled = ''
  previous_disabled = 'disabled' if week == 1

  next_disabled = ''
  next_disabled = 'disabled' if week == WEEK_COUNT

  return <<EOF
  <ul class="pager">
     <li class="previous #{previous_disabled}"><a href="#{linkto_week(week-1)}">&larr; Previous Week</a></li>
     <li class="next #{next_disabled}"><a href="#{linkto_week(week+1)}">Next Week &rarr;</a></li>
  </ul>
EOF
end
