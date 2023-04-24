from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.oauth2 import service_account
import pandas as pd
import SmiteListCreator as slc

SERVICE_ACCOUNT_FILE = 'API_Key.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)


# The ID of a spreadsheet.
SAMPLE_SPREADSHEET_ID = '1yzMqIsI2B7Asgo-QzTDGg42YlebmikCVBxGvb72eooQ'

service = build('sheets', 'v4', credentials=creds)


# for reading
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="Items!A1").execute()
values = result.get('values', [])

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Link of google sheeet template if lost -- "https://docs.google.com/spreadsheets/d/1g8YwMLwrO59EmntXJeOV5Ciu0ts0PyC77Jhm9JM4sII/edit#gid=1092505368"

# opens god and item file datas from scraping the wiki in other .py programs
ItemStatsArray = slc.FileOpenerArray("SmiteItemStats.csv")
GodStatsArray = slc.FileOpenerArray("SmiteGodStats.csv")
# Creates the SmiteItemList of each SmiteItem class, holding all Item Attributes
ItemList = slc.create_ItemClass_list(ItemStatsArray)
GodList = slc.create_godclass_list(GodStatsArray)

#--------------PUTTING ITEM STATS INTO GOOGLE SHEET-------------------------
#creates the list of items to be put into an array to go into google sheet
gs_list = [["Name", "Cost", "Type", "Health","Phys Prots", "Mag Prots", "Physical Power", "Magical Power", "Attack Speed", "Phys Percent Pen", 
            "Mag Percent Pen", "Phys Flat Pen", "Mag Flat Pen", "Crit Chance", "Cooldown Reduction", "LifeSteal", "Mana", "HP5", "MP5", "Move Speed", "CCR", "Passives" ]]

for item in ItemList:
    list1 = []
    list1.append(item.Name)
    list1.append(item.Gold)
    #TYPE
    if item.Physical_Protection > 0 and item.Magical_Protection > 0:
        list1.append("Both")
    elif item.Physical_Power > 0 and item.Magical_Power > 0:
        list1.append("Both")    
    elif item.Physical_Protection > 0 and item.Magical_Protection == 0:
        list1.append("Physical")
    elif item.Magical_Protection > 0 and item.Physical_Protection == 0:
        list1.append("Magical")
    elif item.Physical_Power > 0 and item.Magical_Power == 0:
        list1.append("Physical")    
    elif item.Magical_Power > 0 and item.Physical_Power == 0:
        list1.append("Magical")
    elif item.Physical_Protection == 0 and item.Magical_Protection == 0 and item.Physical_Power == 0 and item.Magical_Power == 0 :
        list1.append("None")   

    list1.append(item.Health)
    list1.append(item.Physical_Protection)
    list1.append(item.Magical_Protection)
    list1.append(item.Physical_Power)
    list1.append(item.Magical_Power)
    list1.append(item.Attack_Speed)
    list1.append(item.Physical_Perc_Pen)
    list1.append(item.Magical_Perc_Pen)
    list1.append(item.Physical_Flat_Pen)
    list1.append(item.Magical_Flat_Pen)
    list1.append(item.Critical_Chance)      
    list1.append(item.Cooldown)
    list1.append(item.Life_Steal)
    list1.append(item.Mana) #mana
    list1.append(item.HP5) #HP5
    list1.append(item.MP5) #MP5
    list1.append(item.Movement_Speed) #Move Speed
    list1.append(item.CCR) #CCR
    list1.append(item.Passive)
    #appending to the array
    gs_list.append(list1)

#writes to the spreadsheet
request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, 
                                range="Items!A1", valueInputOption="USER_ENTERED", body={"values":gs_list}).execute()

#-------------PUTTING GOD STATS INTO GOOGLE SHEET-----------------------------

#Setting up the god name list
godnameslist = [["Name", "Health", "Mana", "Speed", "Range", "Attack/Sec", "AA-Dmg", 
             "Physical Protections", "Magical Protections", "HP5", "MP5" ]]

for god in GodList:
    godname = [god.Name]
    godnameslist.append(godname)
    
request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, 
                                range="Gods!C5", valueInputOption="USER_ENTERED", body={"values":godnameslist}).execute()

#First input for the base god stats
gs_list2 = [["Name", "Health_B", "Mana_B", "Speed_B", "range_B", "Attack/Sec_B", "AA-Dmg_B", 
             "Physical Protections_B", "Magical Protections_B", "HP5_B", "MP5_B" ]]

for god in GodList:
    gb_list1 = []
    gb_list1.append(god.Name)
    gb_list1.append(god.Health_b)
    gb_list1.append(god.Mana_b)
    gb_list1.append(god.Speed_b)
    gb_list1.append(god.Range_b)
    gb_list1.append(god.Attackspeed_b)
    gb_list1.append(god.BA_Damage_b)
    gb_list1.append(god.Physical_Protections_b)
    gb_list1.append(god.Magical_Protections_b)
    gb_list1.append(god.HP5_b)
    gb_list1.append(god.MP5_b)

    gs_list2.append(gb_list1)
                    
                    
#writes to the spreadsheet
request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, 
                                range="Gods_Stats!A1", valueInputOption="USER_ENTERED", body={"values":gs_list2}).execute()
#second input for the scalars
gs_list3 = [["Name", "Health_S", "Mana_S", "Speed_S", "range_S", "Attack/Sec_S", "AA-Dmg_S", 
             "Physical Protections_S", "Magical Protections_S", "HP5_S", "MP5_S" ]]

for god in GodList:
    gscal_list1 = []
    gscal_list1.append(god.Name)
    gscal_list1.append(god.Health_s)
    gscal_list1.append(god.Mana_s)
    gscal_list1.append(god.Speed_s)
    gscal_list1.append(god.Range_s)
    gscal_list1.append(god.Attackspeed_s)
    gscal_list1.append(god.BA_Damage_s)
    gscal_list1.append(god.Physical_Protections_s)
    gscal_list1.append(god.Magical_Protections_s)
    gscal_list1.append(god.HP5_s)
    gscal_list1.append(god.MP5_s)

    gs_list3.append(gscal_list1)
                    
                    
#writes to the spreadsheet
request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, 
                                range="Gods_Stats!M1", valueInputOption="USER_ENTERED", body={"values":gs_list3}).execute()
