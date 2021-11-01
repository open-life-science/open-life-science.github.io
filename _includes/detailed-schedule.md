{% for w in schedule['weeks'] %}

# Week {{ w[0] }}

<i class="fas fa-calendar-alt"></i> **Dates**: {{ w[1].timeframe }}

{% assign week-nb=w[0] %}
{% assign week = w[1] %}
{% include _includes/week.md %}

{% endfor %}