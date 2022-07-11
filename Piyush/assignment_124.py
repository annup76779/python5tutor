##########
# Part A #
##########

def coupon_calculation(spenditure_of_user = None):
    """
        function to calculate the the cap on the spenditure of the user.
        % are given as -

        Money spent Coupon percentage
        --------------------   
            Less than £10 No coupon
            £10 to £60 8%
            £61 to £150 9%
            £151 to £210 10%
            £211 and above 11% Capped at £33
    """
    # data validation 
    if spenditure_of_user is None:
        try:
            spenditure_of_user  = int(input("Cost of groceries: "))
        except ValueError:
            print("Wronge data type")
            return 0, 0
    elif not isinstance(spenditure_of_user, (int, float)):
        print("Wronge data type")
        return 0, 0
    
    if spenditure_of_user< 10:
        print("Less than £10 - No coupon.")
        return 0, 0
    elif 10<= spenditure_of_user <= 60:
        # 8 % of spenditure_of_user
        coupon = spenditure_of_user * 0.08
        print(f"Awarded a discount Coupon of £{coupon} ({8}% of purchase).")
        return 8, coupon
    elif spenditure_of_user <= 150:
        # 9% of spenditure_of_user
        coupon = spenditure_of_user * 0.09
        print(f"Awarded a discount Coupon of £{coupon} ({9}% of purchase).")
        return 9, coupon
    elif spenditure_of_user <= 210:
        # 10% of spenditure_of_user
        coupon = spenditure_of_user * 0.10
        print(f"Awarded a discount Coupon of £{coupon} ({10}% of purchase).")
        return 10, coupon
    elif spenditure_of_user >= 211:
        # 11% of spenditure_of_user capped at £33
        coupon = spenditure_of_user * 0.11
        if coupon > 33: # capped to 33
            coupon = 33
            print(f"Awarded a discount Coupon of £{33} (capped).")
        else:
            print(f"Awarded a discount Coupon of £{coupon} ({11}% of purchase).")
        return 11, coupon
    else:
        return spenditure_of_user
    return 0

# Uncomment following lines to run Part A
# coupon_calculation()


##########
# Part B #
##########
def multi_coupon_calculator(list_of_costs):
    '''The program should loop to accept multiple inputs. For each input, display the amount spend and
    discount for that amount.'''
    coupon_count = {x:0 for x in [0, 8, 9, 10, 11]}
    sum_grosery = 0
    sum_coupon = 0
    # flag to know that this is the first run of the loop
    check = True
    if not list_of_costs:
        min_cost_grosery, max_cost_grosery, max_coupon, min_coupon = 0,0,0,0
    # taking input till user don't enter e
    for spenditure_of_user in list_of_costs:
        # getting the coupon percentage and coupon avarded from coupon_calculation function 
        percentage, coupon = coupon_calculation(spenditure_of_user=spenditure_of_user)
        # incrimenting the count of the % key in the dictionary to make the histogen
        coupon_count[percentage] += 1
        # sum of the groceries
        sum_grosery += spenditure_of_user
        # sum of coupons
        sum_coupon += coupon
        # finding the max and min of 
        # groceries and coupons awarded
        if check:
            max_cost_grosery, min_cost_grosery, min_coupon, max_coupon = spenditure_of_user, spenditure_of_user, coupon, coupon
            check = False
        else:
            max_cost_grosery = max(max_cost_grosery, spenditure_of_user)
            max_coupon = max(max_coupon, coupon)
            min_cost_grosery = min(min_cost_grosery, spenditure_of_user)
            min_coupon = min(min_coupon, coupon)

    print("Total groceries:", sum_grosery)
    print("Total discount:", sum_coupon)
    print("Groceries - Discount:", sum_grosery - sum_coupon)
    # printing histogram 
    print("Histogram")
    print("<£10 (0%) : ", "*" * coupon_count.get(0))
    print("\t10. £60 (8%) :", "*"*coupon_count.get(8))
    print("\t11. £150 (9%) :", "*"*coupon_count.get(9))
    print("\t12. £210 (10%) :","*"*coupon_count.get(10))
    print(">£211 (11%/Cap) :", "*"*coupon_count.get(11))
    # printing the total count of customers
    count_customer = sum(coupon_count.values())
    print(count_customer, "customers")

    ######################
    # Part C (extention) #
    ######################
    # printing the all the coupon percentage
    print(" ".join(map(lambda x: f"{x}%", coupon_count.keys())), end=" ")
    # printing the total number of coupon percentage count
    print(" ".join(map(lambda x: "*"*x, coupon_count.values())))


    ############################
    # Part 4 (exptention of B) #
    ############################
    print("Minimum groceries:", min_cost_grosery)
    print("Maximum groceries:", max_cost_grosery)
    print("Minimum coupon:", min_coupon)
    print("Maximum coupon:", max_coupon)

# Uncomment this line to run the program
# multi_coupon_calculator([10, 14, 58, 62, 200, 8, 512])
