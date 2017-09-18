# dry inventory

def main ():

    import datetime
    today = datetime.date.today()
    name = input("Inventory Taker: ")

    print("DRY GOODS")
    print()
    rTom = int(input("Enter amount of cases of Roma Tomatoes: "))
    while rTom > 6 or rTom < 0:
        rTom = int(input("Enter amount of cases of Roma Tomatoes: "))

    yOs = input("Do we need a bag of Yellow Onion?: ")
    while yOs != "yes" and yOs != "no":
        yOs = input("Do we need a bag of Yellow Onion?: ")

    pbc = input("Do we need a bag of Panko Bread Crumbs?: ")
    while pbc != "yes" and pbc != "no":
        pbc = input("Do we need a bag of Panko Bread Crumbs?: ")

    bc = input("Do we need regular Bread Crumbs?: ")
    while bc != "yes" and bc != "no":
        bc = input("Do we need regular Bread Crumbs?: ")

    crp = int(input("Enter amount of bags of Crushed Red Pepper: "))
    while crp > 4 or crp < 0:
        crp = int(input("Enter amount of bags of Crushed Red Pepper: "))

    srch = int(input("Enter amount of bottles of Sriracha: "))
    while srch > 6 or srch < 0:
        srch = int(input("Enter amount of bottles of Sriracha: "))

    npj = input("Do we need Nacho-Style Pickled Jalapenos?: ")
    while npj != "yes" and npj != "no":
        npj = input("Do we need Nacho-Style Pickled Jalapenos?: ")

    kalO = int(input("Enter amount of containers of Kalamata Olives: "))
    while kalO > 6 or kalO < 0:
        kalO = int(input("Enter amount of containers of Kalamata Olives: "))

    garb = int(input("Enter amount of bags of Garbanzo Beans: "))
    while garb > 3 or garb < 0:
        garb = int(input("Enter amount of bags of Garbanzo Beans: "))

    jasR = input("Do we need a bag of Jasmine Rice?: ")
    while jasR != "yes" and jasR != "no":
        jasR = input("Do we need a bag of Jasmine Rice?: ")

    walns = int(input("Enter amount of bags of Walnuts: "))
    while walns > 4 or walns < 0:
        walns = int(input("Enter amount of bags of Walnuts: "))

    alms = int(input("Enter amount of bags of Almonds: "))
    while alms > 2 or alms < 0:
        alms = int(input("Enter amount of bags of Almonds: "))

    ketc = int(input("Enter amount of containers of Ketchup: "))
    while ketc > 6 or ketc < 0:
        ketc = int(input("Enter amount of containers of Ketchup: "))

    mayoK = int(input("Enter amount of containers of Kraft Mayo: "))
    while mayoK > 6 or mayoK < 0:
        mayoK = int(input("Enter amount of containers of Kraft Mayo: "))

    mustS = int(input("Enter amount of containers of Spicy Mustard: "))
    while mustS > 6 or mustS < 0:
        mustS = int(input("Enter amount of containers of Spicy Mustard: "))

    short = int(input("Enter amount of Shortening (clear fryer oil): "))
    while short > 5 or short < 0:
        short = int(input("Enter amount of Shortening (clear fryer oil): "))

    evoo = int(input("Enter amount of Evoo: "))
    while evoo > 3 or evoo < 0:
        evoo = int(input("Enter amount of Evoo: "))

    bsug = input("Do we need a container of Brown Sugar?: ")
    while bsug != "yes" and bsug != "no":
        bsug = input("Do we need a container of Brown Sugar?: ")

    wsug = input("Do we need a container of White Sugar?: ")
    while wsug != "yes" and wsug != "no":
        wsug = input("Do we need a container of White Sugar?: ")

    bpwd = input("Do we need a container of Baking Powder?: ")
    while bpwd != "yes" and bpwd != "no":
        bpwd = input("Do we need a container of Baking Powder?: ")

    jtah = input("Do we need a Jug of Tahini?: ")
    while jtah != "yes" and jtah != "no":
        jtah = input("Do we need a Jug of Tahini?: ")

    chips = input("Do we need chips?: ")
    while chips != "yes" and chips != "no":
        chips = input("Do we need chips?: ")
    print()

    print("SPICES")
    print()
    sumac = input("Do we need a container of Sumac?: ")
    while sumac != "yes" and sumac != "no":
        sumac = input("Do we need a container of Sumac?: ")

    ksalt = input("Do we need a container of Kosher Salt?: ")
    while ksalt != "yes" and ksalt != "no":
        ksalt = input("Do we need a container of Kosher Salt?: ")

    salt = input("Do we need a container of Plain Salt?: ")
    while salt != "yes" and salt != "no":
        salt = input("Do we need a container of Plain Salt?: ")

    blpep = input("Do we need a container of Black Pepper?: ")
    while blpep != "yes" and blpep != "no":
        blpep = input("Do we need a container of Black Pepper?: ")

    cpep = input("Do we need a container of Cracked Pepper?: ")
    while cpep != "yes" and cpep != "no":
        cpep = input("Do we need a container of Cracked Pepper?: ")

    grangar = input("Do we need a container of Granulated Garlic?: ")
    while grangar != "yes" and grangar != "no":
        grangar = input("Do we need a container of Granulated Garlic?: ")

    opow = input("Do we need a container of Onion Powder?: ")
    while opow != "yes" and opow != "no":
        opow = input("Do we need a container of Onion Powder?: ")

    cpow = input("Do we need a container of Curry Powder?: ")
    while cpow != "yes" and cpow != "no":
        cpow = input("Do we need a container of Curry Powder?: ")

    pap = input("Do we need a container of Paprika?: ")
    while pap != "yes" and pap != "no":
        pap = input("Do we need a container of Paprika?: ")

    chpow = input("Do we need a container of Chili Powder?: ")
    while chpow != "yes" and chpow != "no":
        chpow = input("Do we need a container of Chili Powder?: ")

    cumin = input("Do we need a container of Cumin?: ")
    while cumin != "yes" and cumin != "no":
        cumin = input("Do we need a container of Cumin?: ")

    caypep = input("Do we need a container of Cayenne Pepper?: ")
    while cumin != "yes" and cumin != "no":
        caypep = input("Do we need a container of Cayenne Pepper?: ")

    corsd = input("Do we need a container of Whole Corriander Seed?: ")
    while corsd != "yes" and corsd != "no":
        corsd = input("Do we need a container of Whole Corriander Seed?: ")

    cusd = input("Do we need a container of Whole Cumin Seed?: ")
    while cusd != "yes" and cusd != "no":
        cusd = input("Do we need a container of Whole Cumin Seed?: ")
    print()

    print("DRINKS")
    print()
    water = int(input("Enter amount of cases of Water: "))
    while water > 6 or water < 0:
        water = int(input("Enter amount of cases of Water: "))

    dietC = int(input("Enter amount of cases of Diet Coke: "))
    while dietC > 2 or dietC < 0:
        dietC = int(input("Enter amount of cases of Diet Coke: "))

    coke = int(input("Enter amount of cases of Coke: "))
    while coke > 2 or coke < 0:
        coke = int(input("Enter amount of cases of Coke: "))

    sprite = int(input("Enter amount of cases of Sprite: "))
    while sprite > 2 or sprite < 0:
        sprite = int(input("Enter amount of cases of Sprite: "))

    topo = int(input("Enter amount of cases of Topo Chico: "))
    while topo > 2 or topo < 0:
        topo = int(input("Enter amount of cases of Topo Chico: "))

    cokeM = int(input("Enter amount of cases of Mexican Coke: "))
    while cokeM > 2 or cokeM < 0:
        cokeM = int(input("Enter amount of cases of Mexican Coke: "))

    print()

    print("RAW MATERIALS")
    print()
    wax = input("Do we need a case of Wax Paper (12 x 11.5)?: ")
    while wax != "yes" and wax != "no":
        wax = input("Do we need a case of Wax Paper (12 x 11.5)?: ")

    foil = input("Do we need a case of Foil Sheets?(12 x 11.25: ")
    while foil != "yes" and foil != "no":
        foil = input("Do we need a case of Foil Sheets?(12 x 11.25: ")

    polM = input("Do we need a case of medium size Poly Gloves?: ")
    while polM != "yes" and polM != "no":
        polM = input("Do we need a case of medium size Poly Gloves?: ")

    polL = input("Do we need a case of large size Poly Gloves?: ")
    while polL != "yes" and polL != "no":
        polL = input("Do we need a case of large size Poly Gloves?: ")

    vinM = input("Do we need a case of medium size Vinyl Gloves?: ")
    while vinM != "yes" and vinM != "no":
        vinM = input("Do we need a case of medium size Vinyl Gloves?: ")

    vinL = input("Do we need a case of large size Vinyl Gloves?: ")
    while vinL != "yes" and vinL != "no":
        vinL = input("Do we need a case of large size Vinyl Gloves?: ")

    foilB = input("Do we need a case of Foil Bowls?: ")
    while foilB != "yes" and foilB != "no":
        foilB = input("Do we need a case of Foil Bowls?: ")

    clfb = input("Do we need a case of Clear Lids for Foil Bowls?: ")
    while clfb != "yes" and clfb != "no":
        clfb = input("Do we need a case of Clear Lids for Foil Bowls?: ")

    sugP = input("Do we need a case of Sugar Packs?: ")
    while sugP != "yes" and sugP != "no":
        sugP = input("Do we need a case of Sugar Packs?: ")

    papT = input("Do we need a case of Paper Towels?: ")
    while papT != "yes" and papT != "no":
        papT = input("Do we need a case of Paper Towels?: ")

    saran = input("Do we need a case of Saran Wrap?: ")
    while saran != "yes" and saran != "no":
        saran = input("Do we need a case of Saran Wrap?: ")

    Lfoil = input("Do we need a case of Large Aluminum Foil?: ")
    while Lfoil != "yes" and Lfoil != "no":
        Lfoil = input("Do we need a case of Large Aluminum Foil?: ")

    bupap = input("Do we need a case of Butcher Paper?: ")
    while bupap != "yes" and bupap != "no":
        bupap = input("Do we need a case of Butcher Paper?: ")

    cater = input("Do we need a case of Foil Catering Content and Lids?: ")
    while cater != "yes" and cater != "no":
        cater = input("Do we need a case of Foil Catering Content and Lids?: ")

    bklvP = input("Do we need a case of White Cupcake Paper for Baklava?: ")
    while bklvP != "yes" and bklvP != "no":
        bklvP = input("Do we need a case of White Cupcake Paper for Baklava?: ")

    print()

    print("CLEANING SUPPLIES")
    print()
    stw = input("Do we need a case of Steel Wool?: ")
    while stw != "yes" and stw != "no":
        stw = input("Do we need a case of Steel Wool?: ")

    tbags = input("Do we need a case of Trash bags?: ")
    while tbags != "yes" and tbags != "no":
        tbags = input("Do we need a case of Trash bags?: ")

    fon = input("Do we need a case of 409?: ")
    while fon != "yes" and fon != "no":
        fon = input("Do we need a case of 409?: ")

    deg = input("Do we need a case of Degreaser?: ")
    while deg != "yes" and deg != "no":
        deg = input("Do we need a case of Degreaser?: ")

    sant = input("Do we need a case of Sanitizing Soap?: ")
    while sant != "yes" and sant != "no":
        sant = input("Do we need a case of Sanitizing Soap?: ")

    dsoap = input("Do we need a case of Dawn Soap?: ")
    while dsoap != "yes" and dsoap != "no":
        dsoap = input("Do we need a case of Dawn Soap?: ")

    blc = input("Do we need a case of Bleach?: ")
    while blc != "yes" and blc != "no":
        blc = input("Do we need a case of Bleach?: ")

    gcln = input("Do we need a case of Grill Cleaner?: ")
    while gcln != "yes" and gcln != "no":
        gcln = input("Do we need a case of Grill Cleaner?: ")

    print("\n\n\n\n\n")
    print("ORDER LIST:")
    print()
    print("DRY GOODS:")
    print()
    # Roma Tomatoes
    if rTom >= 6:
        pass
    else:
        rTom = 6 - rTom
        print("Order", rTom, "cases of Roma Tomatoes.")
    # Yellow Onion
    if yOs == "yes":
        print("Order 1 bag of Yellow Onions.")
    # Panko Bread Crumb
    if pbc == "yes":
        print("Order 1 bag of Panko Bread Crumbs.")
    # Regular Bread Crumb
    if bc == "yes":
        print ("Order 1 bag of regular Bread Crumbs.")
    # Bag Crushed Red Pepper
    if crp >= 4:
        pass
    else:
        crp = 4 - crp
        print("Order", crp, "bags of Crushed Red Pepper.")
    # Sriracha
    if srch >= 6:
        pass
    else:
        srch = 6 - srch
        print("Order", srch, "bottles of Sriracha.")
    # Nacho-Style Pickled Jalapenos
    if npj == "yes":
        print("Order 1 bag of Naco-Style Pickled Jalapenos.")
    # Kalamata Olives
    if kalO >= 6:
        pass
    else:
        kalO = 6 - kalO
        print("Order", kalO, "containers of Kalamata Olives.")
    # Garbanzo Beans
    if garb >= 3:
        pass
    else:
        garb = 3 - garb
        print("Order", garb, "bags of Garbanzo Beans.")
    # Jasmine Rice
    if jasR == "yes":
        print("Order 1 bag of Jasmine Rice.")
    # Walnuts
    if walns >= 4:
        pass
    else:
        walns = 4 - walns
        print("Order", walns, "bags of Walnuts.")
    # Almonds
    if alms >= 2:
        pass
    else:
        alms = 2 - alms
        print("Order", alms, "bags of Almonds.")
    # Ketchup
    if ketc >= 6:
        pass
    else:
        ketc = 6 - ketc
        print("Order", ketc, "containers of Ketchup.")
    # Kraft Mayo
    if mayoK >= 6:
        pass
    else:
        mayoK = 6 - mayoK
        print("Order", mayoK, "containers of Kraft Mayo.")
    # Spicy Mustard
    if mustS >= 6:
        pass
    else:
        mustS = 6 - mustS
        print("Order", mustS, "containers of Spicy Mustard.")
    # Shortening (clear fryer oil)
    if short >= 5:
        pass
    else:
        short = 5 - short
        print("Order", short, "boxes of Shortening.")
    # Evoo
    if evoo >= 3:
        pass
    else:
        evoo = 3 - evoo
        print("Order", evoo, "containers of Evoo.")
    # Brown Sugar
    if bsug == "yes":
        print("Order 1 container of Brown Sugar.")
    # White Sugar
    if wsug == "yes":
        print("Order 1 container of White Sugar.")
    # Baking Powder
    if bpwd == "yes":
        print("Order 1 container of Baking Powder.")
    # Jug of Tahini
    if jtah == "yes":
        print("Order 1 jug of Tahini.")
    # Chips
    if chips == "yes":
        print("Order 1 container of Chips.")
    print()

    print("SPICES:")
    print()
    # Sumac
    if sumac == "yes":
        print("Order 1 container of Sumac.")
    # Kosher Salt
    if ksalt == "yes":
        print("Order 1 container of Kosher Salt.")
    # Plain Salt
    if salt == "yes":
        print("Order 1 container of Plain Salt.")
    # Black Pepper
    if blpep == "yes":
        print("Order 1 container of Black Pepper.")
    # Cracked Pepper
    if cpep == "yes":
        print("Order 1 container of Cracked Pepper.")
    # Granulated Garlic
    if grangar == "yes":
        print("Order 1 container of Granulated Garlic.")
    # Onion Powder
    if opow == "yes":
        print("Order 1 container of Onion Powder.")
    # Curry Powder
    if cpow == "yes":
        print("Order 1 container of Curry Powder.")
    # Paprika
    if pap == "yes":
        print("Order 1 container of Paprika.")
    # Chili Powder
    if chpow == "yes":
        print("Order 1 container of Chili Powder.")
    # Cumin
    if cumin == "yes":
        print("Order 1 container of Cumin.")
    # Cayenne Pepper
    if caypep == "yes":
        print("Order 1 container of Cayenne Pepper.")
    # Whole Corriander Seed
    if corsd == "yes":
        print("Order 1 container of Whole Corriander Seed.")
    # Whole Cumin Seed
    if cusd == "yes":
        print("Order 1 container of Whole Cuminn Seed.")
    print()

    print("DRINKS:")
    print()
    # Water
    if water >= 6:
        pass
    else:
        water = 6 - water
        print("Order", water, "cases of Water.")
    # Diet Coke
    if dietC >= 2:
        pass
    else:
        dietC = 2 - dietC
        print ("Order", dietC, "cases of Diet Coke.")
    # Coke
    if coke >= 2:
        pass
    else:
        coke = 2 - coke
        print("Order", coke, "cases of Coke.")
    # Sprite
    if sprite >= 2:
        pass
    else:
        sprite = 2 - sprite
        print("Order", sprite, "cases of Sprite.")
    # Topo Chico
    if topo >= 2:
        pass
    else:
        topo = 2 - topo
        print("Order", topo, "cases of Topo Chico.")
    # Mexican Coke
    if cokeM >= 2:
        pass
    else:
        cokeM = 2 - cokeM
        print("Order", cokeM, "cases of Mexican Coke.")
    print()

    print("RAW MATERIALS:")
    print()
    # Wax Paper
    if wax == "yes":
        print("Order 1 case of Wax Paper (12 x 11.25.")
    # Foil Sheets
    if foil == "yes":
        print("Order 1 case of Foil Sheets (12 x 11.25).")
    # Poly Gloves (medium)
    if polM == "yes":
        print("Order 1 case of medium size Poly Gloves.")
    # Poly Gloves (large)
    if polL == "yes":
        print("Order 1 case of large size Poly Gloves.")
    # Vinyl Gloves (medium)
    if vinM == "yes":
        print("Order 1 case of medium size Vinyl Gloves.")
    # Vinyl Gloves (large)
    if vinL == "yes":
        print("Order 1 case of large size Vinyl Gloves.")
    # Foil Bowls
    if foilB == "yes":
        print("Order 1 case of Foil Bowls.")
    # Clear Lids (for foil bowls)
    if clfb == "yes":
        print("Order 1 case of Clear Lids for Foil Bowls.")
    # Sugar Packs (splenda and stir sticks)
    if sugP == "yes":
        print("Order 1 case of Sugar Packs (spleda and stir sticks).")
    # Paper Towels
    if papT == "yes":
        print("Order 1 case of Paper Towels.")
    # Saran Wrap
    if saran == "yes":
        print("Order 1 case of Saran Wrap.")
    # Large Aluminum Foil
    if Lfoil == "yes":
        print("Order 1 case of Large Aluminum Foil.")
    # Butcher Paper
    if bupap == "yes":
        print("Order 1 case of Butcher Paper.")
    # Foil Catering Containers and Lids
    if cater == "yes":
        print("Order 1 case of Foil Catering Containers and Lids.")
    # White Cupcake Paper for Baklava
    if bklvP == "yes":
        print("Order 1 case of White Cupcake Paper for Baklava.")
    print()


    print("CLEANING SUPPLIES:")
    print()
    # Steel Wool
    if stw == "yes":
        print("Order 1 case of Steel Wool.")
    # Trash Bags
    if tbags == "yes":
        print("Order 1 case of Trash Bags.")
    # 409
    if fon == "yes":
        print("Order 1 case of 409.")
    # Degreaser
    if deg == "yes":
        print("Order 1 case of Degreaser.")
    # Sanitizing Tablets
    if sant == "yes":
        print("Order 1 case of Sanitizing Tablets.")
    # Dawn Soap
    if dsoap == "yes":
        print("Order 1 case of Dawn Soap.")
    # Bleach
    if blc == "yes":
        print("Order 1 case of Bleach.")
    # Grill Cleaner
    if gcln == "yes":
        print("Order 1 case of Grill Cleaner.")

    print()
    print()
    print("Date:", today)
    print(name)


main()