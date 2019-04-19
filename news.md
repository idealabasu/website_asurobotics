---
title: News
layout: page
permalink: /news/
image:
  feature: 'photoshoot_new/yezhou-yang-23.jpg'
---
<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{site.base_path}}{{ post.url }}">{{ post.title }}</a><br>
      <em>{{ post.date | date: '%B %d, %Y' }}</em>
      {% if post.description %}
        <p>{{ post.description }}</p>
      {% else %}
        {{ post.excerpt }}
      {% endif %}
    </li>
  {% endfor %}
</ul>
