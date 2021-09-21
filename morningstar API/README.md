# Morningstar API

This class aims to provide data from morningstar API. It will work for as long as Morningstar does not change their API.

Module is made of different definitions that try to get different reports from http://financials.morningstar.com.

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



Definition `getFinancials(report, period, ticker, market)` returns different financial tables in pandas.Dataframe format. Parameter `report` specifies which financial table we are interested in. Possible values are `'income_statement'`, `'balance_sheet'` or `'cash_flow'` Parameter `period` specifies period of provided data. Possible values are `'annual'` or `'quarterly'` Below is an example of annual income statement for `'AAPL'` ticker.
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

Definition `getHistoricPriceRatios(ticker, market)` returns hist
