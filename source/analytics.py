import pandas as pd

def mean(pair, df):
	df[pair + '_MEAN_R'] = (df[pair + '_HIGH'] + df[pair + '_LOW'])/2
	df[pair + '_MEAN_H'] = (df[pair + '_CLOSE'] + df[pair + '_OPEN'])/2 
	return df