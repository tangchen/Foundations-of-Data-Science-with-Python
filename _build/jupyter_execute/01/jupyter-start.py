### Getting Started in Jupyter

Let's begin exploring JupyterLab using an existing notebook:

**1) Download a Jupyter notebook file.**

We will use the file "intro.ipynb", which is available by clicking on the link below or typing the link into your browser:

**Change this to an Intro notebook when this section is finished**

<a href="https://raw.githubusercontent.com/jmshea/EEL5544/master/Python%20Basics.ipynb" download="python-basics.ipynb">Python Basics</a>

If your browser displays the notebook as text, you will need to tell it to save it as a file. You can usually do this by right-clicking or control-clicking in the browser window and choosing to save the page as a file. For instance in Safari 14, choose the "Save Page As..." menu item. Be sure to name your file with a *.ipynb* ending.)

*Hint:* If your file was saved to your default Downloads folder, be sure to move it to your *notebooks* folder to keep things organized!

**2) Start JupyterLab.**

JupyterLab can be started from the Anaconda-Navigator program that is installed with the Anaconda distribution. Start Anaconda-Navigator, scroll to find JupyterLab and then click the *Launch* button under JupyterLab. JupyterLab should start up in your browser.

*Alternative for command line users:* users that are familiar with the command line can start JupyterLab by typing ```jupyter lab``` at the command prompt (provided the anaconda bin directory is on the command line search path). Because setting this up is specialized to each operating system and command shell, the details are omitted. However, details of how to set up the path for Anaconda can be found at many sites online.



Your JupyterLab should open to a view that looks something like the one below:

![](jupyter-lab-start.png)

```{warning}
If you have used JupyterLab before, it may not look like this -- it will pick up where you left off!
```

The JupyterLab interface has many different parts. 

The JupyterLab interface has many different parts:

1. The **menu bar** is across the very top of the JupyterLab app. We will introduce the use of menus later in this lesson.
2. The **left sidebar** occupies the left side below the menu bar. It includes several different tabs, which you can switch between by clicking the different icons on the very far left of the left sidebar. In the view above, the folder icon is highlighted, which indicates that the file browser is selected. For this book, we will use the left sidebar only to access the file browser.
3. The **main work area** is to the right of the left sidebar. The main work area will usually show whatever document you are working on. However, if you have not opened any document yet, it will show you different types of notebooks that you can open and other tools that you can access. To start a completely new Jupyter notebook file that can run Python 3 code, you could click on the Python 3 icon under ```Notebooks```. For now, you do not need to do that.

Detailed documentation for JupyterLab is available at https://jupyterlab.readthedocs.io/

**3) Navigate to the downloaded notebook.**

Use the file browser in the left sidebar of JupyterLab to navigate to the downloaded file. 

*If the file browser is not already showing your files, click on the folder icon (on the very left hand side of the window) to switch to it.*

Navigation using the file browser should be similar to navigating in most file selection boxes:

* Single click on items to select them
* Double click on folders to navigate into them 
* Double click on files to open them
* As you navigate down into folders, the current path (relative to your starting path) is shown above the file lsit. You can navigate back out of folders by clicking on the *name* of a parent folder in the current path.

If you downloaded the file ```intro.ipynb``` to the ```notebooks``` subdirectory of the ```data-science``` directory, which lies in your home directory, then  you would:

* Double click on the ```data-science``` folder
* Double click on the ```notebooks``` folder
* Double click on the file ```intro.ipynb```

The file ```intro.ipynb``` should open in the main work area.

### Learn the basics of JupyterLab

After opening the ```intro.ipynb``` notebook, take a minute to scroll through the ```intro.ipynb``` notebook before interacting with it. Note that the notebook includes formatted text, graphics, mathematics, and Python programming code. You will learn to use all of these features in working with data and presenting your analyses.

#### Notebook structure

Jupyter notebooks are subdivided into parts called **cells**. Each cell can be used for different purposes; we will use them for either Python code or for Markdown, which is a simple markup language that allows the creation of formatted text with math and graphics. Code cells are subdivided into Input and Output parts. Single click on any part of the ```intro.ipynb``` notebook to select a cell. The selected cell will be indicated by a color bar along the entire left side of the cell.

#### JupyterLab interface modes

The JupyterLab user interface can be in one of two modes, and these modes affect what you can do with a cell:

* In **Edit Mode**, the focus is on one cell, which will be outlined in color (blue on my computer with the default theme), and the cursor will contain a blinking cursor indicating where typed text will appear.
* In **Command Mode**, you cannot edit or enter text into a cell, but you can navigate among cells and use keyboard shortcuts to act on them, including running cells, selecting groups of cells, and copying/cutting/pasting or deleting cells.

There are several ways to 

In **Command Mode**, to switch to **Edit Mode** and begin editing a cell: 

* Double-click on a cell.
* Select a cell using the cursor keys and then press Enter.

In **Edit Mode**, to switch to **Command Mode**:

* Press the ESC key. The current cell is *not evaluated*, but it will be selected in **Command Mode**.
* If editing a cell that is *not* the last cell in the notebook, press Shift-Enter to *evaluate* the current cell and return to **Command Mode**. (If you are in the last cell of the notebook, Shift-Enter will evaluate the current cell, create a new cell below it, and will remain in **EDIT MODE** in the newly created cell.







## More on cells

### Evaluating cells

In **EDIT MODE**, code or Markdown can be typed into a cell. Remember that each cell has a *cell type* associated with it. The cell type does not limit what can be entered into a cell.  The cell type **determines how a cell is evaluated**.  When a cell is evaluated, the contents are parsed by either a Markdown render (for a Markdown cell) or the Python kernel (for a Code cell). Cells may be evaluated in many different ways. Here are a few of the typical ways that we will use:
* Most commonly, we will evaluate the current cell by pressing `shift-Enter` on the keyboard. This will always evaluate the current cell. If this is the last cell in the notebook, it will also insert a new cell below the current cell, so that it is easy to continue building the notebook.
* It is also possible to evaluate a cell using the toolbar at the top of the notebook.  Use the triangular "play" button (pointed to by the red arrow in the image below) to execute the currently selected cell or cells.
![Play button to evaluate a notebook cell](play-button.png)
* Sometimes we wish to make changes in the middle of an existing notebook. To evaluate the current cell and insert a new cell below it, press `alt-Enter` on the computer keyboard.
* Cells can also be run by some of the commands in the `Kernel` menu in the JupyterLab menu. For example, it is always best to reset the Python kernel and run all of the cells in a notebook from top to bottom before sharing a Jupyter notebook with someone else (for example, before submitting an assignment). To do this, click on the `Kernel` menu and choose the `Restart Kernel and Run All Cells...` menu item.

If you enter Markdown into a Code cell or Python into a Markdown cell, the results will not be what you intend. For instance, most Markdown is not valid Python, and so if Markdown is entered into a Code cell, a syntax error will be displayed when the cell is evaluted.  Fortunately, you can change the cell type afterward to make it evaluate properly.

```{admonition} Important!
:class: warning
New cells, including the starting cell of a new notebook, start as *Code* cells.
```

Cells start as *Code* cells, but we often want to enter Markdown instead. We also may wish to switch a *Markdown* cell back to a *Code* cell. There are three easy ways to change the cell type:
* As seen below, you can use the drop-down menu at the top of the notebook to set the cell type to *Code*, *Markdown*, or *Raw*
![](cell-type-dropdown.png)
* If you are in command mode, you can use a keyboard shortcut to change the type of a selected cell. The standard keyboard shortcuts are ```m``` for Markdown and ```y``` for code.
* If you are not in command mode, you can still use a keyboard shortcut, but you will need to press ```ctrl-m``` first, and then press either ```m``` for *Markdown* or ```y``` for *Code*.






## Intro to Markdown in Jupyter

You will use Jupyter to create documents that inform the reader about data. Although we will use code to process the data and generate graphs, that is usually not enough to tell the story to the reader. Markdown is used to add text, heading, mathematics, and other graphics.

The example notebook `intro.ipynb` demonstrates the main features of Markdown that we will need in this book. Recall that you can double click on any cell in the notebook to see the Markdown source. Below is a d the title "Intro to Jupyter and Python" cell to see the Markdown tex. This cell illustrates several features of Markdown:

**1. Headings**

The first cell (starting with "Intro to Markdown") illustrates how to use Markdown to format headings.
Headings are entered by prefacing text by one or more # (usually pronounced "hash") symbols. If you know any HTML, then `# Title` is equivalent to a `<h1>Title</h1>`, `### Subtitle` is equivalent to `<h2>Subtitle</h2>`, etc. Note that you must put a space between the hashes and the text for it to be recognized as a heading.

**2. Text and paragraphs**

The second cell shows paragraphs of text. Regular text can be entered as normal. 
Blank lines between text indicate the start of a new paragraph; press `Enter` twice
at the end of a paragraph to leave such a blank line.
Other line breaks do not create a new paragraph and can be used
to avoid over-long lines of text or to separate sentences so they can be 
more easily reordered in the future.

**3. Emphasis**

The third cell (labeled "***Emphasis***") illustrates how to make text italicized or bold.  Double click on the cell (to view the source text).  
* Text can be italicized by surrounding it by single asterisks, like `*italicize text*`: *italicize text*
* Similarly, text can be bolded by surrounding it by double asterisks, like `**bold text**`: **bold text**
* Text can be both italicized and bolded by surrounding it with triple asterisks, like `***bold and italics***`: ***bold and italics***

**4. Bulleted and Numbered Lists**

The fourth cell illustrates how to make bulleted and numbered lists.

**Bulleted lists** can be created by starting a line with an asterisk and a space, followed by the text of the bulleted item. Bulleted sub-lists can be created by tab-indenting a bulleted list under a bulleted item. For example,

<pre>
* Item 1
    * Item 1.1
    * Item 1.2
*Item 2
</pre>

formats as
* Item 1
    * Item 1.1
    * Item 1.2
*Item 2

**Numbered lists** can be created by starting a line with a number, a period, and a space, followed by the item to be numbered. *Note that the first number you use in a sequence of numbered items will determine the starting point for numbering, but later values are ignored. It is a good habit in most cases to use 1 for every numbered item because then you can rearrange them via cut and pasted without worrying about upsetting the overall list numbering.*  Numbered sub-lists can be created by tab-indenting a numbered list under a numbered item. For example,

<pre>
1. Item 1
    1. Item 1.1
    1. Item 1.2
3. Item 2
</pre>
formats as
1. Item 1
    1. Item 1.1
    1. Item 1.2
3. Item 2

**5. Links and images**

The fifth cell gives an example of a link and an image.

**Links** are easily created by putting the link text in square brackets, followed by the link URL in parentheses, like:
```
[Example link](http://google.com)
```
which is rendered as 

[Example link](http://google.com)

**Images** are entered in a very similar way to URLs. Just put an exclamation point (!) before the square brackets. The text in the square brackets will be used as the "alt text", which is used by screen readers or displayed when hovering the mouse over the image. Images can also be inserted by dragging them from your file manager into a cell. After the Markdown code is inserted, you can edit the alt-text to something more meaningful.

**6. Mathematics**

The sixth cell (labeled "Mathematics") illustrates formatted mathematics.  
Markdown in Jupyter supports sophisticated formatting of mathematics using $\LaTeX$ (pronounced *lay tek*) notation.  
For inline equations (those that will appear in-line with text, include the $\LaTeX$ notation between dollar signs, like `$\sin^2 x$` renders as $\sin^2 x$. 
Longer equations should be displayed separate from the text and can be created by enclosing them between pairs of dollar signs. For example,
<pre>
$$
\int_{0}^{\infty} e^{-x}~dx = 1
$$
</pre>
is rendered as
$$
\int_{0}^{\infty} e^{-x}~dx = 1
$$

**6. Other Markdown formatting**

Markdown has many other features that we will not cover, such as horizontal rules, block quotes, syntax highlighting, and tables.
A good reference for Markdown syntax is
[Markdown Guide(https://www.markdownguide.org/extended-syntax/)](https://www.markdownguide.org/extended-syntax/)
