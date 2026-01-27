---
layout: page
title: Projects in Open Seeds
description: Browse all projects developed by participants across Open Seeds cohorts.
image: https://images.unsplash.com/photo-1585399058947-f68f9db58e5f?q=80&w=3870&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D
photos:
  name: Adomas Aleno
  license: Unsplash License
  url: https://unsplash.com/photos/person-holding-white-printer-paper--ySLeov8m_8
---

{% include _includes/cohort-loop.html %}

Participants join Open Seeds program with a project that they either are already working on or want to develop during this program individually or in teams.
Project ideas can range from solving technical questions to creating an open data project or report, developing an open source software project, writing an open publication, facilitating community/team culture movements, advancing open educational resources or contributing to other existing projects/communities.

# Projects per cohorts



{% for cohort in cohorts %}
    {% assign cohort_name = cohort[0] %}
    {% assign projects = cohort[1].projects %}
    {% assign schedule = cohort[1].schedule %}
    {% assign cohort_start = schedule.weeks['01'].start %}
    {% assign cohort_end = '' %}
    {% for week in schedule.weeks %}
        {% assign cohort_end = week[1].start %}
    {% endfor %}
    {% assign participants = '' %}
    {% for project in projects %}
        {% for p in project.participants %}
            {% capture participants %}{{ participants }}, {{ p }}{% endcapture %}
        {% endfor %}
    {% endfor %}
    {% assign participants = participants | remove_first: ', ' | split: ', ' | uniq | size %}
    {% if participants > 0 %}
- [{{ projects | size }} projects]({% link openseeds/{{ cohort_name }}/projects-participants.md %}#projects) ([{{ participants }} participants]({% link openseeds/{{ cohort_name }}/projects-participants.md %}#participants)) for [**{{ cohort_name | upcase }}**]({% link openseeds/{{ cohort_name }}/index.md %}) ({{ cohort_start }} - {{ cohort_end }})
    {% endif %}
{% endfor %}

# All projects

{% include _includes/openseeds-project.html %}

*This table is based on the work done by Angelica Maineri as part of OLS-7 cohort*