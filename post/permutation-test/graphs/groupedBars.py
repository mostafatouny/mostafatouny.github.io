import numpy as np
import matplotlib.pyplot as plt

def showGroupedBars(categoriesSize_in, groupsNames_in, yLabel_in, title_in):
	# for calculating x-position
	bars_count = len(categoriesSize_in)

	# labels initial locations
	x = np.arange(len(groupsNames_in))
	width = 0.1  # the width of the bars

	fig = plt.figure(figsize=(12, 5))
	ax = plt.subplot()

	# translate canvas, documented for future works
	#translate(ax, 0, -(width*bars_count/2))

	# for each category, construct its corresponding bar
	#for idx, category in enumerate(categoriesSize_in):
	#	ax.bar(x + (idx*width) - (width*bars_count/2), categoriesSize_in[category], width, label=category, align='edge')
	for idx, columnName in enumerate(categoriesSize_in):
		catSeries = categoriesSize_in[columnName]
		catName = catSeries.name
		ax.bar(x + (idx*width) - (width*bars_count/2), (catSeries), width, label=catName, align='edge')
    
	# Add some text for labels, title and custom x-axis tick labels, etc.
	ax.set_ylabel(yLabel_in)
	ax.set_title(title_in)
	ax.set_xticks(x)
	ax.set_xticklabels(groupsNames_in)
	ax.legend()

	fig.tight_layout()
	plt.show()
