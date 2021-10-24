# Wind Energy Analysis and Prediction
---
### Problem Statement

I am an analyst at General Analytics, a consulting company which expertise is in forecasting. Our audience is the forecasting department at (Electric Reliability Council of Texas) or ERCOT, the Texas power regulator. We want to sell them an application that predicts hourly wind power output for the next month. In this project, we will attempt to create a model to predict the hourly wind power output for the ERCOT power grid for a month's time span. Our baseline will be the mean of the power output over a month timespan, and we will see if we can create a model that will outperform that baseline. Our evaluation metrics will be Mean Squared Error, Mean Absolute Error, and Root Mean squared Error.

### Background

A combination of seven power sources supply the Texas power grid, these include Gas, Hydro-Electric, Nuclear, Solar, Wind, Coal, and Other sources. The top three sources are Natural Gas, Wind, and Coal. Historically coal has been the main power generator for American power grids, however, due to climate change policies, American electric power generation is switching to carbon-free renewable energy sources. In America's path to zero carbon emissions, Natural gas, which has a less carbon footprint than coal, has become the reliable transition fuel for America's power generation. In the ERCOT power grid, the two main renewable resources are wind and solar. These two sources do not provide power as consistently as natural gas, solar power output is reduced when it is cloudy and zero at night, wind turbines won't generate power when the wind is not blowing. When these renewable power sources are reduced due to weather or sunlight, Natural Gas power plants increase their power output to meet the demand of the power grid. With a model that can predict wind power output a month into the future, ERCOT can better plan how much natural gas power to feed into the system.

### Description of data

#### Data Included for Analysis
* [`texas_power_gen.csv`](../Data/texas_power_gen.csv): EIA Power Generation Data for ERCOT.
* [`U.S. Energy Information Administration (EIA) - ERCOT Power Data`](https://www.eia.gov/electricity/gridmonitor/dashboard/electric_overview/balancing_authority/ERCO): EIA website for ERCOT Grid.


#### Data Included Streamlit application
*[`EIA API for Texas`](https://www.eia.gov/opendata/qb.php?category=3390202&sdid=EBA.TEX-ALL.TI.HL): EIA API to update Streamlit app.

### Model Selection and performance
| Model | #1 ARIMA | #2 Auto-ARIMA| #3 Prophet (basline)| #4 Prophet (Seasonality)|
|:-----:| :-----:| :-----: | :-----:| :-----: |
| Baseline RMSE mWh | 6620 | 6620 | 6504 | 6504 |
| MSE | 125 E6 | 143 E6 | 37 E6 | 34 E6 |
| RMSE | 11k | 12k | 6.1k | 5.9k |
