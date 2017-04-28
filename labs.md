---
title: Research Labs
description: Learn about the work being done across schools
permalink: /labs/
---
<style type="text/css">
  .noborder {border:0px;
  border-color:rgb(255,255,255);
  box-shadow:none;
  background-color:rgb(255,255,255);}
  .panel p {font-size: 1.125rem;
line-height: 1.44rem;}

  </style>

{% assign sorted_faculty = site.data.faculty | sort:"lab_name" %}

{% capture all_tags %}{% for item in site.data.faculty %}{% for tag in item.tags %}{{ tag }},{% endfor %}{% endfor %}{%endcapture%}
{% assign tag_words = all_tags | split:',' | sort | uniq %}

{% capture school_tags %}{% for item in site.data.faculty %}{{ item.school }},{% endfor %}{%endcapture%}
{% assign school_tag_words = school_tags | split:',' | sort | uniq %}

<p>Filter by Topic: <a data-toggle="collapse" data-parent="#accordion" href="#all"><span class="badge">All</span></a> {% for tag in tag_words %}<a data-toggle="collapse" data-parent="#accordion" href="#{{tag}}"><span class="badge">{{tag}}</span></a> {% endfor %}</p>
<p>Filter by School: <a data-toggle="collapse" data-parent="#accordion" href="#all"><span class="badge">All</span></a> {% for tag in school_tag_words %}<a data-toggle="collapse" data-parent="#accordion" href="#{{tag}}"><span class="badge">{{tag}}</span></a> {% endfor %}</p>

<div class="panel-group" id="accordion">
  <div class="noborder panel panel-default">
    <div id="all" class="panel-collapse collapse in">
      <h2>All</h2>
      {% capture filtered_faculty1 %}{% for item3 in sorted_faculty%}{{item3.name}},{% endfor %}{%endcapture%}
      {% assign filtered_faculty2 = filtered_faculty1 | split:',' | uniq %}
      {% include list_labs.html %}
    </div>
  </div>

  {% for tag3 in tag_words%}
    {% capture jj %}{{ forloop.index0 }}{% endcapture %}
    <div class="noborder panel panel-default">
      <div id="{{tag3}}" class="panel-collapse collapse">
        <h2>{{tag3}}</h2>
        {% capture filtered_faculty1 %}{% for item3 in sorted_faculty %}{% assign tt = item3.tags | split:',' | sort | uniq %}{% for tag4 in tt %}{% if tag3 == tag4 %}{{item3.name}},{% endif %}{% endfor %}{% endfor %}{%endcapture%}
        {% assign filtered_faculty2 = filtered_faculty1 | split:',' | uniq %}
        {% include list_labs.html %}

      </div>
    </div>
  {%endfor%}

  {% for tag3 in school_tag_words%}
    {% capture jj %}{{ forloop.index0 }}{% endcapture %}
    <div class="noborder panel panel-default">
      <div id="{{tag3}}" class="panel-collapse collapse">
        <h2>{{tag3}}</h2>
        {% capture filtered_faculty1 %}{% for item3 in sorted_faculty %}{% if tag3 == item3.school %}{{item3.name}},{% endif %}{% endfor %}{%endcapture%}
        {% assign filtered_faculty2 = filtered_faculty1 | split:',' | uniq %}
        {% include list_labs.html %}
      </div>
    </div>
  {%endfor%}  
</div>
