#Program is ran to cleanup the copy and pasted list of items from the SMITE WIKI
import csv
import json

#--------initializing all necessary list-----------
ItemNameList = []
ItemNameMessy = []


def main():

    
    def NameCSV_clean(item_name_list_messy):
        ItemNameList = []
        BaseNameList = []
        for name in item_name_list_messy:
            if ".png" in name:
                index = (name.find(".png")) + 5
                name_clean = name[index:len(name)]
                ItemNameList.append(name_clean)
                if "(9999)" in name:
                    ItemNameList.remove(name_clean)

        #only using Evolved stacking items and replacing it in the list for the base one
        for name1 in ItemNameList:
            if "Evolved" in name1:
                BaseName = name1[8:]
                BaseNameList.append(BaseName)

        for basename1 in BaseNameList:
            for item in ItemNameList:
                if basename1 in item:
                    index = ItemNameList.index(item)
                    item_evolved = "Evolved " + item
                    ItemNameList[index] = item_evolved
        
        #bugged where its skipping over items that dont contain gold cost and i just ran loop 4 times to catch them all
        for item1 in ItemNameList:
            if ")" not in item1:
                ItemNameList.remove(item1)
        for item2 in ItemNameList:
            if "(" not in item2:
                ItemNameList.remove(item2)
        for item3 in ItemNameList:
            if "Evolved Evolved" in item3:
                ItemNameList.remove(item3)
        for item4 in ItemNameList:
            if "Evolved Evolved" in item4:
                ItemNameList.remove(item4)


        ItemNameList =  sorted(ItemNameList)
        
        return(ItemNameList)
    
    def FileOpener():
        ItemNameMessy = []
        with open('SmiteItemNameList.csv', 'r') as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                for name in row:
                    ItemNameMessy.append(name)
            f.close
        return(ItemNameMessy)
    
    def writer(ItemNameList):
        with open('SmiteItemNameList.csv', 'w') as f:
            for Name in ItemNameList:
                f.write(Name + "\n")
            f.close()





    ItemNameMessy = FileOpener() #opens the item name csv file to get the messy list
    ItemNameList = NameCSV_clean(ItemNameMessy)
    writer(ItemNameList) #writes the ItemNameList to SmiteItemNamelist.csv


    return
main()