# example input:

# categories names and their corresponding intervals
# category at location x corresponds to interval equal or greater than intervals location x and less than location x + 1
# except for last category, has no end

# categories = pd.Series(["low", "moderate", "high", "very high", "extremely high"], dtype="category")
# intervals_categories = [0, 20, 30, 40, 50]


# map a value to its interval
def numToCat(row_in, column_in, categories_in, intervalsCategories_in):
    assert len(categories_in) == len(intervalsCategories_in), "categories and their intervals lens are not equal"
    
    row_catValu = row_in[column_in]
    
    # check if value is in between two boundaries
    for idx in range(len(intervalsCategories_in)-1):
        if row_catValu >= intervalsCategories_in[idx] and row_catValu < intervalsCategories_in[idx+1]:
            return categories_in.iloc[idx]
    # if not, then check if it is greater than latest boundary
    lastIndex = len(categories_in)-1
    if row_catValu >= intervalsCategories_in[lastIndex]:
        return categories_in.iloc[lastIndex]
    # if not either, raise error
    raise ValueError("unexpected value within supposed ranges")
