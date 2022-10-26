---
layout: page
title: Projects & Participants
image: /images/ols-1/project-participants.jpg
photos:
  name: Andrew West
  license: CC BY-NC-SA 2.0
  url: https://flic.kr/p/2aBxKw
---

{% assign people = site.data.people %}
{% assign projects = site.data.ols-4-projects %}

{% assign all-participants = '' %}
{% for project in projects %}
    {% assign p-pparticipants = '' %}
    {% for p in project.participants %}
        {% capture all-participants %}{{ all-participants}}, {{ p }}{% endcapture %}
    {% endfor %}
{% endfor %}

{% assign p-participants = all-participants | remove_first: ', ' | split: ", " | uniq | sort %}

Participants join this program with a project that they either are already working on or want to develop during this program.

For the third round of the Open Life Science program, we are happy to have [{{ p-participants | size }} participants](#participants) with [{{ projects | size }} projects](#projects).

# Projects

{% for project in projects %}
    {% if project.visible != false %}

        {% assign p-pparticipants = '' %}

        {% for p in project.participants %}
            {% capture p-pparticipants %}{{ p-pparticipants }}, ![](https://avatars.githubusercontent.com/{{ p }}){: .people-badge} [{{ people[p].first-name }} {{ people[p].last-name }}](#{{ p }}){% endcapture %}
        {% endfor %}

        {% assign mentor = project.mentor %}
        {% capture p-mentors %}
        {% for p in project.mentors %}with ![](https://avatars.githubusercontent.com/{{ p }}){: .people-badge} [{{ people[p].first-name }} {{ people[p].last-name }}](/people#{{ p }})
        {% endfor %}
        {% endcapture %}

## {{ project.name }}

**By**: {{ p-pparticipants | remove_first: ', ' }}

**Mentored by**: {{ p-mentors | remove_first: 'with ' }}

{% if project.status %}
**Status**: {{ project.status }}
{% endif %}

    {% capture difference %} {{ project.keywords | size | minus:1 }} {% endcapture %}
    {% unless difference contains '-' %}
**Keywords**: {{ project.keywords | join: ', ' }}
    {% endunless %}

{{ project.description }}

    {% endif %}
{% endfor %}

# Participants

<div class="people">
{% for entry in p-participants %}
    {% assign username = entry %}
    {% assign user = people[username] %}
    {% include _includes/people.html username=username user=user %}
{% endfor %}
</div>
