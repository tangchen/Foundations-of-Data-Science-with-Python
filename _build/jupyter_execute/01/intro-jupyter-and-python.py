## Extremely Brief Intro to Jupyter and Python

The purpose of this section is to briefly introduce users to Jupyter and Python. The content here should be treated as an introduction to explore further and is not meant to be comprehensive. There is a broad variety of tutorials on the web for both of these topics, and links are provided for users that need additional instruction.

If you are already familiar with Jupyter and/or Python 3, feel free to skip ahead.

### Why Jupyter notebooks?


<img src="jupyter-logo.svg" alt="Project Jupyter logo" style="width: 150px;"/>


According to the [Project Jupyter web page (https://jupyter.org)](https://jupyter.org), "The Jupyter Notebook is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations and narrative text. Uses include: data cleaning and transformation, numerical simulation, statistical modeling, data visualization, machine learning, and much more."

The reason that Jupyter notebook was chosen for this book:

* Jupyter notebooks can integrate text, mathematics, code, and visualization in a single document, which is very helpful when conveying information about data. In fact, this book was written in a series of Juypter notebooks.
* Jupyter notebooks allow for an *evolutionary approach* to code development. Programs can start as small blocks of code that then can be modified and evolved to create more complex functions.
* **Think of more reasons**

### Why Python?

Python is a general purpose programming language that was originally created by Guido van Rossum. Python was chosen for this book for many reasons:

* **Python is very easy to learn.** Python has simple syntax that is very similar to C, which many engineers will be familiar with. It is also easy to transition to Python from MATLAB scripting, which most electrical engineers will know.
* **Python is an interpreted language,** which means that programmers can run the code directly without having to go through extra steps of compiling their programs.
* **Python interpreters are freely available and easy to install.** In addition, Python and Jupyter are available on all major operating systems, including Windows, MacOS, and Linux.
* **Python is popular for data science and machine learning.** Python is widely used for data science and machine learning in both industry and universities.
* **Python has rich libraries for data science.** Python has many powerful libraries for data science and machine learning. In addition, Python has powerful libraries for a broad array of tasks that making learning Python have additional benefits for other uses.

## How to get started with Juypter and Python

Python and Jupyter are often packaged together in a *software distribution*, and the creators of several distributions include additional Python software libraries, such as for scientific computing. This book assumes the use of the Anaconda distribution, which its creators bill as "The World's Most Popular Data Science Platform" **Add footnote with reference to web page here**. Anaconda's *Individual Edition* is freely available for download from the Anaconda web site:

[![Anaconda Logo](anaconda.png)](https://www.anaconda.com/products/individual)

[Anaconda Individual Edition (https://www.anaconda.com/products/individual)](https://www.anaconda.com/products/individual)

Choose the proper download based on your computer's operating system. You may also have to select a version of Python. This book is based on **Python 3**, which means that any version of Python that starts with the number 3 should work with the code included in this book. For instance, as of January 2021, the Anaconda distribution included Python version 3.8. 

**MAKE THIS A WARNING**
Python version 2 or Python versions after 3 may have syntax changes that cause the programs in this book to not run without modification.

After downloading, install Python in the usual way (for instance, by double-clicking on the downloaded file). Anaconda will install Python and many useful modules for data science, as well as Jupyter notebook and JupyterLab.

**Add Insert explaining Jupyter notebook vs JupyterLab**

**Special notation for a notice**
Note that the term "Jupyter notebook" can refer both to a file format (with *.ipynb* extension) and to an application with a web interface to work with those files. To help avoid confusion, I will write *Jupyter notebook file* whenever referring to such a file, and we will use JuypterLab as the web application for opening and working with such files. As of January 2001, JupyterLab is the "is the next-generation web-based user interface for Project Jupyter." (ref https://jupyterlab.readthedocs.io/en/stable/). Jupyter notebook has a very similar interface, and most users will be able to use either one interchangeably.



### Getting organized

We are almost ready to start using Jupyter and Python. Before you begin to do that, I recommend to take a minute to think about how you will organize your files. To learn data science requires actually working with data and performing analyses. This will result in you generating a lot of Jupyter notebook files, as well as a lot of data files. I suggest that you create a folder for this data-science book (or for the course, if you are using this as a course textbook). This folder should be easily accessible from your home directory because that is the location where JupyterLab will open by default. You may wish to add additional structure underneath that folder. If you create a separate folder for data, I would suggest to make it a subfolder of the one containing your notebooks to make it easiest to access that data.

**Note** that your user directory will be referred to by a tilde (~). Thus one possible organization of your files is shown below:

**Turn this into a prettier image**

\begin{align*}
&\mbox{~} \\
& |\\
&\longrightarrow && \mbox{data-science} \\
&&& | \\
&&& \longrightarrow  &&\mbox{notebooks} \\
&&&&& | \\
&&&&& \longrightarrow  &&\mbox{data} \\
\end{align*}

Within the *notebooks* directory, you may wish to add subfolders, for instance by chapter, topic, or lecture.  