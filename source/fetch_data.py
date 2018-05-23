import pandas as pd
import os
from datetime import datetime
from pairs import pairs

def read(pair, file_path, filename):
	return pd.read_csv(file_path + '/' + filename, skiprows=1) \
	.drop(columns = ['Symbol']) \
	.apply(lambda row: clean_datetime(row), axis = 1) \
	.set_index('Date') \
	.rename(index = str, 
			columns = {	'Volume To' : str(pair + '_TO'), 
						'Volume From' : str(pair + '_FROM'),
						'Open' : str(pair + '_OPEN'),
						'High' : str(pair + '_HIGH'),
						'Low' : str(pair + '_LOW'),
						'Close' : str(pair + '_CLOSE')
						})

def normalize_fiat(df):
	for column in df.columns:	
		if column.find('USD') > 0:
			df[column] = 1/df[column]
	return df

def clean_datetime(row):
	row['Date'] = datetime.strptime(row['Date'], '%Y-%m-%d %I-%p')
	return row

def fetch_data(args):
	file_path = 'historic'
	if (args.pickled.split(' ')[-1]) == 'False':
		df = pd.DataFrame()
		pairs = []

		for filename in os.listdir(file_path):
			print filename
			if filename.endswith('.csv'):
				pair = filename.split('_')[1]
				pairs.append(pairs)
				print pair
				df = read(pair, file_path, filename) \
					.merge(df, how='outer', left_index=True, right_index=True)
		normalize_fiat(df).to_pickle(file_path + '/merged')
		return df
	else:
		return pd.read_pickle(file_path + '/merged')