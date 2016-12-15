---
layout: default
title: Research Labs
description: Learn about the work being done across schools
---

{% assign sorted_labs = site.data.faculty | sort:"lab_name" %}

<div class="container">

{% capture all_tags %}{% for item in site.data.faculty %}{% for tag in item.tags %}{{ tag }},{% endfor %}{% endfor %}{%endcapture%}
{% assign tag_words = all_tags | split:',' | sort | uniq %}

{% capture school_tags %}{% for item in site.data.faculty %}{{ item.school }},{% endfor %}{%endcapture%}
{% assign school_tag_words = school_tags | split:',' | sort | uniq %}

<p>{% for tag in tag_words %}<a href="#"><span class="badge">{{tag}}</span></a> {% endfor %}</p>
<p>{% for tag in school_tag_words %}<a href="#"><span class="badge">{{tag}}</span></a> {% endfor %}</p>


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
        <p>{{item.school}}</p>
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
