# Indeed Graph
A graph of Indeed data science, data engineer, and data analyst jobs.

## Prerequsities

* [pyTigerGraph](https://pypi.org/project/pyTigerGraph/)
* [Kaggle](https://pypi.org/project/kaggle/) (if installing from the API)

## Quick Set Up

1. [Get Started with TigerGraph Cloud](https://developers.tigergraph.com/quickstart)
2. Create an account on [Kaggle](https://kaggle.com/) (if directly importing data from kaggle).
3. Run `IndeedGraph.ipynb`, replacing it with the appropriate credentials.

## Breakdown

### Data
The data is from the [Kaggle Indeed Dataset](https://www.kaggle.com/elroyggj/indeed-dataset-data-scientistanalystengineer).

### EDA

- Removes unnecessary columns
- Replaces empty cells with values

### Scripts

#### Schema

![Indeed Schema](https://miro.medium.com/max/4800/1*qHWh3uc5S00zdGuOVs_SUA.png)

#### Loads
See `IndeedGraph.ipynb`.

#### Query
There are a few queries to grab data for analysis, including:

1. `topSkills.gsql` —> Grabs the top skills.
2. `topSkillsPerSalaryRange.gsql` —> Grabs top skills with the input of a SalaryRange vertex. 

## Projects

None so far. Create one!

## External Links

* [What are the Most Popular Skills for Data Science Jobs? Ask a Graph Database!](https://towardsdatascience.com/what-are-the-most-popular-skills-for-data-science-jobs-ead45f56841?sk=1ffd27241db17bc27f1b8d3610782c91)
