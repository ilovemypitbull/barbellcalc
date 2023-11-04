
barbell = 45
forty_five_plates = 0
twenty_five_plates = 0
ten_plates = 0
five_plates = 0
two_point_five_plates = 0

print("How much weight do you want to lift? (lbs)")
weight = int(input())

if weight >= barbell:
    print("To lift", weight, "lbs, you need:")
    plates_weight = weight-barbell
    print(plates_weight, "lbs added to the barbell")
    print()

    #45 plates
    while plates_weight >= 90:
        forty_five_plates += 2
        plates_weight -= 90

    if forty_five_plates:
        print("You need", forty_five_plates, "x 45 lb plates")

    #25 plates 

    while plates_weight >= 50:
        twenty_five_plates += 2
        plates_weight -= 50

    if twenty_five_plates:
        print("You need", twenty_five_plates, "x 25 lb plates") 

    #10 plates

    while plates_weight >= 20:
        ten_plates += 2
        plates_weight -= 20

    if ten_plates:
        print("You need", ten_plates, "x 10 lb plates") 

    #5 plates

    while plates_weight >= 10:
        five_plates += 2
        plates_weight -= 10

    if five_plates:
        print("You need", five_plates, "x 5 lb plates") 

    #2.5 plates

    while plates_weight >= 5:
        two_point_five_plates += 2
        plates_weight -= 5

    if two_point_five_plates:
        print("You need", two_point_five_plates, "x 2.5 lb plates") 

    #micro plates

    if plates_weight >= 2:
        print("You need one set of microplates") 

else:
    print("This weight is lower than the barbell. Switch to dumbells.")
