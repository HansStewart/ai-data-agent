# Write the data directly - no CSV reading needed!
data = """Month,Year,Passengers,Month_Num,YoY_Growth,Season,Rolling_Avg
JAN,1958,340,1,,Winter,340.0
FEB,1958,318,2,,Winter,329.0
MAR,1958,362,3,,Spring,340.0
APR,1958,348,4,,Spring,343.0
MAY,1958,363,5,,Spring,358.0
JUN,1958,435,6,,Summer,382.0
JUL,1958,491,7,,Summer,430.0
AUG,1958,505,8,,Summer,477.0
SEP,1958,404,9,,Fall,467.0
OCT,1958,359,10,,Fall,423.0
NOV,1958,310,11,,Fall,358.0
DEC,1958,337,12,,Winter,335.0
JAN,1959,360,1,5.88,Winter,360.0
FEB,1959,342,2,7.55,Winter,351.0
MAR,1959,406,3,12.15,Spring,369.0
APR,1959,396,4,13.79,Spring,381.0
MAY,1959,420,5,15.70,Spring,407.0
JUN,1959,472,6,8.51,Summer,429.0
JUL,1959,548,7,11.61,Summer,480.0
AUG,1959,559,8,10.69,Summer,526.0
SEP,1959,463,9,14.60,Fall,523.0
OCT,1959,407,10,13.37,Fall,476.0
NOV,1959,362,11,16.77,Fall,411.0
DEC,1959,405,12,20.18,Winter,391.0
JAN,1960,417,1,15.83,Winter,417.0
FEB,1960,391,2,14.33,Winter,404.0
MAR,1960,419,3,3.20,Spring,409.0
APR,1960,461,4,16.41,Spring,424.0
MAY,1960,472,5,12.38,Spring,451.0
JUN,1960,535,6,13.35,Summer,489.0
JUL,1960,622,7,13.50,Summer,543.0
AUG,1960,606,8,8.41,Summer,588.0
SEP,1960,508,9,9.72,Fall,579.0
OCT,1960,461,10,13.27,Fall,525.0
NOV,1960,390,11,7.73,Fall,453.0
DEC,1960,432,12,6.67,Winter,428.0"""

with open('tableau_advanced.csv', 'w') as f:
    f.write(data)

print("SUCCESS! tableau_advanced.csv created!")
print("36 rows of data ready for Tableau!")