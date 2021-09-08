import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # Get user input for city (chicago, new york city, washington).
    city_name_list = ['chicago','new york city','washington']
    while(True):
        city = input("Would you like to see data for Chicago, New York City, or Washington?\n").lower()
        if city in city_name_list:
            break
    filterdata_name_list = ['month','day','both','none']
    while(True):
        filterdata = input("Would you like to filter the data by month, day, both, or not at all? Type \"none\" for no time filter.\n").lower()
        if filterdata in filterdata_name_list:
            break
    if filterdata == "month":
        # Get user input for month (all, january, february, ... , june)
        month_name_list = ['january', 'february', 'march', 'april', 'may','june']
        while(True):
            month = input("Which Month? January, February, March, April, May, or June?\n").lower()
            if month in month_name_list:
                break
        day = "all"
    elif filterdata == "day":
        # Get user input for day of week (all, monday, tuesday, ... sunday)
        day_name_list = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        while(True):
            day = input("Which Day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?\n").lower()
            if day in day_name_list:
                break
        month = "all"
    elif filterdata == "both":
        # Get user input for month (all, january, february, ... , june)
        month_name_list = ['january', 'february', 'march', 'april', 'may','june']
        while(True):
            month = input("Which Month? January, February, March, April, May, or June?\n").lower()
            if month in month_name_list:
                break
        # Get user input for day of week (all, monday, tuesday, ... sunday)
        day_name_list = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        while(True):
            day = input("Which Day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?\n").lower()
            if day in day_name_list:
                break
    elif filterdata == "none":
        month = "all"
        day = "all"
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The First Statistic...\n')
    start_time = time.time()
    if month != 'all' and day != 'all':
        print("Filter: Both")
    elif month=='all' and day != 'all':
        print("Filter: Day")
        # display the most common month
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        # to find the most common month
        most_common_month = df['month'].mode()[0]
        print('Most Common Month:', months[most_common_month-1])
    elif day=='all' and month!='all':
        print("Filter: Month")
        # display the most common day of week

        # to find the most common day of week
        most_common_day = df['day_of_week'].mode()[0]
        print('Most Common Day Of Week:', most_common_day)
    else:
        print("Filter: None")
        # display the most common month
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        # to find the most common month
        most_common_month = df['month'].mode()[0]
        print('Most Common Month:', months[most_common_month-1])
        
        # display the most common day of week

        # to find the most common day of week
        most_common_day = df['day_of_week'].mode()[0]
        print('Most Common Day Of Week:', most_common_day)
        
    # display the most common start hour
    
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # to find the most common hour
    most_common_hour = df['hour'].mode()[0]

    print('Most Common Start Hour:', most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df, month, day):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Next Statistic...Most Popular Stations and Trip:\n')
    start_time = time.time()
    if month != 'all' and day != 'all':
        print("Filter: Both")
    elif month=='all' and day != 'all':
        print("Filter: Day")
    elif day=='all' and month!='all':
        print("Filter: Month")
    else:
        print("Filter: None")
    # display most commonly used start station
    
    # to find the most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]

    print('Most Commonly Used Start Station:', most_common_start_station)
    
    # display most commonly used end station
    
    # to find the most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]

    print('Most Commonly Used End Station:', most_common_end_station)

    # display most frequent combination of start station and end station trip
    
    # to find the most frequent combination of start station and end station trip
    most_frequent_combination = (df['Start Station']+' - '+df['End Station']).mode()[0]
    print('Most Frequent Combination Of Start Station and End Station Trip:', most_frequent_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df, month, day):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating The Next Statistic....Trip Duration:\n')
    start_time = time.time()
    if month != 'all' and day != 'all':
        print("Filter: Both")
    elif month=='all' and day != 'all':
        print("Filter: Day")
    elif day=='all' and month!='all':
        print("Filter: Month")
    else:
        print("Filter: None")
    # display total travel time
    
    # to find the total travel time
    # in seconds:
    total_travel_time_sec = df['Trip Duration'].sum(axis=0)
    # in minutes:
    total_travel_time_min = total_travel_time_sec/60
    # in hours:
    total_travel_time_hr = total_travel_time_min/60
    
    # print total travel time
    print('Total Travel Time(in seconds):',total_travel_time_sec)
    print('Total Travel Time(in minutes):',total_travel_time_min)
    print('Total Travel Time(in hours):',total_travel_time_hr)
    
    # display mean travel time
    
    # to find mean travel time
    # in seconds:
    mean_travel_time = df['Trip Duration'].mean()
    
    # print mean travel time
    print('Mean Travel Time(in seconds):',mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city, month, day):
    """Displays statistics on bikeshare users."""

    print('\nCalculating The Next Statistic....User Stats:\n')
    start_time = time.time()
    if month != 'all' and day != 'all':
        print("Filter: Both")
    elif month=='all' and day != 'all':
        print("Filter: Day")
    elif day=='all' and month!='all':
        print("Filter: Month")
    else:
        print("Filter: None")
    # Display counts of user types
    
    user_types = df['User Type'].value_counts()
    # print value counts for each user type
    print('User Types Count:')
    print(user_types)
    if city.lower() != "washington":
        # Display counts of gender

        gender_types = df['Gender'].value_counts()
        # print value counts for each gender type
        print('Gender Types Count:')
        print(gender_types)

        # TO DO: Display earliest, most recent, and most common year of birth
        # earliest year of birth
        earliest_birth_year = df['Birth Year'].min()
        # most recent year of birth
        most_recent_birth_year = df['Birth Year'].max()
        # most common year of birth
        most_common_birth_year = df['Birth Year'].mode()[0]

        # print earliest, most recent, and most common year of birth
        print('Earliest Year Of Birth:',int(earliest_birth_year))
        print('Most Recent Year Of Birth:',int(most_recent_birth_year))
        print('Most Common Year Of Birth:',int(most_common_birth_year))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """ Displays raw data of bikeshare. """
    i = 0
    raw = input("Would you like to view individual trip data?Type 'yes' or 'no'\n").lower()
    pd.set_option('display.max_columns',200)

    while True:            
        if raw == 'no':
            break
        elif raw == 'yes':
            print(df[i:i+5]) # TO DO: appropriately subset/slice your dataframe to display next five rows
            raw = input("Would you like to view individual trip data?Type 'yes' or 'no'\n").lower()
            i += 5
        else:
            raw = input("\nYour input is invalid. Please enter only 'yes' or 'no'\n").lower()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, month, day)
        station_stats(df, month, day)
        trip_duration_stats(df, month, day)
        user_stats(df, city, month, day)
        display_raw_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
