---
layout: page
title: Funding, Funders and Partners
image: https://images.unsplash.com/photo-1429962714451-bb934ecdc4ec?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1650&q=80
photos:
  name: Anthony DELANOIX
  license: Unsplash License
  url: https://unsplash.com/photos/hzgs56Ze49s
---

{% assign organizations = site.data.organizations %}

Open Life Science (OLS) is supported through a mix of philantropic support, personal donations, grant funding, and partnerships with institutions.

# Funding

In the table below, we list our funding from philantropies, grants, and institutional patrnerships.

Personal donations come from mentors, experts and other contributors of OLS who chose to donate the honoraria for their work to our general funds, as well as fundraising campaigns, e.g. during cohort graduations.

Funder | Amount | Duration  | Date of Award | Purpose | Proposal
---|---|---|---|---|---
{% for f in site.data.funding -%}
[{{ organizations[f.funder].name }}]({{ organizations[f.funder].site }}) | {{ f.amount }} {{ f.currency }} | {{ f.duration }} | {{ f.date_award }} | {{ f.purpose }}  | {% if f.proposal %}[Proposal]({{ f.proposal }}){% endif %}
{% endfor %}

# Funders

This program has been funded by the following funding organisations!

<div class="entities">
{% for f in site.data.funding %}
    {% assign entity = organizations[f.funder] %}
    {% include _includes/external-entities.html entity=entity type='funder' %}
{% endfor %}
</div>

# Partners

This program is made possible thanks to our partners and collaborating organisations!

<div class="entities">
{% for p in site.data.partners %}
    {% assign entity = organizations[p.partner] %}
    {% assign details = p.details %}
    {% include _includes/external-entities.html entity=entity type='partner' details=details %}
{% endfor %}
</div>
