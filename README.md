# Business Intelligence Assignment 7 - Text classification and geographical data

## Part 1 - Accuracy and recall  
  
For results see [this link](https://github.com/cph-al180/BI_Assignment_8/blob/master/part-1.ipynb)

### Part 1.1
Accuracy is how close a measured value is to the actual (true) value  
Precision is how close the measured values are to each other

### Part 1.2
Precision is the fraction of retrieved documents that are relevant to the query.
For example, for a text search on a set of documents, precision is the number of correct results divided by the number of all returned results.  
  
Recall is the fraction of the relevant documents that are successfully retrieved. For example, for a text search on a set of documents, 
recall is the number of correct results divided by the number of results that should have been returned.  
  
### Part 1.3
Most of our guesses lay around a score of 0.9, which means we are very consistent with guessing right, but our support is'nt that great, so to be more secure in our guesses we need a bigger data sample.  

## Part 2 - Population and t-test

### Part 2.1
T-tests are inference tests, which is a type of test that tells us if we can infer anything from our data, which is supported by a hypothesis.  
We can analyze T-values to gain information about the P-value, which is a probabaility percentile for our hypothesis to be true. If the percentile is at or below 5% (this can vary based on the situation), then the hypothesis is significant.

### Part 2.2  
`T-Value: -3.8682665640568583`  
`P-Value: 0.00041658142370520256` 
  
From the result we can gather that our sample is -3.86 standard deviations from the mean, and the probability of confirming a null hypothesis is 0.04%. This means that it's highly unlikely that the mean height of the sample matches the mean height of our population.

### Part 2.3
`T-Value: 0.1964197529935458`  
`P-Value: 0.84532834985133909`   
  
Since the T-Value is so close to 0, it means that the mean sample and population are fairly close to eachother.  
The P-Value indicates that our hypothesis is highly likely to be true, since it has a probability of 84%. In our case that the sample consists of American citizens.

  







