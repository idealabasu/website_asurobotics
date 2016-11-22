---
layout: default
title: Faculty
description: "Pushing the frontiers of Robotics Research"
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
      <img class="img-responsive" src="{{site.base_path}}{{item.image}}" alt="image">
      <div class="caption">
        <h3>{{item.name}}</h3>
        <h4>{{item.title}}</h4>
        <p><a href="email:{{item.email}}">{{item.email}}</a></p>
        <p>{% for tag2 in item.tags %}<span class="badge">{{tag2}}</span>{% endfor %}</p>
        <p>
          {%comment%}
            {% for tag in item.tags %}
              {% for tag2 in site.faculty_tags %}
                {% if tag == tag2.name %}
                <a href="{{tag2.link}}"><span class="badge">{{tag2.name}}</span></a> 
                {% endif %}
              {% endfor %}
          {% endfor %}
          {%endcomment%}
        </p>
        <p>{{item.description}}</p>
        <p><a href="{{item.lab_link}}" class="btn btn-primary" role="button">Lab Website</a></p>
      </div>
    </div>
    </div>
    {% if ii == '2' %}
    </div>
    {% endif %}
    {% endfor %}
</div>
