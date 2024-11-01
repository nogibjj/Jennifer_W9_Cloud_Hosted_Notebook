[![Install](https://github.com/Jenniferli6/Jennifer_Individual_Project_1/actions/workflows/install.yml/badge.svg)](https://github.com/Jenniferli6/Jennifer_Individual_Project_1/actions/workflows/install.yml)
[![Format](https://github.com/Jenniferli6/Jennifer_Individual_Project_1/actions/workflows/format.yml/badge.svg)](https://github.com/Jenniferli6/Jennifer_Individual_Project_1/actions/workflows/format.yml)
[![Lint](https://github.com/Jenniferli6/Jennifer_Individual_Project_1/actions/workflows/lint.yml/badge.svg)](https://github.com/Jenniferli6/Jennifer_Individual_Project_1/actions/workflows/lint.yml)
[![Test](https://github.com/Jenniferli6/Jennifer_Individual_Project_1/actions/workflows/test.yml/badge.svg)](https://github.com/Jenniferli6/Jennifer_Individual_Project_1/actions/workflows/test.yml)

# Week 9 - Cloud-Hosted Notebook Data Manipulation 

**Google Collab Link**
https://drive.google.com/file/d/1c6_B0UT-frgB0B9p8g0ZmoxinOvXcZJ7/view?usp=sharing 

## Project Introduction
This project aims to set up and utilize a cloud-hosted Jupyter Notebook environment (i.e. Google Colab) to analyze a job application dataset published by the City of Los Angeles. The analysis involves data manipulation such as generating summary statistics and visualizing data to reveal trends in gender and ethnicity among job applicants. 

## Project Data Source
The data used in this analysis comes from a dataset published by data.lacity.org on Data.Gov website, and the data version is as of September 15, 2023. You can find more information about data source via link here: https://catalog.data.gov/dataset/job-applicants-by-gender-and-ethnicity 

## Continuous Integration
This project uses GitHub Actions for continuous integration, automatically running the following jobs:
- Installing dependencies
- Formatting code with Black
- Linting code with Ruff
- Running all tests (script, notebook, and library)

## Statistic Summary 
![alt text](image-2.png)

## Data Visualizations
![alt text](image.png)

![alt text](image-1.png)

## Conclusion
- There is a notable gender imbalance, with male applicants outnumbering female applicants by a considerable margin.
- Ethnicity distribution shows Hispanic and Black applicants as the largest groups, with significant representation from Caucasian applicants as well. Other ethnic groups have much smaller representation.
- These findings suggest potential areas for our future investigation, such as understanding the factors contributing to the gender imbalance in applicants, exploring ways to increase diversity in the applicant pool, etc.

## References
https://github.com/nogibjj/python-ruff-template


