# Etherpad Archiving Guide for OLS cohort calls

## Purpose:

For OLS (since OLS-4), we're using Etherpad for collaborative call notes to ensure accessibility, especially for the screen readers. 
The Etherpad instance hosted by the Software Freedom Conservancy only hosts inactive etherpads for 90 days - so early OLS etherpads will disappear as they fall out of use.  
We need to archive these notes manually if we want to save them.

In the future, this will be done on a weekly basis by whoever processes the call videos. 

## Archiving steps: 

1. In Etherpad, go the the **Import/Export** dialogue, usually denoted by two arrows on the top right or bottom of the screen. ![import/export menu](https://i.imgur.com/yNNqhto.png)
2. Select **Markdown** and download the file onto your computer. 
3. You'll need to edit the etherpad before we archive it. 
    - **HackMD is probably the easiest option** as it doesn't require installing anything and gives a preview of the text when it's nicely formatted. 
    - Alternatively, this could be a program on your computer like [Atom](https://atom.io/) or [VSCode](https://code.visualstudio.com/), or in a Google Docs document.
4. **Important: Anonymise the doc for cohort participants:** Go through the document and review all names and contact details through the entire document, including the icebreaker, rollcall, Q&A sections, etc. 
    a. If the name is an **Expert guest speaker or cohort call host - leave it** in the document, since their materials and recordings will be shared online publicly. 
    b. If the name is a **cohort member, remove it**, since there may be private or semi-private reflections or notes. 
5. Upload it to GitHub on the OLS repo for the cohort (see [OLS-4 repo](https://github.com/open-life-science/ols-4) - this section is deliberately left vague as there are many ways to do this, but we'll be happy to help if you get stuck:
    1.  Navigate to the correct folder for this week. You might need to create it yourself by typing it in the file name field: ![preview of the week name typed into the file name field](https://i.imgur.com/SUiPcax.png)
    2.  Create a new file, and either upload the file you edited or copy/paste the info into the GitHub editor. 
    3.  Make a pull request to the OLS repo! 

