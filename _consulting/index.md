---
layout: page
title: Consulting
description: OLS consulting services including accessibility, ally skills training, and organisational leadership workshops.
permalink: /consulting/
image: https://images.unsplash.com/photo-1429962714451-bb934ecdc4ec?
photos:
  name: Anthony DELANOIX
  license: Unsplash License
  url: https://unsplash.com/photos/hzgs56Ze49s
---

{% assign services = site.consulting | where_exp: "item", "item.name != 'index.md'" %}

<div class="container">
  <section class="section">
    <h1 class="title">Our Consulting Services</h1>
    <div class="columns is-multiline">
      {% for service in services %}
        <div class="column is-one-third">
          <div class="card">
            <div class="card-content">
              <h2 class="title is-4"><a href="{{ service.url }}">{{ service.title }}</a></h2>
              <p class="content">{{ service.excerpt }}</p>
            </div>
          </div>
        </div>
      {% endfor %}
    </div>
  </section>
</div>
