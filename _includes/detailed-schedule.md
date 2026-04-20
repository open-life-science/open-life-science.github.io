{%- for w in schedule['weeks'] -%}
# Week {{ w[0] }}
  {%- if program != 'nebula' -%}<i class="fas fa-calendar-alt"></i>  Week starting on **{{ w[1].start | date: "%B %d, %Y" }}**{%- endif -%}
{%- assign week-nb=w[0] -%}
{%- assign week = w[1] -%}
{% include _includes/week.md %}
{% endfor %}
