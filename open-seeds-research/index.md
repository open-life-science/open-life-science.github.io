---
layout: page
title: 'Open Seeds Research'
image: https://images.unsplash.com/photo-1694002070710-87e709ca4d38
photos:
  name: Dilani Wickramanayake
  license: Unsplash License
  url: https://unsplash.com/@dilani_wicky
---

{% assign community = site.data.community %}
{% assign people = site.data.people %}

## Open Seeds Impact Research

Funded by [Wellcome Trust Open Research Fund 2021](https://wellcome.org/grant-funding/schemes/open-research-fund), this research investigated the **long-term impact** of Open Science training and mentoring interventions, particularly by **Open Seeds**, from a qualitative angle.

*Highlights from this research will be added here along with the publication, which is under peer-review.*

### Outputs

- **Pre-print:** Bernaldo, P., Pereyra Irujo, G., Yehudi, Y., van der Walt, A., Iley, B., Míguez, M. P., Ramos, I., Plomp, E., & Sharan, M. (2025). Examining the impact and limitations of Open Science training: a case study of the "Open Seeds" programme. Zenodo. [https://doi.org/10.5281/zenodo.14930711](https://doi.org/10.5281/zenodo.14930711)
- **Supporting data:** Bernaldo, P., & OLS. (2025). Supporting materials for "Examining the impact and limitations of Open Science training: a case study of the "Open Seeds" programme" [Data set]. Zenodo. [https://doi.org/10.5281/zenodo.15024935](https://doi.org/10.5281/zenodo.15024935)

### Credit authorship contribution statement 

* **Paz Bernaldo**: Conceptualisation, Data Curation, Formal Analysis, Investigation, Methodology, Resources, Writing - original draft, Writing – review & editing https://orcid.org/0000-0002-3129-9020 
* **Yo Yehudi**: Project Administration, Conceptualisation, Methodology, Supervision, Writing - review and editing. https://orcid.org/0000-0003-2705-1724 
* Gustavo Pereyra Irujo: Conceptualisation, Writing - original draft, Writing - review and editing. https://orcid.org/0000-0002-2261-6928 
* Anelda Van der Walt: Methodology, Writing - review & editing. https://orcid.org/0000-0003-4245-8119 
* Irene Ramos: Writing - review & editing. https://orcid.org/0000-0003-3315-2281
* Bethan Iley: Writing - review & editing. https://orcid.org/0000-0002-5813-3303 
* Paz Miguez: Methodology. https://orcid.org/0000-0003-1099-4347 
* Esther Plomp: Writing - review & editing. https://orcid.org/0000-0003-3625-1357 
* Patricia Herterich: Writing - review & editing. https://orcid.org/0000-0002-4542-9906 
* Malvika Sharan:  Conceptualisation, Funding acquisition, Writing - review and editing, Project administration. https://orcid.org/0000-0001-6619-7369 

## Researchers

<div class="people">
{% for entry in community.openseeds %}
    {% assign username = entry %}
    {% assign user = people[username] %}
    {% include _includes/people.html username=username user=user %}
{% endfor %}
</div>
