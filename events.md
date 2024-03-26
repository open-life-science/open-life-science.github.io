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

## Upcoming Events

| Date/Time | Topic/Event | Venue/Location | Speakers/Contact | Organisers |
|-----------|-------------|----------------|------------------|------------|
{%- for event in site.data.events -%}
| {{ event.date }} at {{ event.time }} | {{ event.title }} | - | {{ event.people }} | - |
{%- endfor -%}
