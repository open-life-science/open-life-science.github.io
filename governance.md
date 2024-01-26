---
layout: page
title: Governance Committee
image: /images/about.jpg
photos:
  name: Bérénice Batut
  license: CC BY-SA 4.0
  url: https://flic.kr/p/2gHNtNq
---

{% assign community = site.data.community %}
{% assign people = site.data.people %}

# Governance Committee
The OLS Governance Committee is a dedicated group of individuals appointed to provide strategic oversight and guidance in shaping the governance framework of OLS. This committee provides advisory support in decision-making, transparency, and sustainability within OLS. You can also [read the OLS governance guiding documents]({{ site.github.owner_url }}/ols-governance)


<div class="people">
{% for entry in community.governance %}
    {% assign username = entry %}
    {% assign user = people[username] %}
    {% include _includes/people.html username=username user=user %}
{% endfor %}
</div>
