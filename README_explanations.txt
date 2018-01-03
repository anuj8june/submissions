Task Sections
..............................
..............................

Python
..............................

(1) 
There are two lists given L1 and L2. To find common list just iterate through L1 and check if that value is in L2. This will give a list of common elements.

(2)
To find non common elements in the list, combine both L1 and L2 to make L3. Iterate through L3 and compare with OR condition so that the element is exclusive only to one list.


Javascript
.............................

By iteration compared each value of array with value to be removed that  is zero and used splice function to remove that value.



Analysis
..............................
..............................

Use case 1 - National Achievement Survey
........................................

Full data cleanup and data transformation is explained step by step in Docs/analysis.ipynb

analysis.ipynb was used to generate 3 json files for 3 questions asked in Use cases to minimize the computing load on page and to render fast pages.

These json files are read and then plotted on HTML canvas
