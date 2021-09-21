# Morningstar API

This class aims to provide data from morningstar API. It will work for as long as Morningstar does not change their API.Module is made of different definitions that try to get different reports from http://financials.morningstar.com.

Definition `getKeyRatios(ticker, market)` returns key ratios table in pandas.Dataframe format. Below is an example for `'AAPL'` ticker.
```
                   Unnamed: 0  2011-09  2012-09  2013-09  2014-09  2015-09  2016-09  2017-09  2018-09  2019-09  2020-09      TTM
0             Revenue USD Mil  108,249  156,508  170,910  182,795  233,715  215,639  229,234  265,595  260,174  274,515  347,155
1              Gross Margin %     40.5     43.9     37.6     38.6     40.1     39.1     38.5     38.3     37.8     38.2     41.0
2    Operating Income USD Mil   33,790   55,241   48,999   52,503   71,230   60,024   61,344   70,898   63,930   66,288   99,938
3          Operating Margin %     31.2     35.3     28.7     28.7     30.5     27.8     26.8     26.7     24.6     24.1     28.8
4          Net Income USD Mil   25,922   41,733   37,037   39,510   53,394   45,687   48,351   59,531   55,256   57,411   86,802
..                        ...      ...      ...      ...      ...      ...      ...      ...      ...      ...      ...      ...
96      Cash Conversion Cycle   -51.96   -52.13   -44.50   -48.64   -52.97   -67.29   -75.91   -78.92   -73.76   -60.54   -40.74
97       Receivables Turnover    19.90    19.20    14.22    11.96    13.62    13.23    13.63    12.94    11.28    14.06    19.64
98         Inventory Turnover    70.53   112.12    83.45    57.94    62.82    58.64    40.37    37.17    40.13    41.52    44.74
99      Fixed Assets Turnover    17.26    13.48    10.67     9.82    10.85     8.71     7.54     7.07     6.61     7.40     9.34
100            Asset Turnover     1.13     1.07     0.89     0.83     0.89     0.70     0.66     0.72     0.74     0.83     1.07

[96 rows x 12 columns]
```

Definition `getFinancials(report, period, ticker, market)` returns different financial tables in pandas.Dataframe format. Parameter `report` specifies which financial table we are interested in. Possible values are `'income_statement'`, `'balance_sheet'` or `'cash_flow'`. Parameter `period` specifies period of provided data. Possible values are `'annual'` or `'quarterly'`. Below is an example of annual income statement for `'AAPL'` ticker.
```
            Fiscal year ends in September. USD.       2016-09       2017-09       2018-09       2019-09       2020-09           TTM
0                                       Revenue  2.156390e+11  2.292340e+11  2.655950e+11  2.601740e+11  2.745150e+11  3.471550e+11
1                               Cost of revenue  1.313760e+11  1.410480e+11  1.637560e+11  1.617820e+11  1.695590e+11  2.048040e+11
2                                  Gross profit  8.426300e+10  8.818600e+10  1.018390e+11  9.839200e+10  1.049560e+11  1.423510e+11
3                            Operating expenses           NaN           NaN           NaN           NaN           NaN           NaN
4                      Research and development  1.004500e+10  1.158100e+10  1.423600e+10  1.621700e+10  1.875200e+10  2.112000e+10
5             Sales, General and administrative  1.419400e+10  1.526100e+10  1.670500e+10  1.824500e+10  1.991600e+10  2.129300e+10
6                      Total operating expenses  2.423900e+10  2.684200e+10  3.094100e+10  3.446200e+10  3.866800e+10  4.241300e+10
7                              Operating income  6.002400e+10  6.134400e+10  7.089800e+10  6.393000e+10  6.628800e+10  9.993800e+10
8                              Interest Expense  1.456000e+09  2.323000e+09  3.240000e+09  3.576000e+09  2.873000e+09  2.607000e+09
9                        Other income (expense)  2.804000e+09  5.068000e+09  5.245000e+09  5.383000e+09  3.676000e+09  3.529000e+09
10                          Income before taxes  6.137200e+10  6.408900e+10  7.290300e+10  6.573700e+10  6.709100e+10  1.008600e+11
11                   Provision for income taxes  1.568500e+10  1.573800e+10  1.337200e+10  1.048100e+10  9.680000e+09  1.405800e+10
12        Net income from continuing operations  4.568700e+10  4.835100e+10  5.953100e+10  5.525600e+10  5.741100e+10  8.680200e+10
13                                   Net income  4.568700e+10  4.835100e+10  5.953100e+10  5.525600e+10  5.741100e+10  8.680200e+10
14  Net income available to common shareholders  4.568700e+10  4.835100e+10  5.953100e+10  5.525600e+10  5.741100e+10  8.680200e+10
15                           Earnings per share           NaN           NaN           NaN           NaN           NaN           NaN
16                                        Basic  2.090000e+00  2.320000e+00  3.000000e+00  2.990000e+00  3.310000e+00  5.170000e+00
17                                      Diluted  2.080000e+00  2.300000e+00  2.980000e+00  2.970000e+00  3.280000e+00  5.120000e+00
18          Weighted average shares outstanding           NaN           NaN           NaN           NaN           NaN           NaN
19                                        Basic  2.188300e+04  2.086900e+04  1.982200e+04  1.847100e+04  1.735200e+04  1.684400e+04
20                                      Diluted  2.200100e+04  2.100700e+04  2.000000e+04  1.859600e+04  1.752800e+04  1.702000e+04
21                                       EBITDA  7.333300e+04  7.656900e+04  8.704600e+04  8.186000e+04  8.102000e+04  1.144640e+05
```

Definition `getHistoricPriceRatios(ticker, market)` returns historic price ratios in pandas.Dataframe format. This outpus is not perfect as it does not show dates for each column. Comparing results to data from Morningstar webpage, I was not able to figure out what last column represents (11). The others however represent past years. So column 10 is actually current year - 1, column 9 is current year - 2, etc. Below is an example of historic price ratios report for `'AAPL'` ticker.
```
                 0     1     2     3     4     5     6     7     8     9     10    11
0    Price/Earnings   NaN   NaN   NaN   NaN   NaN   NaN   NaN   NaN   NaN   NaN   NaN
1              AAPL  14.6  12.1  14.1  17.1  11.4  13.9  18.4  13.2  24.7  40.5  27.9
2           S&P 500  13.7  15.0  18.6  18.6  19.0  20.3  22.7  17.1  22.6  28.3  25.3
3        Price/Book   NaN   NaN   NaN   NaN   NaN   NaN   NaN   NaN   NaN   NaN   NaN
4              AAPL   4.9   3.9   4.1   5.8   4.9   4.7   6.4   7.0  14.2  34.1  36.8
5           S&P 500   2.0   2.1   2.6   2.7   2.7   2.8   3.2   2.9   3.4   4.0   4.5
6       Price/Sales   NaN   NaN   NaN   NaN   NaN   NaN   NaN   NaN   NaN   NaN   NaN
7              AAPL   3.5   3.1   3.1   3.7   2.6   3.0   3.9   3.0   5.2   8.5   7.0
8           S&P 500   1.2   1.3   1.7   1.8   1.8   2.0   2.2   1.9   2.4   2.8   3.2
9   Price/Cash Flow   NaN   NaN   NaN   NaN   NaN   NaN   NaN   NaN   NaN   NaN   NaN
10             AAPL  10.1   8.9   9.7  11.3   7.5   9.7  14.0  10.2  19.7  28.8  23.3
11          S&P 500   8.5   9.2  11.2  11.5  11.5  12.4  14.3  11.6  14.4  16.6  18.1
```

Definition `getCurrentPriceRatios(ticker, market)` returns current price ratios table in pandas.Dataframe format. Below is an example for `'AAPL'` ticker.
```
                                           Unnamed: 0                                               AAPL                                       Industry Avg                                            S&P 500                                       AAPL 5Y Avg*                                         Unnamed: 5 Relative to Industry Relative to Industry.1  Unnamed: 8 Relative to S&P 500 Relative to S&P 500.1
0                                                 NaN                                                NaN                                                NaN                                                NaN                                                NaN                                                NaN                  NaN                    NaN         NaN                 NaN                   NaN
1                                      Price/Earnings                                               27.9                                                  —                                               25.3                                               18.8                                                NaN                  NaN                    NaN         NaN                 NaN                   NaN
2                                                 NaN                                                NaN                                                NaN                                                NaN                                                NaN                                                NaN                  NaN                    NaN         NaN                 NaN                   NaN
3                                          Price/Book                                               36.8                                                  —                                                4.5                                                9.7                                                NaN                  NaN                    NaN         NaN                 NaN                   NaN
4                                                 NaN                                                NaN                                                NaN                                                NaN                                                NaN                                                NaN                  NaN                    NaN         NaN                 NaN                   NaN
5                                         Price/Sales                                                7.0                                                  —                                                3.2                                                4.0                                                NaN                  NaN                    NaN         NaN                 NaN                   NaN
6                                                 NaN                                                NaN                                                NaN                                                NaN                                                NaN                                                NaN                  NaN                    NaN         NaN                 NaN                   NaN
7                                     Price/Cash Flow                                               23.3                                                  —                                               18.1                                               16.7                                                NaN                  NaN                    NaN         NaN                 NaN                   NaN
8                                                 NaN                                                NaN                                                NaN                                                NaN                                                NaN                                                NaN                  NaN                    NaN         NaN                 NaN                   NaN
9                                    Dividend Yield %                                                0.6                                                  —                                                1.4                                                1.4                                                NaN                  NaN                    NaN         NaN                 NaN                   NaN
10                                                NaN                                                NaN                                                NaN                                                NaN                                                NaN                                                NaN                  NaN                    NaN         NaN                 NaN                   NaN
11                                   Price/Fair Value                                            Premium                                                  —                                                  —                                                  —                                                NaN                  NaN                    NaN         NaN                 NaN                   NaN
12                                                NaN                                                NaN                                                NaN                                                NaN                                                NaN                                                NaN                  NaN                    NaN         NaN                 NaN                   NaN
13  Data as of 09/20/2021, *Price/Cash Flow uses 3...  Data as of 09/20/2021, *Price/Cash Flow uses 3...  Data as of 09/20/2021, *Price/Cash Flow uses 3...  Data as of 09/20/2021, *Price/Cash Flow uses 3...  Data as of 09/20/2021, *Price/Cash Flow uses 3...  Data as of 09/20/2021, *Price/Cash Flow uses 3...            –  Avg  +              –  Avg  +         NaN           –  Avg  +             –  Avg  +
```

Definition `getForwardPriceRatios(ticker, market)` returns forward price ratios table in pandas.Dataframe format. Below is an example for `'AAPL'` ticker.
```
               Unnamed: 0                    AAPL            Industry Avg                 S&P 500              Unnamed: 4 Relative to Industry Relative to Industry.1  Unnamed: 7 Relative to S&P 500 Relative to S&P 500.1
0                     NaN                     NaN                     NaN                     NaN                     NaN                  NaN                    NaN         NaN                 NaN                   NaN
1  Forward Price/Earnings                    25.6                       —                    21.8                     NaN                  NaN                    NaN         NaN                 NaN                   NaN
2                     NaN                     NaN                     NaN                     NaN                     NaN                  NaN                    NaN         NaN                 NaN                   NaN
3               PEG Ratio                     2.0                       —                       —                     NaN                  NaN                    NaN         NaN                 NaN                   NaN
4                     NaN                     NaN                     NaN                     NaN                     NaN                  NaN                    NaN         NaN                 NaN                   NaN
5       PEG Payback (Yrs)                    11.0                       —                       —                     NaN                  NaN                    NaN         NaN                 NaN                   NaN
6                     NaN                     NaN                     NaN                     NaN                     NaN                  NaN                    NaN         NaN                 NaN                   NaN
7  Data as of 09/20/2021.  Data as of 09/20/2021.  Data as of 09/20/2021.  Data as of 09/20/2021.  Data as of 09/20/2021.            –  Avg  +              –  Avg  +         NaN           –  Avg  +             –  Avg  +
```

Definition `getHistoricPrices(frequency, ticker, market)` returns historic market prices table in pandas.Dataframe format. Parameter `frequency` specifies frequency of data accuired in table. Possible values are `'daily'`, `'weekly'`, `'monthly'`, `'quarterly'` or `'annualy'`. Below is an example for `'AAPL'` ticker.
```
            Date    Open    High     Low   Close         Volume
0     09/20/2021  143.80  144.84  141.27  142.94    123,478,863
1     09/17/2021  148.82  148.82  145.76  146.06    129,868,824
2     09/16/2021  148.44  148.97  147.22  148.79     68,034,149
3     09/15/2021  148.56  149.44  146.37  149.03     83,281,315
4     09/14/2021  150.35  151.07  146.91  148.12    109,296,295
...          ...     ...     ...     ...     ...            ...
4010  02/28/2006    2.56    2.59    2.43    2.45  1,255,103,220
4011  02/27/2006    2.57    2.58    2.52    2.54    783,983,704
4012  02/24/2006    2.57    2.60    2.54    2.55    252,514,472
4013  02/23/2006    2.56    2.61    2.55    2.56    852,676,300
4014  02/22/2006    2.46    2.56    2.43    2.55    963,722,648

[4015 rows x 6 columns]
```

Definition `getAllData(ticker, market)` returns all data that is possible to gather from morningstar api as dictionary of pandas.Dataframe tables. Dictionary includes tables with the following keys:
```
key_ratios
annual:income_statement
quarterly:income_statement
annual:balance_sheet
quarterly:balance_sheet
annual:cash_flow
quarterly:cash_flow
historic_price_ratios
current_price_ratios
forward_prices_ratios
historic_prices:daily
historic_prices:weekly
historic_prices:monthly
historic_prices:quarterly
historic_prices:annualy
```
