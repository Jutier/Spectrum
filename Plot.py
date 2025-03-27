from matplotlib import pyplot as plt
ColorList = ["#e60049", "#0bb4ff", "#1ee348", "#e6d800", "#9b19f5", "#ffa300", "#dc0ab4"]

colorIter = iter(ColorList)
plt.rcParams.update({'font.size': 17})

def plotDF(df, label, y='Counts', x='Channel', color=None, scatter=False, style=None):
	global colorIter

	if color is None:
		try:
			color = next(colorIter)
		except StopIteration:
			colorIter = iter(ColorList)
			color = next(colorIter)
			style = ['-.', 'x']

	elif isinstance(color, int):
		color = ColorList[color%len(ColorList)]

	if scatter:
		plt.scatter(df[x], df[y], label=label, s=30, facecolors='none', edgecolors=color, marker=(style if style else 'o'))

	else:
		plt.plot(df[x], df[y], label=label, color=color, linestyle=(style if style else '-'), linewidth=3)


def plotConfig(title='', xlbl='Channel', ylbl='Counts'):
	global colorIter
	colorIter = iter(ColorList)
	plt.title(title)
	plt.grid(True)
	plt.gca().set_axisbelow(True)
	plt.gcf().set_size_inches(12, 9)
	plt.gca().set_facecolor('#363737')
	plt.minorticks_on()
	plt.xlabel(xlbl)
	plt.ylabel(ylbl)
	plt.xlim(50, 450)
	plt.ylim(0, 120)
	plt.legend()

def savePlots(title, xlbl='Channel', ylbl='Counts', clear=True):
	plotConfig(title, xlbl, ylbl)
	plt.savefig(f'{title}.png', dpi=250)
	if clear:
		plt.clf()

def showPlots(title='', xlbl='Channel', ylbl='Counts'):
	plotConfig(title, xlbl, ylbl)
	plt.show()

