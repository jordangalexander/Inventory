# cold inventory

def main ():

    import datetime
    today = datetime.date.today()
    name = input("Inventory Taker: ")

    print ("COLD PRODUCE")
    print ()
    mint = input("Is the bag of mint less than half full?: ")
    while mint != "yes" and mint != "no":
        mint = input("Is the bag of mint less than half full?: ")
    spMix = int(input("Enter amount of boxes of spring mix: "))
    while spMix > 6 or spMix < 0:
        spMix = int(input("Enter amount of boxes of spring mix: "))
    lem = input("Is the case of lemons less than half full?: ")
    while lem != "yes" and lem != "no":
        lem = input("Is the case of lemons less than half full?: ")
    lim = input("Is the case of limes less than half full?: ")
    while lim != "yes" and lim != "no":
        lem = input("Is the case of limes less than half full?: ")
    shroom = input("Do we need mushrooms?: ")
    while shroom != "yes" and shroom != "no":
        shroom = input("Do we need mushrooms?: ")
    arug = input("Do we need a case of arugula?: ")
    while arug != "yes" and arug != "no":
        arug = input("Do we need a case of arugula?: ")
    bruss = input("Do we need a case of brussels sprouts?: ")
    while arug != "yes" and arug != "no":
        bruss = input("Do we need a case of brussels sprouts?: ")
    avo = input("Do we need a case of avocado?: ")
    while avo != "yes" and avo != "no":
        avo = input("Do we need a case of avocado?: ")
    haba = input("Do we need a bag of habanero?: ")
    while haba != "yes" and haba != "no":
        haba = input("Do we need a bag of habanero?: ")
    serrano = input("Do we need a bag of serrano?: ")
    while serrano != "yes" and serrano != "no":
        serrano = input("Do we need a bag of serrano?: ")
    jalps = input("Do we need a bag of jalapenos?: ")
    while jalps != "yes" and jalps != "no":
        jalps = input("Do we need a bag of jalapenos?: ")
    redOs = int(input("Enter amount of bags of Red Onions: "))
    while redOs > 2 or redOs < 0:
        redOs = int(input("Enter amount of bags of Red Onions: "))
    flParsley = input("Do we need flat leaf parsley?: ")
    while flParsley != "yes" and flParsley != "no":
        flParsley = input("Do we need flat leaf parsley?: ")
    cParsley = input("Do we need curly parsley?: ")
    while cParsley != "yes" and cParsley != "no":
        cParsley = input("Do we need curly parsley?: ")
    spin = input("Do we need a bag of spinach?: ")
    while spin != "yes" and spin != "no":
        spin = input("Do we need a bag of spinach?: ")
    cilan = input("Do we need a case of cilantro?: ")
    while cilan != "yes" and cilan != "no":
        cilan = input("Do we need a case of cilantro?: ")
    carrot = input("Do we need a bag of carrots?: ")
    while carrot != "yes" and carrot != "no":
        carrot = input("Do we need a bag of carrots?: ")
    potato = input("Do we need a bag of potatoes?: ")
    while potato != "yes" and potato != "no":
        potato = input("Do we need a bag of potatoes?: ")
    rBP = input("Do we need a case of red bell peppers?: ")
    while rBP != "yes" and rBP != "no":
        rBP = input("Do we need a case of red bell peppers?: ")
    pob = input("Do we need a case of poblano?: ")
    while pob != "yes" and pob != "no":
        pob = input("Do we need a case of poblano?: ")
    eggP = input("Do we need a case of eggplant: ")
    while eggP != "yes" and eggP != "no":
        eggP = input("Do we need a case of eggplant: ")
    cucu = input("Do we need a case of cucumbers?: ")
    while cucu != "yes" and cucu != "no":
        cucu = input("Do we need a case of cucumbers?: ")
    zucc = input("Do we need a case of zucchini?: ")
    while zucc != "yes" and zucc != "no":
        zucc = input("Do we need a case of zucchini?: ")
    chTom = int(input("Enter amount of containers of Cherry Tomatoes: "))
    while chTom > 6 or chTom < 0:
        chTom = int(input("Enter amount of containers of Cherry Tomatoes: "))
    leeks = input("Do we need a case of Leeks?: ")
    while leeks != "yes" and leeks != "no":
        leeks = input("Do we need a case of Leeks?: ")
    ging = input("Do we need a bag of ginger?: ")
    while ging != "yes" and ging != "no":
        ging = input("Do we need a bag of ginger?: ")
    eggW = int(input("Enter amount of Egg Wash: "))
    while eggW > 6 or eggW < 0:
        eggW = int(input("Enter amount of Egg Wash: "))
    garl = int(input("Enter amount of bags of Garlic: "))
    while garl > 2 or garl < 0:
        garl = int(input("Enter amount of bags of Garlic: "))
    shLett = int(input("Enter amount of cases of Shredded Lettuce: "))
    while shLett > 7 or shLett < 0:
        shLett = int(input("Enter amount of cases of Shredded Lettuce: "))
    fries = int(input("Enter amount of cases of fries: "))
    while fries > 7 or fries < 0:
        fries = int(input("Enter amount of cases of fries: "))
    print()

    print("DAIRY")
    print ()
    smgd = input("Do we need smoked gouda?: ")
    while smgd != "yes" and smgd != "no":
        smgd = input("Do we need smoked gouda?: ")
    brft = input("Do we need pails of feta (brick feta)?: ")
    while brft != "yes" and brft != "no":
        brft = input("Do we need pails of feta (brick feta)?: ")
    mancg = input("Do we need manchego?: ")
    while brft != "yes" and brft != "no":
        mancg = input("Do we need manchego?: ")
    parm = input("Do we need parmesan?: ")
    while brft != "yes" and brft != "no":
        parm = input("Do we need parmesan?: ")
    pcc = int(input("Enter how many cases of philadelphia cream cheese: "))
    while pcc > 2 or pcc < 0:
        pcc = int(input("Enter how many cases of philadelphia cream cheese: "))
    mlk2 = input("Do we need 2% milk?: ")
    while mlk2 != "yes" and mlk2 != "no":
        mlk2 = input("Do we need 2% milk?: ")
    mlkAl = input("Do we need almond milk?: ")
    while mlk2 != "yes" and mlk2 != "no":
        mlkAl = input("Do we need almond milk?: ")
    butt = input("Do we need butter?: ")
    while butt != "yes" and butt != "no":
        butt = input("Do we need butter?: ")
    print ()


    print("PROTEIN")
    print ()
    hkcs = input("Do we need a box of Halal Kids Chicken Strips?: ")
    while hkcs != "yes" and hkcs != "no":
        hkcs = input("Do we need a box of Halal Kids Chicken Strips?: ")
    hcb = input("Do we need Halal Chicken Breasts?: ")
    while hkcs != "yes" and hkcs != "no":
        hcb = input("Do we need Halal Chicken Breasts?: ")
    gymt = input("Do we need Gyro meat?: ")
    while gymt != "yes" and gymt != "no":
        gymt = input("Do we need Gyro meat?: ")
    print()

    print("\n\n\n\n\n")
    print("ORDER LIST:")
    print()

    print("COLD PRODUCE:")
    print()
    # mint
    if mint == "yes":
        print("Order 1 bag of mint.")
    # spring mix
    if spMix >= 6:
        pass
    else:
        spMix = 6 - spMix
        print("Order", spMix, "bags of spring mix.")
    # lemons
    if lem == "yes":
        print("Order 1 case of lemons.")
    # limes
    if lim == "yes":
        print("Order 1 case of limes.")
    # mushrooms
    if shroom == "yes":
        print("Order 1 case of mushrooms.")
    # arugula
    if arug == "yes":
        print("Order 1 case of arugula.")
    # brussels sprouts
    if bruss == "yes":
        print("Order 1 case of brussels sprouts.")
    # avocado
    if avo == "yes":
        print("Order 1 case of avocado.")
    # habanero peppers
    if haba == "yes":
        print("Order 1 bag of habanero peppers.")
    # serrano peppers
    if serrano == "yes":
        print("Order 1 bag of serrano peppers.")
    # jalapeno peppers
    if jalps == "yes":
        print("Order 1 bag of jalapeno peppers.")
    # red onions
    if redOs >= 2:
        pass
    else:
        redOs = 2 - redOs
        print("Order", redOs, "bags of red onions.")
    # flat leaf parsley
    if flParsley == "yes":
        print("Order 1 case of flat leaf parsley.")
    # curly parsley
    if cParsley == "yes":
        print("Order 1 case of curly parsley")
    # spinach (breakfast)
    if spin == "yes":
        print("Order 1 bag of spinach.")
    # cilantro
    if cilan == "yes":
        print("Order 1 case of cilantro.")
    # carrots
    if carrot == "yes":
        print("Order 1 bag of carrots.")
    # potatoes
    if potato == "yes":
        print("Order 1 bag of potatoes.")
    # red bell peppers
    if rBP == "yes":
        print("Order 1 case of red bell peppers.")
    # poblano
    if pob == "yes":
        print("Order 1 case of poblano peppers.")
    # eggplant
    if eggP == "yes":
        print("Order 1 case of eggplant.")
    # cucmbers
    if cucu == "yes":
        print("Order 1 case of cucumbers.")
    # zucchini
    if zucc == "yes":
        print("Order 1 case of zucchini.")
    # cherry tomatoes
    if chTom >= 6:
        pass
    else:
        chTom = 6 - chTom
        print("Order", chTom, "containers of cherry tomatoes.")
    # leeks
    if leeks == "yes":
        print("Order 1 case of leeks.")
    # ginger
    if ging == "yes":
        print("Order 1 bag of ginger.")
    # egg wash
    if eggW >= 6:
        pass
    else:
        eggW = 6 - eggW
        print("Order", eggW, "containers of egg wash.")
    # Garlic
    if garl >= 2:
        pass
    else:
        garl = 2 - garl
        print("Order", garl, "bags of garlic")
    # Shredded Lettuce
    if shLett >= 7:
        pass
    else:
        shLett = 7 - shLett
        print("Order", shLett, "cases of Shredded Lettuce.")
    # Fries
    if fries >= 7:
        pass
    else:
        fries = 7 - fries
        print("Order", fries, "cases of fries.")
    print()

    print("DAIRY:")
    print()
    # smoked gouda
    if smgd == "yes":
        print("Order 1 Smoked Gouda.")
    # pails of feta (brick feta)
    if brft == "yes":
        print("Order 1 Pail of Feta (brick feta).")
    # manchego
    if mancg == "yes":
        print("Order 1 Manchego.")
    # parmesan
    if parm == "yes":
        print("Order 1 Parmesan.")
    # philadelphia cream cheese
    if pcc >= 2:
        pass
    else:
        ppc = 2 - pcc
        print("Order", pcc, "cases of Philadelphia Cream Cheese.")
    # 2% milk
    if mlk2 == "yes":
        print("Order 1 2% milk.")
    # almond milk
    if mlkAl == "yes":
        print("Order 1 Almond Milk.")
    # butter
    if butt == "yes":
        print("Order 1 butter.")
    print()

    print("PROTEIN:")
    print()
    # halal kids chicken strips
    if hkcs == "yes":
        print("Order one box of Halal Kids Chicken Strips.")
    # halal chicken breast
    if hcb == "yes":
        print("Order 1 box of Halal Chicken Breasts.")
    # gyro meat
    if gymt == "yes":
        print("Order 1 box of Gyro meat.")

    print()
    print()
    print("Date:", today)
    print("Inventory Taker:", name)


main ()