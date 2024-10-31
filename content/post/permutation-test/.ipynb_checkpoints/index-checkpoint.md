---
title: Analyzing Disparity Between Users and Journalists Ratings
subtitle: Randomized Shuffling As My First Systematic Analysis
summary: Randomized Shuffling As My First Systematic Analysis
#authors:
#- admin
tags: []
categories: []
date: "2019-02-05T00:00:00Z"
#lastMod: "2019-09-05T00:00:00Z"
featured: true
draft: true

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
image:
  caption: ""
  focal_point: ""
---


## Table of Contents
- [Read Data](#read-data)

### Import Libraries and Local Files


```python
# 3rd-party libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# local-files
import jsonRW as jsRW
import graphs.pie as pieGraph
import graphs.categoricalHeatmap as categoricalHeatmapGraph
import graphs.groupedBars as groupedBarsGraph
import graphs.histogramPdf as histogramPdfGraph
import transformations.transformations as transform
import transformations.discretizeIntoCategories as discIntCat
import statTests.permutationTest as permTest
```

___

## Read Data

### Read Local JSON Data Into a Pandas Dataframe


```python
# a map from each platform to its corresponding dataframe
platform_df = {}
# platform names and their corresonding data file names
platformsNames = ['ps4', 'xbox', 'switch', 'pc']
filesNames = ['ps4.csv', 'xbox.csv', 'switch.csv', 'pc.csv']

# for each platform, then 
for name in platformsNames:
    # read its local json file
    metacritic_list = jsRW.readJson(name)
    # parse it as pandas dataframe, then map platform name to it
    platform_df[name] = pd.DataFrame(metacritic_list)
```


```python
# take a look at a dataframe
platform_df['ps4']
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>critic_rating</th>
      <th>id</th>
      <th>release_date</th>
      <th>title</th>
      <th>user_rating</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>91</td>
      <td>1</td>
      <td>Jul  2, 2019</td>
      <td>final fantasy xiv: shadowbringers</td>
      <td>8.3</td>
    </tr>
    <tr>
      <th>1</th>
      <td>91</td>
      <td>2</td>
      <td>Feb 26, 2019</td>
      <td>nier: automata - game of the yorha edition</td>
      <td>8.5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>91</td>
      <td>3</td>
      <td>Jan 25, 2019</td>
      <td>resident evil 2</td>
      <td>8.8</td>
    </tr>
    <tr>
      <th>3</th>
      <td>90</td>
      <td>4</td>
      <td>Mar 22, 2019</td>
      <td>sekiro: shadows die twice</td>
      <td>7.9</td>
    </tr>
    <tr>
      <th>4</th>
      <td>89</td>
      <td>5</td>
      <td>Sep  6, 2019</td>
      <td>monster hunter: world - iceborne</td>
      <td>8.4</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>335</th>
      <td>39</td>
      <td>336</td>
      <td>Oct 15, 2019</td>
      <td>zombieland: double tap - road trip</td>
      <td>4.6</td>
    </tr>
    <tr>
      <th>336</th>
      <td>37</td>
      <td>337</td>
      <td>Mar  5, 2019</td>
      <td>left alive</td>
      <td>8.3</td>
    </tr>
    <tr>
      <th>337</th>
      <td>36</td>
      <td>338</td>
      <td>Mar  5, 2019</td>
      <td>eternity: the last unicorn</td>
      <td>3.8</td>
    </tr>
    <tr>
      <th>338</th>
      <td>31</td>
      <td>339</td>
      <td>May 30, 2019</td>
      <td>dayz</td>
      <td>2.8</td>
    </tr>
    <tr>
      <th>339</th>
      <td>31</td>
      <td>340</td>
      <td>Mar 29, 2019</td>
      <td>where the bees make honey</td>
      <td>3.2</td>
    </tr>
  </tbody>
</table>
<p>340 rows × 5 columns</p>
</div>



___

## Data Cleansing


```python
# drop unneeded columns and re-organize them 
for name in platformsNames:
    platform_df[name] = platform_df[name][['title', 'user_rating', 'critic_rating']]
```


```python
# take a look at a dataframe, again
platform_df['ps4']
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>title</th>
      <th>user_rating</th>
      <th>critic_rating</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>final fantasy xiv: shadowbringers</td>
      <td>8.3</td>
      <td>91</td>
    </tr>
    <tr>
      <th>1</th>
      <td>nier: automata - game of the yorha edition</td>
      <td>8.5</td>
      <td>91</td>
    </tr>
    <tr>
      <th>2</th>
      <td>resident evil 2</td>
      <td>8.8</td>
      <td>91</td>
    </tr>
    <tr>
      <th>3</th>
      <td>sekiro: shadows die twice</td>
      <td>7.9</td>
      <td>90</td>
    </tr>
    <tr>
      <th>4</th>
      <td>monster hunter: world - iceborne</td>
      <td>8.4</td>
      <td>89</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>335</th>
      <td>zombieland: double tap - road trip</td>
      <td>4.6</td>
      <td>39</td>
    </tr>
    <tr>
      <th>336</th>
      <td>left alive</td>
      <td>8.3</td>
      <td>37</td>
    </tr>
    <tr>
      <th>337</th>
      <td>eternity: the last unicorn</td>
      <td>3.8</td>
      <td>36</td>
    </tr>
    <tr>
      <th>338</th>
      <td>dayz</td>
      <td>2.8</td>
      <td>31</td>
    </tr>
    <tr>
      <th>339</th>
      <td>where the bees make honey</td>
      <td>3.2</td>
      <td>31</td>
    </tr>
  </tbody>
</table>
<p>340 rows × 3 columns</p>
</div>



#### remarks
- user_rating must be on the same scale as critic_rating
- data types need to be checked


```python
# check columns data types
platform_df['ps4'].dtypes
```




    title            object
    user_rating      object
    critic_rating    object
    dtype: object




```python
# convert ratings into a numeric value
#      error ahead!
#df['user_rating'] = pd.to_numeric(df['user_rating'])
#df['critic_rating'] = pd.to_numeric(df['critic_rating'])
```


```python
# get rid of user_rating with value equal to "tbd"

# for each platform
for name in platformsNames:
    # get its dataframe
    df = platform_df[name]
    # get index set in which user_rating is tbd, a non-numeric value
    tbdIndex = df[df['user_rating']=="tbd"].index
    # drop rows specified by indices in which user_rating is tbd
    df = df.drop(labels=tbdIndex, axis='index')
    # set updated data to platform_df
    platform_df[name] = df
```


```python
# convert ratings to a numeric type

# for each platform
for name in platformsNames:
    # get its dataframe
    df = platform_df[name]
    # convert to a numeric type
    df['user_rating'] = pd.to_numeric(df['user_rating'])
    df['critic_rating'] = pd.to_numeric(df['critic_rating'])
    # set updated data to platform_df
    platform_df[name] = df
```


```python
# check data types
platform_df['ps4'].dtypes
```




    title             object
    user_rating      float64
    critic_rating      int64
    dtype: object




```python
# user ratings must be on the same scale as critics ratings, so we multiply them by 10

# for each platform
for platformName in platform_df:
    platform_df[platformName]['user_rating'] = platform_df[platformName]['user_rating'] * 10
```


```python
platform_df['ps4']
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>title</th>
      <th>user_rating</th>
      <th>critic_rating</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>final fantasy xiv: shadowbringers</td>
      <td>83.0</td>
      <td>91</td>
    </tr>
    <tr>
      <th>1</th>
      <td>nier: automata - game of the yorha edition</td>
      <td>85.0</td>
      <td>91</td>
    </tr>
    <tr>
      <th>2</th>
      <td>resident evil 2</td>
      <td>88.0</td>
      <td>91</td>
    </tr>
    <tr>
      <th>3</th>
      <td>sekiro: shadows die twice</td>
      <td>79.0</td>
      <td>90</td>
    </tr>
    <tr>
      <th>4</th>
      <td>monster hunter: world - iceborne</td>
      <td>84.0</td>
      <td>89</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>335</th>
      <td>zombieland: double tap - road trip</td>
      <td>46.0</td>
      <td>39</td>
    </tr>
    <tr>
      <th>336</th>
      <td>left alive</td>
      <td>83.0</td>
      <td>37</td>
    </tr>
    <tr>
      <th>337</th>
      <td>eternity: the last unicorn</td>
      <td>38.0</td>
      <td>36</td>
    </tr>
    <tr>
      <th>338</th>
      <td>dayz</td>
      <td>28.0</td>
      <td>31</td>
    </tr>
    <tr>
      <th>339</th>
      <td>where the bees make honey</td>
      <td>32.0</td>
      <td>31</td>
    </tr>
  </tbody>
</table>
<p>310 rows × 3 columns</p>
</div>



___

### Optional: Store Cleaed Data Into a CSV File


```python
"""
# store data to a csv file

# for each platform
for platformName in platform_df:
    # save to a csv file
    platform_df[platformName].to_csv(str(platformName)+'.csv')
"""
```




    "\n# store data to a csv file\n\n# for each platform\nfor platformName in platform_df:\n    # save to a csv file\n    platform_df[platformName].to_csv(str(platformName)+'.csv')\n"



___

### Compute Disparity (Difference) Between Users and Critics


```python
# for each platform
for name in platform_df:
    # get dataframe of the platform
    df = platform_df[name]
    # for each record, compute distance between user and critic ratings, then set result to a new column
    df['userCritic_difference'] = df.apply(lambda x: abs(x['user_rating']-x['critic_rating']), axis=1)
    # assign updates back to our dataframe
    platform_df[name] = df
```


```python
platform_df['ps4']
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>title</th>
      <th>user_rating</th>
      <th>critic_rating</th>
      <th>userCritic_difference</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>final fantasy xiv: shadowbringers</td>
      <td>83.0</td>
      <td>91</td>
      <td>8.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>nier: automata - game of the yorha edition</td>
      <td>85.0</td>
      <td>91</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>resident evil 2</td>
      <td>88.0</td>
      <td>91</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>sekiro: shadows die twice</td>
      <td>79.0</td>
      <td>90</td>
      <td>11.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>monster hunter: world - iceborne</td>
      <td>84.0</td>
      <td>89</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>335</th>
      <td>zombieland: double tap - road trip</td>
      <td>46.0</td>
      <td>39</td>
      <td>7.0</td>
    </tr>
    <tr>
      <th>336</th>
      <td>left alive</td>
      <td>83.0</td>
      <td>37</td>
      <td>46.0</td>
    </tr>
    <tr>
      <th>337</th>
      <td>eternity: the last unicorn</td>
      <td>38.0</td>
      <td>36</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>338</th>
      <td>dayz</td>
      <td>28.0</td>
      <td>31</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>339</th>
      <td>where the bees make honey</td>
      <td>32.0</td>
      <td>31</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>
<p>310 rows × 4 columns</p>
</div>



### Discretize Disparity Computed Earlier Into Categories


```python
# categories names and their corresponding intervals
# category at location x corresponds to interval equal or greater than intervals location x and less than location x + 1
# except for last category, has no end
categories = pd.Series(["low", "moderate", "high", "very_high", "extremely_high"])
intervals_categories = [0, 20, 30, 40, 50]
```


```python
# compute categories as defined earlier

# loop on platforms
for platformName in platform_df:
    # get dataframe of the platform
    df = platform_df[platformName]
    # add category based on difference just defined
    df['difference_category'] = df.apply(discIntCat.numToCat, axis=1, args=('userCritic_difference', categories, intervals_categories))
    
    # let categories be recognized by pandas
    df['difference_category'] = df['difference_category'].astype("category")
    # re-order categories
    df['difference_category'] = df['difference_category'].cat.set_categories(categories, ordered=True)
    
    
    # assign back to our dataframe
    platform_df[platformName] = df
```


```python
# take a look after our new columns added
platform_df['ps4']
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>title</th>
      <th>user_rating</th>
      <th>critic_rating</th>
      <th>userCritic_difference</th>
      <th>difference_category</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>final fantasy xiv: shadowbringers</td>
      <td>83.0</td>
      <td>91</td>
      <td>8.0</td>
      <td>low</td>
    </tr>
    <tr>
      <th>1</th>
      <td>nier: automata - game of the yorha edition</td>
      <td>85.0</td>
      <td>91</td>
      <td>6.0</td>
      <td>low</td>
    </tr>
    <tr>
      <th>2</th>
      <td>resident evil 2</td>
      <td>88.0</td>
      <td>91</td>
      <td>3.0</td>
      <td>low</td>
    </tr>
    <tr>
      <th>3</th>
      <td>sekiro: shadows die twice</td>
      <td>79.0</td>
      <td>90</td>
      <td>11.0</td>
      <td>low</td>
    </tr>
    <tr>
      <th>4</th>
      <td>monster hunter: world - iceborne</td>
      <td>84.0</td>
      <td>89</td>
      <td>5.0</td>
      <td>low</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>335</th>
      <td>zombieland: double tap - road trip</td>
      <td>46.0</td>
      <td>39</td>
      <td>7.0</td>
      <td>low</td>
    </tr>
    <tr>
      <th>336</th>
      <td>left alive</td>
      <td>83.0</td>
      <td>37</td>
      <td>46.0</td>
      <td>very_high</td>
    </tr>
    <tr>
      <th>337</th>
      <td>eternity: the last unicorn</td>
      <td>38.0</td>
      <td>36</td>
      <td>2.0</td>
      <td>low</td>
    </tr>
    <tr>
      <th>338</th>
      <td>dayz</td>
      <td>28.0</td>
      <td>31</td>
      <td>3.0</td>
      <td>low</td>
    </tr>
    <tr>
      <th>339</th>
      <td>where the bees make honey</td>
      <td>32.0</td>
      <td>31</td>
      <td>1.0</td>
      <td>low</td>
    </tr>
  </tbody>
</table>
<p>310 rows × 5 columns</p>
</div>



### Sort According to Disparity Between Users and Critics


```python
# for each platform
for platformName in platform_df:
    # get platform dataframe
    df = platform_df[platformName]
    # sort it by userCritic_difference
    df = df.sort_values(axis=0, by='userCritic_difference', ascending=False)
    # assign sorted dataframe back to our dataframe
    platform_df[platformName] = df
```

### Basic Stats on Disparity Between Users and Critics


```python
# for each platform
for platformName in platform_df:
    # print platform name
    print("\n", "on ", platformName)
    # show basic stat
    print(platform_df[platformName]['userCritic_difference'].describe())
```

    
     on  ps4
    count    310.000000
    mean      15.893548
    std       13.074530
    min        0.000000
    25%        5.000000
    50%       12.000000
    75%       23.000000
    max       69.000000
    Name: userCritic_difference, dtype: float64
    
     on  xbox
    count    186.000000
    mean      14.801075
    std       13.192881
    min        0.000000
    25%        5.000000
    50%       11.000000
    75%       21.000000
    max       69.000000
    Name: userCritic_difference, dtype: float64
    
     on  switch
    count    364.000000
    mean       6.876374
    std        8.741062
    min        0.000000
    25%        1.750000
    50%        4.000000
    75%        9.000000
    max       58.000000
    Name: userCritic_difference, dtype: float64
    
     on  pc
    count    327.000000
    mean      13.547401
    std       12.322982
    min        0.000000
    25%        4.000000
    50%       10.000000
    75%       19.000000
    max       63.000000
    Name: userCritic_difference, dtype: float64


___

## Categories Size

### Platform x Category 2D Sizes Dataframe


```python
platform_category_size = transform.map_columnCount(platform_df, 'difference_category')
```


```python
platform_category_size
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>low</th>
      <th>moderate</th>
      <th>high</th>
      <th>very_high</th>
      <th>extremely_high</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>ps4</th>
      <td>211</td>
      <td>52</td>
      <td>33</td>
      <td>9</td>
      <td>5</td>
    </tr>
    <tr>
      <th>xbox</th>
      <td>131</td>
      <td>31</td>
      <td>14</td>
      <td>5</td>
      <td>5</td>
    </tr>
    <tr>
      <th>switch</th>
      <td>334</td>
      <td>19</td>
      <td>6</td>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>pc</th>
      <td>249</td>
      <td>43</td>
      <td>22</td>
      <td>8</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>



### Category x Platform 2D Sizes Dataframe


```python
category_platform_size = platform_category_size.transpose()
```


```python
category_platform_size
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ps4</th>
      <th>xbox</th>
      <th>switch</th>
      <th>pc</th>
    </tr>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>low</th>
      <td>211</td>
      <td>131</td>
      <td>334</td>
      <td>249</td>
    </tr>
    <tr>
      <th>moderate</th>
      <td>52</td>
      <td>31</td>
      <td>19</td>
      <td>43</td>
    </tr>
    <tr>
      <th>high</th>
      <td>33</td>
      <td>14</td>
      <td>6</td>
      <td>22</td>
    </tr>
    <tr>
      <th>very_high</th>
      <td>9</td>
      <td>5</td>
      <td>2</td>
      <td>8</td>
    </tr>
    <tr>
      <th>extremely_high</th>
      <td>5</td>
      <td>5</td>
      <td>3</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>




```python
category_platform_size.loc['low', 'ps4']
```




    211



___

## Graphing Disparity Between Users and Critics

### Pie Graph


```python
for columnName in category_platform_size:
    platSeries = category_platform_size[columnName]
    platName = platSeries.name
    pieGraph.showPieGraph(platSeries, platName + ' categories percentages', 6, 6)
```


![png](index_files/index_48_0.png)



![png](index_files/index_48_1.png)



![png](index_files/index_48_2.png)



![png](index_files/index_48_3.png)


### Grouped Bar


```python
groupedBarsGraph.showGroupedBars(platform_category_size, platformsNames, 'categories size', 'categories size by platform')
```


![png](index_files/index_50_0.png)


### Categorical Heatmap


```python
categoricalHeatmapGraph.showCategoricalHeatmap(8, 8, category_platform_size, "categories sizes among platforms")
```


![png](index_files/index_52_0.png)


### Maximum Disparity Between Users and Critics Ratings


```python
platform_df['ps4'].head(20)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>title</th>
      <th>user_rating</th>
      <th>critic_rating</th>
      <th>userCritic_difference</th>
      <th>difference_category</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>93</th>
      <td>nba 2k20</td>
      <td>9.0</td>
      <td>78</td>
      <td>69.0</td>
      <td>extremely_high</td>
    </tr>
    <tr>
      <th>82</th>
      <td>fifa 20</td>
      <td>11.0</td>
      <td>79</td>
      <td>68.0</td>
      <td>extremely_high</td>
    </tr>
    <tr>
      <th>116</th>
      <td>madden nfl 20</td>
      <td>16.0</td>
      <td>76</td>
      <td>60.0</td>
      <td>extremely_high</td>
    </tr>
    <tr>
      <th>79</th>
      <td>gravity ghost: deluxe edition</td>
      <td>27.0</td>
      <td>79</td>
      <td>52.0</td>
      <td>extremely_high</td>
    </tr>
    <tr>
      <th>172</th>
      <td>simulacra</td>
      <td>21.0</td>
      <td>72</td>
      <td>51.0</td>
      <td>extremely_high</td>
    </tr>
    <tr>
      <th>36</th>
      <td>mortal kombat 11</td>
      <td>33.0</td>
      <td>82</td>
      <td>49.0</td>
      <td>very_high</td>
    </tr>
    <tr>
      <th>58</th>
      <td>call of duty: modern warfare</td>
      <td>32.0</td>
      <td>80</td>
      <td>48.0</td>
      <td>very_high</td>
    </tr>
    <tr>
      <th>199</th>
      <td>hitman hd enhanced collection</td>
      <td>21.0</td>
      <td>69</td>
      <td>48.0</td>
      <td>very_high</td>
    </tr>
    <tr>
      <th>217</th>
      <td>mxgp 2019</td>
      <td>20.0</td>
      <td>68</td>
      <td>48.0</td>
      <td>very_high</td>
    </tr>
    <tr>
      <th>224</th>
      <td>we. the revolution</td>
      <td>20.0</td>
      <td>67</td>
      <td>47.0</td>
      <td>very_high</td>
    </tr>
    <tr>
      <th>218</th>
      <td>giga wrecker alt.</td>
      <td>20.0</td>
      <td>67</td>
      <td>47.0</td>
      <td>very_high</td>
    </tr>
    <tr>
      <th>336</th>
      <td>left alive</td>
      <td>83.0</td>
      <td>37</td>
      <td>46.0</td>
      <td>very_high</td>
    </tr>
    <tr>
      <th>65</th>
      <td>dauntless</td>
      <td>34.0</td>
      <td>80</td>
      <td>46.0</td>
      <td>very_high</td>
    </tr>
    <tr>
      <th>285</th>
      <td>darksiders iii: keepers of the void</td>
      <td>18.0</td>
      <td>59</td>
      <td>41.0</td>
      <td>very_high</td>
    </tr>
    <tr>
      <th>286</th>
      <td>attack of the earthlings</td>
      <td>20.0</td>
      <td>59</td>
      <td>39.0</td>
      <td>high</td>
    </tr>
    <tr>
      <th>299</th>
      <td>the lego movie 2 videogame</td>
      <td>18.0</td>
      <td>57</td>
      <td>39.0</td>
      <td>high</td>
    </tr>
    <tr>
      <th>275</th>
      <td>asterix &amp; obelix xxl 3: the crystal menhir</td>
      <td>21.0</td>
      <td>60</td>
      <td>39.0</td>
      <td>high</td>
    </tr>
    <tr>
      <th>68</th>
      <td>lonely mountains: downhill</td>
      <td>41.0</td>
      <td>80</td>
      <td>39.0</td>
      <td>high</td>
    </tr>
    <tr>
      <th>256</th>
      <td>a knight's quest</td>
      <td>24.0</td>
      <td>63</td>
      <td>39.0</td>
      <td>high</td>
    </tr>
    <tr>
      <th>21</th>
      <td>far: lone sails</td>
      <td>44.0</td>
      <td>83</td>
      <td>39.0</td>
      <td>high</td>
    </tr>
  </tbody>
</table>
</div>




```python
platform_df['xbox'].head(20)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>title</th>
      <th>user_rating</th>
      <th>critic_rating</th>
      <th>userCritic_difference</th>
      <th>difference_category</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>70</th>
      <td>nba 2k20</td>
      <td>11.0</td>
      <td>80</td>
      <td>69.0</td>
      <td>extremely_high</td>
    </tr>
    <tr>
      <th>74</th>
      <td>fifa 20</td>
      <td>11.0</td>
      <td>79</td>
      <td>68.0</td>
      <td>extremely_high</td>
    </tr>
    <tr>
      <th>75</th>
      <td>madden nfl 20</td>
      <td>20.0</td>
      <td>79</td>
      <td>59.0</td>
      <td>extremely_high</td>
    </tr>
    <tr>
      <th>9</th>
      <td>mortal kombat 11</td>
      <td>31.0</td>
      <td>86</td>
      <td>55.0</td>
      <td>extremely_high</td>
    </tr>
    <tr>
      <th>115</th>
      <td>timespinner</td>
      <td>23.0</td>
      <td>74</td>
      <td>51.0</td>
      <td>extremely_high</td>
    </tr>
    <tr>
      <th>169</th>
      <td>wolfenstein: youngblood</td>
      <td>20.0</td>
      <td>68</td>
      <td>48.0</td>
      <td>very_high</td>
    </tr>
    <tr>
      <th>57</th>
      <td>call of duty: modern warfare</td>
      <td>37.0</td>
      <td>81</td>
      <td>44.0</td>
      <td>very_high</td>
    </tr>
    <tr>
      <th>10</th>
      <td>nhl 20</td>
      <td>42.0</td>
      <td>85</td>
      <td>43.0</td>
      <td>very_high</td>
    </tr>
    <tr>
      <th>143</th>
      <td>disney classic games: aladdin and the lion king</td>
      <td>30.0</td>
      <td>72</td>
      <td>42.0</td>
      <td>very_high</td>
    </tr>
    <tr>
      <th>24</th>
      <td>far: lone sails</td>
      <td>43.0</td>
      <td>84</td>
      <td>41.0</td>
      <td>very_high</td>
    </tr>
    <tr>
      <th>45</th>
      <td>dauntless</td>
      <td>43.0</td>
      <td>82</td>
      <td>39.0</td>
      <td>high</td>
    </tr>
    <tr>
      <th>106</th>
      <td>far cry new dawn</td>
      <td>37.0</td>
      <td>75</td>
      <td>38.0</td>
      <td>high</td>
    </tr>
    <tr>
      <th>76</th>
      <td>grid</td>
      <td>45.0</td>
      <td>79</td>
      <td>34.0</td>
      <td>high</td>
    </tr>
    <tr>
      <th>248</th>
      <td>wwe 2k20</td>
      <td>11.0</td>
      <td>45</td>
      <td>34.0</td>
      <td>high</td>
    </tr>
    <tr>
      <th>92</th>
      <td>assassin's creed iii remastered</td>
      <td>43.0</td>
      <td>77</td>
      <td>34.0</td>
      <td>high</td>
    </tr>
    <tr>
      <th>160</th>
      <td>genesis alpha one</td>
      <td>35.0</td>
      <td>69</td>
      <td>34.0</td>
      <td>high</td>
    </tr>
    <tr>
      <th>17</th>
      <td>trials rising</td>
      <td>52.0</td>
      <td>85</td>
      <td>33.0</td>
      <td>high</td>
    </tr>
    <tr>
      <th>19</th>
      <td>crash team racing: nitro-fueled</td>
      <td>51.0</td>
      <td>84</td>
      <td>33.0</td>
      <td>high</td>
    </tr>
    <tr>
      <th>204</th>
      <td>narcos: rise of the cartels</td>
      <td>30.0</td>
      <td>63</td>
      <td>33.0</td>
      <td>high</td>
    </tr>
    <tr>
      <th>7</th>
      <td>fell seal: arbiter's mark</td>
      <td>54.0</td>
      <td>86</td>
      <td>32.0</td>
      <td>high</td>
    </tr>
  </tbody>
</table>
</div>




```python
platform_df['pc'].head(20)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>title</th>
      <th>user_rating</th>
      <th>critic_rating</th>
      <th>userCritic_difference</th>
      <th>difference_category</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>203</th>
      <td>nba 2k20</td>
      <td>11.0</td>
      <td>74</td>
      <td>63.0</td>
      <td>extremely_high</td>
    </tr>
    <tr>
      <th>234</th>
      <td>fifa 20</td>
      <td>11.0</td>
      <td>72</td>
      <td>61.0</td>
      <td>extremely_high</td>
    </tr>
    <tr>
      <th>237</th>
      <td>madden nfl 20</td>
      <td>12.0</td>
      <td>72</td>
      <td>60.0</td>
      <td>extremely_high</td>
    </tr>
    <tr>
      <th>77</th>
      <td>call of duty: modern warfare</td>
      <td>25.0</td>
      <td>81</td>
      <td>56.0</td>
      <td>extremely_high</td>
    </tr>
    <tr>
      <th>48</th>
      <td>mortal kombat 11</td>
      <td>27.0</td>
      <td>82</td>
      <td>55.0</td>
      <td>extremely_high</td>
    </tr>
    <tr>
      <th>279</th>
      <td>hearthstone: heroes of warcraft - saviors of u...</td>
      <td>19.0</td>
      <td>68</td>
      <td>49.0</td>
      <td>very_high</td>
    </tr>
    <tr>
      <th>19</th>
      <td>the sims 4: realm of magic</td>
      <td>37.0</td>
      <td>85</td>
      <td>48.0</td>
      <td>very_high</td>
    </tr>
    <tr>
      <th>264</th>
      <td>wolfenstein: youngblood</td>
      <td>22.0</td>
      <td>69</td>
      <td>47.0</td>
      <td>very_high</td>
    </tr>
    <tr>
      <th>383</th>
      <td>left alive</td>
      <td>86.0</td>
      <td>40</td>
      <td>46.0</td>
      <td>very_high</td>
    </tr>
    <tr>
      <th>96</th>
      <td>bury me, my love</td>
      <td>34.0</td>
      <td>80</td>
      <td>46.0</td>
      <td>very_high</td>
    </tr>
    <tr>
      <th>1</th>
      <td>red dead redemption 2</td>
      <td>48.0</td>
      <td>93</td>
      <td>45.0</td>
      <td>very_high</td>
    </tr>
    <tr>
      <th>235</th>
      <td>oninaki</td>
      <td>31.0</td>
      <td>72</td>
      <td>41.0</td>
      <td>very_high</td>
    </tr>
    <tr>
      <th>47</th>
      <td>the sims 4: discover university</td>
      <td>41.0</td>
      <td>82</td>
      <td>41.0</td>
      <td>very_high</td>
    </tr>
    <tr>
      <th>360</th>
      <td>wolfenstein: cyberpilot</td>
      <td>15.0</td>
      <td>54</td>
      <td>39.0</td>
      <td>high</td>
    </tr>
    <tr>
      <th>187</th>
      <td>assassin's creed iii remastered</td>
      <td>36.0</td>
      <td>75</td>
      <td>39.0</td>
      <td>high</td>
    </tr>
    <tr>
      <th>181</th>
      <td>defector</td>
      <td>36.0</td>
      <td>75</td>
      <td>39.0</td>
      <td>high</td>
    </tr>
    <tr>
      <th>68</th>
      <td>the elder scrolls online: dragonhold</td>
      <td>42.0</td>
      <td>81</td>
      <td>39.0</td>
      <td>high</td>
    </tr>
    <tr>
      <th>130</th>
      <td>surviving mars: green planet</td>
      <td>40.0</td>
      <td>78</td>
      <td>38.0</td>
      <td>high</td>
    </tr>
    <tr>
      <th>28</th>
      <td>dirt rally 2.0</td>
      <td>46.0</td>
      <td>84</td>
      <td>38.0</td>
      <td>high</td>
    </tr>
    <tr>
      <th>150</th>
      <td>plants vs. zombies: battle for neighborville</td>
      <td>40.0</td>
      <td>77</td>
      <td>37.0</td>
      <td>high</td>
    </tr>
  </tbody>
</table>
</div>




```python
platform_df['switch'].head(20)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>title</th>
      <th>user_rating</th>
      <th>critic_rating</th>
      <th>userCritic_difference</th>
      <th>difference_category</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>240</th>
      <td>nba 2k20</td>
      <td>15.0</td>
      <td>73</td>
      <td>58.0</td>
      <td>extremely_high</td>
    </tr>
    <tr>
      <th>66</th>
      <td>pillars of eternity: complete edition</td>
      <td>27.0</td>
      <td>82</td>
      <td>55.0</td>
      <td>extremely_high</td>
    </tr>
    <tr>
      <th>94</th>
      <td>pokemon sword / shield dual pack</td>
      <td>29.0</td>
      <td>80</td>
      <td>51.0</td>
      <td>extremely_high</td>
    </tr>
    <tr>
      <th>416</th>
      <td>catan</td>
      <td>18.0</td>
      <td>61</td>
      <td>43.0</td>
      <td>very_high</td>
    </tr>
    <tr>
      <th>123</th>
      <td>mortal kombat 11</td>
      <td>36.0</td>
      <td>78</td>
      <td>42.0</td>
      <td>very_high</td>
    </tr>
    <tr>
      <th>87</th>
      <td>pokemon shield</td>
      <td>44.0</td>
      <td>80</td>
      <td>36.0</td>
      <td>high</td>
    </tr>
    <tr>
      <th>91</th>
      <td>pokemon sword</td>
      <td>45.0</td>
      <td>80</td>
      <td>35.0</td>
      <td>high</td>
    </tr>
    <tr>
      <th>492</th>
      <td>fifa 20: legacy edition</td>
      <td>9.0</td>
      <td>43</td>
      <td>34.0</td>
      <td>high</td>
    </tr>
    <tr>
      <th>476</th>
      <td>devil may cry 2</td>
      <td>84.0</td>
      <td>50</td>
      <td>34.0</td>
      <td>high</td>
    </tr>
    <tr>
      <th>345</th>
      <td>giga wrecker alt.</td>
      <td>35.0</td>
      <td>67</td>
      <td>32.0</td>
      <td>high</td>
    </tr>
    <tr>
      <th>359</th>
      <td>wolfenstein: youngblood</td>
      <td>35.0</td>
      <td>65</td>
      <td>30.0</td>
      <td>high</td>
    </tr>
    <tr>
      <th>280</th>
      <td>mutant year zero: road to eden - deluxe edition</td>
      <td>42.0</td>
      <td>71</td>
      <td>29.0</td>
      <td>moderate</td>
    </tr>
    <tr>
      <th>237</th>
      <td>dauntless</td>
      <td>44.0</td>
      <td>73</td>
      <td>29.0</td>
      <td>moderate</td>
    </tr>
    <tr>
      <th>398</th>
      <td>rad rodgers: radical edition</td>
      <td>34.0</td>
      <td>62</td>
      <td>28.0</td>
      <td>moderate</td>
    </tr>
    <tr>
      <th>432</th>
      <td>farming simulator 20</td>
      <td>32.0</td>
      <td>59</td>
      <td>27.0</td>
      <td>moderate</td>
    </tr>
    <tr>
      <th>466</th>
      <td>whipseey and the lost atlas</td>
      <td>80.0</td>
      <td>54</td>
      <td>26.0</td>
      <td>moderate</td>
    </tr>
    <tr>
      <th>263</th>
      <td>my time at portia</td>
      <td>46.0</td>
      <td>72</td>
      <td>26.0</td>
      <td>moderate</td>
    </tr>
    <tr>
      <th>374</th>
      <td>deponia</td>
      <td>38.0</td>
      <td>64</td>
      <td>26.0</td>
      <td>moderate</td>
    </tr>
    <tr>
      <th>496</th>
      <td>car mechanic simulator</td>
      <td>15.0</td>
      <td>41</td>
      <td>26.0</td>
      <td>moderate</td>
    </tr>
    <tr>
      <th>499</th>
      <td>blades of time</td>
      <td>63.0</td>
      <td>38</td>
      <td>25.0</td>
      <td>moderate</td>
    </tr>
  </tbody>
</table>
</div>




```python
def searchforTitleInPlatform(platformStr_in, game_in):
    tem_df = platform_df[platformStr_in][platform_df[platformStr_in]['title'] == game_in]
    if len(tem_df) == 1:
        return tem_df.iloc[0]
    elif len(tem_df) == 0:
        return -1
    else:
        raise ValueError("unexpected no of games found")
        
searchforTitleInPlatform('xbox', "hitman hd enhanced collection")
```




    title                    hitman hd enhanced collection
    user_rating                                         46
    critic_rating                                       66
    userCritic_difference                               20
    difference_category                           moderate
    Name: 187, dtype: object



### Minimum Disparity Between Users and Critics


```python
platform_df['ps4'].tail(20)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>title</th>
      <th>user_rating</th>
      <th>critic_rating</th>
      <th>userCritic_difference</th>
      <th>difference_category</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>55</th>
      <td>five nights at freddy's vr: help wanted</td>
      <td>78.0</td>
      <td>80</td>
      <td>2.0</td>
      <td>low</td>
    </tr>
    <tr>
      <th>251</th>
      <td>metal wolf chaos xd</td>
      <td>62.0</td>
      <td>63</td>
      <td>1.0</td>
      <td>low</td>
    </tr>
    <tr>
      <th>201</th>
      <td>erica</td>
      <td>70.0</td>
      <td>69</td>
      <td>1.0</td>
      <td>low</td>
    </tr>
    <tr>
      <th>113</th>
      <td>blazing chrome</td>
      <td>75.0</td>
      <td>76</td>
      <td>1.0</td>
      <td>low</td>
    </tr>
    <tr>
      <th>207</th>
      <td>sea of solitude</td>
      <td>68.0</td>
      <td>69</td>
      <td>1.0</td>
      <td>low</td>
    </tr>
    <tr>
      <th>88</th>
      <td>blasphemous</td>
      <td>77.0</td>
      <td>78</td>
      <td>1.0</td>
      <td>low</td>
    </tr>
    <tr>
      <th>339</th>
      <td>where the bees make honey</td>
      <td>32.0</td>
      <td>31</td>
      <td>1.0</td>
      <td>low</td>
    </tr>
    <tr>
      <th>22</th>
      <td>bloodstained: ritual of the night</td>
      <td>84.0</td>
      <td>83</td>
      <td>1.0</td>
      <td>low</td>
    </tr>
    <tr>
      <th>317</th>
      <td>eden-tomorrow</td>
      <td>53.0</td>
      <td>52</td>
      <td>1.0</td>
      <td>low</td>
    </tr>
    <tr>
      <th>78</th>
      <td>knights and bikes</td>
      <td>78.0</td>
      <td>79</td>
      <td>1.0</td>
      <td>low</td>
    </tr>
    <tr>
      <th>38</th>
      <td>efootball pes 2020</td>
      <td>81.0</td>
      <td>82</td>
      <td>1.0</td>
      <td>low</td>
    </tr>
    <tr>
      <th>75</th>
      <td>children of morta</td>
      <td>78.0</td>
      <td>79</td>
      <td>1.0</td>
      <td>low</td>
    </tr>
    <tr>
      <th>306</th>
      <td>ice age: scrat's nutty adventure</td>
      <td>56.0</td>
      <td>55</td>
      <td>1.0</td>
      <td>low</td>
    </tr>
    <tr>
      <th>110</th>
      <td>motogp 19</td>
      <td>76.0</td>
      <td>76</td>
      <td>0.0</td>
      <td>low</td>
    </tr>
    <tr>
      <th>188</th>
      <td>lost ember</td>
      <td>70.0</td>
      <td>70</td>
      <td>0.0</td>
      <td>low</td>
    </tr>
    <tr>
      <th>198</th>
      <td>chocobo's mystery dungeon: every buddy!</td>
      <td>69.0</td>
      <td>69</td>
      <td>0.0</td>
      <td>low</td>
    </tr>
    <tr>
      <th>330</th>
      <td>submersed</td>
      <td>44.0</td>
      <td>44</td>
      <td>0.0</td>
      <td>low</td>
    </tr>
    <tr>
      <th>214</th>
      <td>effie</td>
      <td>68.0</td>
      <td>68</td>
      <td>0.0</td>
      <td>low</td>
    </tr>
    <tr>
      <th>76</th>
      <td>star wars jedi: fallen order</td>
      <td>79.0</td>
      <td>79</td>
      <td>0.0</td>
      <td>low</td>
    </tr>
    <tr>
      <th>56</th>
      <td>blood &amp; truth</td>
      <td>80.0</td>
      <td>80</td>
      <td>0.0</td>
      <td>low</td>
    </tr>
  </tbody>
</table>
</div>



### Games Which Got Higher Ratings From Users Than From Critics


```python
def higherUserRatings(platform_in):
    return platform_df[platform_in][platform_df[platform_in]['user_rating'] > platform_df[platform_in]['critic_rating']].head(10)
    
higherUserRatings('pc')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>title</th>
      <th>user_rating</th>
      <th>critic_rating</th>
      <th>userCritic_difference</th>
      <th>difference_category</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>383</th>
      <td>left alive</td>
      <td>86.0</td>
      <td>40</td>
      <td>46.0</td>
      <td>very_high</td>
    </tr>
    <tr>
      <th>376</th>
      <td>paranoia: happiness is mandatory</td>
      <td>71.0</td>
      <td>47</td>
      <td>24.0</td>
      <td>moderate</td>
    </tr>
    <tr>
      <th>355</th>
      <td>little misfortune</td>
      <td>80.0</td>
      <td>57</td>
      <td>23.0</td>
      <td>moderate</td>
    </tr>
    <tr>
      <th>348</th>
      <td>terminator: resistance</td>
      <td>82.0</td>
      <td>59</td>
      <td>23.0</td>
      <td>moderate</td>
    </tr>
    <tr>
      <th>384</th>
      <td>eternity: the last unicorn</td>
      <td>61.0</td>
      <td>39</td>
      <td>22.0</td>
      <td>moderate</td>
    </tr>
    <tr>
      <th>341</th>
      <td>summer catchers</td>
      <td>83.0</td>
      <td>61</td>
      <td>22.0</td>
      <td>moderate</td>
    </tr>
    <tr>
      <th>365</th>
      <td>bannermen</td>
      <td>72.0</td>
      <td>52</td>
      <td>20.0</td>
      <td>moderate</td>
    </tr>
    <tr>
      <th>374</th>
      <td>i love you, colonel sanders! a finger lickin' ...</td>
      <td>68.0</td>
      <td>50</td>
      <td>18.0</td>
      <td>low</td>
    </tr>
    <tr>
      <th>344</th>
      <td>medieval kingdom wars</td>
      <td>77.0</td>
      <td>60</td>
      <td>17.0</td>
      <td>low</td>
    </tr>
    <tr>
      <th>302</th>
      <td>outbuddies</td>
      <td>83.0</td>
      <td>66</td>
      <td>17.0</td>
      <td>low</td>
    </tr>
  </tbody>
</table>
</div>



___

## A Single Permutation Shuffle Based Trial With Histogram & Probability Density Function
We compare platforms distributions through permutation-test. It is a more systematic approach than relying upon intuition of visualizing and comparing distributions. Given two platforms, We concatenate them into one group. That group's elements are randomly shuffled. Then we divide the group into new two groups. We compare the two distributions of the new two groups and assess whether the insight is still present as in the case of the two original groups of platforms. If the insight is not present in the two new groups, then that would count an evidence on behalf of our hypothesis. That is, The insight (difference in distribution) of original distributions is attributed to the two platforms. In addition, We consider average a p-value of a distribution and utilize it in computing disparity between distributions. Next, We apply this method iteratively.

### Ensure Series Data are Ascendingly Ordered


```python
print(platform_df['ps4']['userCritic_difference'])
print("")
print(platform_df['switch']['userCritic_difference'])
```

    93     69.0
    82     68.0
    116    60.0
    79     52.0
    172    51.0
           ... 
    198     0.0
    330     0.0
    214     0.0
    76      0.0
    56      0.0
    Name: userCritic_difference, Length: 310, dtype: float64
    
    240    58.0
    66     55.0
    94     51.0
    416    43.0
    123    42.0
           ... 
    443     0.0
    89      0.0
    106     0.0
    53      0.0
    208     0.0
    Name: userCritic_difference, Length: 364, dtype: float64


### PS4 Distribution


```python
histogramPdfGraph.showHistPdf(platform_df['ps4']['userCritic_difference'], 30, '#e3e2e2', 'black', 'disparity', 'ps4', 10, 8)
```


![png](index_files/index_68_0.png)


### Average of PS4's Disparity


```python
platform_df['ps4']['userCritic_difference'].mean()
```




    15.893548387096773



### Switch Distribution


```python
histogramPdfGraph.showHistPdf(platform_df['switch']['userCritic_difference'], 30, '#e3e2e2', 'black', 'disparity', 'switch', 10, 8)
```


![png](index_files/index_72_0.png)


### Average of Switch Disparity


```python
platform_df['switch']['userCritic_difference'].mean()
```




    6.876373626373627



### Conclusion
- The difference between _ps4_ and _switch_ distributions is notable
- The difference between _ps4_ and _switch_ means is about 9

### Concatenate Both PS4 and Switch


```python
bothGroups = pd.concat([platform_df['switch']['userCritic_difference'], platform_df['ps4']['userCritic_difference']])
```

### Shuffle and Divide


```python
# permutation based shuffling
rng = np.random.default_rng()
bothGroups = rng.permutation(bothGroups)
# divide into two groups
firstGroup = bothGroups[:int(len(bothGroups)/2)]
secondGroup = bothGroups[int(len(bothGroups)/2):]
```

### First Group Distribution


```python
histogramPdfGraph.showHistPdf(firstGroup, 30, '#e3e2e2', 'black', 'disparity', 'first group', 10, 8)
```


![png](index_files/index_81_0.png)


### First Group Average


```python
firstGroup.mean()
```




    9.928783382789318



### Second Group Distribution


```python
histogramPdfGraph.showHistPdf(secondGroup, 30, '#e3e2e2', 'black', 'disparity', 'second group', 10, 8)
```


![png](index_files/index_85_0.png)


### Second Group Average


```python
secondGroup.mean()
```




    12.118694362017804



### Conclusion
- The difference between first and second groups distributions is not notable alike ps4 and switch
- The difference between first and second groups means is much less than disparity between ps4 and switch distributions

___

## Permutation Test and P-Value Based Statistical Significance
We apply the above method iteratively. The more tests, The more confident we are of our hypothesis. That is, The pattern of two distributions is attributed to the difference in two platforms.


```python
# computes average of a list
def avgOfList(list_in):
    return pd.Series(list_in).mean()
```


```python
# loop on pairs of platforms
for idx, platformName in enumerate(platformsNames):
    for idx_, platformName_ in enumerate(platformsNames):
        # compare only unique pairs
        if idx_ > idx:
            # print pairs of platforms which are compared
            print(platformName, platformName_)
            # apply test for 25 iterations on first and second platforms of the nested loop
            testResults = permTest.permutationTest(25, platform_df[platformName]['userCritic_difference'], platform_df[platformName_]['userCritic_difference'])
            # print results average
            print(avgOfList(testResults))
            print("")
```

    ps4 xbox
    0.4872043010752686
    
    ps4 switch
    8.135987817102968
    
    ps4 pc
    1.6799676922757263
    
    xbox switch
    7.305647096989032
    
    xbox pc
    0.6697090501544217
    
    switch pc
    6.10385164806027
    


### Conclusion
- switch has greatest statistical significance in comparison with other platforms


