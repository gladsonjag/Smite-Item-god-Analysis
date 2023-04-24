import SmiteListCreator as slc
from itertools import combinations

def ItemCombinations(iterable, r):

    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    if pool[indices[0]].Gold < 2400:
        yield tuple(pool[i] for i in indices)

    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        #this if statement removes 400k + combos to make sure the build starts with phys and cheap item in first slot
        if pool[indices[0]].Gold < 2400: 
            yield tuple(pool[i] for i in indices)

def BuildCreator(ItemList, stattype, stattype2, stattype3, itemslots ):
    BuildType_l = []
    for item in ItemList:
        if item.Tier == 3 or item.Tier == 4:
            try:
                if getattr(item, stattype) > 0:
                    BuildType_l.append(item)
            except:
                print("stat was typed in wrong")
            try:
                if getattr(item, stattype2) > 0 and item not in BuildType_l:
                    BuildType_l.append(item)
            except:
                pass
            try:
                if getattr(item, stattype3) > 0 and item not in BuildType_l and not getattr(item, "Physical_Power") > 0 and not getattr(item, "Magical_Power") > 0:
                    BuildType_l.append(item)
            except:
                pass
            if item.Name == "Toxic Blade" or item.Name == "Berserker's Shield" or item.Name == "Archdruid's Fury": #removes toxic blade and berserks shield as we rarely want to build that
                BuildType_l.remove(item)

    builds = list(ItemCombinations(BuildType_l, itemslots))

    return builds

def BuildTesterDmg(BuildList, dmg_b, scaling, protections, st_power, st_Fpen, st_Ppen):

    buildlist_dmg = []
    for build in BuildList:
        BuildPower = 0
        Build_Fpen = 0
        Build_Ppen = 0
        build_copy = []

        for item in build:
            BuildPower += getattr(item, st_power)
            Build_Fpen += getattr(item, st_Fpen)
            Build_Ppen += getattr(item, st_Ppen)

            build_copy.append(item)

        build_copy.append(BuildPower)
        build_copy.append(Build_Fpen)
        build_copy.append(Build_Ppen)

        dmg = Damage((dmg_b + (scaling * BuildPower)),(Build_Ppen),(Build_Fpen),(protections)) #damage, percent pen, flat pen, protections
        build_copy.append(dmg)
        buildlist_dmg.append(build_copy)

    BuildList_S = sorted(buildlist_dmg, key = lambda x: x[-1] , reverse=True)

    return BuildList_S

def BuildTesterProts(BuildList, mage_dmg, mage_scal, mage_p, mage_Ppen, mage_Fpen, phys_dmg, phys_scal, phys_p, phys_Ppen, phys_Fpen):
     
    buildlist_prots = []
    for build in BuildList:
        Build_Pprots = 0
        Build_Mpros = 0
        Build_health = 0
        build_copy = []

        for item in build:
            Build_Pprots += getattr(item, "Physical_Protection")
            Build_Mpros += getattr(item, "Magical_Protection")
            Build_health += getattr(item, "Health")

            build_copy.append(item)

        build_copy.append(Build_Pprots)
        build_copy.append(Build_Mpros)
        build_copy.append(Build_health)


        dmg_mage = Damage((mage_dmg + (mage_scal * mage_p)),(mage_Ppen),(mage_Fpen),(Build_Mpros))
        dmg_phys = Damage((phys_dmg + (phys_scal * phys_p)),(phys_Ppen),(phys_Fpen),(Build_Pprots))
        dmg = dmg_mage + dmg_phys
        effective_health = (Build_health - dmg)
        build_copy.append(dmg)
        build_copy.append(effective_health)

        buildlist_prots.append(build_copy)

    BuildList_S = sorted(buildlist_prots, key = lambda x: x[-1], reverse=True) #sorts by highest to lowest effective health builds

    return BuildList_S

def Damage(dmg_start, percent_p, flat_p, protections):
        if percent_p > 40:
             percent_p = 40
        if flat_p > 40:
             flat_p = 40
        if protections > 325:
            protections = 325
        protections_p = protections - ((percent_p / 100) * protections)
        protections_pf = protections_p - flat_p
        dmg_taken = dmg_start * (100 / (100 + protections_pf))
        return dmg_taken

def guiCreator():
    stattype = 0
    dmg = 0
    scaling = 0
    protections = 0
    mage_dmg = 0
    mage_scal = 0
    mage_p = 0
    mage_Ppen = 0
    mage_Fpen = 0
    phys_dmg = 0
    phys_scal = 0
    phys_p = 0
    phys_Ppen = 0
    phys_Fpen = 0
    print("What stat do you want to test builds for?")
    print("Magical Power?", "Physical Power?", "Ability Protections?")
    stattype = str(input("Type: ").lower())

    if stattype == "magical power" or stattype == "Physical power":
        print("How much damage does the ability do?")
        dmg = int(input("Damage: "))
        print("How much scaling for the ability? \n EXAMPLE: 60'%' scaling = 0.6 ")
        scaling = float(input("Scaling: "))
        print("How many Prots does the enemy Have?")
        protections = int(input())

    if stattype == "ability protections":
        """
        print("Please enter the Ability Dmg, Scaling i.e 0.6, Total Power,  Percent Pen, Flat Pen for a popular Mage Build")
        mage_dmg = float((input("Damage: ")))
        mage_scal = float(input("Scaling: "))
        mage_p = float(input("Power: "))
        mage_Ppen = float(input("'%'Pen: "))
        mage_Fpen = float(input("Flat Pen: "))
        print("Please enter the Ability Dmg, Scaling i.e 0.6, Total Power,  Percent Pen, Flat Pen for a popular ability based Physical Build")
        phys_dmg = float(input("Physical Damage: "))
        phys_scal = float(input("Physical Scaling: "))
        phys_p = float(input("Power: "))
        phys_Ppen = float(input("'%'Pen: "))
        phys_Fpen = float(input("Flat Pen: "))
        """
        #Late game yu huang ult build stats from smitesource
        mage_dmg = 710
        mage_scal = 0.5
        mage_p = 680
        mage_Ppen = 20
        mage_Fpen = 10

        #late game thor ult build from smite source 
        phys_dmg = 360
        phys_scal = 1.0
        phys_p = 310
        phys_Ppen = 30
        phys_Fpen = 35

    return stattype, dmg, scaling , protections, mage_dmg, mage_scal, mage_p, mage_Ppen, mage_Fpen, phys_dmg, phys_scal, phys_p, phys_Ppen, phys_Fpen






def main():

    # opens god and item file datas from scraping the wiki in other .py programs
    ItemStatsArray = slc.FileOpenerArray("SmiteItemStats.csv")
    GodStatsArray = slc.FileOpenerArray("SmiteGodStats.csv")

    # Creates the SmiteItemList of each SmiteItem class, holding all Item Attributes
    ItemList = slc.create_ItemClass_list(ItemStatsArray)
    GodList = slc.create_godclass_list(GodStatsArray)
    
    #----------------------------------------------------------------------------------------------------------------------
    stattype, dmg, scaling , protections, mage_dmg, mage_scal, mage_p, mage_Ppen, mage_Fpen, phys_dmg, phys_scal, phys_p, phys_Ppen, phys_Fpen = guiCreator() #creates interactable UI for testing not done yet
    print("-------------------------------------------------------------------", "\n")
    

    #for best magical power build listings
    if stattype == "magical power":
        BuildsList = BuildCreator(ItemList, "Magical_Power", "stattype2", "stattype3", 6) #gets all builds for magical power items
        BestBuild = BuildTesterDmg(BuildsList, dmg, scaling, protections, "Magical_Power", "Magical_Flat_Pen", "Magical_Perc_Pen") # list of all builds with stat type, dmg, scaling, protections, stattype
        i = 1
        for build in BestBuild[0:3]:               
                print("\nNumber", i, ":")

                print(build[0].Name)
                print(build[1].Name)
                print(build[2].Name)
                print(build[3].Name)
                print(build[4].Name)
                print(build[5].Name)
                print("Power:", build[6])
                print("Flat Penetration:", build[7])
                print("Percent Penetration:", build[8], "%")
                print("Damage:", build[9])
                i += 1

    #for best physical power build listings
    if stattype == "physical power":
        BuildsList = BuildCreator(ItemList, "Physical_Power", "stattype2", "stattype3", 6) # full item list, stattype, item slots
        BestBuild = BuildTesterDmg(BuildsList, dmg, scaling, protections, "Physical_Power", "Physical_Flat_Pen", "Physical_Perc_Pen") # list of all builds with stat type, dmg, scaling, protections, stattype
        i = 1
        for build in BestBuild[0:3]:               
                print("\nNumber", i, ":")

                print(build[0].Name)
                print(build[1].Name)
                print(build[2].Name)
                print(build[3].Name)
                print(build[4].Name)
                print(build[5].Name)
                print("Power:", build[6])
                print("Flat Penetration:", build[7])
                print("Percent Penetration:", build[8], "%")
                print("Damage:", build[9])
                i += 1
    
    if stattype == "ability protections":
        BuildsList = BuildCreator(ItemList, "Physical_Protection", "Magical_Protection", "Health", 6) #gets all builds with these stats
        BestBuild = BuildTesterProts(BuildsList, mage_dmg, mage_scal, mage_p, mage_Ppen, mage_Fpen, phys_dmg, phys_scal, phys_p, phys_Ppen, phys_Fpen)

        i = 1
        for build in BestBuild[0:20]:               
            print("\nNumber", i, ":")
            print(build[0].Name)
            print(build[1].Name)
            print(build[2].Name)
            print(build[3].Name)
            print(build[4].Name)
            print(build[5].Name)
            print("Physical Protections:", build[6])
            print("Magical Protections:", build[7])
            print("Health:", build[8])
            print("Damage Taken:", build[9])
            i += 1


        
    return

main()