import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    # low = 0
    # aveg = 0
    # high = 0
    # for i in range(len(accounts)):
    #     income = accounts['income'][i]
    #     if income < 20000:
    #         low += 1
    #     elif income >= 20000 and income <=50000:
    #         aveg += 1
    #     else:
    #         high += 1
    # return pd.DataFrame([['High Salary', high],['Low Salary',low],['Average Salary', aveg]],columns = ['category','accounts_count'])
    low = accounts[accounts['income'] < 20000]
    aveg = accounts[(accounts['income'] >= 20000) & (accounts['income'] <= 50000)] 
    high = accounts[accounts['income'] > 50000]

    return pd.DataFrame([['High Salary', len(high)],['Low Salary',len(low)],['Average Salary', len(aveg)]],columns = ['category','accounts_count'])
    