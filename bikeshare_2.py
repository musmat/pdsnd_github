import time
import datetime
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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Would you like to see data from Chicago, New York or Washington? : ').lower()
        if  city.lower() not in CITY_DATA:
            print('Incorrect input, please enter the city as they are shown')
            continue
        else:
            break

    # get user input for month (all, january, february, ... , june)
    tf = ['month', 'day', 'both', 'none']

    while True:
        time_filter = input('Do you want to filter by month, day, both or not at all(Enter none)? : ').lower()
        if time_filter.lower() not in tf:
            print('Incorrect input, please type as stated')
            continue
        else:
            break

    if time_filter.lower() == 'month':
        day = "all"
        months = [
                  'january', 'february', 'march', 'april', 'may', 'june'
                 ]

        while True:
            month = input('which month? january, february, march, april, may, june : ').lower()
            if month.lower() not in months:
                print('Incorrect input, please type the months as shown')
                continue
            else:
                break

    elif time_filter.lower() == 'day':
        month = "all"
        days = [
                'monday', 'tuesday', 'wednesday', 'thursday', 'friday',
                'saturday', 'sunday'
              ]

        while True:
            day = input('Which day? monday, tuesday, wednesday, thursday, friday, saturday, sunday : ').lower()
            if day.lower() not in days:
                print('Incorrect input, please type as listed')
                continue
            else:
                break

    elif time_filter.lower() == 'both':
        months = [
                  'january', 'february', 'march', 'april', 'may', 'june'
                 ]

        while True:
            month = input('which month? january, february, march, april, may, june : ')
            if month.lower() not in months:
                print('Incorrect input, please type the months as shown')
                continue
            else:
                break

        # get user input for day of week (all, monday, tuesday, ... sunday)
        days = [
                'monday', 'tuesday', 'wednesday', 'thursday', 'friday',
                'saturday', 'sunday'
              ]

        while True:
            day = input('Which day? monday, tuesday, wednesday, thursday, friday, saturday, sunday : ')
            if day.lower() not in days:
                print('Incorrect input, please type as listed')
                continue
            else:
                break

    elif time_filter.lower() == 'none':
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


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # display the most common month

    # extract hour from the Start Time column to create a month column
    df['month'] = df['Start Time'].dt.month

    # find the most popular month
    popular_month = df['month'].mode()[0]

    print('Most Popular Month:', popular_month)

    # display the most common day of week

    # extract hour from the Start Time column to create a day column
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # find the most popular day of a week
    popular_day = df['day_of_week'].mode()[0]

    print('Most Popular Day:', popular_day)

    # display the most common start hour

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # find the most popular hour
    popular_hour = df['hour'].mode()[0]

    print('Most Popular Start Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]

    print('Most Common Start Station:', common_start_station)

    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]

    print('Most Common End Station:', common_end_station)

    # display most frequent combination of start station and end station trip
    frequent_combination = df.groupby(['Start Station','End Station']).size().nlargest(1)

    print('Most Common Combination Stations:', frequent_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_travel_seconds = sum(df['Trip Duration'])

    # display total travel time
    print('Total Travel Time:', str(total_travel_seconds))

    # display mean travel time
    average_travel_time = np.mean(df['Trip Duration'])
    print('Mean Travel Time:', str(average_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types

    # print value counts for each user type
    user_types = df['User Type'].value_counts()

    print(user_types)

    # Checking the city
    try:

        # print value counts for each gender
        print(df['Gender'].value_counts())

    except KeyError:
        print('Gender data not available on this city data')

    # Display earliest, most recent, and most common year of birth

    # Checking the city
    try:
        # print value counts for earliest year of birth
        print('Earliest Year of Birth', df['Birth Year'].nsmallest().value_counts())

        # print value counts for most recent year of birth
        print('Earliest Year of Birth', df['Birth Year'].nlargest().value_counts())

        # print value counts for most common year of birth
        print('Earliest Year of Birth', df['Birth Year'].value_counts().idxmax())

    except KeyError:
        print('Birth Year data not available on this city data')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):
    start = 0
    stop = 5
    td = ['yes', 'no']

    while True:
        trip_data = input('Do you want to view trip data? answer \'yes\' or \'no\' : ').lower()
        if trip_data not in td:
            print('please type \'yes\' if you want or \'no\' if you don\'t : ')
            continue
        else:
            if trip_data == 'yes':
                print(df.iloc[start : stop])
                start = stop
                stop += 5
                continue
            else:
                break

            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
