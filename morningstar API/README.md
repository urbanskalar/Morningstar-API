# Morningstar API

This class aims to provide data from morningstar API. It will work for as long as Morningstar does not change their API.

Module is made of different definitions that try to get different reports from http://financials.morningstar.com.

Definition getKeyRatios() returns key ratios table in pandas.Dataframe format.
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

