---
layout: default
title: Research Labs
description: Learn about the work being done across schools
---

{% assign sorted_labs = site.data.faculty | sort:"lab_name" %}

<div class="container">

{%comment%}
{% for tag in site.faculty_tags %}
  <a href="{{tag.link}}"><span class="badge">{{tag.name}}</span></a>
{% endfor %}
{%endcomment%}

{% for item in sorted_labs %}

    {%capture ii %}{{ forloop.index0 | modulo: 3 }}{%endcapture%}
    {% if ii == '0' %}
    <div class="row">
    {% endif %}
    <div class="col-sm-4">
    <div class="thumbnail">
      {% for item2 in site.data.lab_images %}
      {% if item2.name == item.name %}
      {% capture image %}{{item2.image}}{% endcapture %}     
      {% endif %}
      {% endfor %}
      <p><a href="{{item.lab_link}}"><img class="img-responsive" src="{{site.base_path}}/assets/labs/{{image}}" alt="lab image"></a></p>
      <div class="caption">
        <h3><a href="{{item.lab_link}}">{{item.lab_name}}</a></h3>
        <p></p>
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
