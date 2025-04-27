import os
import sys


class Logger:
	def __init__(self, filename):
		self.filename = filename
		self.terminal = sys.stdout

		# Clean log_file
		with open(self.filename, "w") as log_file:
			pass

		sys.stdout = self
		sys.stderr = sys.stdout

	def write(self, message):
		"""Writes the message to the log file and also to the terminal."""
		self.terminal.write(message)

		with open(self.filename, "a") as log_file:
			log_file.write(message)

	def flush(self):
		"""Flushes the output for the terminal."""
		self.terminal.flush()

	def restore(self):
		"""Restores the standard output to the original terminal."""
		sys.stdout = self.terminal
		sys.stderr = sys.stdout


class DivergenceError(Exception):
	def __init__(self, message, path=None, context=None):
		super().__init__(message)
		self.message = message
		self.path = path
		self.context = context

	def __str__(self):
		base = f'DivergenceError: {self.message}'
		if self.path:
			base += f'\nPath:\n{self.path}'
		if self.context:
			base += f'\nContext:\n{self.context}'
		return base

def betterStructure(entry, out='DATA', log=True):
	if log:
		print(log)
		logger = Logger('log.txt')

	for day in os.listdir(entry):

		sampleDay = '-'.join(day.split('_')[0:3])

		for directoryName in os.listdir(f'{entry}/{day}'):
			skip = False
			
			dirPath = f'{entry}/{day}/{directoryName}'
			
			while True:
				try:
					fileName = validateDir(dirPath)
					break

				except DivergenceError as e:
					print(e)
					dirPath = input('Please, provide the right path: (or \'continue\' to skip this sample)\n')
					if dirPath == 'continue':
						skip = True
						break

			if skip:
				continue

			while True:
				try:
					name = validateNames(directoryName.upper(), fileName.upper())
					break

				except DivergenceError as e:
					print(e)
					name = input('Please, provide a name for this sample: (or \'continue\' to skip this sample)\n')
					if name == 'continue':
						skip = True
					break

			if skip:
				continue

			for prefix in ['MCA0', 'MCA1']:
				inFile = f'{entry}/{day}/{directoryName}/{prefix}_{fileName}.txt'
				outFile =  f'{out}/{name}_{sampleDay}/{prefix}.tsv'
				betterFiles(inFile, outFile)



def validateDir(directory):
	try:
		directoryContents = os.listdir(directory)
	except NotADirectoryError as e:
		raise DivergenceError(e)


	if len(directoryContents) != 5:
		raise DivergenceError(
			message='This directory has an unexpected amount of content.',
			path=directory,
			context=directoryContents
		)
	names = set()
	for content in directoryContents:
		_, *name = content[:content.rfind('.')].split('_')
		names.add('_'.join(name))
	if len(names) == 1:
		return names.pop()
	else:
		raise DivergenceError(
			message='Something seems wrong with this directory.',
			path=directory,
			context=directoryContents
		)


def validateNames(directoryName, fileName):
	directoryName = directoryName.replace('ET', 'et')
	fileName = fileName.replace('ET', 'et')
	if directoryName == fileName and fileName.isalnum():
		return fileName
	raise DivergenceError(
		message='Couldn\'t resolve sample name.',
		context=f'{directoryName} != {fileName}')


def betterFiles(
	in_file,
	out_file,
	in_sep='\t',
	skip_lines=1,
	columns=['Channel', 'Counts'],
	out_sep='\t'
):
	out_path = os.path.dirname(out_file)


	os.makedirs(out_path, exist_ok=True)
	with open(in_file, 'r') as fin, open(out_file, 'w') as fout:
		fail_lines = []
		fout.write(out_sep.join(columns) + '\n')

		for i, line in enumerate(fin):
			if i < skip_lines:
				continue

			line = line.rstrip().rstrip(',.')
			values = line.split(in_sep)

			if len(values) != len(columns):
				fail_lines.append(f'{i}: ({values})')

			fout.write(out_sep.join(values) + '\n')

	print(f'File saved as: {out_file}')

	if fail_lines:
		print('Warning: Some lines have an unexpected number of columns:\n')
		for line in fail_lines:
			print(line)
