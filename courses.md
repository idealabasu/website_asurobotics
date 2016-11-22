---
layout: page
title: Robotics Courses
description: Explore the range of topics under the Robotics Umbrella
image:
  feature: plains.jpg
---


| Course Number | Title | Level | Faculty | Syllabus | School | Keywords|
|--|--|--|--|--|--|--|
{% for course in site.courses %}| {{course.Course-Number}}| {% if course.link == '' %}{{course.Title}}{%else%}[{{course.Title}}]({{course.link}}){%endif%} | {{course.Level}} | {{course.Faculty}} | {{course.Syllabus-Link}} | {{course.School}} | {{course.Keywords}} |
{% endfor %}
