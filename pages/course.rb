require 'date'

COURSE_NAME="sequence-001"
WEEK_COUNT = 6
COURSE_START = Date.civil(2013, 9, 27)

POINTS_PER_HOMEWORK = 20
EXAM_POINTS = 180
CERTIFICATE_PERCENTAGE = 70
CERTIFICATE_WITH_DISTINCTION_PERCENTAGE = 90
TOTAL_POINTS = POINTS_PER_HOMEWORK * WEEK_COUNT + EXAM_POINTS

WEEK_STARTS = (0...WEEK_COUNT).collect{ |i| COURSE_START + 7*i }
WEEK_ENDS = (0...WEEK_COUNT).collect{ |i| COURSE_START + 7 + 7*i }

COURSERA_COURSE='sequence-001'

def linkto_week(week)
  return '#' if week <= 0 or week > WEEK_COUNT

  return "/#{COURSE_NAME}/wiki/view?page=week#{week}"
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
