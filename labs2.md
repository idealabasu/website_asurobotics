---
layout: default
title: Research Labs
description: Learn about the work being done across schools
permalink: /labs2/
---
<div class="container">

{% capture lab_names %}{% for item in site.data.faculty %}{{ item.lab_name }}{% unless forloop.last %},{% endunless %}{% endfor %}{% endcapture %}
{% assign tag_words = lab_names | split:',' | sort %}


{% for item2 in tag_words %}
  {% for item3 in site.data.faculty %}
    {% if item3.lab_name == item2 %}
      {% assign item = item3 %}
    {% endif %}
  {% endfor %}
  <p>{{item.lab_name}}:  {{item.name}}</p>
{% endfor %}

<button data-toggle="collapse" data-target="#demo">Collapsible</button>

<div id="demo" class="collapse">
Lorem ipsum dolor text....
</div>

</div>
