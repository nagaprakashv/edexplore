# ED Explore
A simple widget for interactive data exploration for those who use Pandas in Jupyter Notebook.    
    
![drawing - Copy](https://github.com/nagaprakashv/explore/assets/13671867/9e666fb5-4eb1-42c3-96e8-53b75f9eddac)       

***
Requirements: Pandas, Jupyter Notebook, and IPyWidgets.

## How to install?
Installing IPyWidgets:     
`pip install ipywidgets`   
or      
`conda install -c conda-forge ipywidgets`   

At times, you may need to enable the ipywidgets notebook extension:    
`jupyter nbextension enable --py widgetsnbextension`

After downloading / extracting the code, go to the directory (in command line) for installation:        
`pip install .`

## How to use?
`import pandas as pd`    
`from edexplore import interact`    
`df = pd.read_csv("xzy.csv")`     
`interact(df)`    
![2024-06-19_16-31](https://github.com/nagaprakashv/explore/assets/13671867/7cd53826-2cf0-41f4-a335-d59bf4fd0af2)


***
Special thanks to Ashwin Rajeev, who introduced IPyWidgets and kickstarted things to me!
***
Copyright (c) 2024 Nagaprakash Venkatesan , 
[FreeBSD License](https://opensource.org/license/BSD-2-Clause)
