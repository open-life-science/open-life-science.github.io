---
layout: page
title: Consulting
image: https://images.unsplash.com/photo-1429962714451-bb934ecdc4ec?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1650&q=80
photos:
  name: Anthony DELANOIX
  license: Unsplash License
  url: https://unsplash.com/photos/hzgs56Ze49s
---

<div class="container">
  <section class="section">
    <h1 class="title">Our Consulting Services</h1>
    <div class="columns is-multiline">
      {% for service in site.data.consulting %}
        <div class="column is-one-third">
          <div class="card">
            <div class="card-content">
              <h2 class="title is-4"><a href="{{ service.url }}">{{ service.name }}</a></h2>
              <p class="content">{{ service.description }}</p>
            </div>
          </div>
        </div>
      {% endfor %}
    </div>
  </section>
</div>
