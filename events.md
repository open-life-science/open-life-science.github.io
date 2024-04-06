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

{%- assign today = site.time | date: '%Y-%m-%d' -%}

## Events

| Date/Time | Topic/Event | Venue/Location | Speakers/Contact | Organisers |
|-----------|-------------|----------------|------------------|------------|
{%- for event in site.events | sort: 'date' | reverse  -%}
{%- assign event_date = event.date | date: '%Y-%m-%d' -%}
| {{ event_date }} at {{ event.time }} | {%- if page.type == "external" -%} [{{ event.title }}]({{ event.event_link }}) {%- else -%} [{{ event.title }}]({{ event.url }}) {% endif %} | {{ event.location }} | {{ event.speakers }} | {{ event.organiser }} |
{%- endfor -%}
