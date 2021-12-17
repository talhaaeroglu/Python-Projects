import pandas as pd
import random

months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
days1 = [31,28,31,30,31,30,31,31,30,31,30,31]
days2 = [31,29,31,30,31,30,31,31,30,31,30,31]
file1 = open("randomdata.txt path","w")
column = ["date,","avg_high,","avg_low,","record_high,","record_low,","avg_precipitation\n"]
file1.writelines(column)
def date_gen(month,year,cycle):
    if cycle == 400:
        return
    else:
        if month > 12:
            month = 1
            year +=1
            if year % 4 == 0:
                n1 = random.randint(1000,2000)
                for i in range(n1):
                    file1.writelines([str(month),"/",str(days1[month-1]),"/",str(year),",",str(random.randint(10, 100)),",",str(random.randint(10, 100)),",",str(random.randint(10, 100)),",",str(random.randint(10, 100)),",",str(random.randint(10, 100)),"\n"])
            else:
                n2 = random.randint(1000,2000)
                for j in range(n2):
                    file1.writelines([str(month),"/",str(days1[month-1]),"/",str(year),",",str(random.randint(10, 100)),",",str(random.randint(10, 100)),",",str(random.randint(10, 100)),",",str(random.randint(10, 100)),",",str(random.randint(10, 100)),"\n"])
        else:
            if year % 4 == 0:
                n3 = random.randint(1000,2000)
                for f in range(n3):
                    file1.writelines([str(month),"/",str(days1[month-1]),"/",str(year),",",str(random.randint(10, 100)),",",str(random.randint(10, 100)),",",str(random.randint(10, 100)),",",str(random.randint(10, 100)),",",str(random.randint(10, 100)),"\n"])
            else:
                n4 = random.randint(1000,2000)
                for t in range(n4):
                    file1.writelines([str(month),"/",str(days1[month-1]),"/",str(year),",",str(random.randint(10, 100)),",",str(random.randint(10, 100)),",",str(random.randint(10, 100)),",",str(random.randint(10, 100)),",",str(random.randint(10, 100)),"\n"])
        month +=1
        cycle += 1
    date_gen(month,year,cycle)

date_gen(1,2010,1)



        

