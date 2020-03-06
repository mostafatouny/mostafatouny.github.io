import numpy as np
import matplotlib.pyplot as plt

def showHistPdf(x_in, numBins_in, colorHist_in, colorFunc_in, xLabel_in, title_in, ySize_in, xSize_in):
	mu = x_in.mean()
	sigma = x_in.std()

	# set y and x sizes
	fig = plt.figure(figsize=(ySize_in, xSize_in))
	ax = plt.subplot()

	# the histogram of the data
	# input is data, number of groups, set pdf to True, set color
	n, bins, patches = ax.hist(x_in, numBins_in, density=1, color=colorHist_in)

	# array of size "number of groups", corresponding to each group
	# magic of pdf
	y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
	np.exp(-0.5 * (1 / sigma * (bins - mu))**2))

	ax.plot(bins, y, colorFunc_in)
	# set labels and titles
	ax.set_xlabel(xLabel_in)
	ax.set_ylabel('Probability Density')
	ax.set_title(title_in)

	fig.tight_layout()
	plt.show()
