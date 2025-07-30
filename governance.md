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

# Governance Advisory Committee

The **OLS Governance Advisory Committee** is formed by individuals appointed from the OLS community.
Their involvement in the governance of OLS ensures transparency, fosters accountability, and provides advisory support to the OLS leadership team.
The Committee provides strategic oversight through regular meetings and reporting, actively shaping our governance framework and contributing to the organisation's long-term sustainability.

For governance-related documentation and updates, please visit our [public GitHub repository]({{ site.github.owner_url }}/ols-governance).
Transparency reports are released by the committee members on our website every six months - read the [most recent report]({% link _posts/2025/05/07/ols-governance-report.md %})).

<div class="people">
{% for entry in community.governance %}
    {% assign username = entry %}
    {% assign user = people[username] %}
    {% include _includes/people.html username=username user=user %}
{% endfor %}
</div>
