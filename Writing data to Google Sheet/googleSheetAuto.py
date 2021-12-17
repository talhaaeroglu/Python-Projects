import pygsheets
import pandas as pd
#authorization
gc = pygsheets.authorize(service_file= """Your credential json file """)

# Reading example data from txt to Dataframe
df = pd.read_csv("""randomData.txt""")
#open the google spreadsheet (where 'PY to Gsheet Test' is the name of my sheet)
sh = gc.open("""GoogleSheet document""")
#select the first sheet 
wks = sh[0]
#function that catches 'cell limit error' and deletes rows to insert new data
col_len_df = len(df.columns)
col_len_wks = wks.cols
if col_len_df != col_len_wks:
    wks.delete_cols(1,col_len_wks-col_len_df)
    wks.delete_rows(2,999)
def rec_func():
    try:
        wks.add_rows(len(df))
        return
    except:
        x = 1
        l = wks.get_col(1)
        l = l[1:]
        #dates = [date.get('date') for date in l]
        first_date = None
        for i in l:
            
            if first_date == None:
                first_date = i
                print(i)
            else:
                if first_date == i:
                    x+=1
                else:
                    if x>= len(df):
                        break
                    else:
                        first_date = i
        wks.delete_rows(2,x)
        rec_func()
rec_func()

#getting row count of google sheet
af = wks.get_all_records()          
ab = len(af)
if(ab != 0):
    wks.set_dataframe(df,(ab+2,1))    
    wks.delete_rows(ab+2,1)
else:
    wks.set_dataframe(df,(1,1))