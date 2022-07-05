# <center><a name="top"></a>Mushroom Classification Project

by: Paige Rackley </center>

<p>
  <a href="https://github.com/paigerackley" target="_blank">
    <img alt="Paige" src="https://img.shields.io/github/followers/paigerackley?label=Follow_Paige&style=social" />
  </a>

 * * *  
[[Project Description](#project_description)]
[[Project Planning](#planning)]
[[Data Dictionary](#dictionary)]
[[Data Acquire and Prep](#wrangle)]
[[Data Exploration](#explore)]
[[Modeling](#model)]
[[Conclusion](#conclusion)]
___



## <a name="project_description"></a>Project Description:
The goal of this project is to clean and organize mushroom data and create a model that can accurately predict what class the mushroom is in, which in this case, is either edible or poisonous. Having a model that will accurately depict this can save many lives, as in many cases, eating poisonous mushrooms can be a death sentence. We have acquired data that tells us characteristics about an assortment of mushrooms that will help us decide what are important features that can help our predictions.

- Construct a Classification model that can properly predict the class of mushrooms.

- Present a report that shows my processes and how I came to my conclusions. 
  
***
## <a name="planning"></a>Project Planning:
  
  
 ### Project Goals: 
My goals are to use the data I have to create a ML Classification model that can accurately predict when a mushroom is either edible or poisonous. Through exploring the data I have, I want to be able to zero in on features that I consider to be directly correlated in predicting a mushrooms class. I want my final model to be as accurate as possible, as the models predictions of False Negatives is extremely important for one that is relying on the model.

  
  
 ### Deliverables:
> - A final report notebook
> - Workbooks that were used while going through the steps to create my model
> - Py files containing functions used in final notebook
> - A project summary write up

###  Executive Summary: 
Evidence from statisal tests and visualizations supports the claim that the cap color, odor, habitat and population of mushrooms are related to their class. My recommendation is to focus on these features when attempting to identify as a mushroom is poisonous or edible, as these features have shown trends that help predict its class.
  
        
### Initial Hypothesis/Questions: 
- cap_color (The mushroom cap color) is related to mclass.
- the odor of the mushroom helps determine its mclass.
- the habitat of mushrooms help determine its mclass.
- the population of mushrooms can help determine its mclass.

[[Back to top](#top)]


## <a name="dictionary"></a>Data Dictionary  
[[Back to top](#top)]

### Data Used

Target|Datatype|Definition|
|:-------|:--------|:----------|
| mclass | object | class of mushroom either edible or poisoneous |

|Feature|Datatype|Definition|
|:-------|:--------|:----------|
| habitat      | object |    habitat for edible and poisoneous mushrooms |
| population      | object | how many mushrooms(edible or poisoneous) |
| odor       | object | the scent of the mushroom |
| cap_color       | object | the color of the mushroom cap |


***

## <a name="wrangle"></a>Data Acquisition and Preparation
  
 ## Acquire
The data was acquired from [Kaggle.com](https://www.kaggle.com/datasets/uciml/mushroom-classification?datasetId=478&sortBy=voteCount). Kaggle is a wonderful website with datasets you can download directly onto your personal device to explore. In order to use this dataset, you will need to click on the hyperlink that will take you directly to this Mushroom Dataset. There will be a button for you to download the CSV directly onto your device.

  
## Prepare
The reason we want to do this is because calling columns that contain dashes can be tricky and sometimes doesn't work. We want to avoid any issues that may occur later on so we can focus in on our testing and modeling.

Since I planned on using 'cap_color', 'odor', 'habitat', and 'population' as my features, I needed to create a dummies dataframe because they are non-binary.


Other functions created:


<font color= green><b>def split_mush_data(df):</font></b> This function was created to split our mushroom data into train, validate, and test. This is nested in the prepare function, so it does not need to be called seperately.


<font color= green><b>def encode_y(x):</font></b>This function is created for Logistic Regression model to turn y into a binary column during modeling phase. 
  
[[Back to top](#top)]


  
## <a name="explore"></a>Data Exploration:
  ###  Explore
Viewing our visuals we found these trends:
- Edible have either no smell or smell like foods we like (almond, anise) while poisonous tend to have strong and sometimes offputting smells that should raise a red flag.
- edible tends to be browns/greys/neutrals while poisonous tend to be brighter, red/pink the majoirty of the time.
- mushrooms that are alone or 'scattered' are much more likley to be poisonous than edible.
- if you see a mushroom growing in an urban area, it's more than likely edible, but I wouldn't test it unless you are sure.
 
[[Back to top](#top)]

### Takeaways from exploration:
Exploration through visuals and chi squared tests show a relationship between the four features explored and our target variable. We will continue to use these in our modeling stages.

## <a name="model"></a>Modeling:
   ## What are we focusing on?

Since False Negatives are very important in this case, we are wanting to focus on our precision and accuracy. A False Negative in this case would mean that we would claim a mushroom is edible when it was poisoneous which could be a life or death situation, so we are wanting the highest accuracy and highest precision as possible.

#### Takeways after Train models:

As shown, all of these models are extremely close in precision and accuracy. Another question is, are we seeing overfitting? There is really no way to know at this point until we test our models on validate. If we see an extreme loss of performance, we will know that we are overfit. With everything considered, it seems it will be best to move all 4 models into validate to check.

#### Takeways from Validate:
    - We can confirm overfitting is not happening, as our performance did not plummit.
    - Still very consistent and high 90's.
    - KNN dropped the most.
    
    #### Although all of our models did perform wonderfully, we have to decide which to move into Test. I went with my Random Tree model, as all of our stats stuck at 99%.
  
[[Back to top](#top)]



## <a name="conclusion"></a>Conclusion:
  
 # Conclusion:

#### After our testing, we were able to prove that cap color, odor, habitat and population were major features that were able to determine a mushrooms class.

#### Out of all of our models, we were able to get a Random Forest model with an accuracy of 99% and precision of 99%.

#### Although the other models did not beat Random Forest, they all did exceptionally well, with not one result of the 4 dropping below a 96%.


  
### With more time:
- I would like to explore other features to see how much they help in determining class.
- I would also like to see if there were columns that not only help determine class, but if some columns/features were dependent of one another as well

## Recomendations: 
####
- When trying to determine if a mushroom is poisonous or edible:
        - Most edible mushrooms are browns/grays while poisonous tend be brighter, pink/red.
        - Most edible mushrooms smell like nothing, or like other familiar foods (almonds, anise) while poisonous tend to be offputting (fishy, foul, pungent, spicy)
        - The likelihood of a mushroom being poisonous if on its own and not in a group is extremely likely.


[[Back to top](#top)]
  
  
  **How to Reproduce**
- [x] Read this README.md
- [ ] You will need to download the mushroom.csv for the data contained at https://www.kaggle.com/datasets/uciml/mushroom-classification?datasetId=478&sortBy=voteCount
- [ ] Use the functions I have created that are contained in my python files
      - You will want the acquire and prepare files for acquiring and prepping data for exploring and modeling
      - I have a seperate python file called charts.py that contains the code for my visuals
- [ ] Have fun doing your own exploring, modeling, and more! 
