---
layout: page
title: Events & Outreach
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

# Events

Past and upcoming events either organised by OLS or where OLS presented.

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

# Interviews, media mentions, spotlights, shoutouts

OLS mentions around the web.

### 2023
- The Science in Real Life Podcast: _Open Science, founding Open Seeds / Open Life Science (OLS) and getting into academia backwards with Yo Yehudi, Executive Director Open Seeds_. [Spotify](https://open.spotify.com/episode/3iH7n6nKJGPnLDpw9nhHKQ), [Anchor.fm](https://anchor.fm/s/de20d8c8/podcast/play/72415957/https%3A%2F%2Fd3ctxlq1ktw2nl.cloudfront.net%2Fstaging%2F2023-5-21%2Fd76f80cd-2d11-ce32-bd23-3b28c8df8f3c.mp3), [[Archived link](https://web.archive.org/web/20260128225632/https://d3ctxlq1ktw2nl.cloudfront.net/staging/2023-5-21/d76f80cd-2d11-ce32-bd23-3b28c8df8f3c.mp3)]

- Code for Thought Podcast: _RSE in Asia (Saranjeet Kaur and Jyoti Boghal)_. <https://codeforthought.buzzsprout.com/1326658/episodes/12813116-en-rse-in-asia>, [[Archived link](https://web.archive.org/web/20250516234318/https://codeforthought.buzzsprout.com/1326658/episodes/12813116-en-rse-in-asia)] 

### 2021
- Galaxy Community Hub: _Open Life Science program & the Galaxy community: involvement in OLS-3 and invitation to apply to the next cohort_. <https://galaxyproject.org/news/2021-06-ols/>, [[Archived link](https://web.archive.org/web/20260128224623/https://galaxyproject.org/news/2021-06-ols/)] 


### 2020
- CogX: _Awards shortlist update!_ [Archived link](https://web.archive.org/web/20201022234044/https://cogx.co/blog/cogx-awards-2020-shortlisted/)
- Software Sustainability Institute blog: _Open Life Science: where we are_. <https://www.software.ac.uk/blog/open-life-science-where-we-are>, [[Archived link](https://web.archive.org/web/20260128224843/https://www.software.ac.uk/blog/open-life-science-where-we-are)] 
- Software Sustainability Institute blog: _Key skills to know before mentoring_. <https://www.software.ac.uk/blog/2020-10-09-key-skills-know-mentoring>, [[Archived link]()] 
- The Alan Turing Institute Spotlights: _Malvika Sharan_. <https://www.turing.ac.uk/people/spotlights/malvika-sharan>, [[Archived link](https://web.archive.org/web/20210227221747/https://www.turing.ac.uk/people/spotlights/malvika-sharan)] 
- EOSC-Life News: _4 Projects awarded funding within First Training Open Call_. <https://www.eosc-life.eu/news/4-projects-awarded-funding-within-first-training-open-call/>, [[Archived link](https://web.archive.org/web/20201229172246/https://www.eosc-life.eu/news/4-projects-awarded-funding-within-first-training-open-call/)] 
- Galaxy Community Hub: _Open Life Science program & the Galaxy community: involvement in OLS-2 and invitation to apply to the next cohort_. <https://galaxyproject.org/news/2020-12-22-ols/>, [[Archived link](https://web.archive.org/web/20250906161052/https://galaxyproject.org/news/2020-12-22-ols/)] 


### 2019
- Software Sustainability Institute blog: _Supercharge your open project with leadership training_. <https://www.software.ac.uk/blog/2019-11-22-supercharge-your-open-project-leadership-training>, [[Archived link](https://web.archive.org/web/20260128224200/https://www.software.ac.uk/blog/supercharge-your-open-project-leadership-training)]

