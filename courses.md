---
title: Robotics Courses
description: Explore the range of topics under the Robotics Umbrella
permalink: /courses/
---


| Course Number | Title | Level | Faculty | School | Description |
|--|--|--|--|--|--|--|
{% for course in site.data.courses %}| {{course.Course-Number}}| {% if course.link == '' %}{{course.Title}}{%else%} <a href="{{course.link}}" target="_blank">{{course.Title}}</a>{%endif%} | {{course.Level}} | {{course.Faculty}} | {{course.School}} | {{course.Keywords}} |
{% endfor %}
