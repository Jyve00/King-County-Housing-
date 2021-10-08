![image](https://user-images.githubusercontent.com/75384559/136581557-5d9179a3-dc1b-4f97-ac4c-28d4719a06d4.png)


# King County Housing Project
   A project to analyse the housing data for King County in Washington State to solve an issue for our stakeholders. 
   
   
  # Github Repo Outline
```
├── Data                                <- Contains the raw and cleaned datasets 
├── Notebooks                           <- Contains jupyter notebook with extra models not used in Main.ipynb
├── Visuals                             <- Folder containing charts, graphs and maps showing the data analysis
├── Main.ipynb                          <- Analysis broken down with Jupyter Notebook
├── .gitignore                          <- Refrence to types of files for Github to ignore
├── functions.py                        <- Python file with functions to check prediction models
├── Presentation.pdf                    <- PDF version of pr
├── README.md                           <- Outline and Repo overview
└── main.py                             <- main jupyter notebook with out Final Model and summary
```
 
 # Overview
 
   The city of Seattle is looking to improve low property value neighborhoods. They want to know which neighborhoods would benefit the most from the grants, and what the grants should be used for. We will be using a dataset of individual houses from King County in Washington state. Using this data, we will use linear regression modeling make recommendations to the city of seattle on which features of a home will increase the property value the most. After our analysis we discovered that the most important features in determing property value were

-Latitude
-Grade
-Squarefoot living space
-View
-Condition.

We decided to reccomend that the city gives grants to homeowners to improve the condition of their home, since this was the most realistic option out of the five most important features.
   

# Business Problem

The city of Seattle is looking to improve low property value neighborhoods. They are looking to give grants to homeowners in neighborhoods with low-grade houses to improve the property value of the neighborhood. They want to know which neighborhoods would benefit the most from and grants. They want to know what should the homeowners use their grants for to improve the property value the most?



# Data

The dataset consists of data on individual houses from King County in Washington state. This dataset consists of data from houses sold between May 2014 to May 2015. Using this data, we will be looking to make recommendations to the city of seattle on which variables will increase the property value the most. There are 21598 rows and 21 columns in this dataset. Our target variable in this dataset will be the "price" column, which is the amount the house was sold for.


A list and description of all columns can be found here: https://github.com/Jyve00/Project2/blob/main/Data/column_names.md

We intend to use the columns in our final model.:

-Latitude
-Grade
-Sqft_living
-View
-Condition
-Longitude
-Sqft lot
-Floors
-Year built


# Methods


Before continuing a note about how we evaluated our models. We decided to focus on three primary metrics to measure our models against eachother:

R-Squared
Mean Squared Error
Mean Absolute Error
We also checked the assumptions of linearity for each model, and factored that into our analysis:

Linearity
Multicolinearity
Residual Normality
Heteroskedacity
Our functions for checking all of these things can be found in our functions file






# Results



Conclusions
Our final model is typically of by $88k~$90k USD. We considered how we should recommend features for the city to give grants for and looked at the importance of the features in our model. We decided that even though Latitude, grade, and SQFT Living Space were are important features we did not want to recommend them. First, it would not be feasible for homeowners to attempt to change the latitude or grade of their house. Second, a homeowner would need a significant amount of money from the grant in order to change the Living Space of their house, and we decided that it would be also be unrealistic and too expensive to ask them to do so.

Because of this, we recommend that the city give grants for improving the condition of the house. This is the most realistic option among the most important features in our model. We have also prepared a list of low value homes that have not been renovated, in hopes of providing a starting point for the city to determining who may be eligible for these grants.

The primary issue this model may not solve, however, is the costs associated with repairing homes. Moving forward, we would like to analyze the differences in costs it may take to repair homes in different kinds of conditions.
