import pandas as pd

# this is the script that was used to generate creditcard.parquet
# it requires creditcard.csv to be downloaded from kaggle to run
# creditcard.csv is not included in this repository due to its size

# read in csv
cc_csv = pd.read_csv("../data/creditcard.csv")

# turn all column names to lowercase
cc_csv.columns = [x.lower() for x in cc_csv.columns]

# select the time, v1, and v2 columns
cc ={
	'time': pd.Series(cc_csv['time'], dtype='int32'),
	'amount': pd.Series(cc_csv['amount'], dtype='float32'),
	'class': pd.Series(cc_csv['class'], dtype='bool'),
	'v1': pd.Series(cc_csv['v1'], dtype='float32'),
	'v2': pd.Series(cc_csv['v2'], dtype='float32'),
	'v3': pd.Series(cc_csv['v3'], dtype='float32'),
	'v4': pd.Series(cc_csv['v4'], dtype='float32'),
	'v5': pd.Series(cc_csv['v5'], dtype='float32'),
	'v6': pd.Series(cc_csv['v6'], dtype='float32'),
	'v7': pd.Series(cc_csv['v7'], dtype='float32'),
	'v8': pd.Series(cc_csv['v8'], dtype='float32'),
	'v9': pd.Series(cc_csv['v9'], dtype='float32'),
	'v10': pd.Series(cc_csv['v10'], dtype='float32'),
	'v11': pd.Series(cc_csv['v11'], dtype='float32'),
	'v12': pd.Series(cc_csv['v12'], dtype='float32'),
	'v13': pd.Series(cc_csv['v13'], dtype='float32'),
	'v14': pd.Series(cc_csv['v14'], dtype='float32'),
	'v15': pd.Series(cc_csv['v15'], dtype='float32'),
	'v16': pd.Series(cc_csv['v16'], dtype='float32'),
	'v17': pd.Series(cc_csv['v17'], dtype='float32'),
	'v18': pd.Series(cc_csv['v18'], dtype='float32'),
	'v19': pd.Series(cc_csv['v19'], dtype='float32'),
	'v20': pd.Series(cc_csv['v20'], dtype='float32'),
	'v21': pd.Series(cc_csv['v21'], dtype='float32'),
	'v22': pd.Series(cc_csv['v22'], dtype='float32'),
	'v23': pd.Series(cc_csv['v23'], dtype='float32'),
	'v24': pd.Series(cc_csv['v24'], dtype='float32'),
	'v25': pd.Series(cc_csv['v25'], dtype='float32'),
	'v26': pd.Series(cc_csv['v26'], dtype='float32'),
	'v27': pd.Series(cc_csv['v27'], dtype='float32'),
	'v28': pd.Series(cc_csv['v28'], dtype='float32'),
}

cc = pd.DataFrame(cc)

# write to parquet
cc.to_parquet('../data/creditcard.parquet', engine='pyarrow')