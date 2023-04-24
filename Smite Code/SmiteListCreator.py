import csv
import re
import pandas as pd
import numpy as np



class Item:  # Class that holds all SmiteItem Attributes 

        Name: str
        Gold: int
        Tier: int  # 4 is glyph
        Physical_Power: int
        Physical_Flat_Pen: int
        Physical_Perc_Pen: int
        Physical_Protection: int
        Magical_Power: int
        Magical_Flat_Pen: int
        Magical_Perc_Pen: int
        Magical_Protection: int
        Attack_Speed: int
        Critical_Chance: int
        Cooldown: int
        Movement_Speed: int
        Life_Steal: int
        Health: int
        HP5: int
        MP5: int
        Mana: int
        CCR: int
        Passive: str

        def __init__(self, Name, Gold, Stats):

            self.Name = Name
            self.Gold = Gold
            self.Tier = 0  # 4 is glyph
            self.Physical_Power = 0
            self.Physical_Flat_Pen = 0
            self.Physical_Perc_Pen = 0
            self.Physical_Protection = 0
            self.Magical_Power = 0
            self.Magical_Flat_Pen = 0
            self.Magical_Perc_Pen = 0
            self.Magical_Protection = 0
            self.Attack_Speed = 0
            self.Critical_Chance = 0
            self.Cooldown = 0
            self.Movement_Speed = 0
            self.Life_Steal = 0
            self.Health = 0
            self.HP5 = 0
            self.Mana = 0
            self.MP5 = 0
            self.CCR = 0
            self.Passive = "Passive - N/A"

            # checks what Tier the item is 4 means its a glyph
            if "Tier 1" in Stats[1] or "Tier 2" in Stats[1] or "Tier 3" in Stats[1]:
                self.Tier = int(re.sub(r'[^0-9]', '', Stats[1]))
            else:
                self.Tier = 4

            # Getting the Passive to not interfer with the Loop below getting integers for all the Item Stats
            if "PASSIVE" in Stats[-2] or "AURA" in Stats[-2]:
                self.Passive = str(Stats[-2])
                Stats.remove(Stats[-2])

            # getting all the stats to the correct attributes
            for stat in Stats[2:-1]:
                if "Physical Power" in stat:
                    self.Physical_Power = int(re.sub(r'[^0-9]', '', stat))
                if "Physical Penetration" in stat and "%" not in stat:
                    self.Physical_Flat_Pen = int(re.sub(r'[^0-9]', '', stat))
                if "% Physical Penetration" in stat:
                    self.Physical_Perc_Pen = int(re.sub(r'[^0-9]', '', stat))
                if "Physical Protection" in stat:
                    self.Physical_Protection = int(re.sub(r'[^0-9]', '', stat))
                if "Magical Power" in stat:
                    self.Magical_Power = int(re.sub(r'[^0-9]', '', stat))
                if "Magical Penetration" in stat and "%" not in stat:
                    self.Magical_Flat_Pen = int(re.sub(r'[^0-9]', '', stat))
                if "% Magical Penetration" in stat:
                    self.Magical_Perc_Pen = int(re.sub(r'[^0-9]', '', stat))
                if "Magical Protection" in stat:
                    self.Magical_Protection = int(re.sub(r'[^0-9]', '', stat))
                if "Attack Speed" in stat:
                    self.Attack_Speed = int(re.sub(r'[^0-9]', '', stat))
                if "Critical Strike Chance" in stat:
                    self.Critical_Chance = int(re.sub(r'[^0-9]', '', stat))
                if "Cooldown Reduction" in stat:
                    self.Cooldown = int(re.sub(r'[^0-9]', '', stat))
                if "Movement Speed" in stat:
                    self.Movement_Speed = int(re.sub(r'[^0-9]', '', stat))
                if "Lifesteal" in stat:
                    self.Life_Steal = int(re.sub(r'[^0-9]', '', stat))
                if "Health" in stat:
                    self.Health = int(re.sub(r'[^0-9]', '', stat))
                if "HP5" in stat:
                    hp5_ = (re.sub(r'[^0-9]', '', stat))
                    self.HP5 = int(hp5_[:-1]) #this removes the extra 5 left behind from the text HP5
                if "Mana" in stat:
                    self.Mana = int(re.sub(r'[^0-9]', '', stat))
                if "MP5" in stat:
                    mp5_ = (re.sub(r'[^0-9]', '', stat))
                    self.MP5 = int(mp5_[:-1]) #this removes the extra 5 left behind from the text MP5
                if "Crowd Control Reduction" in stat:
                    self.CCR = int(re.sub(r'[^0-9]', '', stat))

            return
class God:  # Class that holds all SmiteGod Attributes

        # Varibles meant to be updated with update function based on input level
        Name: str
        Health: float
        Mana: float
        Speed: float
        Range: float
        Attackspeed: float
        BA_Damage: float
        Physical_Protections: float
        Magical_Protections: float
        HP5: float
        MP5: float
        # Base Stats used in update function
        Health_b: float
        Mana_b: float
        Speed_b: float
        Range_b: float
        Attackspeed_b: float
        BA_Damage_b: float
        Physical_Protections_b: float
        Magical_Protections_b: float
        HP5_b: float
        MP5_b: float
        # Scalars for Leveling
        Health_s: float
        Mana_s: float
        Speed_s: float
        Range_s: float
        Attackspeed_s: float
        BA_Damage_s: float
        Physical_Protections_s: float
        Magical_Protections_s: float
        HP5_s: float
        MP5_s: float

        # update function that changes attributes based on inpute level for god object
        def update(self, level):
            level = level - 1
            if level <= 20:
                self.Health = self.Health_b + (level * self.Health_s)
                self.Mana = self.Mana_b + (level * self.Mana_s)
                self.Speed = self.Speed_b + (level * self.Speed_s)
                self.Range = self.Range_b + (level * self.Range_s)
                self.Attackspeed = self.Attackspeed_b + (level * self.Attackspeed_s)
                self.BA_Damage = self.BA_Damage_b + (level * self.BA_Damage_s)
                self.Physical_Protections = self.Physical_Protections_b + (level * self.Physical_Protections_s)
                self.Magical_Protections = self.Magical_Protections_b + (level * self.Magical_Protections_s)
                self.HP5 = self.HP5_b + (level * self.HP5_s)
                self.MP5 = self.MP5_b + (level * self.MP5_s)
            else:
                raise ValueError("No Gods above level 20")
            return self

        def __init__(self, Name, god_base_stats, god_scalar_stats):

            # Zero defualt values
            self.Name = Name
            self.Health = 0
            self.Mana = 0
            self.Speed = 0
            self.Range = 0
            self.Attackspeed = 0
            self.BA_Damage = 0
            self.Physical_Protections = 0
            self.Magical_Protections = 0
            self.HP5 = 0
            self.MP5 = 0

            # get all base Stats in for lvl 1 God
            self.Health_b = god_base_stats[0]
            self.Mana_b = god_base_stats[1]
            self.Speed_b = god_base_stats[2]
            self.Range_b = god_base_stats[3]
            self.Attackspeed_b = god_base_stats[4]
            self.BA_Damage_b = god_base_stats[5]
            self.Physical_Protections_b = god_base_stats[6]
            self.Magical_Protections_b = god_base_stats[7]
            self.HP5_b = god_base_stats[8]
            self.MP5_b = god_base_stats[9]

            # get all the scalar stats to level the Gods properly
            self.Health_s = god_scalar_stats[0]
            self.Mana_s = god_scalar_stats[1]
            self.Speed_s = god_scalar_stats[2]
            self.Range_s = god_scalar_stats[3]
            self.Attackspeed_s = god_scalar_stats[4]
            self.BA_Damage_s = god_scalar_stats[5]
            self.Physical_Protections_s = god_scalar_stats[6]
            self.Magical_Protections_s = god_scalar_stats[7]
            self.HP5_s = god_scalar_stats[8]
            self.MP5_s = god_scalar_stats[9]

            return
def FileOpenerArray(filename):
        array = []
        with open(filename, 'r') as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                list1 = []
                for stat in row:
                    list1.append(stat)
                array.append(list1)
        return array
def create_ItemClass_list(ItemStatsArray):
        ItemList = []
        for item_ in ItemStatsArray:
            SmiteItem = Item(item_[0], int(item_[-1]), item_)
            ItemList.append(SmiteItem)

        return ItemList
def create_godclass_list(god_stats_array):
        GodList = []

        # getting base stats and scalars seperating to be allocated correctly to the base and scalar attribute respectively
        for god in god_stats_array:
            base_stat_list = []
            scalar_stat_list = []

            for stat in god:
                if "(" in stat and stat != god[6]:
                    stat1 = stat
                    stat2 = stat
                    i = stat.index("(")
                    try:
                        i2 = stat.index("%")
                    except:
                        i2 = stat.index(")")
                    # for base stat list
                    base_stat_list.append(float(stat1[:i-1]))
                    # for scalar stat list
                    scalar_stat_list.append(float(stat2[i+2:i2]))

                # to ignore the power scaling part of the attack power stat
                if stat == god[6]:
                    i3 = stat.index("(")
                    i4 = stat.index(")")
                    base_stat_list.insert(6, float(stat[:i3]))
                    scalar_stat_list.insert(6, float(stat[i3+3:i4]))

            # creates the God Object and appends to the list of all god objects with attributes
            SmiteGod = God(god[0], base_stat_list, scalar_stat_list)
            GodList.append(SmiteGod)

        return GodList


        # using the ratio we can turn physical protections into an equivilent magical protection scale to allow for better # comparison
        ratio = avg_mag_prots / avg_phys_prots
        all_prot = physical_protection * ratio
        return all_prot





        return

    
def main():
    # opens god and item file datas from scraping the wiki in other .py programs
    ItemStatsArray = FileOpenerArray("SmiteItemStats.csv")
    GodStatsArray = FileOpenerArray("SmiteGodStats.csv")

    # Creates the SmiteItemList of each SmiteItem class, holding all Item Attributes
    ItemList = create_ItemClass_list(ItemStatsArray)
    GodList = create_godclass_list(GodStatsArray)


main()



