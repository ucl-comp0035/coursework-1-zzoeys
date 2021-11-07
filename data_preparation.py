import pandas as pd

if __name__ == '__main__':
    
    # Print all sheet names
     all_sheets = pd.ExcelFile('data/business-demographics.xlsx')
     print(all_sheets.sheet_names)
    
     survivalrates = {}
     
     # Read the sheets with business survival rates
     for i in range(2002, 2019):
          survivalrates[str(i)] = pd.read_excel('data/business-demographics.xlsx', sheet_name= str(i) + ' Survival Rates', skiprows=1)

     # Print the number of rows and columns in the dataframe
     print(survivalrates['2002'].shape)

     # Remove 'Births' and the columns with survival rates in numbers
     for i in range(2002, 2019):
          survivalrates[str(i)].drop(survivalrates[str(i)].columns[[2, 3, 5, 7, 9, 11]], axis=1, inplace=True)
    
     # Rename columns
     for i in range(2002, 2019):
          survivalrates[str(i)].rename(columns={'Per cent': '1 Year Survival in %', 'Per cent.1': '2 Year Survival in %', 'Per cent.2': '3 Year Survival in %','Per cent.3': '4 Year Survival in %','Per cent.4': '5 Year Survival in %',}, inplace=True)
    
     # Check for missing values
     print(survivalrates['2002'].isnull().sum())
     print(survivalrates['2002'].isna().sum())

     missing_rows_na = survivalrates['2002'][survivalrates['2002'].isna().any(axis=1)]
     print(missing_rows_na)

     missing_rows_na = survivalrates['2002'][survivalrates['2002'].isna().any(axis=1)]
     print(missing_rows_na)

     for i in range(2002, 2019):
          survivalrates[str(i)] = survivalrates[str(i)].iloc[1:34]

     for i in range(2002, 2019):
          survivalrates[str(i)].drop(columns = survivalrates[str(i)].columns[(survivalrates[str(i)] == ':').any()], inplace = True)

     print(survivalrates['2002'].info(verbose=True))

     # Read the Active Enterprises by year sheet
     activeenterprises = pd.read_excel('data/business-demographics.xlsx', sheet_name= 'Active Enterprises by year')

     activeenterprises = activeenterprises.iloc[1:34]

     print(activeenterprises.isnull().sum())
     print(activeenterprises.isna().sum())

     # Convert the headers from integers to string
     activeenterprises.columns = activeenterprises.columns.map(str)

     print(activeenterprises.info(verbose=True))

     for i in range (2002, 2020):
          activeenterprises[str(i)] = activeenterprises[str(i)].astype(int)

     # Save only the relevant sheets (maybe try diff file for each set of sheets)
     with pd.ExcelWriter('data/prepared_data.xlsx') as writer:  
          activeenterprises.to_excel(writer, sheet_name='Active Enterprises by Year')
          for i in range(2002, 2019):
               survivalrates[str(i)].to_excel(writer, sheet_name= str(i) + ' Survival Rates')

