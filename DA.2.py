    
    
    
    Good morning guys!
    
    Ill be audible from 12:15 PM sharp
    
    We are waiting for everyone to join.
    
    Mark your attendance on the group.
    
    Shut down your Mic and Camera.
    
    
        End to End Data Analytics Application

1. Get the Data
2. Descriptive Statistics
3. EDA (Exploratory Data Analysis)
4. Estimation
5. Hypothesis Testing

* Get the Data

1. Verify the source of the data generation pipeline to
    understand the nature of data.
    
2. Understand and validate the type of data (extension)

Explanation : Some times the data that we will provided by
the client comes from an internal ERP software, sometimes
from a conducted survey, sometimes from some kind of 
electronic sensor and sometimes from a social media channel.

AQI Index : Air Quality Index
Suppose you want to analyse or predict global warming
according to the green house gases. You maybe very good with
statistics but still you need some kind of sensor to tell
you about the presence of a particular gas only then you can 
start the process of analysis. 

In most cases a small and simple dataset is often a csv file.
But some other popular file extensions are, .data, .sql
.json, .xlsx, .tsv etc

.csv, .tsv : Pandas is the best library to work with
.json, .sql : Apache Spark is the best tool to work with
.zip is compressed data format which is mostly extracted
first and then used.
.gzip is also the same.

* Descriptive Statistics

1. Define the data types of all the attributes (columns)

2. Gather the estimate of location, estimate of correlation,
    estimate of variability etc
    
3. Mark boundaries of preprocessing based on the type
    of attributes
    
Explanation

In most cases the type of data is,

Integer / Float : Easy to handle
String : Medium complexity
Textual : Difficult to handle
Date and Time : Super Difficult to handle
Binary : Images or Videos | Difficult to handle

Integer/Float attributes ka example could be the age and
height column, weight, bank account number, otp etc

String : Categorical predefined strings, for example, gender
attribute will contain male, female, or others. 

Textual : Remarks or Feedback column is an example of 
    textual data. People are free to write whatever they
    want. And sometimes they dont even write full senetences
    but rather answer with an emoji. 

Date and Time : The problem with Date and Time is that every
    country or zone has its own implementation of the 
    date format. 

    dd-mm-yyyy
    mm-dd-yyyy
    
    09/11 : 11 September
    26/11 : 26 November
    
    Date toh fir bhi theek thi, Time column toh bohot 
    jyada badtameez hai.
    
    Pucho kaise?
    
Woh aise ki time column can take multiple forms like

timestamp : wednesday (12:10 PM) thursday (12:15 PM)
time elapsed : wednesday (12:10 PM to 01:00 PM)
                 thursday (12:15 PM to 01:30 PM)
                 
                 or 
                 
                 wednesday (50 minutes)
                 thursday (75 minutes)
                 it could be anything like this format
                 
"Textual Data aur Date & Time Data jyada difficult hone ki \
wajah se humne DA me kayi independent branches bana lee hai \

Textual Data : Natural Language Processing
Data & Time : Time Series Analysis
"
NLP and TSA can be taught separately.   
    
After that, we need to measure and find out 

* The Estimate of Location (data kaha pe rehta hai)

"Data jaha pe rehta hai, usko stats me mean, median ya \
mode kehte hai"

* The Estimate of Variability

"Standard deviation and Variance of the data."

* The Estimate of Correlation

"Measuring the statistical metric that describes \
relationship among data points. Pearson's correlation \
coefficient or fisher's correlation coefficient."

Marital Status
No of Children

Different type of attributes are preprocessed differently
for example, if there is a missing value in the age column,
you can simply replace that missing value by the mean
of all the values. 

Lekin yeh kaam kisi missing pixel value for image mat
kar dena nahi toh dikkat ho jayegi. Image aur binary
data k case me alag strategies select ki jaati hai.


* EDA (Exploratory Data Analysis)

America ki khoj kisne ki thi?

How do you discover new or hidden paths?
By exploration.

EDA simply means using all the graphical tools available
at your end to tell a story from the data.
Some popular ones are:
    
    1. Histogram
    2. Scatterplot
    3. Boxplot
    4. Heatmap
    5. Geomplot
    6. Globeplot
    7. Animationplot
    8. Piechart
    9. Barplot
    10. etc
    
Let me show you ki aapki zindagi bhale ek din khatam ho
jaaye lekin plot ka type kabhi khatam nahi hoga.

Yeh raha uska evidence.

* Estimation

Statistics provides a lot of concepts for estimation. The
most popular of which is the p-value estimation.
It is extremely useful in hypothesis testing. There are
other metrics of estimationas well.


* Hypothesis Testing

What exactly is a hypothesis?
Ans: An opinion made by someone can be called as a hypothesis.

In real world, hypothesis' are quite common. 
DA provides a way to test these statements or opinions
and find out which one among them is actually (factually)
correct.

1. Flight is the safest mode of travel.
2. Men is more arrogant as compared to women.
3. Men are better at being leaders and innovators as 
    compared to women.
4. Women are better cooks than men.
5. Indians are generally the smarter breed of people.

Abhi aapka opinion kuch bhi ho, mai aapko fact bata deta
hoon. Future me aise datasets pe kaam karenge, jo inn
facts ko aapke saamne rakhega. Aisa ek dataset humare paas
aaj he maujud hai. We will be working on it today.

(True, True, True, False, False)

Since we have now written our bible and it is only the
second class today. We can now start with practicals.

From Monday onwards, we will be doing more and more examples
along with the necessary theory.

Aaj ka dataset aata hai world bank ki site se, yeh ek
kaafi common dataset hai, jo ki kaggle pe bhi available hai

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('DemographicData.csv')

X = dataset.iloc[:, [2, 3]].values

plt.scatter(X[:, 0], X[:, 1])
plt.xlabel('Birth Rate')
plt.ylabel('Internet Users')
plt.show()

Have I considered the Income group?

z = dataset.iloc[:, -1]
z.value_counts()

z = z.values

from sklearn.preprocessing import LabelEncoder
lab = LabelEncoder()
z = lab.fit_transform(z)
lab.classes_

0: High Income
1: Low Income
2: Lower Middle Income
3: Upper Middle Income

plt.scatter(X[z == 0, 0], X[z == 0, 1], c = "r", label = "High Income")
plt.scatter(X[z == 1, 0], X[z == 1, 1], c = "g", label = "Low Income")
plt.scatter(X[z == 2, 0], X[z == 2, 1], c = "b", label = "Lower Middle Income")
plt.scatter(X[z == 3, 0], X[z == 3, 1], c = "y", label = "Upper Middle Income")
plt.xlabel('Birth Rate')
plt.legend()
plt.title('Analysis on the World Bank Dataset')
plt.ylabel('Internet Users')
plt.show()

Insights : Birth rate and Internet users have a negative
            linear relationship. 
            
Low Birth rate, High Internet Users --> High Income
High Birth rate, Low Internet Users --> Low Income

"I know that the syntax structure does not makes sense \
to you as of now. You might not feel very comfortable \
with it. But soon it will all make sense."

Programming is like driving, the more you do it, the 
better you get. 

statistics_ is a tuple that contains the calculated value
by a class. 

    