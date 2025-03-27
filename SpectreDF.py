import pandas as pd

def readRP1(file):
	ch = []
	cnt = []
	with open(file, 'r') as f:
		line = 0
		for x in f:
			if line > 5:
				n = int(x[0:-1])
				cnt.append(n)
				ch.append(line-5)
			line += 1
	df = pd.DataFrame({'Channel':ch, 'Counts':cnt})
	return df

def readMCA(file, norm=False):
	df = pd.read_table(file, skiprows=1, names=('Channel', 'Counts'))
	if norm:
		rod = readMCA(file.replace('MCA0', 'MCA1')) # Creates a DataFrame for the normalized yield
		normFactor = norm/areaAB(rod, 'Counts', 100, 120)
		df['Norm'] = df['Counts']*normFactor
	return df

def ToRP1(orgn, dstn, A='A', B='B', beam='4HE++', MeV='1.2', phi='15', theta='0'):
	with open(orgn, 'r') as O, open(dstn, 'x') as D:
		D.write(f'EMPTY\nBEAM {beam}  CHOFF 0 CONV  {A} , {B}\n' + 
		f'FILE {dstn} FWHM 21 GEOM IBM\nIDE {dstn} MEV {MeV} PHI {phi}\n' + 
		f'THETA {theta}\nSWALLOW\n')
		for x in O:
			_, value, n = x.split('\t',)
			if value.isnumeric():
				D.write(value+n)

def areaAB(df, column, A, B):
	if A > B:
		A, B = B, A
	return df[column].iloc[A:B+1].sum()

def smooth(df, column, win=5):
	df['Smooth'] = df[column].rolling(win).mean()
	df['Smooth'] = df['Smooth'].fillna(df[column])

def tableSciD(sampleDict, sampleList, col='Norm'):
	with open('SciDavisImport.txt', 'w') as f:
		f.write('Channel')
		for A in sampleList:
			f.write(' ')
			f.write(A)
		f.write('\n')
		for i in range(512):
			f.write(str(i))
			for A in sampleList:
				f.write(' ')
				f.write(str(sampleDict[A].loc[i, col]))
			f.write('\n')