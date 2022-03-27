import pandas as pd
import numpy as np
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

df = pd.read_csv('EncountersQueryload.csv',sep=',', error_bad_lines=False, index_col=False, dtype='unicode')
#correcting datatypes
df = df.astype({'encounterID':int})
df = df.astype({'_year':int})
df = df.astype({'_month':int})
df = df.astype({'duration':int})
df = df.astype({'extraTime':int})
# print(df.dtypes)

# fill null values
df['presentingProblem'].fillna('N/A', inplace = True)
df['ClinicName'].fillna('N/A', inplace = True)
df['Description'].fillna('N/A', inplace = True)
df['discharge_reason'].fillna('N/A', inplace = True)
# print(df.head())
#2-------------------------------Creating the Encounters by year & Month-----------------------------------
# I completed this section before looking at the cross tab file, which is why I'm using for loops and ended 
# a manual approach approach with multiple dataframes

# start empty display dataframe
enncoutersYMdf = pd.DataFrame()

# getting years list
max_yr =df['_year'].max()
min_yr =df.iloc[0,1]
years = []
for i in range(max_yr+1-min_yr):
    years.append(min_yr)
    min_yr += 1

# filtering out misc years less than 2008 from df
wOutLesserYrs = df[(df['_year']>2007)]

# append 1st columm
enncoutersYMdf['Years'] = years

# for loops to create a working list of counts by month per year
# and append them the empty dataframe
for m in range(1,13):
    workinglist=[]
    for y in range(len(years)):
        mthCountDf =wOutLesserYrs[(wOutLesserYrs['_year']==years[y]) & (wOutLesserYrs['_month'] == m)]
        workinglist.append(mthCountDf.shape[0])
    enncoutersYMdf[m] = workinglist

#rename columns and print
enncoutersYMdf.columns =['Years','Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
# print(enncoutersYMdf)

#...........this section for creating the Duration table using crosstab...........................................
# obtain actual encounter data- ie. all scheduled
sch_encounters = wOutLesserYrs[(wOutLesserYrs['scheduled']=='yes')]

# encounter duration empty dataframe
encountersDur = pd.DataFrame()

# for loop concating rows of data that match the 15 min increment of duration to dispaly up
# to 105 min
for d in range(15,120,15):
    encountersDur = pd.concat([sch_encounters[(sch_encounters['duration']==d)],encountersDur], ignore_index=True)
# print(encountersDur.shape[0])

# filtring for encnounters greater then 105 min
longEncounter = sch_encounters[(sch_encounters['duration']> 105 )]

# select year and durations
selection = longEncounter.loc[:,['_year', 'duration']]
selection.columns =['_year','duration']
# print(selection)

# cross tabe to build base table of ecounter counts 
year_duration_Ec = pd.crosstab(encountersDur._year,encountersDur.duration)
# appending all long enounters
year_duration_Ec[999] = selection['_year'].value_counts()
# print(year_duration_Ec)

#....................................Non scheduled encounters......................................
unscheduledAppt = df[(df['scheduled']=='no')&(df['_year']> 2007)]
nonSchEnct = pd.crosstab(unscheduledAppt._year,unscheduledAppt.scheduled)
# print(nonSchEnct)

#3.-----------------------------To HTML-------------------------------------------------------------
# prefix & suffix & templates
prefix = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Family Health Team</title>
    <h1>Family Health Team</h1>
    <p>Encounters for all Family Health Units at end of August, 2013</p>
</head>
<body>

"""
suffix = """

</body>
</html>
"""
table_totals_temp = """<p>
    <strong>Total:</strong> {}
</p>
"""
table_simp_sum ="""<p>{}</p>
"""
table_titles = """<p><strong>{}</strong></p>"""

#..........................base html tables........................
table1 = enncoutersYMdf.to_html()
table2 = year_duration_Ec.to_html()
table3 = nonSchEnct.to_html()
# ........................counts and totals....................
table1_tot = wOutLesserYrs['encounterID'].count()
table2_tot = sch_encounters['encounterID'].count()
table3_tot = nonSchEnct['no'].sum(axis=0)

#......formating templates with titles, counts. and totals...............
table1Title = table_titles.format('Encounters by Year and Month')
table2Title = table_titles.format('Encounters by Scheduled Duration')
table3Title = table_titles.format('Non-scheduled Encounters')
table1Totalsum =table_totals_temp.format(table1_tot)
table2_simple_sum = table_simp_sum.format(table2_tot)
table3_simple_sum = table_simp_sum.format(table3_tot)
table2_3Totalsum=table_totals_temp.format(table2_tot+table3_tot)
#............................Main body concatenation order..................
main_body = table1Title +table1 + table1Totalsum + table2Title + table2 + table2_simple_sum +table3Title + table3 + table3_simple_sum + table2_3Totalsum


# file = open('FHT_encounters.html', 'w')
# file.write(prefix + main_body + suffix)
# file.close()

# 4.----------------Send to email---------------------------
from_addr = 'agdawner@gmail.com'
to_addr = 'alicegaoglad@gmail.com'

msg = MIMEMultipart()
msg['From'] = from_addr
msg['To'] = to_addr
msg['Subject'] = 'These are the encouter data from Family Health Team'

body = prefix + main_body + suffix
msg.attach(MIMEText(body, 'html'))

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

server.login(from_addr, 'Rabbit5Please')

text = msg.as_string()

resp = server.sendmail(from_addr, to_addr, text)
print('resp:', resp)

server.quit()