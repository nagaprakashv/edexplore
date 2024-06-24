# EDExplore
A simple widget for interactive EDA / QA for those who use Pandas in Jupyter Notebook.       
    
<img src="https://github.com/nagapv/edexplore/assets/13671867/9ddef93e-433f-40f1-b629-886b8b00a333" width=40% height=40%>     
     
https://github.com/nagapv/edexplore/ | https://pypi.org/project/edexplore/    
         
***   

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
         
<img src="https://github.com/nagapv/edexplore/assets/13671867/9f0a94dd-b308-4a13-9ff9-14dc9bbf5bfe" width=100% height=100%>    
           
***   
Special thanks to Ashwin Rajeev, who introduced IPyWidgets to me long back!
***
Copyright (c) 2024 Nagaprakash Venkatesan , 
[FreeBSD License](https://opensource.org/license/BSD-2-Clause)
