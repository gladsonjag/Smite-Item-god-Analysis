from bs4 import BeautifulSoup
import requests
import pandas
import csv
import json
import re



def main():

    #list for main code
    GodNameList = []
    UrlList = []
    GodData = []

    #-------------------Functions-----------------
    def fileopen():
        GodNameList = []
        with open('SmiteGodNameList.csv', 'r') as f:
            reader = csv.reader(f, delimiter=',')
            
            for row in reader:
                for name in row:
                    GodNameList.append(name)
            f.close()
        return (GodNameList)
    
    def create_url_list(god_list):
        url_list = []
        for name in god_list:
            url_list.append("https://smite.fandom.com/wiki/" + str(name))
        return(url_list)
    
    def get_god_info(url_list,GodNameList):
        god_data_array = []
        for url in url_list:
            page_to_scrape = requests.get(url)
            soup = BeautifulSoup(page_to_scrape.content, 'html.parser')


            table = soup.find("table", class_="infobox")
            god_data_n = []
            god_data = []
            for row in table.find_all("td"):
                god_data_n.append(row.text)
            if len(god_data_n) == 23:
                del god_data_n[0:12]
                del god_data_n[6]
            else:
                raise ValueError("god_data does not have a len of 22") #in case an issue comes with parsing wiki and getting more or less rows
            for stat in god_data_n:
                god_data.append(stat.replace("\n", ""))

            god_data.insert(0,GodNameList[(url_list.index(url))])
            god_data_array.append(god_data)
        

        return(god_data_array)

    def filewriter(god_stats):
        with open('SmiteGodStats.csv', 'w') as f:
            for stat in god_stats:
                f.write(",".join(stat) + "\n")
            f.close()
        return
    #-------------------Functions-----------------


    #-----------------Main Code----------------------
    GodNameList = fileopen()
    UrlList = create_url_list(GodNameList)
    GodDataArray = get_god_info(UrlList, GodNameList) #GodNameList is just to append to 0 index before writing to file

    filewriter(GodDataArray)



 





    return
main()