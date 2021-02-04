# Introduction

## Who is this book for?

This book is targeted toward engineers, whether working or still in school. It is written by an Electrical and Computer Engineer, and it is generally designed toward engineers with the following assumptions. 

**Background Knowledge**
This book assumes the reader has
* Basic computer-programming ability (knowing Python is helpful, but not required)
* Knows (one-dimensional) differential and integral calculus
* Knows how to work with complex numbers

This book was designed as the primary textbook for a 4-credit, semester-long course for engineers, which is taught in the Department of Electrical and Computer Engineering at the University of Florida. It is designed to be a broad introduction to data science, but it is also designed to replace courses in *Engineering Statistics* and *Computational Linear Algebra*

## Why learn data science from this book?

This book uses a **comptutional first** approach to data science. We take advantage of the power of modern computers to visualize, transform, and simulate data. In particular, we use an approach to statistics in which statistical tests are conducted by carrying out simulations that draw samples from the data being analyzed. This approach has the following benefits:
* **We start working with real data sets quickly** because this approach does not require a lot of mathematical background and the computer does all the mathematical manipulation and plotting.
* **Simulation models are easy for students to create and understand.** The results do not rely on any arcane formulas but only the ability to build very simple simulations that draw from the experimental data.
* **This approach is more general than the traditional approach.** It does not rely on the data coming from specific probability distributions, and the same simulation can be used to generate frequentist or Bayesian statistics. 

## What is data science? 

Our world is filled with information. In fact, many times the amount of information we have access to can be overwhelming. 

As engineers, our goal is to make sense of the world and use what we learn to take action. 

Information about some topic that is collected together is referred to as data. This is especially true if the information is numerical or categorical in nature. Typically, data includes multiple observations of some *population* of interest. Here, the population can literally be people, or it can be any other group, such as power plants, stars, etc.

The main goal of this book, and a general goal of data scientists, is to **generate meaning from data**.

Data scientists often start with a research question. For instance:
* Is the climate changing?
* Do gun laws affect firearms mortality?
* How reliable are mammograms (x-rays used to detect breast cancer)?
* How fast was the COVID-19 corona virus spreading when it first became prevalent in the United States in the Spring of 2020?
* **ADD MORE QUESTIONS FROM BOOK HERE**

One of the goals of a data scientist is to take broad research questions and translate them into questions that can be answered using data. For instance, here are some ways that the questions above may be reformulated so that they can be answered with data:
* Instead of "Is the climate changing?", a data scientist may ask a much more specific question, such as "Has the temperature in Miami, FL increased over the past 40 years?"
* Instead of "Do gun laws affect firearms mortality?", a data scientist may ask about a specific law, such as "How did the federal assault weapons ban of XXXX affect firearms mortality?" Or the data scientist may look at the affect of different numbers of laws across states: "How does the number of state gun laws affect firearms mortality?" 
* To determine how reliable mammograms are, a data scientist may ask "If a patient's mammogram comes back positive, what is the probability that patient has breast cancer?"
* In assessing the rate of spread of the COVID-19 virus, the data scientst may ask "Was the number of cases growing exponentially in March of 2019? If so, what was the exponential growth rate?"

## What data science topics does this book cover?

Data science is a very broad topic. Data scientists use many different tools in making sense of data, from programming for data cleaning to advanced machine learning algorithms.

![Data science tools covered in this class](attachment:image.png)

This book focuses on some of the fundamental tools used to create meaning from data, and the focus is also on tools that are generally useful for engineers in other contexts. The topics that are focused on in this book include:

* **Simulation** is used to carry out statistical tests and to model random phenomena.
* **Visualization** is used to transform data into graphical forms that help to understand the data or tell a story about the data.
* **Statistics** is used to determine whether observations made from the data are meaningful or could just be attributed to randomness in the data.
* **Probability** is used to create mathematical models for random phenomena; these models can be used to develop optimal estimators and decisions.
* **Linear algebra** is used to transform data or find relationships among data.

Throughout this book, we use two key tools to enable our computational approach:

* **Jupyter** is a web-based notebook environment. Jupyter notebooks can include text, mathematics, graphics, executable program code, interactive widgets, and more.
* **Python** is a general-purpose computing language that has a rich set of libraries that support data science activities.


```{toctree}
:hidden:
:titlesonly:


intro-jupyter-and-python
jupyter-start
python-start
../02/fair-experiments1
```
