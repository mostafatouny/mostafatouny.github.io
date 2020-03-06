import pandas as pd
import numpy as np

def permutationTest(iterationsNum, firstGroup, secondGroup):
    # difference of both groups averages
    firGroAvg = firstGroup.mean()
    secGroAvg = secondGroup.mean()
    groAvgDif = abs(firGroAvg - secGroAvg)
    
    # concatenate both groups into one group
    bothGroups = pd.concat([firstGroup, secondGroup])
    # random generator
    rng = np.random.default_rng()
    
    # store test results
    testResults = []
    for it in range(iterationsNum):
        # shuffle the group by permutation
        bothGroups = rng.permutation(bothGroups)
        # divide into two groups
        shuFirGro = bothGroups[:int(len(bothGroups)/2)]
        shuSecGro = bothGroups[int(len(bothGroups)/2):]

        # difference of shuffled two groups averages
        shuFirAvg = shuFirGro.mean()
        shuSecAvg = shuSecGro.mean()
        shuAvgDif = abs(shuFirAvg - shuSecAvg)
        
        # compare the two shuffeled groups with pristine ones
        itResult = abs(groAvgDif - shuAvgDif)
        # store result
        testResults.append(itResult)
    
    return testResults
