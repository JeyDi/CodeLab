# Python projects

This folder contains a number of projects that are useful for learning and understanding the basic of modern development with Python.

The goal is to try to create small demos to become familiar with the code and the technologies used within the AI team.

If you find any error or problems in the python template project (tempy) or in this guide please open a merge request with the changes.

## Requirements

List of requirements that you have to follow before starting the projects

## Project 1: Understand the basic of python development

The goal of this project is to try and test the basic of python development with the tools we are using in the team.

Remember to try to develop inside the dev environment servers (gpu1, gpu2, analytics) when you are in the office and continue in your pc when you are away from the office, so you can get more familiar with git and the environment management on different machines.

1. Follow the guide in tempy repository to download the `base` project template in a sub folder of this project folder, like: `projects/project1`
2. Enter in the project and install the dependencies with poetry
3. Start familiarizing with vscode debugger, try to launch the project in debug mode to see the result
4. Add new functionalities to the project and create some test with pytest:
   - function to transform strings in upper case
   - function to generate random numbers
   - function to load a csv file with pandas and another one in polars (adding also the libraries)
   - function to modify the csv and save to disk the result with pandas and polars
5. Create a jupyter notebook to load the python file functions and do some operations with this functions
6. Create pytest about the functions and launch the test with vscode test suite to see check if it's working properly your code
7. Check the `makefile` and try to launch some command, for example to install pre-commit and launch pre-commit checks
8. Push everything in your branch

At the end of this project you be able to:

- Understand the basic of modern python development with poetry and vscode
- Be able to interact and modify code with our codebase and logics
- Overview of the tools and approaches we are using

Remember to always push your changes to the project branch in git!

## Project 2: Understand the basic of Data Science projects

If you are a data scientist it's important to get more familiar with some technologies we are using in the team to manage the full lifecycle of the project (from the raw data, to training to data versioning and MLOps).

In particular:

- **Hugging face and pytorch**: for model training and usage
- **dvc** for data versioning
- some of our **internal packages**:
  - data connector: for data retrieval and management
  - swordfish: for some NLP tasks
  - flowme: for model lifecycle management
  - sniply: a collection of python functions

The goal of this project is to create a simple NLP project using technologies mentioned here.

### Description of the project

The main goal of this project is to create a small classification algorithm based on SPECTER v2 that take the 2023 articles (only title and abstract) and the journal where are published and if a new article arrive it suggest to the user what is the best journal where to publish.

In particular you need to:

1. Generate the dataset extracting 2023 articles with tile, abstract and journal_id
2. Create a classification layer on top of SPECTER v2 model and train the classifier with this new dataset
3. Measure the performances and create a small prediction function to generate small predictions

### Activities

1. Create the project with tempy and install all the dependencies
2. Retrieve informations from the database.
3. Generate the dataset using title, abstract, article_id, journal_id. Journal_id it's the predictor. Be careful on the distribution of the article in the journals, remove the journals with few publications, take in account only larger journals.
4. Create some dynamic visualization to see the distribution of the articles in the journals
5. Version the data using dvc in our s3 repository
6. Extend the model by adding the classification layer, then train the classification layer with the new dataset. Try to use swordfish in this task.
7. Use flowme to version the model and save it in onnx format with the result
8. Create a function to retrieve predictions passing a title and abstract and generate the journal where to publish with a probability attached.

### Considerations

Try to not use jupyter notebooks, use python files instead with the vscode debugger.

Try to create functions after you try to generalize the behaviors of the business logic you wrote, this is important because in the next exercise you will need to use this functions again.

Swordfish library it's not fully complete with classification capabilities, please check other projects code like Ethicality or Journal Finder to see how you can implement the classification layer on top of the model.

At the end of this project you have to show the performances of the model, show an example on how the inference it's working, where the model is saved with some information about training statistics, the data versioned and the code written.

#### Documentation

## Project 3: Understand the basic of Streamlit

After you practice with the base project and the tools we have in the team it's time to work on the first dashboard!

In the team we are using **streamlit** as internal tool to develop web applications and dashboard.

It's a simple and limited tool compared to some javascript framework (like React or Vue), but it's useful and we are making good things with that.

The goal of this project is to develop a simple user interface that use the model you trained in the [project 2](#project-2-understand-the-basic-of-data-science-projects) to propose to the user some suggestion, in particular:

- It's important to have a user interface that have a title and abstract input
- Add some sliders and button to customize the launch of the model (like the number of results), it's better to use the **sidecolumn** instead the **default section**
- When the user press a button it will display below the input section the list of prediction with suggestions (in a table)
- For every result in the table add also the possibility to check more information about the journal that you can find in the db using the journal_id.
- Add another page with notes and description of the model

### Additional steps

Be careful when you have to use the **streamlit cache**, we have some caching mechanism in other project that you can check like **Eureka**, **Article Similarity** or **EtymologAI**.

To launch the project you can use the **vscode debugger** and the terminal also, we suggest you to try and get familiar with both ways.

It is important that the application is **dockerized** so that it can be launched within the gpu workstation by docker-compose.

As an additional feature you can send an email notification to your mail address saying that there has been a new prediction.

For now it's not required to store the prediction in a dedicated database, you have the chance to see the postgres database in the next project.

Remember also here to create a new project inside your branch. Everything need to be versioned with git and don't use any jupyter notebook here.

## Project 4: Understand the basic of API

## Project 5: Understand the basics of Data Management Workflow

## References

- [Python project ideas](https://data-flair.training/blogs/python-project-ideas/)
- [Realpython projects](https://realpython.com/tutorials/projects/)
- [Python projects](https://hackr.io/blog/python-projects)
- [Python projects for beginners](https://www.freecodecamp.org/news/python-projects-for-beginners/)
- [Python project ideas topics beginners](https://www.upgrad.com/blog/python-projects-ideas-topics-beginners/)
- [Python projects for beginners](https://www.dataquest.io/blog/python-projects-for-beginners/)
- [Practical python](https://practicalpython.yasoob.me/toc.html)
