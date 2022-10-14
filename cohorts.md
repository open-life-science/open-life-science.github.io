---
layout: page
title: All Open Life Science Cohorts till Date!
image: /images/syllabus.jpg
photos:
  name: Niklas Morberg
  license: CC BY-NC 2.0
  url: https://flic.kr/p/5BXB6s
---

# Cohorts

<div class='cohort-grid'>
  <div class="flip-card">
  <div class="flip-card-inner">
    <div class="flip-card-front">
    <h1>OLS - 1</h1>
    </div>
    <div class="flip-card-back">
   <a href='ols-1'><h2>Click here to find out more about the first cohort!</h2></a>
    </div>
  </div>
 </div>

 
 <div class="flip-card">
  <div class="flip-card-inner">
    <div class="flip-card-front">
    <h1>OLS - 2</h1>
    </div>
    <div class="flip-card-back">
      <a href='ols-2'><h2>Click here to find out more about the second cohort!</h2></a>
    </div>
  </div>
 </div>

 
 <div class="flip-card">
  <div class="flip-card-inner">
    <div class="flip-card-front">
    <h1>OLS - 3</h1>
    </div>
    <div class="flip-card-back">
      <a href='ols-3'><h2>Click here to find out more about the third cohort!</h2></a>
    </div>
  </div>
 </div>

 <div class="flip-card">
  <div class="flip-card-inner">
    <div class="flip-card-front">
    <h1>OLS - 4</h1>
    </div>
    <div class="flip-card-back">
      <a href='ols-4'><h2>Click here to find out more about the fourth cohort!</h2></a>
    </div>
  </div>
 </div>

 <div class="flip-card">
  <div class="flip-card-inner">
    <div class="flip-card-front">
    <h1>OLS - 5</h1>
    </div>
    <div class="flip-card-back">
      <a href='ols-5'><h2>Click here to find out more about the fifth cohort!</h2></a>
    </div>
  </div>
 </div>

  <div class="flip-card">
  <div class="flip-card-inner">
    <div class="flip-card-front">
    <h1>OLS - 6</h1>
    </div>
    <div class="flip-card-back">
      <a href='ols-6'><h2>Click here to find out more about the sixth cohort!</h2></a>
    </div>
  </div>
 </div>
</div>

# The OLS Program
{:.no_toc}

**Purpose**: Training for early stage researchers and young leaders interested in furthering their
Open Science skills

**Outcome**: Ambassadors for Open Science practice, training and education across multiple European
and international bioinformatics communities.

**Process**: A 15-16 week mentoring & training program, based on the [Mozilla Open Leader program](https://foundation.mozilla.org/en/opportunity/mozilla-open-leaders/), helping participants in becoming Open Science ambassadors by using three principles:

1. **Sharing** essential knowledge required to create, lead, and sustain an Open Science project.
2. **Connecting** members across different communities, backgrounds, and identities by creating space in this program for them to share their experiences and expertise.
3. **Empowering** them to become effective Open Science ambassadors in their communities.

{% include _includes/toc.html %}

# Our Goals and Learning Objectives

The vision of Open Life Science program is to strengthen Open Science skills for early stage researchers and young leaders in life science.

At the end of the program, our participants will be able to:
- Describe and define the terms *openness*, *open science*, *open leadership*, *community interactions*, *value exchanges*, *inclusivity*, *accessibility*, *open Science practices in developing resources and training*
- Learn how to apply those principles to open leadership and working open in their projects and communities
. Learn how to collect, invite, and tell stories that demonstrate how and why openness benefits the communities they serve
- Give original examples for the types of openness in science
- Design
  - Illustrate the need for a project, its vision, and its goals
  - Embrace and communicate the benefits of Open Science and how to strategically apply different open practices to their work
  - Identify the public resources to share their data
  - Identify the different type of Open Access and associated journals
- Build
  - Start any project with openness in mind from day one
  - Setup a project repository on GitHub using best practices for enabling collaboration
  - Choose and apply open licenses appropriately
- Empower
  - Create and enforce a safe working environment
  - Promote the values of Open Science to empower others to lead and collaborate
  - Include a broad range of contributors in their work
  - Communicate their work and vision in a 2min demo of elevator pitch
- Lead an open project in science

# OLS Cohorts - An Overview

<!-- OLS-1 -->
{% assign ols-1-projects = site.data.ols-1-projects %}
{% assign ols-1-experts = site.data.ols-1-metadata.experts %}
{% assign mentors = '' %}
{% assign participants = '' %}
{% for project in ols-1-projects %}
    {% assign p-pparticipants = '' %}
    {% for p in project.participants %}
        {% capture participants %}{{ participants}}, {{ p }}{% endcapture %}
    {% endfor %}
    {% for m in project.mentors %}
        {% capture mentors %}{{ mentors }}, {{ m }}{% endcapture %}
    {% endfor %}
{% endfor %}
{% assign ols-1-mentors = mentors | remove_first: ', ' | split: ", " | uniq | sort %}
{% assign ols-1-participants = participants | remove_first: ', ' | split: ", " | uniq | sort %}
{% assign ols-1-schedule = site.data.ols-1-schedule %}
{% assign ols-1-end = '' %}
{% for w in ols-1-schedule.weeks %}
    {% assign ols-1-end = w[1].start %}
{% endfor %}
<!-- OLS-2 -->
{% assign ols-2-projects = site.data.ols-2-projects %}
{% assign ols-2-experts = site.data.ols-2-metadata.experts %}
{% assign mentors = '' %}
{% assign participants = '' %}
{% for project in ols-2-projects %}
    {% assign p-pparticipants = '' %}
    {% for p in project.participants %}
        {% capture participants %}{{ participants}}, {{ p }}{% endcapture %}
    {% endfor %}
    {% for m in project.mentors %}
        {% capture mentors %}{{ mentors }}, {{ m }}{% endcapture %}
    {% endfor %}
{% endfor %}
{% assign ols-2-mentors = mentors | remove_first: ', ' | split: ", " | uniq | sort %}
{% assign ols-2-participants = participants | remove_first: ', ' | split: ", " | uniq | sort %}
{% assign ols-2-schedule = site.data.ols-2-schedule %}
{% assign ols-2-end = '' %}
{% for w in ols-2-schedule.weeks %}
    {% assign ols-2-end = w[1].start %}
{% endfor %}
<!-- OLS-3 -->
{% assign ols-3-projects = site.data.ols-3-projects %}
{% assign ols-3-experts = site.data.ols-3-metadata.experts %}
{% assign ols-3-facilitators = site.data.ols-3-metadata.facilitators %}
{% assign mentors = '' %}
{% assign participants = '' %}
{% for project in ols-3-projects %}
    {% assign p-pparticipants = '' %}
    {% for p in project.participants %}
        {% capture participants %}{{ participants}}, {{ p }}{% endcapture %}
    {% endfor %}
    {% for m in project.mentors %}
        {% capture mentors %}{{ mentors }}, {{ m }}{% endcapture %}
    {% endfor %}
{% endfor %}
{% assign ols-3-mentors = mentors | remove_first: ', ' | split: ", " | uniq | sort %}
{% assign ols-3-participants = participants | remove_first: ', ' | split: ", " | uniq | sort %}
{% assign ols-3-schedule = site.data.ols-3-schedule %}
{% assign ols-3-end = '' %}
{% for w in ols-3-schedule.weeks %}
    {% assign ols-3-end = w[1].start %}
{% endfor %}
<!-- OLS-4-->
{% assign ols-4-projects = site.data.ols-4-projects %}
{% assign ols-4-experts = site.data.ols-4-metadata.experts %}
{% assign ols-4-facilitators = site.data.ols-4-metadata.facilitators %}
{% assign mentors = '' %}
{% assign participants = '' %}
{% for project in ols-4-projects %}
    {% assign p-pparticipants = '' %}
    {% for p in project.participants %}
        {% capture participants %}{{ participants}}, {{ p }}{% endcapture %}
    {% endfor %}
    {% for m in project.mentors %}
        {% capture mentors %}{{ mentors }}, {{ m }}{% endcapture %}
    {% endfor %}
{% endfor %}
{% assign ols-4-mentors = mentors | remove_first: ', ' | split: ", " | uniq | sort %}
{% assign ols-4-participants = participants | remove_first: ', ' | split: ", " | uniq | sort %}
{% assign ols-4-schedule = site.data.ols-4-schedule %}
{% assign ols-4-end = '' %}
{% for w in ols-4-schedule.weeks %}
    {% assign ols-4-end = w[1].start %}
{% endfor %}
<!-- OLS-5-->
{% assign ols-5-projects = site.data.ols-5-projects %}
{% assign ols-5-experts = site.data.ols-5-metadata.experts %}
{% assign ols-5-facilitators = site.data.ols-5-metadata.facilitators %}
{% assign mentors = '' %}
{% assign participants = '' %}
{% for project in ols-5-projects %}
    {% assign p-pparticipants = '' %}
    {% for p in project.participants %}
        {% capture participants %}{{ participants}}, {{ p }}{% endcapture %}
    {% endfor %}
    {% for m in project.mentors %}
        {% capture mentors %}{{ mentors }}, {{ m }}{% endcapture %}
    {% endfor %}
{% endfor %}
{% assign ols-5-mentors = mentors | remove_first: ', ' | split: ", " | uniq | sort %}
{% assign ols-5-participants = participants | remove_first: ', ' | split: ", " | uniq | sort %}
{% assign ols-5-schedule = site.data.ols-5-schedule %}
{% assign ols-5-end = '' %}
{% for w in ols-5-schedule.weeks %}
    {% assign ols-5-end = w[1].start %}
{% endfor %}
<!-- OLS-6-->
{% assign ols-6-projects = site.data.ols-6-projects %}
{% assign ols-6-experts = site.data.ols-6-metadata.experts %}
{% assign ols-6-facilitators = site.data.ols-6-metadata.facilitators %}
{% assign mentors = '' %}
{% assign participants = '' %}
{% for project in ols-6-projects %}
    {% assign p-pparticipants = '' %}
    {% for p in project.participants %}
        {% capture participants %}{{ participants}}, {{ p }}{% endcapture %}
    {% endfor %}
    {% for m in project.mentors %}
        {% capture mentors %}{{ mentors }}, {{ m }}{% endcapture %}
    {% endfor %}
{% endfor %}
{% assign ols-6-mentors = mentors | remove_first: ', ' | split: ", " | uniq | sort %}
{% assign ols-6-participants = participants | remove_first: ', ' | split: ", " | uniq | sort %}
{% assign ols-6-schedule = site.data.ols-6-schedule %}
{% assign ols-6-end = '' %}
{% for w in ols-6-schedule.weeks %}
    {% assign ols-6-end = w[1].start %}
{% endfor %}

Cohort | Schedule | Projects | Mentors | Experts | Facilitators
--- | --- | --- | --- | --- | ---
[OLS-1]({% link ols-1.md %}) | [{{ ols-1-schedule.weeks['01'].start }} - {{ ols-1-end }}]({% link _ols-1/schedule.md %}) | [{{ ols-1-participants | size }} mentees](/ols-1/projects-participants#participants) working on [{{ ols-1-projects | size }} projects](/ols-1/projects-participants#projects) | [{{ ols-1-mentors | size }} mentors](/ols-1#mentors) | [{{ ols-1-experts | uniq | size }} experts](/ols-1#experts) | 
[OLS-2]({% link ols-2.md %}) | [{{ ols-2-schedule.weeks['01'].start }} - {{ ols-2-end }}]({% link _ols-2/schedule.md %}) | [{{ ols-2-participants | size }} mentees](/ols-2/projects-participants#participants) working on [{{ ols-1-projects | size }} projects](/ols-2/projects-participants#projects) | [{{ ols-2-mentors | size }} mentors](/ols-2#mentors) | [{{ ols-2-experts | uniq | size }} experts](/ols-2#experts) | 
[OLS-3]({% link ols-3.md %}) | [{{ ols-3-schedule.weeks['01'].start }} - {{ ols-3-end }}]({% link _ols-3/schedule.md %}) | [{{ ols-3-participants | size }} mentees](/ols-3/projects-participants#participants) working on [{{ ols-3-projects | size }} projects](/ols-3/projects-participants#projects) | [{{ ols-3-mentors | size }} mentors](/ols-3#mentors) | [{{ ols-3-experts | uniq | size }} experts](/ols-3#experts) | [{{ ols-3-facilitators | uniq | size }} facilitator](/ols-3#facilitators)
[OLS-4]({% link ols-4.md %}) | [{{ ols-4-schedule.weeks['01'].start }} - {{ ols-4-end }}]({% link _ols-4/schedule.md %}) | [{{ ols-4-participants | size }} mentees](/ols-4/projects-participants#participants) working on [{{ ols-4-projects | size }} projects](/ols-4/projects-participants#projects) | [{{ ols-4-mentors | size }} mentors](/ols-4#mentors) | [{{ ols-4-experts | uniq | size }} experts](/ols-4#experts) | [{{ ols-4-facilitators | uniq | size }} facilitators](/ols-4#facilitators)
[OLS-5]({% link ols-5.md %}) | [{{ ols-5-schedule.weeks['01'].start }} - {{ ols-5-end }}]({% link _ols-5/schedule.md %}) | [{{ ols-5-participants | size }} mentees](/ols-5/projects-participants#participants) working on [{{ ols-5-projects | size }} projects](/ols-5/projects-participants#projects) | [{{ ols-5-mentors | size }} mentors](/ols-5#mentors) | [{{ ols-5-experts | uniq | size }} experts](/ols-5#experts) | [{{ ols-5-facilitators | uniq | size }} facilitators](/ols-5#facilitators)
[OLS-6]({% link ols-6.md %}) | [{{ ols-6-schedule.weeks['01'].start }} - {{ ols-6-end }}]({% link _ols-6/schedule.md %}) | [{{ ols-6-participants | size }} mentees](/ols-6/projects-participants#participants) working on [{{ ols-6-projects | size }} projects](/ols-6/projects-participants#projects) | [{{ ols-6-mentors | size }} mentors](/ols-6#mentors) | [{{ ols-6-experts | uniq | size }} experts](/ols-6#experts) | [{{ ols-6-facilitators | uniq | size }} facilitators](/ols-6#facilitators)