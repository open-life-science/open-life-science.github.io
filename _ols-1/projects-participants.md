---
layout: page
title: Projects & Participants
image: /images/ols-1/project-participants.jpg
photos:
  name: Andrew West
  license: CC BY-NC-SA 2.0
  url: https://flic.kr/p/2aBxKw
---

{% assign mentors = site.data.people %}
{% assign participants = site.data.ols-1-participants %}
{% assign projects = site.data.ols-1-projects %}

Participants join this program with a project that they either are already working on or want to develop during this program.

For the first round of the Open Life Science program, we are happy to have [{{ participants | size }} participants](#participants) with [{{ projects | size }} projects](#projects). 

# Projects

{% for project in projects %}
    {% if project.visible != false %}

        {% capture p-pparticipants %}
        {% for p in project.participants %}, ![](https://avatars.githubusercontent.com/{{ p }}){: .people-badge} [{{ participants[p].name }}](#{{ p }})
        {% endfor %}
        {% endcapture %}

        {% assign mentor = project.mentor %}
        {% capture p-mentors %}
        {% for p in project.mentors %}with ![](https://avatars.githubusercontent.com/{{ p }}){: .people-badge} [{{ mentors[p].name }}](/about#{{ p }})
        {% endfor %}
        {% endcapture %} 

## {{ project.name }}

**By**: {{ p-pparticipants | remove_first: ', ' }}

**Mentored by**: {{ p-mentors | remove_first: 'with ' }} 

{{ project.description }}

    {% endif %}
{% endfor %}

# Participants

<div class="people">
{% for entry in participants %}
    {% assign username = entry[0] %}
    {% assign user = participants[username] %}
    {% include _includes/people.html user=user username=username %}
{% endfor %}
</div>