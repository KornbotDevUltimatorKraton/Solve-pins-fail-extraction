import os 
import math
import json 
import pandas as pd
import subprocess 
import psycopg2 # Getting the data from the postgres database and insert the json file into the list of the data
from PyPDF2.generic import FloatObject 

username = str(subprocess.check_output("uname -a",shell=True)) # Get the the username of the computer reading from the client computer 
Getusername = username.split("-")[0].split(" ")[1]  #Get the username
EXTRACT  = "/home/"+str(Getusername)+"/Automaticsoftware/tempolarydocextract" #Tempolary read the file extraction from the pdf specification function
CONFIG   = "/home/"+str(Getusername)+"/Automaticsoftware/Configuresearch" # Config file

inputcomp = "drv8320" #Testlist={'drv8873','drv8846','bq25616','bq25731','drv8320'}

getpage = 4
#Getting the csv file and dataframe 
df = pd.read_csv(EXTRACT+"/"+inputcomp+"/"+inputcomp+"_"+str(getpage)+".csv")
print(df) #Getting the data frame before extracting the name from the columns into the list and starte to running the editor in xml file
#Getting the pins name data 
PinsNamepack = []
PinsNumpack  = []
IONamepack = [] # Getting the io name pack 
Packagingdata = {} 
PackagewithIO = {} 
completepack = {} 
completeioname = {} 
n = 1
n1 = 0
n2 = 2
print("Header name",df.values.tolist()[0])  # Specify the 2 difference package from component using second row of first column you will found nan on the list
print(df.columns.values[n1]) #Getting the the columns 0 of the data frame testing getting name from the detected dataframe 
for il in range(1,len(df[df.columns.values[n1]])):
              print(str(il),df[df.columns.values[n1]].values[il]) #Getting the list if the pins testing 
              PinsNamepack.append(df[df.columns.values[n1]].values[il])
for il in range(1,len(df[df.columns.values[n]])):
              print(str(il),df[df.columns.values[n]].values[il]) #Getting the list if the pins testing 
              PinsNumpack.append(df[df.columns.values[n]].values[il])

for il in range(1,len(df[df.columns.values[n2]])):
              print(str(il),df[df.columns.values[n2]].values[il]) #Getting the list if the pins testing 
              IONamepack.append(df[df.columns.values[n2]].values[il])

print(PinsNamepack)
print(PinsNumpack)
print(IONamepack)
for match in range(0,len(PinsNamepack)):
          Packagingdata[PinsNamepack[match]] = PinsNumpack[match]
for re in range(0,len(PinsNamepack)):
          PackagewithIO[PinsNamepack[re]] = IONamepack[re] # Mapping the gpio name  
completepack[inputcomp] = Packagingdata
completeioname[inputcomp] =  PackagewithIO 
print(completepack)
print(completeioname)
listConfig = os.listdir(CONFIG)
def Configure(configfile): 
     try: 
       data = open(CONFIG+"/"+str(configfile),'r') #Open the configuretion file for the path 
       datas = data.readline()
       transfer = json.loads(datas)
       return transfer
     except:
        print("Not found the configure file please check again")
config_data = Configure(listConfig[0])
print(config_data.get('pinsconfig').get('Pins')) # Finding the matching of the list in percentage using sequence matcher
print("Header name",df.values.tolist()[0])  # Specify the 2 difference package from component using second row of first column you will found nan on the list
print("Second name",df.values.tolist()[1])  # Specify the 2 difference package from component using second row of first column you will found nan on the list
