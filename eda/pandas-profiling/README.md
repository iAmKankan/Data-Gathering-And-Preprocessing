## Index
![Dark](https://user-images.githubusercontent.com/12748752/126914729-75e0fed5-fdaa-4216-81c8-719340e80694.png)



<p align="center"> <img src="https://ydataai.github.io/pandas-profiling/docs/assets/logo_header.png" width=30%/>
</p>

Primary goal is to provide a one-line **Exploratory Data Analysis (EDA)** experience in a consistent and fast solution. Like pandas **_df.describe()_** function, that is so handy, pandas-profiling delivers an extended analysis of a **DataFrame** while alllowing the data analysis to be exported in different formats such as **html** and **json**.

### Installation
![Light](https://user-images.githubusercontent.com/12748752/126914730-b5b13ba9-4d20-4ebf-b0ed-231af4c8b984.png)

```Python
pip install -U pandas-profiling
```

### Quickstart
```Python
import numpy as np
import pandas as pd
from pandas_profiling import ProfileReport

df = pd.DataFrame(np.random.rand(100, 5), columns=["a", "b", "c", "d", "e"])
```
#### To generate the standard profiling report, merely run:

```Python
profile = ProfileReport(df, title="Pandas Profiling Report")
```

### Using inside Jupyter Notebooks
![Light](https://user-images.githubusercontent.com/12748752/126914730-b5b13ba9-4d20-4ebf-b0ed-231af4c8b984.png)

There are two interfaces to consume the report inside a _Jupyter notebook_ (see animations below): through _widgets_ and through an _embedded HTML report_.


<p align="center"> <img src="https://pandas-profiling.ydata.ai/docs/master/_images/widgets.gif" width=70%/>
</p>

This is achieved by simply displaying the report as a set of widgets. In a Jupyter Notebook, run:

```Python
profile.to_widgets()
```

The HTML report can be directly embedded in a cell in a similar fashion:

```Python
profile.to_notebook_iframe()
```


## Exporting the report to a file
To generate a HTML report file, save the ProfileReport to an object and use the to_file() function:

```Python
profile.to_file("your_report.html")
```

Alternatively, the report’s data can be obtained as a JSON file:

```Python
# As a JSON string
json_data = profile.to_json()
# As a file
profile.to_file("your_report.json")
```









## Reference
![Dark](https://user-images.githubusercontent.com/12748752/126914729-75e0fed5-fdaa-4216-81c8-719340e80694.png)
* [Doc](https://pandas-profiling.ydata.ai/docs/master/pages/getting_started/overview.html#key-features)
