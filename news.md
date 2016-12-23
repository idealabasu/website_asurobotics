---
title: News
layout: page
permalink: /news/
---

{% for post in site.posts %}
  <li>
    <span class="post-meta">{{ post.date | date: "%b %-d, %Y" }}</span>

    <h2>
      <a class="post-link" href="{{ post.url | prepend: site.base_path }}">{{ post.title }}</a>
    </h2>
    
  </li>
{% endfor %}
