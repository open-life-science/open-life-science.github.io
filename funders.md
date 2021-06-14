---
layout: page
title: Funders and Partners
image: https://images.unsplash.com/photo-1429962714451-bb934ecdc4ec?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1650&q=80
photos:
  name: Anthony DELANOIX
  license: Unsplash License
  url: https://unsplash.com/photos/hzgs56Ze49s
---

# Funders

This program has been funded by the following funding organisations!

<div class="entities">
{% for entry in site.data.funders %}
    {% assign fundername = entry[0] %}
    {% assign entity = site.data['funders'][fundername] %}
    {% include _includes/external-entities.html entity=entity type='funder' %}
{% endfor %}
</div>

# Partners

This program is made possible thanks to our partners and collaborating organisations!

<div class="entities">
{% for entry in site.data.partners %}
    {% assign partnername = entry[0] %}
    {% assign entity = site.data['partners'][partnername] %}
    {% include _includes/external-entities.html entity=entity type='partner' %}
{% endfor %}
</div>
