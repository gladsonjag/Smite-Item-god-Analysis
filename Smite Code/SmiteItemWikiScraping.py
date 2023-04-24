from bs4 import BeautifulSoup
import requests
import pandas
import csv
import json
import re

def main():
    #list
    ItemList = []
    

    def find_str_indexes(string, char):
        return [i for i, ltr in enumerate(string) if ltr == char]

    def get_item_data(url):
        page_to_scrape = requests.get(url)
        soup = BeautifulSoup(page_to_scrape.content, 'html.parser')
        item_data = []
        item_data_return = []

        table = soup.find("table", class_="infobox")
        for row in table.find_all("td"):
            item_data.append(row.text)
        try:
            for i in range(1,10): #runs a loop removing \n artifacts that come from scraping the HTML website
                item_data.remove('\n')
        except:
            pass
        for stat in item_data:
            if ("+") not in stat and stat != item_data[-1] and stat != item_data[1]:
                pass
            else:
                item_data_return.append(stat)

        return(item_data_return)
    
    def fileopen():
        ItemNameList = []
        ItemGoldList = []
        with open('SmiteItemNameList.csv', 'r') as f:
            reader = csv.reader(f, delimiter=',')
            
            for row in reader:
                for name_gold in row:
                    index = name_gold.find("(")
                    name = name_gold[:index - 1]
                    ItemNameList.append(name)

                    gold = name_gold[index+1:-1]
                    ItemGoldList.append(gold)

            f.close()
        return (ItemNameList, ItemGoldList)

    def create_url_list(item_name_list):
        url_list = []
        for item_name in item_name_list:
            url_list.append("https://smite.fandom.com/wiki/" + str(item_name))
        return(url_list)
   
    def filewriter(item_stats):
        with open('SmiteItemStats.csv', 'w') as f:
            for item_stat in item_stats:
                f.write(",".join(item_stat) + "\n")
            f.close()
        return

    def datacleanup(item_data, ItemName, GoldCost):
        item_n = []
        item_stats = []
        #removing the \n and removing any empty elements in the list of stats for the item
        for i in item_data:
            item  = i.replace("\n", "")
            item_ = item.replace(",", "")
            item_n.append(item_)

        #appending the tier to the front
        item_stats.append(item_n[0])

        #seperating the different stats into their indidual strings or indicies to be easily analyzed later
        if "+" in item_n[1]:
            item1 = item_n[1]
            index = find_str_indexes(item1, "+")

            if len(index) == 1:
                stat1 = item1[index[0]:]
                item_stats.append(stat1)
            if len(index) == 2:
                stat1 = item1[index[0]:index[1]-1]
                item_stats.append(stat1)
                stat2 = item1[index[1]:]
                item_stats.append(stat2)
            if len(index) == 3:
                stat1 = item1[index[0]:index[1]-1]
                item_stats.append(stat1)
                stat2 = item1[index[1]:index[2]-1]
                item_stats.append(stat2)
                stat3 = item1[index[2]:]
                item_stats.append(stat3)
            if len(index) == 4:
                stat1 = item1[index[0]:index[1]-1]
                item_stats.append(stat1)
                stat2 = item1[index[1]:index[2]-1]
                item_stats.append(stat2)
                stat3 = item1[index[2]:index[3]-1]
                item_stats.append(stat3)
                stat4 = item1[index[3]:]
                item_stats.append(stat4)
            if len(index) == 5:
                stat1 = item1[index[0]:index[1]-1]
                item_stats.append(stat1)
                stat2 = item1[index[1]:index[2]-1]
                item_stats.append(stat2)
                stat3 = item1[index[2]:index[3]-1]
                item_stats.append(stat3)
                stat4 = item1[index[3]:index[4]-1]
                item_stats.append(stat4)
                stat5 = item1[index[4]:]
                item_stats.append(stat5)
            

        #appending the passive to the end
        if ('PASSIVE') in item_n[-1] or ('AURA') in item_n[-1]:  
            item_stats.append(item_n[-1])
        #appending item name to index 0
        item_stats.insert(0, ItemName)
        #appending item gold cost to index -1
        item_stats.append(GoldCost)
        return item_stats
    
    ItemNameList, ItemGoldList = fileopen() #opens the item name csv file which contains item names and gold cost for all items each in respective list
    url_list = create_url_list(ItemNameList) #creates url list

    #A loop to get all the item data from the url list
    for url in url_list:
        name = ItemNameList[url_list.index(url)]
        gold = ItemGoldList[url_list.index(url)]

        item_data = get_item_data(url)
        ItemList.append(datacleanup(item_data, name, gold))


    
    

    filewriter(ItemList) #writes the item_stats list to a .csv file
    #also note if Tier isnt 1,2, or 3 its a glyph
    return
main()




