import pandas as pd

'''
Excel:
packages: xlwt (older xls format), openpyxl (new xlsx format), xlrd (read)
read from Excel: df = pd.read_excel('name.xlsx')
write to Excel: df.to_excel('new_table.xlxs')
'''

df = pd.read_csv('survey_results_public.csv')

pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)

#print(df)
print(df.shape)
print(df.info())

##df.head(10)
##df.tail(10)

#scheme_df = pd.read_csv('survey_results_schema.csv')
# Change index to the information in Column
scheme_df = pd.read_csv('survey_results_schema.csv', index_col='Column')
print(scheme_df)

print(df.columns)
print(df['Hobbyist'].value_counts())

print(df.loc[[0],'Hobbyist'])
print(df.loc[[0],'Hobbyist':'Employment'])

print(scheme_df.loc['Hobbyist'])
print(scheme_df.loc['MgrIdiot', 'QuestionText'])
# without inplace - does not affect the data, only for the moment
scheme_df.sort_index(inplace=True)
print(scheme_df)

# Filter
high_salary = (df['ConvertedComp'] > 70000)
print(df.loc[high_salary, ['Country', 'LanguageWorkedWith', 'ConvertedComp']])

countries = ['United States','India', 'Canada']
filt = df['Country'].isin(countries)
print(df.loc[filt, ['Country']])

filtLang = df['LanguageWorkedWith'].str.contains('Python', na = False)
print(df.loc[filtLang, ['LanguageWorkedWith']])

# Sort
#df.sort_values(by='Country', inplace = True)
df.sort_values(by=['Country','ConvertedComp'], ascending = [True, False], inplace = True)
print(df[['Country','ConvertedComp']].head(10))

# 10 largest
print(df['ConvertedComp'].nlargest(10))   # This shows only salaries
print(df.nlargest(10, 'ConvertedComp'))   # This prints everything about the 10 largest salaries

# Statistical overview
print(df.describe())
print('Median: ', df['ConvertedComp'].median())
print('Number of answers (without NaN)', df['ConvertedComp'].count())
print('Hobbyist: ', df['Hobbyist'].value_counts())
print('SocialMedia: ', df['SocialMedia'].value_counts(normalize = True))   # in per-cent

# Grouping of data
# SocialMedia per country
country_grp = df.groupby(['Country'])
country_grp.get_group('India')

filter = df['Country'] == 'India'
print(df.loc[filt]['SocialMedia'].value_counts())

print(country_grp['SocialMedia'].value_counts())
print(country_grp['SocialMedia'].value_counts().loc['United States'])

print(country_grp['ConvertedComp'].median())

# Running more aggregate function
print(country_grp['ConvertedComp'].agg(['median', 'mean']))

# Dropping NaN values
# df.dropna(axis = 'index',how='any')
