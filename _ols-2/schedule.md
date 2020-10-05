---
layout: page
title: OLS-2 schedule
image: https://images.unsplash.com/photo-1435527173128-983b87201f4d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1047&q=80
photos:
  name: Eric Rothermel
  license: CC BY
  url: https://unsplash.com/photos/FoKO4DpXamQ
---

{% assign schedule = site.data.ols-2-schedule %}
{% assign cohort = 'ols-2' %}

{% include _includes/overall-schedule.md %}

{% for w in schedule %}

# Week {{ w[0] }}

<i class="fas fa-calendar-alt"></i> **Dates**: {{ w[1].timeframe }}

{% assign week-nb=w[0] %}
{% assign week = w[1] %}
{% include _includes/week.md %}

{% endfor %}
