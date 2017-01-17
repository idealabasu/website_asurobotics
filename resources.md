---
title: Robotics Resources
description: Learn how to access robotics resources on campus
permalink: /resources/
carousel-images:
#  - DSC_0021.JPG
#  - DSC_0007.JPG
#  - DSC_0008.JPG
#  - DSC_0010.JPG
  - DSC_0011.JPG
  - DSC_0014.JPG
  - DSC_0001.JPG
  - DSC_0003.JPG
  - DSC_0004.JPG
  - DSC_0006.JPG
  - DSC_0015.JPG
  - DSC_0016.JPG
  - DSC_0017.JPG
  - DSC_0018.JPG
  - DSC_0020.JPG
  - DSC_0023.JPG
  - DSC_0025.JPG
  - DSC_0027.JPG
  - DSC_0028.JPG
  - DSC_0029.JPG
  - DSC_0030.JPG
  - DSC_0031.JPG
  - DSC_0032.JPG
  - DSC_0033.JPG
  - DSC_0034.JPG
---

<style type="text/css">
  .carousel-caption {bottom:none; top:500px;
</style>

## Tempe Campus

<div class="row">
  <div class="col-md-4">
    <img alt="" class="img-responsive" src="{{site.base_path}}/assets/images/drone-space.jpg" />
  </div>
  <div class="col-md-8">
    <h3>eDroneZone Lab</h3>
    <p>
      Tempe Campus<br>
      Physical Education Building East (PEBE), Room 143
    </p>
  </div>
</div>
&nbsp;
<div class="row">
  <div class="col-md-4">
    <img alt="" class="img-responsive" src="{{site.base_path}}/assets/images/3DprintLab2.jpg" />
  </div>
  <div class="col-md-8">
    <h3>3D Print Lab</h3>
    <p>
      <a href="http://rts.clas.asu.edu/mis" target="_blank">Link <i class="fa fa-external-link"></i></a><br>
      Tempe Campus<br>
      ECF Building, Room 103
    </p>
  </div>
</div>
&nbsp;
<div class="row">
  <div class="col-md-4">
    <img alt="" class="img-responsive" src="{{site.base_path}}/assets/images/MachineShop3.jpg" />
  </div>
  <div class="col-md-8">
    <h3>Machine Shop</h3>
    <p>
      <a href="http://fse3dprintlab.wikispaces.asu.edu/" target="_blank">Link <i class="fa fa-external-link"></i></a><br>
      Tempe Campus<br>
      PSF Building, Room 64<br>
      Contact
    </p>
  </div>
</div>
&nbsp;
<div class="row">
  <div class="col-md-4">
    <img alt="" class="img-responsive" src="{{site.base_path}}/assets/images/NanoFab1.jpg" />
  </div>
  <div class="col-md-8">
    <h3>Nano Fab</h3>
    <p>
      <a href="http://engineering.asu.edu/nanofab/" target="_blank">Link <i class="fa fa-external-link"></i></a><br>
      Tempe Campus<br>
      ERC Building, Basement
    </p>
  </div>
</div>
&nbsp;
<div class="row">
  <div class="col-md-4">
    <img alt="" class="img-responsive" src="{{site.base_path}}/assets/images/" />
  </div>
  <div class="col-md-8">
    <h3>Gait-Motion Capture Lab</h3>
    <p>
      Tempe Campus<br>
      ECC Building, Room 117
    </p>
  </div>
</div>

## Polytechnic Campus
The Polytechnic School, one of the six Fulton Schools of Engineering at Arizona State University, is ideally equipped to help you with your next robotics project.  Research on the Polytechnic campus  primarily takes place in the Technology Center, which is recently expanded its research capabilities to encompass an ~ 875 square-foot motion-capture lab and three new robotics lab spaces in Fall 2016.

<div class="row">
  <div class="col-md-4">
    <div id="carousel-example-generic" class="carousel slide"  data-ride="carousel">
      <!-- Indicators -->
      <ol class="carousel-indicators">
        {% for item in page.carousel-images %}
          {% capture ii %}{{ forloop.index0 }}{% endcapture %}
          <li data-target="#carousel-example-generic" data-slide-to="{{ii}}"{% if ii == '0' %} class="active"{% endif %}></li>
        {%endfor%}
      </ol>
      <div class="carousel-inner" role="listbox">
        {% for item in page.carousel-images %}
          {% capture ii %}{{ forloop.index0 }}{% endcapture %}
          <div class="item{% if ii == '0' %} active{% endif %}">
            <img class="img-responsive" src="{{site.base_path}}/assets/carousels/startup-lab/{{item}}" alt="...">
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
  </div>
  <div class="col-md-8">
    <h3>Startup Lab</h3>
    <p>
      <a href="https://poly.engineering.asu.edu/research/startuplabs/" target="_blank">https://poly.engineering.asu.edu/research/startuplabs/ <i class="fa fa-external-link"></i></a><br>
      Technology Center(TECH)
    </p><p>
      "Making" space is available in the "Startup Lab", a 15,000 square-foot general-purpose fabrication and development area in the Technology Center which houses many of the larger shared pieces of fabrication equipment which can be used for class, project, and personal use.  
    </p><p>
      The Startup Lab has several important pieces of equipment as well, including: A Shop Bot Wood 3D Router, a 50 Watt Epilog Laser Engraver and Cutter, a 90-Watt large-bed Full Spectrum laser cutter, a multi-material Objet Connex3 350 printer, an Objet 30 printer, and several ABS plastic 3D printers including a Dimension Elite, a Fortus 450, a Fortus 250, a UPrint, and four Lulzbot Minis.  We will also use the micro scribe digitizer probe, the 3D Scanner, Vinyl Cutter, Sewing Machine, Vacuum Former, Injection Molding Press and the variety of hand tools which are also available as needed.
    </p>
  </div>
</div>
&nbsp;
<div class="row">
  <div class="col-md-4">
    <img alt="" class="img-responsive" src="{{site.base_path}}/assets/images/motion-capture.jpg" />
  </div>
  <div class="col-md-8">
    <h3>Motion Capture Lab</h3>
    <p>
      Technology Center(TECH), Room 184
    </p><p>
      This is an ~875 Square-foot motion capture studio outfitted with a split treadmill, a vicon vision system, a video projector, and a force platform for use with research into biomechanics and robotic systems
    </p>
  </div>
</div>
