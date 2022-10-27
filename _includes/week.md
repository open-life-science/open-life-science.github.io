{% for c in week.calls %}

## {{ c.type }} call: {{ c.title }}

{% if c.type != "Mentor-Mentee" and c.date %}
<i class="fas fa-calendar-alt"></i> **Date**: {{ c.date }}{% if c.time %}, at [{{ c.time }} Universal Time](https://arewemeetingyet.com/UTC/{{ c.date | date: "%Y-%m-%d" }}/{{ c.time }}/
{{ cohort | upcase }}%20Cohort%20Call%20(Week%20{{ week-nb }})) ([<i class="fas fa-calendar-plus"></i> *Add to your calendar*]({{ c.calendar-event }})){% endif %}
{% else %}
<i class="fas fa-calendar-alt"></i> **Date**: During the week starting on {{ week.start }} (to define with mentors)
{% endif %}

<i class="fas fa-clock"></i> **Duration**: {{ c.duration }}

{% if c.hosts %}
{% assign hosts = '' %}
{% for p in c.hosts %}{% capture hosts %}{{ hosts }}, {{ site.data.people[p].first-name }} {{ site.data.people[p].last-name }}{% endcapture %}{% endfor %}
<i class="fas fa-user-friends"></i> **Hosts**: {{ hosts | remove_first: ', ' }}
{% endif %}

{% if c.content %}
### In this call

{{ c.content | markdownify }}

{% endif %}

{% if c.type == "Cohort" %}

**Resources**:
- <i class="fas fa-clipboard"></i> [Notes]({{ c.notes }})
- <i class="fab fa-youtube"></i> {% if c.recording %} [Recording]({{ c.recording }}) {% else %} Recording available on the [OLS YouTube channel]({{ site.youtube }}) after the call {% endif %}
{% for r in c.resources %}
- {% if r.type == 'slides' %}<i class="fas fa-file-powerpoint"></i>{% elsif r.type == 'document' %} <i class="fas fa-file"></i>{% elsif r.type == 'external-link' %} <i class="fas fa-external-link-square-alt"></i>{% endif %} {% if r.link %} [{{ r.title }}]({{ r.link }}){% else %} {{ r.title }}{% endif %}{% if r.type == 'slides' and r.speaker %}, by [{{ site.data.people[r.speaker].first-name }} {{ site.data.people[r.speaker].last-name }}](/{{ cohort }}#{{ r.speaker }}) {% endif %}
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