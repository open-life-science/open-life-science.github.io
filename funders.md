---
layout: page
title: Funders and Partners
image: https://images.unsplash.com/photo-1530043123514-c01b94ef483b?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1650&q=80
photos:
  name: Mathew Schwartz
  license: Unsplash License
  url: https://unsplash.com/photos/PgNE82MUHAY
---

# Funders

This program has been funded by the following funding organisations!

<div class="funders">
{% for entry in site.data.funders %}
    {% assign fundername = entry[0] %}
    {% assign funder = site.data['funders'][fundername] %}
    {% include _includes/funders.html funder=funder %}
{% endfor %}
</div>

# Partners

This program is made possible thanks to our partners and collaborating organisations!

<div class="partners">
{% for entry in site.data.partners %}
    {% assign partnername = entry[0] %}
    {% assign partner = site.data['partners'][partnername] %}
    {% include _includes/partners.html partner=partner %}
{% endfor %}
</div>
