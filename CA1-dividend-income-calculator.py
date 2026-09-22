robo_advisor = r'''
       ______
      /      \
     |  O  O  |      Vanguard Digital Advisor  
     |   ___  |      Ready to manage your portfolio efficiently!
     |  \___/ |
     \________/    
      /|     |\
     / |_____| \
    /  |     |  \
   |   |_____|   |
   |   |     |   |
   |___|_____|___|
      /       \
     |_________|

'''

prompt_price ="💵Please enter the stock price per share: $"

prompt_dividend = "💰Please enter the dividend amount per share: $"

prompt_shares ="Please enter the number of shares you hold: "

prompt_frequency = """📅Please enter the frequency of divident payments.
1 - Monthly\n2 - Quarterly\n3 - Semi-annually\n4 - Annually
"""
prompt_reinvest = """💸Will Vanguard Digital Advisor be authorized to automatically
reinvest your dividend income?\nY - Yes \nN - No"""

prompt_exit = """Exit or Continue the program
E - Exit\nC - Continue
"""

# To simplify this coding task, we will make two assumptions.
# Assumption 1: your script should assume that all user inputs are valid.
# Yes, it is an overly optimistic assumption. We will address it in later class sessions.
# Assumption 2: Your script should assume the stock price and dividend per share remain constant throughout the year.

# TODO 5 Add try-except statements to validate user inputs, and refine the script accordingly.
# The helper functions below keep asking until the user enters a valid value.
def get_positive_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                raise ValueError
            return value
        except ValueError:
            print("😥Please enter a number greater than 0 and try again.")

def get_choice(prompt, valid_options):
    while True:
        choice = input(prompt).strip().upper()
        if choice in valid_options:
            return choice
        print("😥You entered an invalid input. Please try again.")

while True:
    print(robo_advisor)
    price = get_positive_number(prompt_price)
    # TODO 1 Prompt the the user to enter the remaining information
    shares = get_positive_number(prompt_shares)  # fractional shares are allowed
    dividend = get_positive_number(prompt_dividend)
    frequency = int(get_choice(prompt_frequency, ["1", "2", "3", "4"]))
    reinvest = get_choice(prompt_reinvest + "\n", ["Y", "N"])

    # Determine the multiplier based on the frequency of dividend payment
    if frequency == 1: # The user selects the monthly option.
        multiplier = 12 # There are 12 dividend payments over a year.
    # TODO 2 Complete the remaining conditional statments and assignments
    elif frequency == 2: # The user selects the quarterly option.
        multiplier = 4
    elif frequency == 3: # The user selects the semi-annual option.
        multiplier = 2
    else: # The user selects the annual option.
        multiplier = 1

    # Determine if the user allows dividend reinvestment.
    if reinvest == "N":
        # Calculate the one-period dividend payment based on the dividend per share and the number of shares
        one_period_payment = dividend * shares
        # TODO 3 Calculate the annual dividend income without reinvestment
        # Hint 1: Annual dividend income = one-period payment × the number of payments made in a Year
        annual_payment = one_period_payment * multiplier

        print(f"🤑Your annual dividend income without reinvestments is ${annual_payment:,.2f}.")
    else:
        annual_payment = 0
        # TODO 4 Calcaulte the annual dividend income with reinvestments
        # Hint 1: Use a loop statement
        # Hint 2: For each iteration, three variables, one_period_payment, annual_payment and shares will be assigned new values.
        for period in range(multiplier):
            one_period_payment = dividend * shares       # dividend paid this period
            annual_payment += one_period_payment         # add it to the year's income
            shares += one_period_payment / price         # buy fractional shares with it

        print(f"🤑Your annual dividend income with reinvestments is ${annual_payment:,.2f}.")
        print(f"📈You will hold {shares:,.4f} shares at the end of the year.")

    calculator_exit = get_choice(prompt_exit, ["E", "C"])
    if calculator_exit == "E":
        print("👋Thank you for using Vanguard Digital Advisor. Goodbye!")
        break
    else:
        pass


"""
a) Generative AI declaration:
   I used a generative AI tool (Claude, by Anthropic) to help complete the TODO
   sections of this script. I reviewed every line, ran the program myself, and
   checked the results by hand. Example: 100 shares at $50, $0.50 dividend paid
   quarterly gives $200.00 a year without reinvestment and $203.02 with
   reinvestment. I am responsible for the final code.

b) How this script could be applied and extended to other financial advisory services:
   - Portfolio view: let the user enter several stocks in one session and show
     total dividend income across the whole portfolio.
   - Retirement planning: project dividend income over many years (e.g., 10 or
     30 years) to show when it could cover a target yearly spending amount.
   - Savings goals: add a regular monthly contribution, so the tool shows how
     fast a client reaches a goal such as a house down payment.
   - Comparing options: run the same inputs with and without reinvestment side
     by side, or compare two stocks, to help clients choose.
   - The same input, calculate, display loop can be reused for other calculators,
     such as bond coupon income, GIC interest, or loan and mortgage payments.

c) Additional parameters that could make the projections more realistic:
   - Dividend growth rate: most companies raise dividends over time.
   - Stock price growth or change: reinvested dividends buy shares at the price
     on each payment date, not one fixed price.
   - Taxes: withholding tax on foreign dividends, and tax treatment in a TFSA,
     RRSP, or non-registered account.
   - Fees: management fees or trading fees on reinvestment.
   - Dividend cuts or suspensions, and a range of outcomes (best, expected, worst)
     instead of a single number.
   - Inflation, to show income in today's dollars.
   - Currency exchange rates for US-listed stocks held by Canadian clients.
"""
