{% for c in week.calls %}

## {{ c.type }} call: {{ c.title }}



{% if c.type != "Mentor-Mentee" and c.date %}
<i class="fas fa-calendar-alt"></i> **Date**: {{ c.date }}{% if c.time %}, at [{{ c.time }} Universal Time](https://arewemeetingyet.com/UTC/{{ c.date | date: "%Y-%m-%d" }}/{{ c.time }}/
{{ cohort | upcase }}%20Cohort%20Call%20(Week%20{{ week-nb }})) {% if c.calendar-event %}([<i class="fas fa-calendar-plus"></i> *Add to your calendar*]({{ c.calendar-event }})){% endif %}{% endif %}
{% else %}
<i class="fas fa-calendar-alt"></i> **Date**: During the week starting on {{ week.start }} (to define with mentors)
{% endif %}

<i class="fas fa-clock"></i> **Duration**: {{ c.duration }}

{% if c.hosts %}
    {% assign hosts = '' %}
    {% for p in c.hosts %}{% capture hosts %}{{ hosts }}, [{{ site.data.people[p].first-name }} {{ site.data.people[p].last-name }}]({% link people.md %}#{{ p }}){% endcapture %}{% endfor %}
<i class="fas fa-user-friends"></i> **Hosts**: {{ hosts | remove_first: ', ' }}
{% endif %}

{% if c.learning_objectives %}
### Learning objectives

At the end of this call, learners will be able to:

    {% for lo in c.learning_objectives %}
- {{ lo | markdownify }}
    {% endfor %}

{% endif %}

{% if c.content %}
### In this call

{{ c.content | markdownify }}

{% endif %}

{% if c.before %}
### Before the call

{% for lo in c.before %}
- {{ lo | markdownify }}
{% endfor %}

{% endif %}

{% if c.type == "Cohort" or c.type == "Skill-up" %}

<div class="columns">
<div class="column is-half" markdown=1>

### Talks

{% for r in c.talks %}
- <i class="fas fa-file-powerpoint"></i>{% if r.slides %} [{% if r.title %}{{ r.title }}{% else %}{{ r.tag }}{% endif %}]({{ r.slides }}){% else %} {{ r.title }}{% endif %}{% if r.speakers %}{% assign speakers = '' %} {% for p in r.speakers %}{% capture speakers %}{{ speakers }}, [{{ site.data.people[p].first-name }} {{ site.data.people[p].last-name }}]({% link people.md %}#{{ p }}){% endcapture %}{% endfor %} by {{ speakers | remove_first: ', ' }}{% endif %}
{% endfor %}

### Resources

- <i class="fas fa-clipboard"></i> [Notes]({{ c.notes }})
- <i class="fab fa-youtube"></i> {% if c.recording %} [Recording]({{ c.recording }}) {% else %} Recording available on the [OLS YouTube channel]({{ site.youtube }}) after the call {% endif %}
{% for r in c.resources %}
- {% if r.type == 'slides' %}<i class="fas fa-file-powerpoint"></i>{% elsif r.type == 'document' %} <i class="fas fa-file"></i>{% elsif r.type == 'external-link' %} <i class="fas fa-external-link-square-alt"></i>{% endif %} {% if r.link %} [{{ r.title }}]({{ r.link }}){% else %} {{ r.title }}{% endif %}
{% endfor %}

</div>

{% if c.recording %}
<div class="column">
    <div>
        <iframe
            style="width:100%;height:100%;min-height:300px;"
            src="{{ c.recording | replace: 'youtu.be/', 'youtube.com/embed/' | replace: '?t', '?start' }}"
            title="YouTube video player"
            frameborder="0"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
            allowfullscreen>
        </iframe>
    </div>
</div>
{% endif %}

</div>

{% endif %}

{% if c.after %}
### After the call

{% for lo in c.after %}
- {{ lo | markdownify }}
{% endfor %}

{% endif %}

{% endfor %}