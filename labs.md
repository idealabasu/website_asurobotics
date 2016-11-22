---
layout: default
title: Research Labs
description: Learn about the work being done across schools
image:
  feature: plains.jpg
---
<div class="container">

{%comment%}
{% for tag in site.faculty_tags %}
  <a href="{{tag.link}}"><span class="badge">{{tag.name}}</span></a>
{% endfor %}
{%endcomment%}

  {% for item in site.faculty %}
    {%capture ii %}{{ forloop.index0 | modulo: 3 }}{%endcapture%}
    {% if ii == '0' %}
    <div class="row">
    {% endif %}
    <div class="col-sm-4">
    <div class="thumbnail">
      {%comment%}<img class="img-responsive" src="..." alt="lab image">{%endcomment%}
      <div class="caption">
        <h3>{{item.lab_name}}</h3>
        <p><a href="{{item.lab_link}}">{{item.lab_link}}</a></p>
        <p>{{item.lab_description}}</p>
        <p>{% for tag2 in item.tags %}<span class="badge">{{tag2}}</span> {% endfor %}</p>
      </div>
    </div>
    </div>
    {% if ii == '2' %}
    </div>
    {% endif %}
    {% endfor %}
</div>