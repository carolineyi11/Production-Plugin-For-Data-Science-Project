# Production-Plugin-For-Data-Science-Project

###### Using DI-Production extensions to run Python scripts

## Terminology 
 
**DI-Production** DI-Production provides various options for process flow management as part of the Diver Solution. “DI-Production” also applies to the DIProduction incorporated in Workbench.\
**DI-DiveLine** The server component of the Diver Solution which enables flexible, scalable authentication of users and centralized access to your DI Models. It also administers named users and groups and shares processing with various DI Clients, such as ProDiver and DivePort.\
**Extensions** Custom user-made nodes in DI-Production.\
**Python**  An open-source programming language.\
**Linear Regression(LR)** In statistics, linear regression is a linear approach to modeling the relationship between a scalar response and one or more explanatory variables.

## Requirements 
 
**DI-Production** or DI Workbench (Tool to access DI-Production): We advise using **7.0 or newer**.
 
Working command-line version of the **Python 3** software installed on laptop, workstation or server with the following libraries:\
numpy\
pandas\
matplotlib\
pickle\
sys

## Introduction to Files
**LR_Build_Deploy.prd**: Main Production script that combines building and deploying linear regression model

**lr_model_build.pre**: Extension file using LR_Model_Build.prd

**LR_Model_Build.prd**: Run LR_Production_Extension_Build.py to build linear regression model
##### Parameters
 - **file input** Path and name of the input file for testing (Example: /data/di/projects/Appointments_Prediction/programs/LR_extension/bike_day_raw.csv)
 - **model output** Path and name of the output LR model (Example: /data/di/projects/Appointments_Prediction/programs/LR_extension/LR_model.sav)
 - **OHE output** Path and name of the one hot encoder output (Example: /data/di/projects/Appointments_Prediction/programs/LR_extension/ohe.sav)
 - **Target Variable** Name of the target variable (Example: cnt)

**LR_Production_Extension_Build.py**: Python script to build linear regression model

**lr_model_deploy.pre**: Extension file using LR_Model_Deploy.prd

**LR_Model_Deploy.prd**: Run LR_Production_Extension_Deploy.py to deploy linear regression model
##### Parameters
 - **file input** Path and name of the input file for testing (Example: /data/di/projects/Appointments_Prediction/programs/LR_extension/bike_day_raw.csv)
 - **model input** Path and name of the input LR model (Example: /data/di/projects/Appointments_Prediction/programs/LR_extension/LR_model.sav)
 - **OHE input** Path and name of the one hot encoder input (Example: /data/di/projects/Appointments_Prediction/programs/LR_extension/ohe.sav)
 - **Target Variable** Name of the target variable (Example: cnt)
 - **Output File** Path and name of the output file (Example: /data/di/projects/Appointments_Prediction/programs/LR_extension/output_file.txt)

**LR_Production_Extension_Deploy.py**: Python script to deploy linear regression model

**bike_day_raw.csv**: Input data file for testing
- **season** : season (1:winter, 2:spring, 3:summer, 4:fall)
- **mnth** : month ( 1 to 12)
- **holiday** : whether day is holiday or not (extracted from [Web Link])
- **weekday** : day of the week
- **workingday** : if day is neither weekend nor holiday is 1, otherwise is 0.
+ **weathersit** :
- 1: Clear, Few clouds, Partly cloudy, Partly cloudy
- 2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist
- 3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds
- 4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog
- **temp** : Normalized temperature in Celsius. The values are derived via (t-t_min)/(t_max-t_min), t_min=-8, t_max=+39 (only in hourly scale)
- **atemp**: Normalized feeling temperature in Celsius. The values are derived via (t-t_min)/(t_max-t_min), t_min=-16, t_max=+50 (only in hourly scale)
- **hum**: Normalized humidity. The values are divided to 100 (max)
- **windspeed**: Normalized wind speed. The values are divided to 67 (max)
- **cnt**: Count of total rental bikes including both casual and registered

**Production_Extension_Guidance.pdf**: Guidance on how to create and install a DI-Production extension 


## Installation Steps
 1: Use the two extension files to set up production extensions (See Production_Extension_Guidance.pdf for details)
Extension **LR Model Build**: Production script "LR_Model_Build.prd"\
Extension **LR Model Deploy**: Production script "LR_Model_Deploy.prd"

*Modify the path of python software and python code files in the production scripts if necessary.

 2: Open the production script "LR_Build_Deploy.prd" and config all the parameters

 3: Run the production script "LR_Build_Deploy.prd" to build linear regression model and to create output file with predicted target value
