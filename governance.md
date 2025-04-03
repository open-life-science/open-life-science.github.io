---
layout: page
title: Governance Committee
image: /images/2024-02-governance-page-benjamin-combs-wuU_SSxDeS0-unsplash.jpg
photos:
  name: Benjamin Combs
  license: Unsplash
  url: https://unsplash.com/photos/person-showing-green-plant-wuU_SSxDeS0
---

{% assign community = site.data.community %}
{% assign people = site.data.people %}

# Governance Committee
The OLS Governance Committee is a dedicated group of individuals appointed to provide strategic oversight and guidance in shaping the governance framework of OLS. This committee provides advisory support in decision-making, transparency, and sustainability within OLS. You can also [read the OLS governance guiding documents]({{ site.github.owner_url }}/ols-governance).

For governance-related documentation and updates, please visit our [public GitHub repository]({{ site.github.owner_url }}/ols-governance).


<div class="people">
{% for entry in community.governance %}
    {% assign username = entry %}
    {% assign user = people[username] %}
    {% include _includes/people.html username=username user=user %}
{% endfor %}
</div>
