# ¿Qué es el análisis exploratorio de datos (EDA)?

Fuente: [IBM Think](https://www.ibm.com/think/topics/exploratory-data-analysis)  
_Copia local para lectura fuera de línea. El formato original puede verse en la URL._

---

What is Exploratory Data Analysis? | IBM 








































































































































































































Analytics

What is exploratory data analysis (EDA)?

What is EDA?

Exploratory data analysis (EDA) is used by data scientists to analyze and investigate data sets and summarize their main characteristics, often employing data visualization methods.


EDA helps determine how best to manipulate data sources to get the answers you need, making it easier for data scientists to discover patterns, spot anomalies, test a hypothesis, or check assumptions.


EDA is primarily used to see what data can reveal beyond the formal modeling or hypothesis testing task and provides a provides a better understanding of data set variables and the relationships between them. It can also help determine if the statistical techniques you are considering for data analysis are appropriate. Originally developed by American mathematician John Tukey in the 1970s, EDA techniques continue to be a widely used method in the data discovery process today.


Join over 100,000 subscribers who read the latest news in tech

Stay up to date on the most important—and intriguing—industry trends on AI, automation, data and beyond with the Think Newsletter, delivered twice weekly. See the  IBM Privacy Statement .


Thank you! 

You are subscribed.


Why is EDA important in data science?

The main purpose of EDA is to help look at data before making any assumptions. It can help identify obvious errors, as well as better understand patterns within the data, detect outliers or anomalous events, find interesting relations among the variables.


Data scientists can use exploratory analysis to ensure the results they produce are valid and applicable to any desired business outcomes and goals. EDA also helps stakeholders by confirming they are asking the right questions. EDA can help answer questions about standard deviations, categorical variables, and confidence intervals. Once EDA is complete and insights are drawn, its features can then be used for more sophisticated data analysis or modeling, including machine learning .


Mixture of Experts | 17 April, episode 103

Decoding AI: Weekly News Roundup




Join our world-class panel of engineers, researchers, product leaders and more as they cut through the AI noise to bring you the latest in AI news and insights.







Watch all episodes of Mixture of Experts

EDA tools

Specific statistical functions and techniques you can perform with EDA tools include:


Clustering and dimension reduction techniques, which help create graphical displays of high-dimensional data containing many variables.




Univariate visualization of each field in the raw dataset, with summary statistics.




Bivariate visualizations and summary statistics that allow you to assess the relationship between each variable in the dataset and the target variable you’re looking at.




Multivariate visualizations, for mapping and understanding interactions between different fields in the data.




K-means clustering, which is a clustering method in unsupervised learning where data points are assigned into K groups, i.e. the number of clusters, based on the distance from each group’s centroid. The data points closest to a particular centroid will be clustered under the same category. K-means clustering is commonly used in market segmentation, pattern recognition, and image compression.




Predictive models, such as linear regression, use statistics and data to predict outcomes.


Types of EDA

There are four primary types of EDA:


Univariate non-graphical 

Univariate graphical 

Multivariate non-graphical 

Multivariate graphical 


Univariate non-graphical

This is simplest form of data analysis, where the data being analyzed 
consists of just one variable. Since it’s a single variable, it doesn’t 
deal with causes or relationships. The main purpose of univariate 
analysis is to describe the data and find patterns that exist within it.


Univariate graphical

Non-graphical methods don’t provide a full picture of the data. Graphical methods are therefore required. Common types of univariate graphics include:




Stem-and-leaf plots, which show all data values and the shape of the distribution.




Histograms, a bar plot in which each bar represents the frequency (count) or proportion (count/total count) of cases for a range of values.




Box plots, which graphically depict the five-number summary of minimum, first quartile, median, third quartile, and maximum.


Multivariate nongraphical

Multivariate data arises from more than one variable. Multivariate non-graphical EDA techniques generally show the relationship between two or more variables of the data through cross-tabulation or statistics.


Multivariate graphical

Multivariate data uses graphics to display relationships between two or more sets of data. The most used graphic is a grouped bar plot or bar chart with each group representing one level of one of the variables and each bar within a group representing the levels of the other variable.


Other common types of multivariate graphics include:


Scatter plot, which is used to plot data points on a horizontal and a vertical axis to show how much one variable is affected by another.




Multivariate chart, which is a graphical representation of the relationships between factors and a response.




Run chart, which is a line graph of data plotted over time.




Bubble chart, which is a data visualization that displays multiple circles (bubbles) in a two-dimensional plot.




Heat map, which is a graphical representation of data where values are depicted by color.


Exploratory data analysis languages

Some of the most common data science programming languages used to create an EDA include:


Python: An interpreted, object-oriented programming language with dynamic semantics. Its high-level, built-in data structures, combined with dynamic typing and dynamic binding, make it very attractive for rapid application development, as well as for use as a scripting or glue language to connect existing components together. Python and EDA can be used together to identify missing values in a data set, which is important so you can decide how to handle missing values for machine learning.




R: An open-source programming language and free software environment for statistical computing and graphics supported by the R Foundation for Statistical Computing. The R language is widely used among statisticians in data science in developing statistical observations and data analysis.


For a deep dive into the differences between these approaches, check out " Python vs. R: What's the Difference? "


Link copied

Download our ebook to get actionable steps you can take to make your organization's data AI-ready. 

Resources

Podcast

Podcast: Decision Intelligence: Thoughtful, data-driven choices

Learn about the concept of decision intelligencd and how data-driven decision-making can create real impact within your business

Watch now 

Ebook

Unleash the power of AI for seamless data integration

Discover how a unified, AI-powered data integration approach can help you move faster, reduce complexity, and unlock the full potential of your data

Get the ebook 

Ebook

Your AI is only as good as your data

See a framework that can help organizations manage and prepare quality data to meet the requirements of their AI use cases.

Read the ebook 

Report

IBM named a Leader in the 2025 Gartner Magic Quadrant for Data Integration Tools

Access the full report to learn why IBM is recognized as a Leader

Download the report 

Report

IDC names IBM a Leader

Download the report to learn why IBM is recognized as a leader for Worldwide Data Integration Software Platforms

Explore the report 

Webinar

Bridging the data engineering skills gap

Get an exclusive look at 3 authoring styles that empower every user, regardless of skill level, to build pipelines, speeding delivery and ensuring data teams can meet the businessís growing demands.

Watch here 

Report

IBM named a Leader in Data Science and Machine Learning

Read how IBM is delivering flexible, AI-focused solutions that empower data scientists and machine learning engineers to build, deploy, and govern impactful AI applications across their enterprises.

Get the report 

Webinar

Unlock your unstructured data to boost AI accuracy

Learn how to automate and scale data access, enrichment, storage, and delivery of AI-ready unstructured and structured data to power accurate, differentiated gen AI.

Watch now 

Related solutions

IBM® watsonx.data™

Watsonx.data enables you to scale analytics and AI with all your data, wherever it resides, through an open, hybrid and governed data store.


Discover watsonx.data

Data science tools and solutions

Use data science tools and solutions to uncover patterns and build predictions by using data, algorithms, machine learning and AI techniques.


Explore data science solutions

Data and analytics consulting services

Unlock the value of enterprise data with IBM Consulting, building an insight-driven organization that delivers business advantage.


Discover analytics services

Take the next step 

Unify all your data for AI and analytics with IBM® watsonx.data™. Put your data to work, wherever it resides, with the hybrid, open data lakehouse for AI and analytics.


Discover watsonx.data 

Explore data science solutions
