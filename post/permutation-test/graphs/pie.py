import pandas as pd
import matplotlib.pyplot as plt

def showPieGraph(series_in, title_in, ySize_in, xSize_in):
	#plt.close('all')
	# construct a series based on it
	pie_series = pd.Series(series_in, name=title_in)
	# plot a pie chart
	pie_series.plot.pie(figsize=(ySize_in,xSize_in))
	plt.show()
