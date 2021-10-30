# ADM-HW2

![steam](https://www.vortez.net/contentteller.php?ct=news&action=file&id=18653)

In this github repository we stored the files written for the second Homework of the ADM course.

### File and Scripts descriptions
1. __`main.ipynb`__:
    > This is the notebook where we have developed our answers to all the research questions and theoretical questions. We have already runned all the notebook.
    
        Research Questions
            1. [RQ1]: Exploratory Data Analysis (EDA)
                - Application more reviewed 
                - Correlation matrix
                - Time and Language
                - Viral Comments
                - Games more played
                - Active players
                - Languages and subplots
    
            2. [RQ2]:
                - Plot the number of reviews for each application in descending order.
                - What applications have the best Weighted Vote Score?
                - Which applications have the most and least recommendations
                - How many of these applications where purchased, and how many where given for free?
        
            3. [RQ3]:
                - What is the most common time that authors review an application? For example, authors usually write a review at 17:44.
                - Create a function that receives as a parameter a list of time intervals and returns the plot the number of reviews for each of the intervals
                - Use the function just created to plot the number of reviews between different time intervals.
    
            4. [RQ4]:
                - What are the top 3 languages used to review applications?
                - Create a function that receives as parameters both the name of a data set and a list of languages’ names and returns a data frame filtered only with the reviews written in the provided languages.
                - Use the function created in the previous literal to find what percentage of these reviews (associated with the top 3 languages) were voted as funny?
                - Use the function created to find what percentage of these reviews (associated with the top 3 languages) were voted as helpful?
          
            5. [RQ5]:
                - Plot the top 10 most popular reviewers and the number of reviews.
                - What applications did the most popular author review?
                - How many applications did he/she purchase, and how many did he/she get as free? Provide the number (count) and the percentage.¶
                - How many of the applications he/she purchased reviewed positively, and how many negatively? How about the applications he received for free?¶
          
            6. [RQ6]:
                - What is the average time (days and minutes) a user lets pass before he updates a review?¶
                - Plot the top 3 authors that usually update their reviews.¶
                 
            7. [RQ7]:
                - What’s the probability that a review has a Weighted Vote Score equal to or bigger than 0.5?
                - What’s the probability that a review has at least one vote as funny given that the Weighted Vote Score is bigger than 0.5?
                - Is the probability that “a review has at least one vote as funny” independent of the “probability that a review has a Weighted Vote Score equal or bigger than 0.5"?
          
            8. [RQ8]:
                -Is there a significant difference in the Weighted Vote Score of reviews made in Chinese vs the ones made in Russian? Use an appropriate statistical test or technique and support your choice.
                - Can you find any significant relationship between the time that a user lets pass before he updates the review and the Weighted Vote Score? Use an appropriate statistical test or technique and support your choice.¶
                - Is there any change in the relationship of the variables mentioned in the previous literal if you include whether an application is recommended or not in the review? Use an appropriate statistical test or technique and support your choice.¶
                - What are histograms, bar plots, scatterplots and pie charts used for?¶
                - What insights can you extract from a Box Plot?
            
        Theoretical Questions
            1. [TQ1]:
                1. What does the algorithm compute?
                2. What is asymptotically the running time of the algorithm in the worst case, as a function of n?
                3. What is asymptotically the running time of the algorithm in the best case?

            2. [TQ2]:
                1. How much running time does it take to execute splitSwap(a, 0, n)? 
                2. What does this algorithm do? Is it optimal? Describe the mechanism of the algorithm in details.

            3. [TQ3]:
                - Provide a counterexample to the heuristic of ordering objects in increasing order of weight and then visit them sequentially
                - Provide a counterexample to the heuristic of ordering objects in decreasing order of values, and then visit them sequentially
                - Provide a counterexample to the heuristic of ordering objects in decreasing relative value (v_i / w_i), and then visit them sequentially
             
      
2. __`functions.py`__:
  > Python script in which we have written the useful functions to solve the RQ3, RQ4 and the function *parsedate* to transform the unix timestamps.
3. __`images/`__: 
  > Directory where are stored images used in the theoretical questions.
4. __`Theoretical Question.pdf`__: 
  > pdf file where we have elaborated the Theoretical questions. But we have also added these answers at the end of the notebook. 
