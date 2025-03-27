"""I use Jupyterlab and installed black PEP8 styling and also used isort.
The formatting should now be correct.
I also shortened some sentences and removed print("") statements and replaced it with \n for efficiency.
"""

import math

print("Choose your calculator: \n")
print("Investment calculator \t - Calculates total interest on an investment.")
print("Bond calculator \t - Calculates total cost of home loan.")
# cont stands for 'continue'. When it statement is True,
# user is allowed to continue to the following step
cont_choice = False
invest_calc_cont = False
error_message = "\nInvalid input. Please try again."  # displys this message if user gives incorrect input

print(
    "\nImportant notice: When asked for deposit amount or interest rate, use "
    " "
    ","
    " or "
    "."
    " to indicate decimal places. "
    "When asked to enter year, month or current house value, only enter integer values.\n"
)
while not cont_choice:
    # forces user to choose a valid input

    calc_choice = input("\nType 'investment' or 'bond' to confirm your choice: ")

    # Investment choice
    if calc_choice.lower() == "investment":
        while True:
            # fixes unnecessary elements in input
            deposit_amount = (
                input("\nEnter deposit amount (H$): ")
                .replace("H$", "")
                .replace(",", ".")
                .replace("'", "")
            )
            try:
                deposit_format = float(deposit_amount) and float(deposit_amount) > 0
                break
            except ValueError:
                print(error_message)
        deposit_amount = round(float(deposit_amount), 2)

        while True:
            interest_rate = (
                input("Enter interest rate (%): ")
                .replace("%", "")
                .replace(",", ".")
                .replace("'", "")
            )  # fixes input elements

            try:
                interest_rate_format = float(interest_rate) and float(interest_rate) > 0
                break
            except ValueError:
                print(error_message)
        interest_rate = float(interest_rate)

        while True:
            years = input("Enter number of year(s) you want to invest: ")
            try:
                yearcheck = int(years) and int(years) > 0
                break
            except ValueError:
                print(error_message)
        years = int(years)

        while not invest_calc_cont:
            # corrects input mistakes
            interest = (
                input("Enter 'simple' or 'compound' to choose your investment type: ")
                .lower()
                .replace("'", "")
            )
            if interest == "simple":
                # calculates simple investment
                simple_calc = round(
                    deposit_amount * (1 + (interest_rate / 100 * years)), 2
                )
                print(
                    f"\n A simple interest for {years} year(s) with a deposit "
                    f"of {deposit_amount:.2f} H$ and interest rate of {interest_rate}%, will result in a total of "
                    f"{simple_calc:.2f} H$"
                )
                invest_calc_cont = True
            elif interest == "compound":

                # calculates compound investment
                compound_calc = round(
                    deposit_amount * math.pow(1 + (interest_rate / 100), years), 2
                )
                print(
                    f"\n A compound interest for {years} years with a deposit of "
                    f"{deposit_amount:.2f} H$ and interest rate of {interest_rate}%, "
                    f"will result in a total of {compound_calc:.2f} H$"
                )
                invest_calc_cont = True
            else:
                print(error_message)

    # Bond choice
    elif calc_choice.lower() == "bond":  # taking account of case issues
        while True:
            current_house_value = input("Enter current value of house (H$): ").replace(
                "H$", ""
            )  # fixes unnecessary elements in input
            try:
                format_current_house_value = (
                    int(current_house_value) and int(current_house_value) > 0
                )
                break

            except ValueError:
                print(error_message)
        current_house_value = int(current_house_value)

        while True:
            interest_rate = (
                input("Enter interest rate (%): ").replace(",", ".").replace("%", "")
            )  # fixes unnecessary elements in input.
            try:
                check_rate = float(interest_rate) and float(interest_rate) > 0
                break
            except ValueError:
                print(error_message)
        interest_rate = float(interest_rate) / 100 / 12

        while True:
            months = input("Enter the number of month(s) you will repay the bond: ")

            try:
                months_check = int(months) and int(months) > 0
                break
            except ValueError:
                print(error_message)
        months = int(months)

        bond_calc = round(
            (interest_rate * current_house_value)
            / (1 - (1 + interest_rate) ** (-months)),
            2,
            )
        # Calculates bond and rounds to 2 decimal places

        print(
            f"\n You will need to pay {bond_calc:.2f} H$ "
            f"in {months} month(s) if you want a bond for a {current_house_value} "
            f"H$ house with an interest rate of {interest_rate*100}%."
            )

    # when user enters incorrect input when choosing a calculator
    else:
        print(error_message)