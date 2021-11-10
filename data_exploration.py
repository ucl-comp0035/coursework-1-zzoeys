import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

if __name__ == '__main__':
    
    def clean_data(df):

        '''Convert the column names to strings and set the column 'Borough' as the index.'''

        df.columns = df.columns.map(str)
        df.set_index('Borough', inplace=True)

    def remove_code(df):
        
        '''Remove the column 'Code'.'''

        df.drop(['Code'], axis = 1, inplace = True)

    # Read and clean sheets on survival rates
    survivalrates = {}

    for i in range(2002, 2019):
        survivalrates[str(i)] = pd.read_excel('data/prepared_data.xlsx', sheet_name= str(i) + ' Survival Rates')
        clean_data(survivalrates[str(i)])

    # Read and clean sheet on active enterprises
    activeenterprises = pd.read_excel('data/prepared_data.xlsx', sheet_name= 'Active Enterprises by Year')
    clean_data(activeenterprises)

    # Read and clean sheet on death rates
    deathrates = pd.read_excel('data/prepared_data.xlsx', sheet_name= 'Death Rates in % by Year')
    clean_data(deathrates)

    # Remove the column for 'Code' as it is not numeric
    remove_code(survivalrates['2002'])

    # Transpose the dataframe so that it can be plotted
    survivalrates_transposed = survivalrates['2002'].transpose()

    # Plot the transposed dataframe for all boroughts
    survivalrates_transposed.plot()
    plt.title('Survival Rates of Businesses that started in 2002')
    plt.xlabel('Survival Rates')
    plt.ylabel('%')
    plt.savefig('charts/survival_rates_2002.png')

    # Remove the column for 'Code' as it is not numeric
    remove_code(activeenterprises)

    # Transpose the dataframe
    activeenterprises_transposed = activeenterprises.transpose()

    # Convert the data to int 
    activeenterprises_transposed = activeenterprises_transposed.astype(int)

    # Plot the transposed dataframe for all boroughs
    activeenterprises_transposed.plot()
    plt.title('Active Enterprises Through the Years')
    plt.xlabel('Years')
    plt.ylabel('Numbers')
    plt.savefig('charts/active_enterprises.png')

    # Remove the column for 'Code' as it is not numeric
    remove_code(deathrates)

    # Plot a boxplot of the deathrates for each year
    sns.boxplot(data = deathrates)
    plt.title('Death Rates Through the Years')
    plt.xlabel('Years')
    plt.ylabel('%')
    plt.savefig('charts/boxplot_deathrates.png')

    # Create a list and append 'Borough'
    five_year_survival_rate_list = []
    five_year_survival_rate_list.append(list(survivalrates['2002'].index))

    # Append the relevant 5-year survival rates for businesses created in various years
    for i in range (2002, 2015):
        five_year_survival_rate_list.append(list(survivalrates[str(i)]['5 Year Survival in %']))

    # Transpose and read the dataframe
    five_year_survival_rate_df = pd.DataFrame(five_year_survival_rate_list).transpose()

    # Set the column names
    five_year_survival_rate_df.columns=['Borough', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014']

    # Clean the data
    clean_data(five_year_survival_rate_df)

    # Convert datatype from object to int
    five_year_survival_rate_df = five_year_survival_rate_df.astype(float)

    # Plot a boxplot of the 5-year survival rates in different years
    sns.boxplot(data=five_year_survival_rate_df)
    plt.title('5-Year Survival Rates Through the Years')
    plt.xlabel('Years')
    plt.ylabel('%')
    plt.savefig('charts/boxplot_5year_survival_rate.png')

    # Remove the column for 'Code' as it is not numeric
    for year in [2005, 2012, 2013, 2014]:
        remove_code(survivalrates[str(year)])

    # Plot the outliers
    survivalrates['2005'].loc['Newham'].plot(label = 'Newham in 2005')
    survivalrates['2012'].loc['Lambeth'].plot(label = 'Lambeth in 2012')
    survivalrates['2013'].loc['Lambeth'].plot(label = 'Lambeth in 2013')
    survivalrates['2014'].loc['Lambeth'].plot(label = 'Lambeth in 2014')
    plt.title('Survival Rates for Outliers')
    plt.xlabel('Survival Rates')
    plt.ylabel('%')
    plt.legend()
    plt.savefig('charts/survival_rates_outliers.png')

    # Add a column with the average 5-year survival rate in each borough
    five_year_survival_rate_df['mean'] = five_year_survival_rate_df.iloc[:, 1:14].mean(axis=1)

    # Add a new sheet to the existing file
    with pd.ExcelWriter('data/prepared_data.xlsx',
                    mode = 'a', engine='openpyxl') as writer:  
        five_year_survival_rate_df.to_excel(writer, sheet_name='5-Year Survival Rates')
 
    # Plot a bar graph with the 5-year survival rate average for each borough
    five_year_survival_rate_df.sort_values('mean', ascending = False)['mean'].plot.bar()
    plt.title('5-Year Survival Rate Average')
    plt.xlabel('Borough')
    plt.ylabel('%')
    plt.savefig('charts/bargraph_average_5-year_survival_rate.png')

    # Identify the borough with the highest average 5-year survival rate
    max = five_year_survival_rate_df['mean'].idxmax()
    print('Borough with the highest average 5-year survival rate is ' + str(max) + ' with a survival rate of ' + str(round(five_year_survival_rate_df['mean'].max())) + '%')

    # Plot a bar graph of with the number of active enterprises in each borough in 2019
    activeenterprises.sort_values('2019', ascending = False)['2019'].plot.bar()
    plt.title('Number of Active Enterprises in 2019')
    plt.xlabel('Borough')
    plt.ylabel('Number')
    plt.savefig('charts/bargraph_active_enterprises_2019.png')

    # Identify the borough with the highest number of active enterprises in 2019
    max = activeenterprises['2019'].idxmax()
    print('The borough with the highest number of active enterprises in 2019 is ' + str(max) + ' with ' + str(activeenterprises['2019'].max()) + ' enterprises.')

    # Add a column with the average death rate in each borough
    deathrates['mean'] = deathrates.iloc[:, 1:14].mean(axis = 1)

    # Round the averages to one decimal place
    deathrates['mean'] = deathrates['mean'].round(decimals = 1)

    # Replace the old sheet with the new sheet without outliers and with a column with the averages
    with pd.ExcelWriter('data/prepared_data.xlsx',
                    mode = 'a', engine='openpyxl') as writer:  
        deathrates.to_excel(writer, sheet_name='Death Rates in % by Year') 

    # Plot a bar graph of death rate averages for each borough
    deathrates.sort_values('mean', ascending = True)['mean'].plot.bar()
    plt.title('Average Death Rates in each Borough')
    plt.xlabel('Borough')
    plt.ylabel('%')
    plt.savefig('charts/bargraph_ave_deathrates.png')

    # Identify the borough with the lowest average death rate
    min = deathrates['mean'].idxmin()
    print('The borough with the lowest average death rate is ' + str(min) + ' with a death rate of ' + str(deathrates['mean'].min()) + ' %')