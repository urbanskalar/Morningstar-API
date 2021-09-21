import requests
from requests.structures import CaseInsensitiveDict
import pandas as pd
import io


class api(object):
    """
    Downloads financial data from http://financials.morningstar.com/
    """

    def __init__(self):
        """
        Constructs the morningstar api instance.
        """

        # Start new session
        self.session = requests.Session()
        
        # Create empty dicitionary to save http responses
        self.responses = {}
        
        # Create empty dictionary to save parsed results
        self.results = {}
        
        

    def getAllData(self, ticker: str, market: str = ''):
        """
        Downloads and returns all data for the given market:ticker combo.
        Results are returned in dictionary of pandas.Dataframe objects containing data.
        """
        
        # Create empty dictionary to save parsed results
        self.results = {}
        
        # Get key ratios report
        self.getKeyRatios(ticker, market)
                
        # Get all possible financial reports
        reports = ['income_statement', 'balance_sheet', 'cash_flow']
        periods = ['annual', 'quarterly']
        for report in reports:
            for period in periods:
                self.getFinancials(report, period, ticker, market)
                
        # Get historic price ratios
        self.getHistoricPriceRatios(ticker, market)
        
        # Get current price ratios
        self.getCurrentPriceRatios(ticker, market)
        
        # Get forward price ratios
        self.getForwardPriceRatios(ticker, market)
        
        # Get historic prices
        frequencies = ['daily', 'weekly', 'monthly', 'quarterly', 'annualy']
        for frequency in frequencies:
            self.getHistoricPrices(frequency, ticker, market)
        
        # Return results
        return self.results
    
    def getKeyRatios(self, ticker: str, market: str = ''):
        """
        Downloads and returns key ratios for the given market:ticker combo.
        Results are returned as an array of pandas.DataFrame.
        """
		
		# Check if market is specified and add ':' if it is
        if market:
            market = market + ':'
		
        # Generate url and header
        url = (r'http://financials.morningstar.com/finan/ajax/exportKR2CSV.html?' + r'&callback=?&t={0}&region=usa&culture=en-US&cur=USD'.format(market + ticker))
        header = CaseInsensitiveDict()
        header["Referer"] = (r'https://financials.morningstar.com/ratios/r.html?t={0}&culture=en&platform=sal'.format(market + ticker))
		
        # Send request and save response
        resp = self.session.get(url, headers=header)
        self.responses['key_ratios'] = resp
        
        # Parse data from response and save it to results
        csv = pd.read_csv(io.BytesIO(self.responses['key_ratios'].content), encoding='utf8', skiprows=2)
        csv = csv[(csv['Unnamed: 0'] != 'Key Ratios -> Efficiency Ratios') & (csv['Unnamed: 0'] != 'Key Ratios -> Financial Health') & (csv['Unnamed: 0'] != 'Key Ratios -> Cash Flow') & (csv['Unnamed: 0'] != 'Key Ratios -> Growth') & (csv['Unnamed: 0'] != 'Key Ratios -> Profitability')]
        self.results['key_ratios'] = csv
        
        # Return dataframe with result
        return csv
        
            
        
    def getFinancials(self, report: str, period: str,  ticker: str, market: str = ''):
        """
        Downloads and returns specified financial report for the given market:ticker combo.
        Results are returned as an array of pandas.DataFrame.
        """
        
        # Check if correct report input parameter is used
        if report == 'income_statement':
            report_ = 'is'
        elif report == 'balance_sheet':
            report_ = 'bs'
        elif report == 'cash_flow':
            report_ = 'cf'
        else:
            raise ValueError()
        
        # Check if correct period input parameter is used
        if period == 'annual':
            period_ = '12'
        elif period == 'quarterly':
            period_ = '3'
        else:
            raise ValueError()
        
        # Check if market is specified and add ':' if it is
        if market:
            market = market + ':'
            
                   
        # Generater header for request
        header = CaseInsensitiveDict()
        header["Referer"] = (r'http://financials.morningstar.com/income-statement/is.html?t={0}&region=usa&culture=en-US'.format(market + ticker))
		
        # Generate url
        """ URL construction legend:
            reportType: is = Income Statement, cf = Cash Flow, bs = Balance Sheet
            period: 12 for annual reporting, 3 for quarterly reporting
            dataType: this doesn't seem to change and is always A
            order: asc or desc (ascending or descending)
            columnYear: 5 or 10 are the only two values supported, 10 years report need register
            number: The units of the response data. 1 = None 2 = Thousands 3 = Millions 4 = Billions      """
        url = (r'http://financials.morningstar.com/ajax/ReportProcess4CSV.html?t=' + market + ticker +
            r'&region=usa&culture=en-US&cur=USD' +
            r'&reportType=' + report_ + r'&period=' + period_ +
            r'&dataType=A&order=asc&columnYear=5&rounding=3&view=raw')
        
        # Send request and save response
        resp = self.session.get(url, headers=header)
        self.responses[period + ":" + report] = resp
        
        # Parse data from response and save it to results
        csv = pd.read_csv(io.BytesIO(self.responses[period + ":" + report].content), encoding='utf8', skiprows=1)
        self.results[period + ":" + report] = csv
        
        # Return dataframe with result
        return csv
                
    def getHistoricPriceRatios(self, ticker: str, market: str = ''):
        """
        Downloads and returns historic price ratios for the given market:ticker combo.
        Results are returned as an array of pandas.DataFrame.
        """
		
		# Check if market is specified and add ':' if it is
        if market:
            market = market + ':'
		
        # Generate url and header
        url = (r'http://financials.morningstar.com/valuate/valuation-history.action?&t={0}&type=price-earnings'.format(market + ticker))
        
        # Send request and save response
        resp = self.session.get(url)#, headers=header)
        self.responses['historic_price_ratios'] = resp
        
        # Parse data from response and save it to results
        html = pd.read_html(io.BytesIO(self.responses['historic_price_ratios'].content), encoding='utf8')
        self.results['historic_price_ratios'] = html[0]
        
        # Return dataframe with result
        return html[0]

    def getCurrentPriceRatios(self, ticker: str, market: str = ''):
        """
        Downloads and returns current price ratios for the given market:ticker combo.
        Results are returned as an array of pandas.DataFrame.
        """
		
		# Check if market is specified and add ':' if it is
        if market:
            market = market + ':'
		
        # Generate url and header
        url = (r'http://financials.morningstar.com/valuate/current-valuation-list.action?&t={0}'.format(market + ticker))
        
        # Send request and save response
        resp = self.session.get(url)#, headers=header)
        self.responses['current_price_ratios'] = resp
        
        # Parse data from response and save it to results
        html = pd.read_html(io.BytesIO(self.responses['current_price_ratios'].content), encoding='utf8')
        self.results['current_price_ratios'] = html[0]
        
        # Return dataframe with result
        return html[0]
            
    def getForwardPriceRatios(self, ticker: str, market: str = ''):
        """
        Downloads and returns forward price ratios for the given market:ticker combo.
        Results are returned as an array of pandas.DataFrame.
        """
		
		# Check if market is specified and add ':' if it is
        if market:
            market = market + ':'
		
        # Generate url and header
        url = (r'http://financials.morningstar.com/valuate/forward-valuation-list.action?&t={0}'.format(market + ticker))
        
        # Send request and save response
        resp = self.session.get(url)#, headers=header)
        self.responses['forward_prices_ratios'] = resp
        
        # Parse data from response and save it to results
        html = pd.read_html(io.BytesIO(self.responses['forward_prices_ratios'].content), encoding='utf8')
        self.results['forward_prices_ratios'] = html[0]
        
        # Return dataframe with result
        return html[0]
        
    def getHistoricPrices(self, frequency: str, ticker: str, market: str = ''):
        """
        Downloads and returns history prices for the given market:ticker combo.
        Results are returned as an array of pandas.DataFrame.
        """
		
		# Check if correct frequency input parameter is used
        if frequency == 'daily':
            frequency_ = 'd'
        elif frequency == 'weekly':
            frequency_ = 'w'
        elif frequency == 'monthly':
            frequency_ = 'm'
        elif frequency == 'quarterly':
            frequency_ = 'q'
        elif frequency == 'annualy':
            frequency_ = 'a'
        else:
            raise ValueError()
		
		
		# Check if market is specified and add ':' if it is
        if market:
            market = market + ':'
		
        # Generate url and header
        url = (r'http://performance.morningstar.com/perform/Performance/stock/exportStockPrice.action?t=' + market + ticker + r'&pd=max&freq=' + frequency_ + r'&sd=&ed=&pg=0&culture=en-US&cur=USD')
        
        # Send request and save response
        resp = self.session.get(url)#, headers=header)
        self.responses['historic_prices'] = resp
        
        # Parse data from response and save it to results
        csv = pd.read_csv(io.BytesIO(self.responses['historic_prices'].content), encoding='utf8', skiprows = 1)
        self.results['historic_prices' + ':' + frequency] = csv
        
        # Return dataframe with result
        return csv





