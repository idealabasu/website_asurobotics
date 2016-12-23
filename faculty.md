---
layout: page
title: Faculty
description: "Pushing the frontiers of Robotics Research"
image:
  feature: basketball_robot016-crop.jpg
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

<p><a data-toggle="collapse" data-parent="#accordion" href="#all"><span class="badge">All</span></a> {% for tag in tag_words %}<a data-toggle="collapse" data-parent="#accordion" href="#{{tag}}"><span class="badge">{{tag}}</span></a> {% endfor %}</p>
<p><a data-toggle="collapse" data-parent="#accordion" href="#all"><span class="badge">All</span></a> {% for tag in school_tag_words %}<a data-toggle="collapse" data-parent="#accordion" href="#{{tag}}"><span class="badge">{{tag}}</span></a> {% endfor %}</p>

{%comment%}
<a data-toggle="collapse" data-parent="#accordion" href="#collapse1"><span class="badge">tag1</span></a>
<a data-toggle="collapse" data-parent="#accordion" href="#collapse2"><span class="badge">tag2</span></a>
<a data-toggle="collapse" data-parent="#accordion" href="#collapse3"><span class="badge">tag3</span></a>
{%endcomment%}


<div class="panel-group" id="accordion">
  <div class="noborder panel panel-default">
    <div id="all" class="panel-collapse collapse in">
      {% capture filtered_faculty1 %}{% for item3 in sorted_faculty%}{{item3.name}},{% endfor %}{%endcapture%}
      {% assign filtered_faculty2 = filtered_faculty1 | split:',' | uniq %}
      {% include faculty_list.html %}
    </div>
  </div>

  {% for tag3 in tag_words%}
    {% capture jj %}{{ forloop.index0 }}{% endcapture %}
    <div class="noborder panel panel-default">
      <div id="{{tag3}}" class="panel-collapse collapse">
        {% capture filtered_faculty1 %}{% for item3 in sorted_faculty %}{% for tag4 in item3.tags %}{% if tag3 == tag4 %}{{item3.name}},{% endif %}{% endfor %}{% endfor %}{%endcapture%}
        {% assign filtered_faculty2 = filtered_faculty1 | split:',' | uniq %}
        {% include faculty_list.html %}
        
      </div>
    </div>
  {%endfor%}

  {% for tag3 in school_tag_words%}
    {% capture jj %}{{ forloop.index0 }}{% endcapture %}
    <div class="noborder panel panel-default">
      <div id="{{tag3}}" class="panel-collapse collapse">
        {% capture filtered_faculty1 %}{% for item3 in sorted_faculty %}{% if tag3 == item3.school %}{{item3.name}},{% endif %}{% endfor %}{%endcapture%}
        {% assign filtered_faculty2 = filtered_faculty1 | split:',' | uniq %}
        {% include faculty_list.html %}
      </div>
    </div>
  {%endfor%}  
</div>
{%comment%}




{% for item in sorted_faculty %}
{% capture ii %}{{ forloop.index0 | modulo: 3 }}{% endcapture %}
{% if ii == '0' %}
<div class="row">
{% endif %}
<div class="col-sm-4">
{% for item2 in site.data.faculty_images %}
{% if item2.name == item.name %}
{% capture image %}{{item2.image}}{% endcapture %}     
{% endif %}
{% endfor %}
<div class="thumbnail">
<img class="img-responsive" src="{{site.base_path}}/assets/headshots/{{image}}" alt="image">
<div class="caption">
<h3>{{item.name}}</h3>
<h4>{{item.title}}, {{item.school}}</h4>
<p><a href="email:{{item.email}}">{{item.email}}</a></p>
<p>{{item.description}}</p>
<p><a href="{{item.lab_link}}" title="{{item.lab_link}}" target="_blank">{{item.lab_link}} <i class="fa fa-external-link"></i></a></p>
<p>{% for tag2 in item.tags %}<span class="badge">{{tag2}}</span> {% endfor %}</p>
</div>
</div>
</div>
{% if ii == '2' %}
</div>
{% endif %}
{% endfor %}



{%endcomment%}
