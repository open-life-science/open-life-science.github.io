---
layout: page
toc: true
title: Fiscal Hosting
description: Fiscal sponsorship for open research communities, offering financial and administrative support through OLS.
permalink: /open-incubator/fiscal-hosting/
image: https://images.unsplash.com/photo-1560328055-e938bb2ed50a
photos:
  name: Kelli McClintock
  license: CC BY-SA 4.0
  url: https://images.unsplash.com/photo-1560328055-e938bb2ed50a
---

# Fiscal Sponsorship

As part of OLS's commitment to growing open researchers, OLS is experimenting with offering Fiscal Sponsorship. This model is well-known in the United States, with sponsors such as [Numfocus](https://numfocus.org/) and [Code for Science and Society](https://www.codeforsociety.org/) existing as nonprofit organisations that offer fiscal sponsorship for their constituent communities. To our knowledge there are fewer UK-based fiscal sponsors that specialise in open research related needs, that are willing to take on small projects, or who are willing to act as fiscal sponsors for projects outside of the US or UK. 

Communities that have participated in an OLS training cohort, or worked with OLS in other capacities, are welcome to apply to become a fiscally sponsored community ([FSC](#fsc)).

# FAQs

## What is Fiscal Sponsorship?

Research projects that are part of universities or big institutes have support from their institutions to handle human and legal infrastructure. For research and community building projects that aren't part of a university, a **fiscal sponsor** like OLS can handle these kinds of activities: for example, making sure staff get paid on time, issuing contracts, reviewing budgets, and consulting with legal advice as/when needed. 

## What is an OLS Fiscally Sponsored Community?

An OLS fiscally sponsored community (FSC) is a group of people working on open research or other OLS-adjacent domains for whom OLS handles infrastructure to help them receive grants or undertake contracts in order to do their work. 

OLS charges 15% of grants received by FSCs to support our fiscal sponsorship work. 

## How can we become a FSC?

Communities that have participated in an OLS training cohort, or worked with OLS in other capacities, are welcome to apply to become a FSC.

Please fork the [FSC community template repo](https://github.com/open-life-science/fiscally-sponsored-community-templates), which should guide you through creating issues as to-dos for the basic docs we expect. [You can also read our internal policy page for FSCs and Fellows.]({% link fiscal-hosting/fsc-policies.md %}) 

The TL;DR version of the requirements are:

* At least **three members** who are responsible for organisational governance, and who will be signatories on contracts.   
* A **dispute resolution process** for disputes between community members.   
* A **succession policy** for what happens if key project members leave or become unresponsive/unavailable for some reason.  
* A **roadmap** for your planned activities as an FSC. We want to know what your plans are for the community in the short, medium and long term.  
* Scoping for a **grant** that you might want to apply for as an FSC.

### What if we don't have three members of our community who are willing to be signatories yet?

We ask that there are **three** members who are willing to sign agreements and contracts as part of showing that the community is stable. 

If you don't yet have three members who are ready to sign contracts on behalf of a community, but you have a plan to get to that position, consider applying to become an **Incubation Fellow.** 

### Why do you need a dispute resolution process?

Handling disagreements and disputes is a normal part of managing communities. It's important to have policies in place that explain how you will handle disagreements between community members **before** your community has major disagreements. OLS will not resolve disputes on your behalf. We ask for a dispute resolution process to be in place so that the community is robust even when members disagree. 

### Why do you need a succession plan?

Life happens: community members may no longer be able to commit to taking on governance and contract responsibilities for a community. We ask FSCs to have a succession plan in place to ensure that the community remains sustainable even if a member steps away. 

### What should a FSC roadmap look like?

A roadmap should cover the purpose of the community–what you want to achieve in open research, open science and/or community building. It should also outline your planned activities in the short term (over the next year), in the medium term (1-2 years), and in the long term (3-5 years). 

## What is an OLS Incubation Fellow?

An OLS Incubation Fellow is a person working on open research or other OLS-adjacent domains who is working towards building a sustainable community, for whom OLS handles the infrastructure to help them receive grants or undertake contracts in order to do this work. 

OLS charges 7.5% of grants received by Incubation Fellows to support our fiscal sponsorship work.

### Is an Incubation Fellow the same as a Resident Fellow?

Incubation fellows are affiliated with OLS with the aim of building a sustainable community. Resident Fellows are also affiliated with OLS, but have different aims. At present we only take open applications for Incubation Fellows. 

## How can I become an Incubation Fellow?

Individuals that have participated in an OLS training cohort, or worked with OLS in other capacities, are welcome to apply to become an Incubation Fellow.

Please fork the Incubation Fellow community template repo, which should guide you through creating issues as to-dos for the basic docs we expect. [You can also read our internal policy page for FSCs and Fellows.]({% link fiscal-hosting/fsc-policies.md %})

The TL;DR version of the requirements are:

* A **roadmap** for your planned activities as an Incubation Fellow. We want to know what your plans are to build a sustainable community.  
* A **grant** **or other source of funding** that you have identified to support you in this work. 

### What should an Incubation Fellow roadmap look like?

We want to see what activities and steps you plan to take to build a sustainable community. This can be an OLS FSC–see the requirements above–or another form of community (for example, an independent organisation, or a community with a different fiscal sponsor) if that's a better fit. We expect your roadmap to cover about a year: we don't anticipate taking on Incubation Fellows for longer than this. 

### Can I be an Incubation Fellow without funding?

At present, we are only taking on Incubation Fellows when they have funding. Please keep an eye out for other opportunities to work with OLS!

## We already have an organisation, but we'd like to work with OLS on a project

Great! Drop us an email at team \[at\] we-are-ols.org  with more information. We can fiscally sponsor individual projects, but we can also collaborate directly with other organisations when it makes sense to do so.  

## I'd like to be an Incubation Fellow or part of an FSC, but…

### …I don't have any experience with applying for grants.

We can help you put together an application! In fact, we prefer to work closely with our FSCs and Incubation Fellows on their grant applications. 

### …I don't have a connection with OLS yet.

At the moment, we are only entering into fiscal sponsorship arrangements with people who have already been part of an OLS training cohort, or worked with OLS in other capacities. Please do [subscribe to our newsletter](https://openlifescience.civicrm.org/civicrm/newsletter) to find out more about how you can work with us!

## How can I apply?

Please go ahead and [fork the repo](https://github.com/open-life-science/fiscally-sponsored-community-templates) to apply to become an FSC or a Fellow. Send us an email at fsc \[at\] we-are-ols.org to let us know you're working on the repo as well!

## Who are your current FSCs and Incubation Fellows?

### Current Fiscally Sponsored Communities (FSC)
{% assign f_community = site.data.community.fiscal_communities %}
{% assign incubator_fellows = site.data.community.incubator_fellows %}


<div class="entities">
{% for c in f_community %}
    {% assign entity = c %}
    {% assign details = c.details %}
    {% include _includes/external-entities.html entity=entity type='fiscal_communities' details=details %}
{% endfor %}
</div>

### Current Incubator Fellows
{% assign f_community = site.data.community.fiscal_communities %}
<div class="entities">
{% for fellow in incubator_fellows %}
    {% assign entity = fellow %}
    {% assign details = fellow.details %}
    {% include _includes/external-entities.html entity=entity type='fiscal_communities' details=details %}
{% endfor %}
</div>
