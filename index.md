---
layout: default
title: ASU Robotics
description: "Innovating in the field of Robotics"
carousel-images:
  - DiscoverEDay-2016-Poly-9642a.jpg
  - 20160901PanagiotisArtemiadis03.jpg
  - 2016-12-02 16.49.57.jpg
  - 2016-10-14 15.07.51.jpg
  - DiscoverEDay-2016-Poly-9628a.jpg
  - DiscoverEDay-2016-Poly-9637a.jpg
  - DiscoverEDay-2016-Poly-9693a.jpg
  - 12973087_10207425984500397_2859409810083467075_o.jpg
  - 13217446_10207661186940311_4240935783057552354_o.jpg
  - DSCF6893small.jpg
  - vlcsnap-2015-04-01-09h59m23s59.png
  - IMG_20160727_122058653.jpg
  - Mind Drones.00_03_24_28.Still003.jpg
---
<style type="text/css">
  .carousel-caption {bottom:none; top:500px;
</style>
{%comment%}
<div class="jumbotron">
  <div class="container">
  </div>
</div>
{%endcomment%}

<div class="container">

<h2>News</h2>
<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a></br>
      <em>{{ post.date | date: '%B %d, %Y' }}</em>
      {% if post.custom_excerpt %}
        <p>{{ post.custom_excerpt }}</p>
      {% else %}
        {{ post.excerpt }}
      {% endif %}
    </li>
  {% endfor %}
</ul>

<hr/>

<h2>
Get Involved
</h2>

<div class="row">
    <div class="col-md-4 text-center">
      <h1><a href="{{site.base_path}}/labs"><i class="fa fa-flask" aria-hidden="true"></i></a></h1>
      <p>
      Find a <a href="{{site.base_path}}/labs">lab</a> to do research.    
      </p>
    </div>
    <div class="col-md-4 text-center">
    <h1><a href="{{site.base_path}}/courses"><i class="fa fa-university" aria-hidden="true"></i></a></h1>
      <p>
      Take a <a href="{{site.base_path}}/courses">course</a> taught by our faculty!
      </p>
    </div>
    <div class="col-md-4 text-center">
    <h1><a href="{{site.base_path}}/resources"><i class="fa fa-wrench" aria-hidden="true"></i></a></h1>
      <p>
      Make a robot in one of our <a href="{{site.base_path}}/resources">maker spaces</a>!
      </p>
    </div>
</div>

<hr/>

<div id="carousel-example-generic" class="carousel slide"  style="max-height: 700px; overflow: hidden;" data-ride="carousel">
  <!-- Indicators -->
  <ol class="carousel-indicators">
  {% for item in page.carousel-images %}
  {% capture ii %}{{ forloop.index0 }}{% endcapture %}
    <li data-target="#carousel-example-generic" data-slide-to="{{ii}}"{% if ii == '0' %} class="active"{% endif %}></li>
  {%endfor%}
  </ol>

  <!-- Wrapper for slides -->
  <div class="carousel-inner" role="listbox">
  {% for item in page.carousel-images %}
  {% capture ii %}{{ forloop.index0 }}{% endcapture %}
    <div class="item{% if ii == '0' %} active{% endif %}">
      <img src="{{site.base_path}}/assets/images/carousel/{{item}}" alt="...">
{%comment%}
      <div class="carousel-caption">
        This is a caption
      </div>
{%endcomment%}

    </div>
{%endfor%}
  </div>

  <a class="left carousel-control" href="#carousel-example-generic" role="button" data-slide="prev">
    <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>
    <span class="sr-only">Previous</span>
  </a>
  <a class="right carousel-control" href="#carousel-example-generic" role="button" data-slide="next">
    <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
    <span class="sr-only">Next</span>
  </a>
</div>


<h2>
Our Mission
</h2>

<div class="row" style="margin-top:0;">
<div class="col-md-6">
<div class="panel panel-default">
  <div class="panel-heading">
    <h3 class="panel-title">Make Change</h3>
  </div>
  <div class="panel-body">
  Help drive positive change in society by connecting researchers at Arizona State University to collaboratively pursue advancements in robotics technologies, systems and education that will serve our most critical needs.
  </div>
</div>
</div>
<div class="col-md-6">
<div class="panel panel-default">
  <div class="panel-heading">
    <h3 class="panel-title">Leverage our Community</h3>
  </div>
  <div class="panel-body">
  Solve our problems more quickly and effectively by utilizing ASU’s growing, multidisciplinary research community and expanding its impact by establishing high-quality research relationships with industry, government and the public.
  </div>
</div>
</div>
<div class="col-md-6">
<div class="panel panel-default">
  <div class="panel-heading">
    <h3 class="panel-title">Solve Problems</h3>
  </div>
  <div class="panel-body">
  Explore the potential of robotics to help meet an array of challenges in the realms of health care, education, transportation, manufacturing, national defense, public safety, environmental health, communications, sustainable energy systems and earth and space exploration.
  </div>
</div>
</div>
<div class="col-md-6">
<div class="panel panel-default">
  <div class="panel-heading">
    <h3 class="panel-title">Nurture the Future</h3>
  </div>
  <div class="panel-body">
  Nurture the next generation of robotics researchers through innovative educational practices, in-lab experiences and mentoring in entrepreneurship that create opportunities for students to develop their creative abilities, trains them to be skilled problem solvers and prepares them to establish themselves in the robotics community and in industry.
  </div>
</div>
</div>
</div>

{%comment%}
1. Help drive positive change in society by connecting researchers at Arizona State University to collaboratively pursue advancements in robotics technologies, systems and education that will serve our most critical needs.
1. Solve our problems more quickly and effectively by utilizing ASU’s growing, multidisciplinary research community and expanding its impact by establishing high-quality research relationships with industry, government and the public.
1. Explore the potential of robotics to help meet an array of challenges in the realms of health care, education, transportation, manufacturing, national defense, public safety, environmental health, communications, sustainable energy systems and earth and space exploration.
1. Nurture the next generation of robotics researchers through innovative educational practices, in-lab experiences and mentoring in entrepreneurship that create opportunities for students to develop their creative abilities, trains them to be skilled problem solvers and prepares them to establish themselves in the robotics community and in industry.
{%endcomment%}
<hr/>

<h2>
Join our Community
</h2>

<div class="row space-bot-xl" style="margin-top:0;">
<div class="col-sm-6 col-md-4 space-bot-md"><img alt="" class="img-responsive space-bot-md" /><h3><a href="https://webapp4.asu.edu/programs/t5/graduate/false"><button class="btn btn-blue btn-block btn-lg">Explore degrees</button></a></h3>
</div>
<div class="col-sm-6 col-md-4 space-bot-md"><img alt="" class="img-responsive space-bot-md" /><h3><a href="https://www.asu.edu/gradapp"><button class="btn btn-gold btn-block btn-lg">Apply now</button></a></h3>
</div>
<div class="col-sm-6 col-md-4 space-bot-md"><img alt="" class="img-responsive space-bot-md" /><h3><a href="https://requestinfo.asu.edu/prospect_form"><button class="btn btn-gold btn-block btn-lg">Request information</button></a></h3>
</div>
</div>
<hr/>

</div>
