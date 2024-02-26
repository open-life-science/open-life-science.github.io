<script type="application/ld+json" >
{%- assign sep="" -%}
[
{%- for w in schedule.weeks -%}
    {%- for c in w[1].calls -%}
        {%- if c.type == "Cohort" -%} {% capture name %}{{ c.type }} call for the week {{ w[0] }} of {{ cohort }} cohort of {{ site.title }}: {{ c.title }}{% endcapture %}
    {{ sep }}{
        "@context": "https://schema.org",
        "@type": "Course",
        "@id": "{{ site.url }}/{{ cohort }}/schedule#week-{{ w[0] }}",
        "dct:conformsTo": {
            "https://purl.org/dc/terms/conformsTo": {
                "@id": "https://bioschemas.org/profiles/Course/1.0-RELEASE",
                "@type": "CreativeWork"
            }
        },
        "description": "{{ site.title }} is a mentoring mentoring & training program for Open Science ambassadors. It runs cohorts with calls every 1-2 weeks. This course is a {{ name }}",
        "keywords": "Open Science",
        "name": "{{ name }}",
        "about": {
            "@type": "DefinedTerm",
            "@id": "https://edamontology.org/topic_4010",
            "inDefinedTermSet": "https://edamontology.org",
            "termCode": "topic_4010",
            "name": "Open Science",
            "url": "https://bioportal.bioontology.org/ontologies/EDAM/?p=classes&conceptid=http%3A%2F%2Fedamontology.org%2Ftopic_4010"
        },
        "educationalLevel": "Beginner",
        "inLanguage": "en-US",
        "hasCourseInstance": {
            "@context": "https://schema.org",
            "@type": "CourseInstance",
            "dct:conformsTo": {
                "https://purl.org/dc/terms/conformsTo": {
                    "@id": "https://bioschemas.org/profiles/CourseInstance/1.0-RELEASE",
                    "@type": "CreativeWork"
                }
            },
            "courseMode": ["online", "synchronous"],
            "courseWorkload": "90-minutes long cohort call",
            "startDate" : "{{ c.date | date: "%Y-%m-%d" }}",
            "endDate" :"{{ c.date | date: "%Y-%m-%d" }}",
            "inLanguage": "en-US",
            "duration": "{{ c.duration }}",
            "name" : "{{ c.title }}",
            "offers": {
                "@type": "Offer",
                "price": "0",
                "priceCurrency": "GBP"
            }
        },
        "hasPart": [
            {
                "@context": "https://schema.org",
                "@type": "LearningResource",
                "dct:conformsTo": {
                    "https://purl.org/dc/terms/conformsTo": {
                        "@id": "https://bioschemas.org/profiles/TrainingMaterial/1.0-RELEASE",
                        "@type": "CreativeWork"
                    }
                },
                "description": "Notes and recording for {{ name }}",
                "keywords": "Open Science",
                "name": "Notes and recording for {{ name }}",
                "about": {
                    "@type": "DefinedTerm",
                    "@id": "https://edamontology.org/topic_4010",
                    "inDefinedTermSet": "https://edamontology.org",
                    "termCode": "topic_4010",
                    "name": "Open Science",
                    "url": "https://bioportal.bioontology.org/ontologies/EDAM/?p=classes&conceptid=http%3A%2F%2Fedamontology.org%2Ftopic_4010"
                },
                "educationalLevel": "Beginner",
                "hasPart": [
                    {
                        "@type": "CreativeWork",
                        "url": "{{ c.notes }}",
                        "name": "Notes for {{ name }}"
                    }{% if c.recording %},
                    {
                        "@type": "CreativeWork",
                        "url": "{{ c.recording }}",
                        "name": "Recording for {{ name }}"
                    }{% endif %}
                ],
                "inLanguage": "en-US",
                "learningResourceType": ["handout", "video"],
                "license": "https://creativecommons.org/licenses/by-sa/4.0/",
                "contributor":  [
                    {
                        "@type": "Organization",
                        "name": "Open Life Science",
                        "email": "{{ site.email }}",
                        "url": "{{ site.url }}"
                    }
                    {%- for r in c.resources -%}{% if r.type == 'slides' and r.speaker %}
                    ,{
                        "@type": "Person",
                        "name": "{{ site.data.people[r.speaker].first-name }} {{ site.data.people[r.speaker].last-name }}",
                        "url": "{{ site.url }}/people#{{ r.speaker }}"
                    }
                    {% endif %}{%- endfor -%}
                    {%- if c.hosts -%}{% for r in c.hosts %}
                    ,{
                        "@type": "Person",
                        "name": "{{ site.data.people[r].first-name }} {{ site.data.people[r].last-name }}",
                        "url": "{{ site.url }}/people#{{ r }}"
                    }
                    {% endfor %}{%- endif -%}
                ]
            }
        ],
        "license": "https://creativecommons.org/licenses/by-sa/4.0/",
        "provider":  [{
            "@type": "Organization",
            "name": "Open Life Science",
            "email": "{{ site.email }}",
            "url": "{{ site.url }}"
        }]
        {%- if c.learning_objectives -%}{%- assign lo-sep="" -%}
        ,"teaches": [
            {%- for lo in c.learning_objectives -%}
                {{ sep }}"The learners will be able to {{ lo }}",
                {%- assign sep=", " -%}
            {%- endfor -%}
        ]
        {%- endif -%}
    }      
        {%- assign sep="," -%}
        {%- endif -%}
    {%- endfor -%}
{%- endfor -%}
]
</script>

{% include _includes/overall-schedule.md %}
{% include _includes/detailed-schedule.md %}
