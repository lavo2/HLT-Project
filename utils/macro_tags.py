def get_meat_tags():
    meat_tags = """
    Meat,18514
    Poultry,7982
    Chicken,6079
    Beef,5164
    Pork,3918
    Bacon Recipes,2969
    Sausage Recipes,2507
    Easy Chicken,1698
    Turkey Recipes,1415
    Steak,1292
    Ham,1090
    Lamb Recipes,673
    Grilled Chicken,601
    Grilled Steak,437
    Chorizo,424
    Ribs Recipes,414
    Meatballs,398
    Duck Recipes,394
    Pork Chop,371
    Veal,363
    Roasted Chicken,355
    Fried Chicken,337
    Chicken Wing,287
    Pork Roast,286
    Pork Tenderloin,224
    Thanksgiving Turkey,270
    Chicken Breast,242
    Beef Stew,217
    Short Ribs,200
    Meatloaf,199
    Mexican Chicken,199
    Chicken Salad,191
    Beef Chili,167
    Andouille Sausage,149
    Pork Loin,147
    Chicken Thigh,142
    Beef Tenderloin,141
    Chicken Stew,139
    Roasted Turkey,133
    Flank Steak,128
    Pulled Pork,124
    Cheeseburger,108
    Quail Recipes,99
    Smoked Pork,91
    Turkey Breast,89
    Venison Recipes,86
    Steak Salad,81
    Pork Shoulder,81
    Leg of Lamb,78
    Chicken Curry,77
    Filet Mignon,77
    Baked Chicken,76
    Meatball Appetizer,76
    Roast Beef,74
    Turkey Burger,74
    Thai Chicken,73
    Chicken and Dumpling,64
    Smoked Turkey,60
    Grilled Pork Chop,55
    Chicken Soup,55
    Prime Rib,54
    Chicken Casserole,53
    Pork Rib,50
    Italian Meatball,50
    New York Strip Steak,46
    Beef Stroganoff,45
    Pork Butt,44
    Stuffed Chicken Breast,43
    Chicken Chili,42
    Stuffed Pork Chops,41
    Beef Bourguignon,41
    Turkey Meatloaf,40
    Brined Turkey,37
    Sausage Casserole,36
    Chicken and Rice,35
    Turkey Chili,34
    Osso Buco,33
    Sesame Chicken,29
    Lamb Stew,26
    Jerk Chicken,25
    Goose Recipes,24
    Pheasant Recipes,24
    Baked Ham,23
    Salisbury Steak,23
    Oven Fried Chicken,21
    Chicken Cacciatore,20
    Beef Wellington,19
    Chicken Cordon Bleu,16
    Chicken Piccata,16
    Sausage Gravy,16
    Turkey Gravy,16
    White Chicken Chili,15
    Pepper Steak,14
    Sweet And Sour Chicken,12
    Teriyaki Chicken,12
    Orange Chicken,10
    Ham Salad,7
    Sweet and Sour Pork,1
    """

    meat_tags = meat_tags.split('\n')

    meat = []
    for tag in meat_tags:
        name = tag.split(',')[0]
        meat.append(name.strip())

    # at this point, the first and last element of the list is empty, so we remove it
    meat = meat[1:-1]
    return meat


def get_fish_tags():
    fish_tags = """
    Fish,5099
    Shellfish Recipes,5895
    Shrimp,3164
    Salmon,1508
    Crab Recipes,909
    Easy Shrimp Recipes,886
    Scallop Recipes,698
    Tuna Recipes,669
    Clam Recipes,636
    Lobster,420
    Oyster Recipes,405
    Grilled Shrimp,366
    Mussel,357
    Anchovy,388
    Bass,338
    Smoked Salmon,282
    Squid Recipes,278
    Shrimp Salad,243
    Trout Recipes,194
    Seafood Soup,174
    Caviar,173
    Spicy Shrimp,167
    Baked Fish,134
    Sushi Recipes,126
    Crab Cake,125
    Tilapia Recipes,121
    Catfish,119
    Swordfish,99
    Crawfish,99
    Salmon Salad,94
    Crab Salad,93
    Shrimp Cocktail,90
    Grilled Salmon,77
    Baked Salmon,43
    Flounder Recipes,41
    Lobster Salad,34
    Lobster Tail,26
    Coconut Shrimp,24
    Shrimp Creole,23
    Rockfish,22
    Sturgeon Recipes,22
    Salmon Burger,20
    Tuna Salad,17
    Lobster Roll,17
    Salmon Mousse,16
    Eel Recipes,14
    Baked Tilapia,14
    Lobster Ravioli,4
    Lobster Bisque,1
    """

    fish_tags = fish_tags.split('\n')

    fish = []
    for tag in fish_tags:
        name = tag.split(',')[0]
        fish.append(name.strip())

    # at this point, the first and last element of the list is empty, so we remove it
    fish = fish[1:-1]
    return fish
    
def get_dessert_tags():
    dessert_tags = """
    Dessert,14747
    Easy Dessert Recipes,3875
    Fruit Dessert Recipes,2983
    Cookie,2102
    Cake,2081
    Pie Recipes,1444
    Apple Dessert,887
    Ice Cream,862
    Cupcake,750
    Pudding Recipes,560
    Chocolate Cake,511
    Sugar Cookie,469
    Chocolate Cookie Recipes,463
    Cream Cheese Frosting,429
    Biscuit,389
    Brownie,370
    Cheesecake,355
    Muffin,270
    Chocolate Cupcake,232
    White Chocolate,219
    Chocolate Chip Cookie,140
    Chocolate Pie,135
    Creme Brulee,102
    Biscotti,70
    Panna Cotta,66
    Ice Cream Cake,61
    Peanut Butter Cookie Recipes,55
    Chocolate Cheesecake,54
    Chocolate Fudge,54
    Chocolate Fondue,48
    Gelato,44
    Fruit Cheesecake,42
    Pumpkin Cheesecake,27
    Chocolate Frosting,25
    Strawberry Cheesecake,13
    """

    dessert_tags = dessert_tags.split('\n')

    dessert = []
    for tag in dessert_tags:
        name = tag.split(',')[0]
        dessert.append(name.strip())

    # at this point, the first and last element of the list is empty, so we remove it
    dessert = dessert[1:-1]
    return dessert

def get_dairy_tags():
    dairy_tags = """
    Dairy Recipes,10048
    Cheddar,1477
    Cream Cheese Recipes,1437
    Mozzarella Recipes,1205
    Buttermilk,1141
    Ricotta,880
    Parmesan Cheese Recipes,705
    Feta,581
    Blue Cheese,544
    Cheesy Potatoes,491
    Cream Cheese Frosting,429
    Gruyere Recipes,368
    Macaroni and Cheese,330
    Swiss Cheese Recipes,227
    Provolone Recipes,220
    Brie,209
    Goat Cheese Recipes,201
    Fondue Recipes,191
    Grilled Cheese Recipes,76
    Cheese Ball,31
    """

    dairy_tags = dairy_tags.split('\n')

    dairy = []
    for tag in dairy_tags:
        name = tag.split(',')[0]
        dairy.append(name.strip())

    # at this point, the first and last element of the list is empty, so we remove it
    dairy = dairy[1:-1]
    return dairy


def get_veg_tags():
    veg_tags = """
    Vegan,7777
    Vegetarian,5561
    Vegetarian Meals,593
    """

    veg_tags = veg_tags.split('\n')

    veg = []
    for tag in veg_tags:
        name = tag.split(',')[0]
        veg.append(name.strip())

    # at this point, the first and last element of the list is empty, so we remove it
    veg = veg[1:-1]
    return veg