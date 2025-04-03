---
layout: page
title: Events
description: The hub of all OLS events
image: https://images.unsplash.com/photo-1503428593586-e225b39bddfe
photos:
  name: The Climate Reality Project
  license: CC BY-SA 4.0
  url: https://images.unsplash.com/photo-1503428593586-e225b39bddfe
---

{% assign people = site.data.people %}
{% assign date_format = site.minima.date_format | default: "%b %-d, %Y" %}
{% assign events = site.events | sort: 'date_start' | reverse %}

This page lists all past and upcoming events either organised by OLS or where OLS presented.

<table class="eventtable table is-striped">
  <thead>
    <tr>
      <th>Date</th>
      <th>Type</th>
      <th>Event</th>
      <th>Location</th>
      <th>Contributions from OLS</th>
    </tr>
  </thead>
  <tbody>
  {% for event in events  %}
    {% unless event.draft %}
    <tr>
      <td> {{ event.date_start | date: date_format }} {% if event.date_end %} - {{ event.date_end | date: date_format }}{% endif %} </td>
      <td>{{ event.type | capitalize }}</td>
      <td>
        <a class="eventtable-title" href="{% if event.external %}{{ event.external }}{% else %}{{ event.url }}{% endif %}">{{ event.title }}</a>
        <br>
        <span class="eventtable-description">{{ event.description }}</span>
      </td>
      <td> 
        {% if event.location.name == "Online" %}
        Online
        {% else %}
        {{ event.location.city }}, {{ event.location.country }}
        {% endif %}
      </td>
      <td>
        {% if event.contributions.organisers %}
          {% assign group = event.contributions.organisers %}
          {% include _includes/avatars.html %}
        <span class="eventtable-contribution">Organisers:</span> {{ avatars | remove_first: ', ' }}
        <br/>
        {% endif %}
        {% if event.contributions.instructors %}
          {% assign group = event.contributions.instructors %}
          {% include _includes/avatars.html %}
        <span class="eventtable-contribution">Instructors:</span> {{ avatars | remove_first: ', ' }}
        <br/>
        {% endif %}
        {% if event.contributions.facilitators %}
          {% assign group = event.contributions.facilitators %}
          {% include _includes/avatars.html %}
        <span class="eventtable-contribution">Facilitators:</span> {{ avatars | remove_first: ', ' }}
        <br/>
        {% endif %}
        {% if event.contributions.helpers %}
          {% assign group = event.contributions.helpers %}
          {% include _includes/avatars.html %}
        <span class="eventtable-contribution">Helpers:</span> {{ avatars | remove_first: ', ' }}
        <br/>
        {% endif %}
        {% if event.contributions.talks %}
        <span class="eventtable-contribution">Talks</span>
        <br/>
          {% for talk in event.contributions.talks %}
            {% assign group = talk.speakers %}
            {% include _includes/avatars.html %}
            <i>"{{ talk.title }}"</i>&nbsp;
            {% include _includes/event-support.html contribution=talk %}
            {% if talk.speakers %}by {{ avatars | remove_first: ', ' }}{% endif %}
            <br/>
          {% endfor %}
        <br/>
        {% endif %}
        {% if event.contributions.posters %}
        <span class="eventtable-contribution">Posters</span>
        <br/>
          {% for poster in event.contributions.posters %}
            {% assign group = poster.presenters %}
            {% include _includes/avatars.html %}
            <i>"{{ poster.title }}"</i> 
            {% if poster.poster %}([<i class="fas fa-image"></i> Poster]({{ poster.poster }})){% endif %} 
            {% if poster.presenters %}by {{ avatars | remove_first: ', ' }}{% endif %}
            <br/>
          {% endfor %}
        <br/>
        {% endif %}
        {% if event.contributions.workshops %}
        <span class="eventtable-contribution">Workshops</span>
        <br/>
          {% for workshop in event.contributions.workshops %}
            {% assign group = workshop.facilitators %}
            {% include _includes/avatars.html %}
            <i>"{{ workshop.title }}"</i>&nbsp;
            {% include _includes/event-support.html contribution=workshop %}
            {% if workshop.facilitators %}by {{ avatars | remove_first: ', ' }}{% endif %}
            <br/>
          {% endfor %}
        <br/>
        {% endif %}
      </td>
    </tr>
    {% endunless %}
  {% endfor %}
  </tbody>
</table>
