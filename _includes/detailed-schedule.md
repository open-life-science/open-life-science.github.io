{% for w in schedule['weeks'] %}

# Week {{ w[0] }}

<i class="fas fa-calendar-alt"></i> Week starting on **{{ w[1].start }}**

{% assign week-nb=w[0] %}
{% assign week = w[1] %}
{% include week.md %}

{% endfor %}
