{% for c in week.calls %}

## {{ c.type }} call: {{ c.title }}

{% if c.type == "Cohort" %}
<i class="fas fa-calendar-alt"></i> **Date**: {{ c.date }}{% if c.time %}, at [{{ c.time }} European Time](https://arewemeetingyet.com/Berlin/{{ c.date | date: "%Y-%m-%d" }}/{{ c.time }}/
{{ cohort | upcase }}%20Cohort%20Call%20(Week%20{{ week-nb }})) ([<i class="fas fa-calendar-plus"></i> *Add to your calendar*]({{ c.calendar-event }})){% endif %}

{% else %}
<i class="fas fa-calendar-alt"></i> **Date**: {{ week.timeframe }}

{% endif %}

<i class="fas fa-clock"></i> **Duration**: {{ c.duration }}

{% if c.content %}
### In this call

{{ c.content | markdownify }}

{% endif %}

{% if c.type == "Cohort" %}

**Resources**:
- <i class="fas fa-clipboard"></i> [Notes]({{ c.notes }})
- <i class="fab fa-youtube"></i> {% if c.recording %} [Recording]({{ c.recording }}) {% else %} Recording available on the [OLS YouTube channel]({{ site.youtube }}) after the call {% endif %}
{% for r in c.resources %}
- {% if r.type == 'slides' %}<i class="fas fa-file-powerpoint"></i> {% else %} <i class="fas fa-file"></i>{% endif %} [{{ r.title }}]({{ r.link }}){% if r.type == 'slides' %}, by [{{ site.data.people[r.speaker].first-name }} {{ site.data.people[r.speaker].last-name }}](/{{ cohort }}#{{ r.speaker }}) {% endif %}
{% endfor %}

{% endif %}

{% if c.before %}
### Before the call

{{ c.before | markdownify }}
{% endif %}

{% if c.after %}
### After the call

{{ c.after | markdownify }}
{% endif %}

{% endfor %}