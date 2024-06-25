# EDExplore
A simple widget for interactive EDA / QA for those who use Pandas in Jupyter Notebook.     
    
<img src="https://github.com/nagapv/edexplore/assets/13671867/9ddef93e-433f-40f1-b629-886b8b00a333">     

***   
[https://github.com/nagapv/edexplore/](https://github.com/nagapv/edexplore/) | [https://pypi.org/project/edexplore/](https://pypi.org/project/edexplore/)    
***    
     
## Hello World!    
Here is the new **_EDExplore_** for interactive EDA and QA.     

Many of us explore a lot of data in a given day, asking ourselves various questions and/or looking for insights. We end up using some functions or conditions repeatedly every hour, for each dataset, r.e.p.e.a.t.e.d.l.y! May it be exploring a new dataset, validating or verifying the quality, ensuring dataset integrity, etc. _Yes, you are in the right place_!
    
There are a few widgets / GUIs for Pandas (on Jupyter Notebooks) already out there. Compared to them, ***Interact*** in _EDExplore_ is neither fancy nor heavily loaded with features but a simple interactive function!    
        
That is being said, why EDExplore extension matters? Because -   
1) It simplifies the Pandas dataframe usage (even more)!   
2) Makes it easy to apply most common conditions.    
3) Helps combine multiple conditions without coding effort.   
4) Readable samples!    
5) Is a _plain_ interactive widget.    
    
The **_EDExplore_**  should make the EDA and QA processes more easy and let the analyst think of new and challenging tasks instead of what existing condition should be _written_ next to verify the data!    
    
Please share your feedback and help me improve it! You can write to me at npv3105 at outlook.com :)     
      
## How to install?
`python -m pip install edexplore`

If you want to do it locally:-    
After downloading / extracting the code, go to the directory (in command line) for installation:        
`python -m pip install .` OR `pip install .`   
     
At times, you may need to enable the ipywidgets notebook extension:    
`jupyter nbextension enable --py widgetsnbextension`           
     
## How to use?
`import pandas as pd`    
`from edexplore import interact`    
`df = pd.read_csv("xzy.csv")`     
`interact(df)`    
         
Here is the **[detailed reference](../docs/interact.ipynb)** with screenshots.
           
***
Copyright (c) 2024 Nagaprakash Venkatesan , 
[MIT License](https://github.com/nagapv/edexplore/blob/main/LICENSE)
