import pandas as pd

if __name__ == '__main__':
    
     # Read the sheets on survival rates in a dictionary
     survivalrates = {}
    
     # Read the sheets and skip a row
     for i in range(2002, 2019):
          survivalrates[str(i)] = pd.read_excel('data/business-demographics.xlsx', sheet_name= str(i) + ' Survival Rates', skiprows=1)

     # Remove 'Births' and the columns with survival rates in numbers
     for i in range(2002, 2019):
          survivalrates[str(i)].drop(survivalrates[str(i)].columns[[2, 3, 5, 7, 9, 11]], axis=1, inplace=True)
    
     # Rename columns
     for i in range(2002, 2019):
          survivalrates[str(i)].rename(columns={'Per cent': '1 Year Survival in %', 'Per cent.1': '2 Year Survival in %', 'Per cent.2': '3 Year Survival in %','Per cent.3': '4 Year Survival in %','Per cent.4': '5 Year Survival in %',}, inplace=True)

     # Only keep rows with borough information
     for i in range(2002, 2019):
          survivalrates[str(i)] = survivalrates[str(i)].iloc[1:34]

     # Rename 'Area' to 'Borough'
     for i in range(2002, 2019):
          survivalrates[str(i)].rename(columns={'Area': 'Borough'}, inplace = True)  

     # Remove columns that contain ':'
     for i in range(2002, 2019):
          survivalrates[str(i)].drop(columns = survivalrates[str(i)].columns[(survivalrates[str(i)] == ':').any()], inplace = True)

     # Round all numbers to one decimal place
     for i in range(2002, 2019):
          survivalrates[str(i)] = survivalrates[str(i)].round(decimals = 1)

     # Set the index to the column 'Borough'
     for i in range(2002, 2019):
          survivalrates[str(i)].set_index('Borough', inplace=True)

     # Read the Active Enterprises by year sheet
     activeenterprises = pd.read_excel('data/business-demographics.xlsx', sheet_name= 'Active Enterprises by year')

     # Only keep rows with borough information
     activeenterprises = activeenterprises.iloc[1:34]

     # Rename 'Area' to 'Borough'
     activeenterprises.rename(columns={'Area': 'Borough'}, inplace = True)  

     # Convert the headers from integers to string
     activeenterprises.columns = activeenterprises.columns.map(str)

     # Convert the numerical data to int
     for i in range (2002, 2020):
          activeenterprises[str(i)] = activeenterprises[str(i)].astype(int)

     # Set the index to the column 'Borough'
     activeenterprises.set_index('Borough', inplace=True)

     # Read the sheets and skip a row
     enterprisedeaths = pd.read_excel('data/business-demographics.xlsx', sheet_name= 'Enterprise deaths by year', skiprows=1)

     # Rename 'Area' to 'Borough'
     enterprisedeaths.rename(columns={'Area': 'Borough'}, inplace = True) 

     # Convert the column names from integers to string
     enterprisedeaths.columns = enterprisedeaths.columns.map(str)

     # Remove columns with number of businesses
     for i in range (2004, 2020):
          enterprisedeaths.drop([str(i)], axis = 1, inplace = True)

     # Drop columns with only null values
     enterprisedeaths.dropna(axis = 1, how = 'all', inplace = True)

     # Rename columns by removing '.1' at the end 
     enterprisedeaths.columns = enterprisedeaths.columns.str.strip(to_strip = '.1')
     enterprisedeaths.columns = enterprisedeaths.columns.map(str)

     # Rename the column '20' to '2011'
     enterprisedeaths.rename(columns={'20': '2011'}, inplace = True)  

     # Only keep rows with borough information
     enterprisedeaths = enterprisedeaths.iloc[1:34]

     # Round all numbers to one decimal place
     enterprisedeaths = enterprisedeaths.round(decimals = 1)

     # Set the index to the column 'Borough'
     enterprisedeaths.set_index('Borough', inplace=True)

     # Rename 20 to 2011
     enterprisedeaths.rename(columns={"20": "2011"}, inplace = True)

     # Save only the relevant sheets 
     with pd.ExcelWriter('data/prepared_data1.xlsx') as writer:  
          activeenterprises.to_excel(writer, sheet_name='Active Enterprises by Year')
          enterprisedeaths.to_excel(writer, sheet_name='Death Rates in % by Year')
          for i in range(2002, 2019):
               survivalrates[str(i)].to_excel(writer, sheet_name= str(i) + ' Survival Rates')