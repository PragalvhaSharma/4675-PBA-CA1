# BUSI 4675 Programming for Business Applications, HBA2 Fall 2026
# Professor: Yi (Zoe) Zou
# Coding Assignment 1, Part 1 - Coca-Cola Touchless Vending Machine App
# Team: Jeffrey Liu, Jibbe Hamers, Pragalvha Sharma

# Below an ASCII art of a Coca-Cola vending machine
# Triple quotes (""") or (''') in Python allow you to write strings that span multiple lines.
vending_machine = """
 __________________________________
|                                  |
|      ____________________        |
|     |                    |       |
|     |   Coca-Cola Canada |       |
|     |____________________|       |
|                                  |
|   ____  ____  ____  ____  ____   |
|  |    ||    ||    ||    ||    |  |
|  |Coca||Cola||    ||    ||    |  |
|  |____||____||____||____||____|  |
|                                  |
|    ________________________      |
|   |                        |     |
|   |   [1] Coke Classic     |     |
|   |   [2] Diet Coke        |     |
|   |   [3] Coke Zero        |     |
|   |   [4] Cherry Coke      |     |
|   |________________________|     |
|                                  |
|  [___________________________]   |
|__________________________________|

"""

prompt_drink_menu="""
  1-Coke Classic ($1.5/can)
  2-Diet Coke ($1.80/can)
  3-Coke Zero ($1.75/can)
  4-Cherry Coke ($2.00/can)
  
😀Please enter a number and select your drink: 
"""

prompt_payment = """😊Proceed with the payment from your digital wallet?
Y - ✔️Yes, pay for my drink selection.
N - ❌No, cancel my drink selection.
"""
while True:
    print (vending_machine)

    # Prompt user to make a drink selection
    while True:
        try:
            drink_option = int(input (prompt_drink_menu))
            # Prompt the user that they have entered a number that is out of range
            if drink_option  < 1 or drink_option  > 4:
                raise ValueError
            # Break out of the loop and continue if the user's selection is a valid one.
            break
            # Prompt the user that they have entered something that is not an integer.
        except ValueError:
            print("😥You entered an invalid input. Please try again.")

    # TODO 1 Complete the remaining three conditional statements and assignments
    if drink_option == 1:
        unit_price = 1.5
    #Write your block of code below
    elif drink_option == 2:
        unit_price = 1.80
    elif drink_option == 3:
        unit_price = 1.75
    elif drink_option == 4:
        unit_price = 2.00

    # Prompt the user to enter the quantity
    while True:
        try:
            quantity = int(input("😄Please enter the product quantity (Enter a number between 1 and 6): "))
            # Prompt the user that they have entered a number that is out of range
            if quantity  < 1 or quantity  > 6:
                raise ValueError
            # Break out of the loop and continue if the user's selection is a valid one.
            break
            # Prompt the user that they have entered something that is not an integer.
        except ValueError:
            print("🤨You entered an invalid input. Please try again.")
        
    # TODO 2 Based on the user's drink selection and quantity, calculate the subtotal before tax.
    # Remove the # below and complete your code
    subtotal_cost = unit_price * quantity

    # TODO 3 Calculate the total cost with an HST of 13% and display the total cost to the user
    # Remove the # below and complete your code
    total_cost = subtotal_cost * 1.13
    print(f"🧾Your total cost including 13% HST is ${total_cost:.2f}.")

    # Prompt user to confirm or cancel the payment
    while True:
        try:
            payment_confirmation = input(prompt_payment).strip().upper()
            # Prompt the user if they did not enter a letter Y or a letter N
            if payment_confirmation != "Y" and payment_confirmation != "N":
                raise ValueError
            # Break out of the loop and continue if the user's selection is a valid one.
            break
        except ValueError:
            print("😥You entered an invalid input. Please try again.")
            
    # TODO 4 Compelte the conditional statement below
    # Remove the # below and complete your code
    if payment_confirmation == "Y":
        # TODO 5 Display the receipt
        # The receipt should print out the selected item number, the item quantity, subtotal and total cost
        # Remove the # marks below and complete your code
        receipt = f"""
🧾Here is your receipt.
  Item number:  {drink_option}
  Quantity:     {quantity}
  Subtotal:     ${subtotal_cost:.2f}
  HST (13%):    ${total_cost - subtotal_cost:.2f}
  Total cost:   ${total_cost:.2f}
🥤Thank you for choosing Coca-Cola. Enjoy your drink!
"""
        print(receipt)

        # Do not change the indentation of the break command below
        break # the break command here exits the outer loop
    # the else statement continues the outer loop to line 43- print (vending_machine).
    else:
        print("❌Your drink selection has been cancelled. Returning to the menu.")

# TODO 6 Final comments
"""
a) Generative AI declaration:
   Our team used Claude (Anthropic) as a coding aid. We reviewed and tested all code.

b) How I would improve the app:
   - Name the drink on the receipt (e.g., "2 - Diet Coke") instead of only the
     item number, by storing the drinks in a dictionary of {option: (name, price)}.
     This would also replace the if/elif block and make adding new drinks easier.
   - Let the user add several drinks to one cart before paying, instead of one
     drink type per purchase.
   - Track stock for each drink and show "sold out" when it runs out.
   - Let the user pick a wallet (Apple Pay, Google Pay, etc.) and simulate a
     declined payment, so the app handles failed payments.
   - Add an option to exit the app from the menu, and offer a digital receipt
     by email or text.
   - Add promotions, such as a discount when buying 6 cans.
"""