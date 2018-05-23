import pandas as pd
import os
from datetime import datetime
import argparse
from static import pairs, columns
from fetch_data import fetch_data
from analytics import mean

def main(args):
	data = fetch_data(args)
	print data.shape
	data = calculate_pairs(data, mean)
	print data.tail()
	print data.columns

def calculate_pairs(data, func):
	for pair in pairs:
		data  =  func(pair, data)
	return data

if __name__=='__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('--pickled', 
						choices = ['True', 'False'],
						type=str,
                    	help='Do you want to use Pickled Data?')
	args = parser.parse_args()
	parser = argparse.ArgumentParser()

	main(args)