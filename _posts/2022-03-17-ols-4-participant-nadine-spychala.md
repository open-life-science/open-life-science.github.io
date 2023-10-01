---
layout: post
title: 'OLS-4 speed blog: Developing a library in Python for applying measures of emergence and complexity'
authors:
- nadinespy
image: ../images/2022-04-01-header-image-speed-blod-nadine.jpg
photos:
  name: Illustration by Nadine Spychala
  url: https://nadinespy.github.io/
---

## Project background
My main motivator to initiate this project was to be able to do research on formal measures of emergence & complexity that

1. is in accordance with standards in open & reproducible science, and
2. allows an easy comparison among different measures & data.<br>

I found that in order to achieve this, quite a few things would need to be tackled, e. g., making measures accessible in the first place (as some of them have been implemented in programming languages that are published under profit software licenses), having software that complies to FAIR principles, or developing a comparative testing environment which enables the testing of different measures under the same constraints.<br>

My thought was: If achieving my goals will require substantial long-term efforts, then anyone else pursuing a similar endeavour would probably need to put the same efforts into it – why not spare potential future redundancy, and write a software library in Python as part of an open-source project to join forces with potential contributors – aiming for FAIR software in the best possible way, implementing an exhaustive set of measures, as well as providing good guidance on how to conduct comparative applications of the measures?

## Expectations from this program
I wanted to have guidance in developing a stable library that will help in applying measures of emergence and complexity as easily as possible, ensure that outcomes are replicable, and allow to draw informed conclusions about comparisons among measures. I considered code reviews & guidance on general software engineering principles very helpful in that respect. I also wanted to know more about the building blocks of collaborative open-source projects, and be around like-minded people with whom I share the same attitudes in the quest for solid & incremental science, cooperation, and inclusivity.

## Goals set at the beginning of the program
During my participation in OLS-4, I wanted to come up with a library that
applies a set of recent measures of emergence and complexity to either simulated or empirical data – using possibly only one line of code, making comparisons among them easy,

- informs the user about possible use cases, caveats, and anything that is important to keep in mind when applying the measures,
- explains the measures in the first place in a tutorial-like fashion, including commonalities and differences that will be showcased in example models,
- guides the user in drawing conclusions about the measures by providing suitable visualizations of the outcomes,
- is as stable as possible, i.e., using best practices from software engineering, such as test-driven development, version control, and implementation across different computers and working environments.

## Key understanding and accomplishments
While I couldn’t tackle yet the development of educational resources of my library, I managed to finalize software that allows applying one or a set of different measures to one or multiple datasets using only one line of code – an achievement I am extremely happy about! For now, one measure of emergence is implemented and can be applied. As the current code is scalable, adding further measures will be very easy. Moreover, the output of this one line of code delivers a variable which stores both results and parameters so as to be able to easily retrieve cases of interest and visualize them.

During OLS-4, I also started to finally implement some code testing and think about possible “formats” of usage (e. g., shall the library be executed via a command line interface, Docker image, or do I want the user to work directly in Python?). The feedback I got from my mentors and code reviewers in this regard was particularly helpful.

OLS-4 has also got me started on open science project essentials like code of conduct and contributor guidance specifications.

## The main goals achieved in this project
What I’ve done:

- developed software which allows applying one or more measures to one or multiple datasets in one line of code, and which delivers a pandas dataframe storing all results alongside respective parameters,

```
import complex_py as cp

# define what data to use/generate, and what measures of emergence
# to apply to those data via the following five variables:

#       model_function:      contains functions to generate/load your data
#       model_variables:     contains parameters for generating/loading your data
#       emergence_functions: contains functions to calculate measures of emergence
#       measure_variables:   contains parameters for calculating emergence
#       parameters:          contains all parameters (data- and measure-related ones)

# compute measures of emergence for all parameter combination:
emergence_df = cp.compute_emergence(model_functions, model_variables,
                                    emergence_functions, measure_variables, parameters)
```

- implemented one measure of emergence easily to be complemented by other measures as the code is scalable,
- started to implement code testing as well as visualization techniques of the results,
- started to think about the “format” in which to offer this library to potential users,
- started to add/work on open science project essentials like a code of conduct or readme files.

Still to do:

- develop tutorials about a) how to use the library, including use cases, caveats, and anything that is important to keep in mind when applying the measures, and b) the measures themselves, including definitions, commonalities and differences that will be showcased in example models,
- make a decision about how the library shall be used (e. g., directly in Python, via a command line interface or a Docker image),
- continue to work on visualizing results, code testing, as well as code of conduct and contributing guidelines (will be high priority once a first version is released which will     then be open to potential contributors),
- implement further measures.

## The initial steps
At the point where OLS-4 started, I was still struggling to make a measure of emergence work in Python via 'oct2py()' - a Python library which allows the calling of Matlab functions in Python. The battle continued for about 3 months after which – with a few hacky interventions – I was able to use it in Python. Clearly, a long-term solution will involve porting those Matlab functions into Python (something everyone my mentor and other code reviewers were heavily stressing)… but as this will be quite some task, it’s good to have this work-around in the meantime to progress on other parts of the project.

## What elements helped you get there?
The support of the broader OLS community, OLS Founders, my mentor, other OLS Project Leads, as well as other people I could ask for help and guidance have tremendously helped me in progressing in both my project as well as my involvement in the open science community and advocacy for open science practices. I particularly valued the 1-to-1 conversations I had with my mentor as well as with multiple OLS experts who were willing to review my code. I also enjoyed the inputs during various cohort calls where I learned about important aspects of Open Leadership.

# Next steps

## My immediate next step is to...

... implement another measure! I will also tackle the porting of Matlab functions into Python, and start working on educational resources for the library – both for users and potential future contributors.

## Longer term tasks
My main tasks for the next year will be to accomplish the tasks described above and release a first version for others to use as well as to contribute to. This will also involve spreading the word about the library and doing some advertisements.
Overall, I hope that this project will contribute to making research on emergence & complexity more open, reproducible, and inclusive in the long run!

## Staying connected

- Stay in touch with the OLS community.
- Stay in touch with The Turing Way community (which has substantial overlap with the OLS community).

# Special mentions and acknowledgements

I am thankful to

- the OLS community and OLS Founders Yo, Malvika, Berenice and Emmy,
- my mentor Dario Pescini for all his support,
- Jessica Scheick and Sarah Gibson for reviewing my code,
- Moritz Boos who has delved deeply into my code and given me tremendously helpful and detailed feedback on it.

