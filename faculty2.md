---
layout: default
title: Research Labs
description: Learn about the work being done across schools
---
<div class="container">
<style type="text/css">
  .noborder {border:0px;
  border-color:rgb(255,255,255);
  box-shadow:none;
  background-color:rgb(255,255,255);}
</style>

{% assign last_names_list = site.data.faculty | sort:"lab_name" %}
{% for item2 in last_names_list %}
  <p>{{item2.name}}</p>
{% endfor %}


<a data-toggle="collapse" data-parent="#accordion" href="#collapse1">
Collapsible Group 1</a>
<a data-toggle="collapse" data-parent="#accordion" href="#collapse2">
Collapsible Group 2</a>
<a data-toggle="collapse" data-parent="#accordion" href="#collapse3">
Collapsible Group 3</a>

<div class="panel-group" id="accordion">
 <div class="noborder panel panel-default">
   <div id="collapse1" class="panel-collapse collapse in">
     Lorem ipsum dolor sit amet, consectetur adipisicing elit,
     sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad
     minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
     commodo consequat.
   </div>
 </div>
 <div class="noborder panel panel-default">
   <div id="collapse2" class="panel-collapse collapse">
   Lorem ipsum dolor sit amet, consectetur adipisicing elit,
   sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad
   minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
   commodo consequat.
   </div>
 </div>
 <div class="noborder panel panel-default">
   <div id="collapse3" class="panel-collapse collapse">
   Lorem ipsum dolor sit amet, consectetur adipisicing elit,
   sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad
   minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
   commodo consequat.
   </div>
 </div>
</div>

</div>
