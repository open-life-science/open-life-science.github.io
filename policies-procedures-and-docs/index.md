---
layout: page
title: Policies, Procedures & Documents
image: https://images.unsplash.com/photo-1683178861337-ca70ef8c0db3
photos:
  name: Zetong Li
  license: CC-BY
  url: https://images.unsplash.com/photo-1683178861337-ca70ef8c0db3
---

<h1>{{ page.title }}</h1>

<ul>
  {% for doc in site.policies-procedures-and-docs %}
    <li>
      <a href="{{ doc.url }}">{{ doc.name }}</a>
    </li>
  {% endfor %}
</ul>
