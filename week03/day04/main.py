# ROA (Return on Assets)
def roa(net_income, assets):
    """
    ROA (Return on Assets)
    
    Args:
        net_income (double): net income, net profit
        assets (double): total assets
    """
    return net_income / assets


# ROE (Return on Equity)
def roe(net_income, equity):
    """
    ROE (Return on Equity)

    Args:
        net_income (double): net income, net profit
        equity (double): total shareholders' equity
    """
    return net_income / equity


# ROI (Return on Investment)
def roi(current_investment, cost_of_investment):
    """
    ROI (Return on Investment)

    Args:
        current_investment (double): 
        cost_of_investment (double): initial cost, outlay
    """
    
    return (current_investment - cost_of_investment) / cost_of_investment


# ROIC (Return on Invested Capital)
def roic(capital, nopat):
    """
    ROIC (Return on Invested Capital)

    nopat = net income - dividends
    capital = debt + equity
    
    
    Args:
        capital (double): invested capital
        nopat (double): net operating profit after tax
    """
    return nopat / capital


# ROCE (Return on Capital Employed)
def roce(ebit, assets, liabilities):
    """
    ROCE (Return on Capital Employed)

    Args:
        ebit (double): Earnings before Interest, Taxes
        assets (double): 
        liabilities (double):
    """
    return ebit / (assets - liabilities)


# EBITDA Margin (Earnings before Interest, Taxes, Depreciation, and Amortization Margin) 
def ebitda_margin(ebit, depreciation, amortization, revenue):
    """
     EBITDA 
     (Earnings before Interest, Taxes, Depreciation, and Amortization)

    Args:
        ebit (double): Earnings before Interest and Tax
        depreciation (double): 
        amortization (double): 
        revenue (double): 
    """
    return (ebit + depreciation + amortization) / revenue


# EBIT (Earnings before Interest and Tax Margin)
def ebit_margin(ebit, revenue):
    """
    EBIT (Earnings before Interest and Tax)

    Args:
        ebit (double): Earnings before Interest and Tax
        revenue (double): 
    """
    return ebit / revenue


# Net Profit Margin(Net Margin)
def net_porfit_margin(revenue, cogs, opex, intrest, taxes):
    """
    Net Profit Margin(Net Margin) = net profit / revenue

    Args:
        revenue (double): 
        cogs (double): cost of goods sold
        opex (double): operating expense
        intrest (double):
        taxes (double):
    """
    return (revenue - (cogs + opex + intrest + taxes)) / revenue


# Gross Profit Margin
def gross_profit_margin(revenue, cogs):
    """
    Gross Profit Margin

    Args:
        revenue (double): 
        cogs (double): cost of goods sold
    """
    return (revenue - cogs) / revenue


# ROS (Return on Sales) or Operating Margin
def ros(revenue, ebit):
    """
    ROS (Return on Sales) or Operating Margin
    ebit (operating earning) = revenue - (cogs + opex)
    Args:
        revenue (double): 
        ebit (double): earnings before interest and taxes
    """
    return ebit / revenue


# Net Profit Margin ()
def net_profit_margin(net_income, revenue):
    """
    Net Profit Margin

    Args:
        net_income (double):
        revenue (double):
    """
    return net_income / revenue


#######################################################


# Debt to Equity Ratio
def debt_to_equity_ratio(liability, equity):
    """
    Debt to Equity Ratio
    liability = Short Term Debt + Long Term Debt + Other Fixed Payments

    Args:
        liability (double): 
        equity (double): 
    """
    return liability / equity


# Equity Ratio
def equity_ratio(equity, assets):
    """
    Equity Ratio

    Args:
        equity (double): 
        assets (double): 
    """
    return equity / assets


# Debt Ratio
def debt_ratio(liability, assets):
    """
    Debt Ratio

    Args:
        liability (): Short Term Debt + Long Term Debt
        assets (): 
    """
    return liability / assets


#######################################################


# Asset Turnover Ratio
def asset_turnover_ratio(revenue, avg_assets):
    """
    Asset Turnover Ratio
    

    Args:
        revenue (double): 
        avg_assets (double): (Total Assets ending + Total Assets beginning) / 2
    """
    return revenue / avg_assets


# Inventory Turnover Ratio
def inventory_turnover_ratio(cogs, avg_inventory):
    """
    Inventory Turnover Ratio

    Args:
        cogs (double): cost of goods solds
        avg_inventory (double): (Inventory ending + Inventory beginning) / 2
    """
    return cogs  / avg_inventory

# Inventory Turnover Days
def inventory_turnover_days(cogs, avg_inventory):
    """

    Args:
        cogs (double): 
        avg_inventory (double):
    """
    return 365 / (cogs / avg_inventory)


#######################################################


# Current Ratio
def current_ratio(assets, liability):
    """
    Current Ratio

    Args:
        assets (): 
        liability (): 
    """
    return assets / liability


# Quick Ratio
def quick_ratio(cash,
                shortterm_marketable_securties,
                accounts_receivable, liability):
    """
    Quick Ratio (Acid-Test Ratio)

    Args:
        cash (double): 
        shortterm_marketable_securties (double): 
        accounts_receivable (double): 
    """
    return (cash + shortterm_marketable_securties + accounts_receivable) / liability


# Cash Ratio
def cash_ratio(cash, cash_equivalent, liability):
    """
    Cash Ratio (Cash Asset Ratio)

    Args:
        cash (double): 
        cash_equivalent (double):
    """
    return (cash + cash_equivalent) / liability

 