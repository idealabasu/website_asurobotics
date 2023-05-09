---
title: Faculty
description: "Pushing the frontiers of Robotics Research"
image:
  feature: 'photoshoot_new/hamid-marvi-19.jpg'
permalink: /faculty/
---

<style type="text/css">
  .noborder {border:0px;
  border-color:rgb(255,255,255);
  box-shadow:none;
  background-color:rgb(255,255,255);}
  .panel p {font-size: 1.125rem;
line-height: 1.44rem;}

  </style>

{% assign sorted_faculty = site.data.faculty | sort:"last_name" %}

{% capture all_tags %}{% for item in site.data.faculty %}{% for tag in item.tags %}{{ tag }},{% endfor %}{% endfor %}{%endcapture%}
{% assign tag_words = all_tags | split:',' | sort | uniq %}

{% capture school_tags %}{% for item in site.data.faculty %}{{ item.school }},{% endfor %}{%endcapture%}
{% assign school_tag_words = school_tags | split:',' | sort | uniq %}

<div class="panel-group" id="accordion">
  <div class="noborder panel panel-default">
    <div id="all" class="panel-collapse collapse in">
      <h2>All</h2>
      {% capture filtered_faculty1 %}{% for item3 in sorted_faculty%}{{item3.name}},{% endfor %}{%endcapture%}
      {% assign filtered_faculty2 = filtered_faculty1 | split:',' | uniq %}
      {% include faculty_list.html %}
    </div>
  </div>
</div>
