from matplotlib import pyplot as plt
ColorList = ["#e60049", "#0bb4ff", "#1ee348", "#e6d800", "#9b19f5", "#ffa300", "#dc0ab4"]

colorIter = iter(ColorList)

def plotDF(df, label, y='Counts', x='Channel', color=None, scatter=False, style=None):
	"""
	Plots data from a DataFrame with optional customizations.

	Parameters:
	df : pandas.DataFrame
		The DataFrame containing the data to be plotted.
	label : str
		The label for the plot, used in the legend.
	y : str, optional (default='Counts')
		The column name in `df` to be plotted on the y-axis.
	x : str, optional (default='Channel')
		The column name in `df` to be plotted on the x-axis.
	color : str or int, optional (default=None)
		The color of the plot. If None, the color is chosen sequentially from a predefined list of colors.
		If an integer is provided, it is used as an index to select a color from the list.
	scatter : bool, optional (default=False)
		If True, a scatter plot is generated; otherwise, a line plot is used.
	style : str or None, optional (default=None)
		The style of the plot (e.g., linestyle or marker). If None, a default style is used.
	"""
	global colorIter

	if color is None:
		try:
			color = next(colorIter)
		except StopIteration:
			colorIter = iter(ColorList)
			color = next(colorIter)
			#style = ['-.', 'x'] # This is the old way, and it shouldn't be nescessary

	elif isinstance(color, int):
		color = ColorList[color%len(ColorList)]

	if scatter:
		plt.scatter(df[x], df[y], label=label, s=30, facecolors='none', edgecolors=color, marker=(style if style else 'o'))

	else:
		plt.plot(df[x], df[y], label=label, color=color, linestyle=(style if style else '-'), linewidth=3)

def styleConfig(**kwargs):
	"""
	Configures the styling of the current plot, including font size, title, and more.

	Parameters:
	font_size : int, optional (default=16)
		The font size for the plot text, including axis labels, title, and ticks.
	figsize : tuple, optional (default=(12, 9))
		The size of the figure in inches, specified as a tuple (width, height).
	facecolor : str, optional (default='#363737')
		The background color of the plot area.
	title : list, optional (default=[''])
		The title of the plot. You can pass a list where the first element is the title 
		string and the second element is any additional keyword arguments for the title 
		function (e.g., fontsize, color, etc.).
	minorticks : bool, optional (default=True)
		Whether or not to enable minor ticks on the axes.
	legend : bool, optional (default=True)
		Whether or not to display the legend on the plot.
	grid : bool, optional (default=True)
		Whether or not to display the grid on the plot.
	"""
	style = {
		'font_size': 16,
		'figsize': (12, 9),
		'facecolor': '#363737',
		'title': [''], # ['Title', {Kwargs}]
		'minorticks': True,
		'legend': True,
		'grid': True
	}
	style.update(kwargs)

	plt.rcParams.update({'font.size': style['font_size']})
	plt.gcf().set_size_inches(*style['figsize'])
	plt.gca().set_facecolor(style['facecolor'])
	plt.title(*style['title'])

	if style['minorticks']:
		plt.minorticks_on()
	if style['legend']:
		plt.legend()

	plt.grid(style['grid'])
	plt.gca().set_axisbelow(True)

def axisConfig(**kwargs):
	"""
	Configures the axis labels, limits, scales, and tick marks of the plot.

	Parameters:
	xlbl : list, optional (default=['X'])
		The label for the x-axis. You can pass a list where the first element is the label 
		string and the second element is any additional keyword arguments for the xlabel function 
		(e.g., fontsize, color, etc.).
	ylbl : list, optional (default=['Y'])
		The label for the y-axis. You can pass a list where the first element is the label 
		string and the second element is any additional keyword arguments for the ylabel function 
		(e.g., fontsize, color, etc.).
	xlim : tuple, optional (default=None)
		The limits for the x-axis. If None, the axis limits are set automatically.
	ylim : tuple, optional (default=None)
		The limits for the y-axis. If None, the axis limits are set automatically.
	xscale : str, optional (default='linear')
		The scale for the x-axis. Common options are 'linear', 'log', etc.
	yscale : str, optional (default='linear')
		The scale for the y-axis. Common options are 'linear', 'log', etc.
	xticks : list, optional (default=None)
		A list of positions at which to place ticks on the x-axis. If None, the ticks are set automatically.
	yticks : list, optional (default=None)
		A list of positions at which to place ticks on the y-axis. If None, the ticks are set automatically.
	"""
	axis = {
		'xlbl': ['X'], # ['X', {Kwargs}]
		'ylbl': ['Y'], # ['Y', {Kwargs}]
		'xlim': None,
		'ylim': None,
		'xscale': 'linear',
		'yscale': 'linear',
		'xticks' : None,
		'yticks' : None
	}
	axis.update(kwargs)

	plt.xlabel(*axis['xlbl'])
	plt.ylabel(*axis['ylbl'])

	plt.xlim(axis['xlim'])
	plt.ylim(axis['ylim'])

	plt.xscale(axis['xscale'])
	plt.yscale(axis['yscale'])

	plt.xticks(axis['xticks'])
	plt.yticks(axis['yticks'])


def plotConfig(**kwargs):
	"""
	Configures the overall plot style and axis settings.

	This function combines the style and axis configuration by calling
	the `styleConfig` and `axisConfig` functions. It initializes the color iterator 
	for plots and applies the given configuration settings to the plot.

	Parameters:
	**kwargs : keyword arguments, optional
		Additional keyword arguments passed to styleConfig and axisConfig functions.
	"""
	global colorIter
	colorIter = iter(ColorList)
	styleConfig(**kwargs)
	axisConfig(**kwargs)

def savePlots(fileName, clear=True):
	"""
	Saves the current plot to a file and optionally clears the figure.

	This function saves the current figure to a PNG file with the specified fileName 
	and applies tight bounding box and zero padding. It also clears the plot figure 
	after saving if specified.

	Parameters:
	fileName : str
		The file name for saving the plot (e.g., 'file.png').
	clear : bool, optional (default=True)
		Whether to clear the current figure after saving it.
	"""
	plt.savefig(f'{fileName}.png', dpi=250, bbox_inches='tight', pad_inches=0)
	if clear:
		plt.clf()

def showPlots():
	"""
	Shows...
	"""
	plt.show()

