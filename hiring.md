---
title: Hiring
layout: page
permalink: /hiring/
---
<div class="row">
  <div class="col-md-6 col-md-offset-2 col-xs-12 col-xs-offset-0">
    <h2> Research Positions</h2>
  </div>
</div>

{% for post in site.jobs %}
<div class="row">
    <div class="col-md-6 col-md-offset-2 col-xs-10 col-xs-offset-0">
    <ul>
    <li>
      <a target="_blank" href="{{site.base_path}}{{ post.url }}">{{ post.title }}</a><br>
      <em>{{ post.date | date: '%B %d, %Y' }}</em>
      <p>
        {{ post.content | strip_html | strip_newlines | truncate: 100 }}
      </p>
     </li>
     </ul>
     </div>
    <div class="col-md-2 col-xs-2"><a href="{{site.base_path}}{{ post.url }}" targer="_blank"><button type="button" class="btn btn-primary btn-lg">Go...</button></a></div>
</div>
{% endfor %}
