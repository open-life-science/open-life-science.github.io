---
layout: page
title: Events
description: The hub of all OLS events
image: https://images.unsplash.com/photo-1535016120720-40c646be5580?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1740&q=80
photos:
  name: Alex Litvin
  url: https://unsplash.com/photos/MAYsdoYpGuk
---

{% for event in site.data.events %}
    {% if event.category == internal %}
## OLS-organised events
<div class="container">
  <div class="columns">
    <div class="column is-one-third">
      <a href="">
        <div class="card custom-card">
            <div class="card-content">
              <img src="" class="image is-128x128" alt="">
              <h1>{{ event.title }}</h1>
              <p>{{ event.date }} at {{ event.time }}</p>
            </div>
        </div>
      </a>
    </div>
  </div>
</div>
    {% else %}

## We will be speaking at:
<div class="container">
  <div class="columns">
    <div class="column is-one-third">
      <a href="">
        <div class="card custom-card">
            <div class="card-content">
              <img src="" class="image is-128x128" alt="">
              <h1>{{ event.title }}</h1>
              <p>- by {{ event.people }}</p>
              <p>{{ event.date }} at {{ event.time }}</p>
            </div>
        </div>
      </a>
    </div>
  </div>
</div>
    {% endif %}
{% endfor %}