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
You can also [read the OLS governance guiding documents]({{ site.github.owner_url }}/ols-governance).


<div class="people">
{% for entry in community.governance %}
    {% assign username = entry %}
    {% assign user = people[username] %}
    {% include _includes/people.html username=username user=user %}
{% endfor %}
</div>
