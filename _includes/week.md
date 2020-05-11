{% for c in week.calls %}

# {{ c.type }} call: {{ c.title }}

{% if c.type == "Cohort" %}
<i class="fas fa-calendar-alt"></i> **Date**: {{ c.date }}, at [{{ c.time }} European Time](https://arewemeetingyet.com/Berlin/{{ c.date | date: "%Y-%m-%d" }}/{{ c.time }}/OLS-2%20Cohort%20Call%20(Week%20{{ w[0] }})) ([<i class="fas fa-calendar-plus"></i> *Add to your calendar*]({{ c.calendar-event }}))

{% else %}
<i class="fas fa-calendar-alt"></i> **Date**: {{ week.timeframe }}

{% endif %}

<i class="fas fa-clock"></i> **Duration**: {{ c.duration }}

{% if c.content %}
## In this call

{{ c.content | markdownify }}

{% endif %}

{% if c.type == "Cohort" %}

**Resources**:
- <i class="fas fa-clipboard"></i> [Notes]({{ c.notes }})
- <i class="fab fa-youtube"></i> {% if c.recording %} [Recording]({{ c.recording }}) {% else %} Recording available on the [OLS YouTube channel]({{ site.youtube }}) after the call {% endif %}

{% endif %}

{% if c.before %}
## Before the call

{{ c.before | markdownify }}
{% endif %}

{% if c.after %}
## After the call

{{ c.after | markdownify }}
{% endif %}

{% endfor %}