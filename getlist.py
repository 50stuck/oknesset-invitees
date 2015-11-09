import urllib.request
import time
import json
import re
import csv

with open('academicmuzmanim_b.csv', 'a', encoding='utf-8') as csvfile: #start the csv with wanted fields
        fieldnames = ['urlnum', 'committee', 'date', 'muzmanim']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for urlnum in range(10475,0,-1): #all protocols up till now
            url="https://oknesset.org/api/v2/committeemeeting/" +str(urlnum) +"/?format=json"
        
            try:
                input = urllib.request.urlopen(url).read().decode("utf-8")
            except:
                time.sleep(5) #in case the servers times out - wait 5 seconds and try again
                
            fullprot = json.loads(input)["protocol"]
    
            for item in fullprot:
                if item["header"]=="מוזמנים": #look for relevant part of protocoal by header
                    academic=re.findall('.*ד"ר.*', item["body"])+re.findall('.*פרופ.*', item["body"]) #regex to find academics
                            
            for item in academic:
                writer.writerow({'urlnum':str(urlnum), 'committee':json.loads(input)["committee"], 'date':json.loads(input)["date"],  'muzmanim':str(item)}) #write to file
csvfile.close()