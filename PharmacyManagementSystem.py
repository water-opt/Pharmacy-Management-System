# initial products
productDict = {
    "vitaminC": 12.0,
    "vitaminE": 14.5,
    "coldTablet": 6.4,
    "vaccine": 32.6,
    "fragrance": 25.0,
    "prescription": ['vaccine',]
}

# order history
orderDict = {
    "Tom": {
        "orders": [
            {
                "products": {"vitaminC": 1},
                "total": 12.0,
                "earnedRewards": 12
            },
            {
                "products": {"fragrance": 1, "vitaminE": 2},
                "total": 54.0,
                "earnedRewards": 54
            },
            {
                "products": {"coldTablet": 3, "vitaminC": 1},
                "total": 31.2,
                "earnedRewards": 31
            }
        ]
    }
}

# initial customers
customersDict = {
    "Kate": 120,
    "Tom": 32,
}

#data input
def display():
    product = 'null'
    quantity = 0
    name = 'null'

    # saving the products that need a prescription in a list
    prescriptionList = productDict["prescription"]

    # username validation
    tempName = input('\nEnter the name of the customer [e.g. Huong]:')
    while 1:
        if tempName.isalpha():
            name = tempName
            break
        else:
            print('Please enter a valid name.')
            tempName = input('Enter the name of the customer [e.g. Huong]:')
            continue

    # check whether the name exists in the dictionary
    if name not in customersDict:
        customersDict[name] = 0

    while True:
        tempProducts = input('Enter the product [enter a valid product only, e.g. vitaminC, coldTablet]: ')
        tempProductList = [product.strip() for product in tempProducts.split(",")]

        Valid = True

        for tempProduct in tempProductList:
            if tempProduct not in productDict:
                print(f'The product {tempProduct} is not valid. Please enter a valid product list.')
                Valid = False
                break

        if Valid:
            productList = tempProductList
            break

    while True:
        quantities = input('Énter the quantities [enter positive integers only, e.g. 1, 2, 3, 4]:')
        tempQuantityList = [quantity.strip() for quantity in quantities.split(",")]

        Valid = True

        for tempQuantity in tempQuantityList:
            quantity = int(tempQuantity)
            if quantity < 0 or quantity == 0:
                print('Enter a valid quantity [quantities cannot be negative or 0]')
                Valid = False
                break
        if Valid:
            quantityList = tempQuantityList
            break

    for product in productList:
        if product in prescriptionList:
            while True:
                # answer check
                tempAnswer = input(f"The product {product} requires a doctor' prescription, do you have one? (y/n): ")
                if tempAnswer == 'n':
                    quantityList.pop(productList.index(product))
                    productList.remove(product)
                    break
                elif tempAnswer == 'y':
                    break
                else:
                    print('Invalid input. Please enter either "y" or "n".')

    inputFunc(productList, name, quantityList)

# product add/ update
def manageProducts():
    while True:
        productsInput = input(
            "Enter the products, prices, and the doctor's prescription requirements [e.g., toothpaste 5.2 n, shampoo 8.2 n]: ")
        productsDataList = [item.strip() for item in productsInput.split(',')]

        # prices validity
        pricesIsValid = True

        for productData in productsDataList:
            product, price, prescription = [item.strip() for item in productData.split(' ')]

            # price validation [price > 0]
            try:
                price = float(price)
                if price <= 0:
                    pricesIsValid = False
                    break
            except ValueError:
                pricesIsValid = False
                break

            # prescription requirement validation ['y' or 'n']
            if prescription.lower() not in ['y', 'n']:
                pricesIsValid = False
                break

        prescriptionList = productDict["prescription"]

        if pricesIsValid:
            for productData in productsDataList:
                product, price, prescription = [item.strip() for item in productData.split(' ')]

                if product in productDict:
                    productDict[product] = price
                    if prescription.lower() == 'y':
                        prescriptionList.append(product)
                else:
                    productDict[product] = price
                    if prescription.lower() == 'y':
                        prescriptionList.append(product)

            productDict["prescription"] = prescriptionList
            print("\nInformation updated.\n")
            break
        else:
            print(
                "\nInvalid input. Valid inputs. [prices should be greater than o and prescription requirement should be 'n' or 'y']")
            continue

# display existing customers
def existingCustomers():
    print('\n################################')
    print('\tCustomers & Reward points')
    print('################################')

    for customer, reward_points in customersDict.items():
        print(f'{customer.ljust(20)} {str(reward_points).rjust(10)}')

    print('\n')

# display existing products
def existingProducts():
    print('\n################################')
    print('\t\t\tProducts')
    print('################################')

    for product, price in productDict.items():
        print(f'{product.ljust(20)} {str(price).rjust(10)}')

    print('\n')

def orderHistory():
    # user name input
    name = input("Enter the name of the user: ")
    print(f'\nThis is the order history of {name}')

    # checking the name given as an input
    if name in orderDict:
        orders = orderDict[name]["orders"]

        # formatting the history
        print('\t\t\tProducts\t\t\t\t\t\tTotal Cost\t\t\t\tEarned Rewards')
        for i, orderDetails in enumerate(orders, start=1):
            productsDisplay = ", ".join([f"{quantity} x {product}" for product, quantity in orderDetails["products"].items()])
            print(f"Order {i:<5} {productsDisplay:<31} Total Cost: {orderDetails['total']:<11} Earned Rewards: {orderDetails['earnedRewards']}")
            # print(f"Order {i} {productsDisplay}, Total Cost: {orderDetails['total']}, Earned Rewards: {orderDetails['earnedRewards']}")
    else:
        print(f"No order history exists for user - {name}")

# selection navigation
selectionDict = {
    1:display,
    2:manageProducts,
    3:existingCustomers,
    4:existingProducts,
    5:orderHistory
}

# selection menu for the functions
def menu():
    while True:
        # features
        print('\nWelcome to the RMIT pharmacy!\n')
        print('###################################################################')
        print('You can choose from the following options:')
        print('1. Make a purchase')
        print('2. Add/update information of products')
        print('3. Display existing customers')
        print('4. Display existing products')
        print('5. Display a customer order history')
        print('0. Exit the program')
        print('###################################################################')
        option = input('Choose one option: ')

        option = int(option)

        if option == 0:
            break  # Exit the loop and the program
        elif option in selectionDict:
            selectionDict[option]()
        else:
            print('Invalid selection.')

#total calculation
def calcTotal(product, quantity):
    total = productDict[product] * int(quantity)
    return total

#save new rewards amount calculation
def saveRewards(customer, total):
    customersDict[customer] = customersDict[customer] + total

#calculations callings
def inputFunc(productList, name, quantityList):
    subTotal = 0
    totalRewards = 0
    productStoreNewDict = {}
    #display
    print('--------------------------------')
    print('\t\t\tReceipt')
    print('--------------------------------')

    for i in range(len(productList)):
        product = str(productList[i])
        quantity = int(quantityList[i])

        #store products and quantity dictionary temporary for storing
        productStoreNewDict[product] = quantity

        # calling rewards and total calculation functions
        total = calcTotal(product, quantity)

        subTotal += total

        #display
        print(f'Name:\t\t\t\t{name}')
        print(f'Product:\t\t\t{product}')
        print(f'Unit Price:\t\t\t{productDict[product]} (AUD)')
        print(f'Quantity:\t\t\t{quantity}')

    if customersDict[name] >= 100:
        cashToBeDeducted = float(rewardToCash(name))
        finalAmount = subTotal - cashToBeDeducted
    else:
        finalAmount = subTotal

    totalRewards = round(subTotal)
    saveRewards(name, totalRewards)

    print('--------------------------------')
    print(f'Total cost:\t\t\t{finalAmount} (AUD)')
    print(f'Earned reward:\t\t{totalRewards}\n')

    order = {
        "products": productStoreNewDict,
        "total": float(finalAmount),
        "earnedRewards": int(totalRewards)
    }

    if name in orderDict:
        orderDict[name]["orders"].append(order)
    else:
        orderDict[name] = {"orders": [order]}

# reward points to cash
def rewardToCash(name):
    rewards = customersDict[name]
    if rewards >= 100:
        rewardCash = int(rewards/100)*10
        customersDict[name] = rewards - (round(rewards/100))*100
    else:
        rewardCash = rewards

    return rewardCash

#calling display function
menu()