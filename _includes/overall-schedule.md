During the program,

- Mentors and mentees meet every 2 weeks [for a 30 minutes call](/ols-2#mentor-mentee-calls)
- Mentees participate every ~2 weeks to [90-minutes cohort calls](/ols-2#cohort-calls) during which the program leaders introduce new topics and resources, facilitate break-out discussions, and invite expert from the field to give talks
- Mentees can meet together for coworking sessions every 2 weeks [for a 30 minutes call](/ols-2#coworking-calls)
- Mentors take part to [4 mentoring calls](/ols-2#mentors-calls)

Organizers will inform participants of the week schedule by email.

<iframe src="https://calendar.google.com/calendar/embed?height=400&amp;wkst=1&amp;bgcolor=%23ffffff&amp;ctz=Europe%2FParis&amp;src=b3BlbmxpZmVzY2lAZ21haWwuY29t&amp;color=%23EF6C00&amp;mode=AGENDA&amp;showNav=0&amp;showTitle=0&amp;showPrint=0&amp;showTabs=1&amp;showCalendars=0" style="border-width:0" width="1152" height="600" frameborder="0" scrolling="no"></iframe>

[<i class="fas fa-calendar-plus"></i> *Subscribe to the OLS calendar*](https://calendar.google.com/calendar?cid=b3BlbmxpZmVzY2lAZ21haWwuY29t)

<!-- Any modification of the content should be done in the _data/ols-X-schedule.yaml file -->

| Week | Call | Date | Topic | Agenda |
|------|------|------|-------|--------|
{%- for w in schedule %}
{%- capture w-desc %}**Week {{ w[0] }}**: {{ w[1].timeframe }}{% endcapture %}
{%- for c in w[1].calls %}
{%- capture date %}{% if c.type != "Mentor-Mentee" %}{{ c.date }} {% if c.time %}([{{ c.time }} European Time](https://arewemeetingyet.com/Berlin/{{ c.date | date: "%Y-%m-%d" }}/{{ c.time }}/OLS-2%20{{ c.type }}%20Call%20(Week%20{{ w[0] }}))){% endif %}{% endif %}{% endcapture %}
| {{ w-desc }} | [{{ c.type }}](/ols-2#{{ c.type | downcase | remove: "(" | remove: ")" | remove: "@" | remove: ":" | remove: "," | replace: " ", "-" }}-calls) | {{ date }} | [**{{ c.title }}**](/ols-2/schedule#week-{{ w[0] }}) | {% if c.agenda %}{{ c.agenda }}{% endif %} |
{%- assign w-desc = "" %}
{%- endfor %}
{%- endfor %}
