# CPI
Research &amp; modelling CPI rate in Ukraine

The research is not finished yet, 
so some models will appear in updated code
during March, 2020

## Visual analysis performed:

 - rolling mean
 - autocorrelation &amp; partial autocorrelation function
 - seasonal decomposition
 - pair plot
 - correlation plot

## Loss functions used:

 - mean squared error
 - dynamic time warping

## Models used for time series modelling:

 - ARIMAX - AutoRegressive 
 Integrated Moving Average with
 eXogenous variables
 - VARMAX - Vector AutoRegressive 
 Moving Average with
 eXogenous variables
 - SARIMAX - Seasonal AutoRegressive 
 Integrated Moving Average with
 eXogenous variables
 - Facebook Prophet - library, developed by Facebook 
 for time series analysis
 
 ## Regression models used:
 
  - Linear regression
  - Ridge regression
  
 ## Conclusions
 
  1. Correlation plot shows Philips curve:
  corr(inflation, employment) = 0.91
  
  2. Best results:
  
  - ARIMAX (4,0,0) = AR   (4)
  - ARIMAX (3,0,3) = ARMA (3,3)