import morningstar

# Construct ms instance
ms = morningstar.api()

# Get all data
# ms.getAllData('AAPL')

# Get key ratios report
print(ms.getKeyRatios('AAPL').to_string())
                
# Get annual income statement
print(ms.getFinancials('income_statement', 'annual', 'AAPL').to_string())
                
# Get historic price ratios
print(ms.getHistoricPriceRatios('AAPL').to_string())
        
# Get current price ratios
print(ms.getCurrentPriceRatios('AAPL').to_string())
        
# Get forward price ratios
print(ms.getForwardPriceRatios('AAPL').to_string())
        
# Get daily historic prices
print(ms.getHistoricPrices('daily', 'AAPL').to_string())
