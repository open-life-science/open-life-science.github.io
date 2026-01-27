---
layout: page
title: Partners
description: Organizations partnering with OLS to support open science training and community building.
image: https://images.unsplash.com/photo-1429962714451-bb934ecdc4ec?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1650&q=80
photos:
  name: Anthony DELANOIX
  license: Unsplash License
  url: https://unsplash.com/photos/hzgs56Ze49s
---

{% assign organizations = site.data.organizations %}

<div class="entities">
{% for p in site.data.community.partners %}
    {% assign entity = organizations[p.organization] %}
    {% assign details = p.details %}
    {% include _includes/external-entities.html entity=entity type='partner' details=details %}
{% endfor %}
</div>
