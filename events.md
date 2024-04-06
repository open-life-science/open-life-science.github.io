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
## Upcoming Events
| Date/Time | Topic/Event | Venue/Location | Speakers/Contact | Organisers |
|-----------|-------------|----------------|------------------|------------|
{%- for event in site.events -%}
{%- assign event_date = event.date | date: '%Y-%m-%d' -%}
{%- assign diff_in_months = {{ today | minus: event_date }}%}
{% if diff_in_months <= 4 %}
| {{ event.date }} at {{ event.time }} | {%- if page.type == "external" -%} [{{ event.title }}]({{ event.event_link }}) {%- else -%} [{{ event.title }}]({{ event.url }}) {% endif %} | {{ event.location }} | {{ event.speakers }} | {{ event.organiser }} |
{% else %}
## Past Events
| Date/Time | Topic/Event | Venue/Location | Speakers/Contact | Organisers |
|-----------|-------------|----------------|------------------|------------|
| {{ event.date }} at {{ event.time }} | {%- if page.type == "external" -%} [{{ event.title }}]({{ event.event_link }}) {%- else -%} [{{ event.title }}]({{ event.url }}) {% endif %} | {{ event.location }} | {{ event.speakers }} | {{ event.organiser }} |
{%- endif -%}
{%- endfor -%}
