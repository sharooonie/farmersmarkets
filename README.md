<html>

<h2> Farmers Market Analysis - Where can you sell your product? </h2>

<p>This repo provides supporting information for a proof of concept (POC).  The data product explained by this POC is a recommendation system focused on helping local farmers find the nearest farmers' market with the highest probability to sell their produce.  The program could also help fans of farmers' markets to find the nearest market with product they are seeking. </p> 
<h3>1. Problem Formulation</h3>

<p>If you were a local baker without a store front, how would you know where to sell your produce?  What you if you had three farmers' markets within 50 miles of you that sold similar products but only one of them never has any stalls for baked goods? How do local farmers without a support system within the U.S. agricultural infrastructure find their way to a farmers' market?</p>

<h3>2. Create a Hypothesis</h3>

<p>Create a recommendation system that allows the user of the program to determine what type of recommendation they are looking for.  If they are buying, they are looking for the product sold in all of the "drivable" distances.  If they are selling, they are avoiding saturated markets, long distances that may make the early morning drive costly, and successfully active farmers' markets.</p>
<p>Question related to this Data Science Project at time of Class Presentation:  What County in the U.S. is mostly selling Wild Harvested produce or Cheese?  And, vice versa?</p>

<h3>3. Data Analysis & Testing (iterative)</h3>

<p>   3a.  Goals</p>

<p>User input*: Key parameters required by the programs' users would be location by means of Zip Code and County, desirable distance for travel and products of interest.  Due to the population the program is intended to interact with, a web-front is needed.  

<p>Data Gathering: The USDA maintains the National Farmers' Market Directory.  This file is updated regularly because data input to the dataset is voluntary.  Due to the frequency of data updates, it can be inferred that many farmers' market utilize this dataset for subsidies, marketing and/or advertising.  (As such, it should be expected that this program already has a great deal of competition.)  </p>

<p>Data Cleansing: </p>
<p>- Python allowed for recreating the 'updateTime'.  Because the dataset is voluntarily updated, we can infer that the 'updateTime' is related to significant changes to the existence of the farmers' market.  It can vary from initial establishment to creation of social media marketing to closing or relocation of the market.  For the purpose of the POC, we assumed this date is mostly related to initial establishment so we can use Python and Pandas to visualize about how many farmers' markets are opening across the US by region, state or otherwise. Refer to https://github.com/sharooonie/farmersmarkets/blob/master/GA-Project-OverviewOfUSFarmersMarkets.ipynb for more information.</p>
<p>- Excel allowed for creation of a column called region.  Python by way of MapReduce likely could have achieved the same results. Refer to https://github.com/sharooonie/farmersmarkets/blob/master/GA-Project-OverviewOfUSFarmersMarkets.ipynb for more information.</p>
<p>- The produce columns had inconsistent null values. Pandas facilitated the standardization of blank fields for modeling.</p>
<p>- See below for additional data cleansing activities that would further improve the quality and usability of this dataset. </p>

<p>*Based on the nature of this POC, these portions of the program has not been built.</p>

<h3>4. Create a Data Product</h3>



<h5>Files Explained:</h5>


<h5>References Used:</h5>


<h5>Additional Information:</h5>  <p>The following are analysis conducted that did not appear to help the creation of the program. Note the original hypothesis for the project was to attempt predicting county in the U.S. where the next farmers' market would be established.  However, through review of the data set, it was clear the National Farmers' Market Directory dataset was insufficient. </p>
<p>(A) The US Census data for poverty and education were reviewed to help solve the original hypothesis.  However, based on the unrealistic nature of a local farmer being able to sell produce across the country or oblivious to the economic conditions of surrounding livable areas, the hypothesis was edited to solve the problem.  Additionally, the datasets appeared to already be results of previous analysis per review. The US Census datasets were therefore excluded from the remainder of the data science analysis.</p>
<p>LINK: http://www.census.gov/did/www/saipe/data/index.html</p>
<p>(B) The National Farmers' Market Directory records seasonal availability by market.  However, the format of the data input is not easily interpretable.  Python, Pandas, and their libraries could greatly improve the usability of the inforamtion in the dataset. </p>
<p>LINK: http://www.census.gov/did/www/saipe/data/index.html</p>

</html>
