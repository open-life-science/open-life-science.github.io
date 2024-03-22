---
layout: page
title: Events
description: The hub of all OLS events
image: https://images.unsplash.com/photo-1535016120720-40c646be5580?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1740&q=80
photos:
  name: Alex Litvin
  url: https://unsplash.com/photos/MAYsdoYpGuk
---

## Upcoming Events

| Date/Time | Topic/Event | Venue/Location | Speakers/Contact | Organisers |
|------|---------------------|----------------|------------------|----|
{% for event in site.data.events %}
| {{ event.date }} at {{ event.time }} | {{ event.title }} | {{ event.event.location }} | {{ event.people }} |  logo  |
{% endfor %}
