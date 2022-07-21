import os
import sys

try:
    import pandas as pd
except:
    print("As pandas is not available, installing pandas")
    os.system("python -m pip install pandas xlrd")
import pandas as pd

def portfolio_expected_rate_of_returns(w1, w2, expected_return1, expected_return2):
    """
        function to calculate the expected rate of return by formula-
            E(rp) = w1E(e1) + w2E(r2)
    """
    rp = []
    for weight_of_fund_1, weight_of_fund_2 in zip(w1, w2):
        rp.append(
            (weight_of_fund_1 * expected_return1 + weight_of_fund_2 * expected_return2)
        )
    return rp


def portfolio_volatilities(w1, w2, standard_deviation_of_fund1, standard_deviation_of_fund2, correlation_12):
    """
    function to calculate the standard deviation of the portfolio
    """
    vp = []
    for weight_of_fund_1, weight_of_fund_2 in zip(w1, w2):
        vp.append(
            (
                (weight_of_fund_1 ** 2) * (standard_deviation_of_fund1**2) +
                (weight_of_fund_2 ** 2) * (standard_deviation_of_fund2**2) +
                (2 * weight_of_fund_1 * weight_of_fund_2 * standard_deviation_of_fund1 \
                    * standard_deviation_of_fund2 * correlation_12)
            )**0.5
        )
    
    return vp


def portfolio_quatratic_utility(expected_rate_of_returns, portfolio_volatility, A):
    """
    function to calculate the portfolio quatratic utility
    where: 
        A: the risk aversion coefficient

    Returns up: list of portfolio_quadratic_utility
    """
    up = []
    for expected_rate, volatility in zip(expected_rate_of_returns, portfolio_volatility):
        up.append(
            expected_rate - (0.5 * A * (volatility) ** 2)
        )
    return up

def cal_sharp_ratio(expected_rate, portfolio_volatility, risk_free_return):
    """ finding the sharp ratio of the portfolio """
    sp = []
    for rate, volatility in zip(expected_rate, portfolio_volatility):
        sp.append(
            (rate - risk_free_return) / volatility
        )
    return sp


def get_new_capital_weights(g1, g2, h1, h2, rp):
    weight_of_fund_1, weight_of_fund_2 = [], []
    for return_rate in rp:
        weight_of_fund_1.append(round(g1 + return_rate * h1, 4))
        weight_of_fund_2.append(round(g2 + return_rate * h2, 4))

    return weight_of_fund_1, weight_of_fund_2


def get_df_gen(df):
    check = True
    for x in df.iterrows():
        if check:
            continue
        yield x


def main():
    '''main function for the project'''
    choice = input("~~~~DATA ENTER CHOICES~~~~~\n"\
                   "   1. Read from keyboard\n"\
                   "   2. Read from Excel file\n"\
                   "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    if choice.strip() == "1":
        print("Enter details, enter 'n' to exit. ")
        data = []
        data.append(float(input("expected rate of return for first fund: "))) # 0
        data.append(float(input("expected rate of return for second fund: "))) # 1
        data.append(float(input("volatility for first fund: ")))# 2
        data.append(float(input("volatility for second fund: "))) # 3
        data.append(float(input(" the correlation coefficient: "))) # 4
        data.append(float(input("the risk aversion coefficient: "))) # 5
        data.append(float(input("a risk free rate of return: "))) # 6
    elif choice.strip() == "2":
        # reading excel file entered
        try:
            df = pd.read_excel(input("Enter path/filename to excel: "))
            data = df.values.tolist()[0]
        except:
            print("Not a valid path of excel")
            sys.exit(0)

    # making weights where capital weight is 1.0 always
    w1, w2 = [0.0,], [1.0,]
    for _ in range(10000):
        w1.append(round(w1[-1] + 0.0001, 4))
        w2.append(round(w2[-1] - 0.0001, 4))

    # calculating and making the list of the Protfolio expected rate of returns
    rp = portfolio_expected_rate_of_returns(w1, w2, data[0], data[1])

    # calculating and making  the list of the Portfolio volatility
    vp = portfolio_volatilities(w1, w2, data[2], data[3], data[4]) 

    # Portfolio quadratic utility in expectation
    e_up = portfolio_quatratic_utility(rp, vp, data[5])

    # calculating sharp ratio 
    s_p = cal_sharp_ratio(rp, vp, data[6])

    if (input("Do you want to compute capital weights using the Huang and Litzenberger(HL) method: (y/n)").strip()+" ")[0].lower() == "y":
        # finding capital weights
        ## finding g
        g1 = data[1] / (data[1] - data[0])
        g2 = 1 - g1

        ## finding h
        h1 = 1 / (data[0] - data[1])
        h2 = 0 - h1

        w1, w2 = get_new_capital_weights(g1, g2, h1, h2, rp)

    # now finding new portfolio standard deviation from new wights
    efvp = portfolio_volatilities(w1, w2, data[2], data[3], data[4])

    # making pandas dataframe
    df = pd.DataFrame(
        sorted([[w1[x], w2[x], round(rp[x], 4), round(efvp[x], 4), round(e_up[x], 4), round(s_p[x], 4)] for x in range(len(w1))], key = lambda x: x[2]),
        columns=["Capital Weight 1", "Capital Weight 2", "Portfolio expected return", "Volatility", "Utility", "Sharp Ratio"]
    )
    print(df.to_string())
    print("Max Utility Value: \n",max(df.iterrows(), key = lambda x: x[1][4])[1], sep="", end="\n\n")
    print("Max Sharp Ratio: \n", max(df.iterrows(), key = lambda x: x[1][5])[1], sep="",end="\n\n")

main()