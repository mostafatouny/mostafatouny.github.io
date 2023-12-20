import pandas as pd
import numpy as np


def columnCount(column_in, groupCol_in):
    columnSize = column_in.groupby(groupCol_in).size()
    columnSize = columnSize.rename_axis("")
    return columnSize

# construct a map between a df key and its value categories count
def map_columnCount(mapDf_in, groupCol_in):
    # a map between a platform name and its categories count
    categoriesCount = []

    for key in mapDf_in:
        # count categories among all records
        columnGroupSize = columnCount(mapDf_in[key], groupCol_in)
        categoriesCount.append(columnGroupSize)
        
    categoriesSizeDf = pd.DataFrame(categoriesCount, index=mapDf_in.keys())
        
    return categoriesSizeDf


# construct a 2d-list whose elements represent maps sizes of some category
def map_categoriesSize(categories_in, mapDf_in, dfCategoriesCount_in, catIndex_in):

    categoriesSize = {}

    # loop on categories
    for category in categories_in:
        categoryList = []
        # append platforms sizes of current category
        for key in mapDf_in:
            categoryList.append(dfCategoriesCount_in[key][category])
        
        indexedCategory = pd.Series(data=categoryList, index=catIndex_in)
        
        # append platforms sizes of the category into whole 2d-list
        categoriesSize[category] = indexedCategory
        
    return categoriesSize


# construct categories size as 2d list in order of
# extremely high, very high, .., low
def ConstCategoriesSize_2dList(categoriesSize_in):

    categoriesSize_2dList = []

    categories_size = list(categoriesSize_in.items())

    # loop on categories names and their corresponding elements
    for category, elemsLis in categories_size:
        # append to whole 2dList
        categoriesSize_2dList.append(elemsLis)

    # convert to numpy array
    categoriesSize_2dList = np.array(categoriesSize_2dList)
    
    return categoriesSize_2dList
