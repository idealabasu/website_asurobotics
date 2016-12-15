---
layout: default
title: Faculty
description: "Pushing the frontiers of Robotics Research"
image:
  feature: basketball_robot016.jpg
---
<div class="container">
{%comment%}
{% for tag in site.faculty_tags %}
  <a href="{{tag.link}}"><span class="badge">{{tag.name}}</span></a>
{% endfor %}
{%endcomment%}

{% assign sorted_faculty = site.data.faculty | sort:"last_name" %}
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
      <p><a href="{{item.lab_link}}" title="{{item.lab_link}}" target="_blank">{{item.lab_link}} <i class="fa fa-external-link"></i></a></p>
    </div>
  </div>
  </div>
  {% if ii == '2' %}
  </div>
  {% endif %}
{% endfor %}
</div>
