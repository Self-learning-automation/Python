def Processing(pickedProduct):
    money = int(input("Please insert your money: "))
    picked = int(input('''Please select your drinks: 
          1. Coke 
          2. Pepsi 
          3. 7up 
          4. Monster 
          5. Rockstar 
          6. Red Bull
          '''))
    products = ['Coke', 'Pepsi', '7up', 'Monster', 'Rockstar', 'Red Bull']
    for product in products:
        if money < 5:
            print("Please check your amount !!")
            break
        if money == 5 and picked == 1:
            print("Please pick up your " + products[0])
            pickedProduct = products[0]
            print(pickedProduct)
            break
        elif money == 5 and picked == 2:
            print("Please pick up your " + products[1])
            pickedProduct = products[1]
            break
        elif money == 5 and picked == 3:
            print("Please pick up your " + products[2])
            pickedProduct = products[2]
            break
        else:
            if money > 5 and picked == 4:
                print("Please pick up your " + products[3])
                pickedProduct = products[3]
                break
            elif money > 5 and picked == 5:
                print("Please pick up your " + products[4])
                pickedProduct = products[4]
                break
            elif money > 5 and picked == 6:
                print("Please pick up your " + products[5])
                pickedProduct = products[5]
                break
    return pickedProduct

def Repeation(pickedSelection):
    selection = int(input('''Do you want to re-buy?
    1. Yes
    2. No
    '''))

    if selection == 1:
        Processing("Coke")
        pickedSelection = 1
    elif selection == 2:
        print("Thank for your purchase and see you again")
    else:
        print("Your selection is not correct !!")
        Repeation(1)
    return pickedSelection

'''if __name__ == '__main__':
    Processing("Coke")
    Repeation(1)'''












