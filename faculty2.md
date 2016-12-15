---
layout: default
title: Research Labs
description: Learn about the work being done across schools
---
<div class="container">

{% assign last_names_list = site.data.faculty | sort:"lab_name" %}
{% for item2 in last_names_list %}
  <p>{{item2.name}}</p>
{% endfor %}

</div>
