import time
import pandas as pd


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ['january', 'february', 'march', 'april', 'may', 'june']

days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    city = ''
    while city not in CITY_DATA.keys():

        print("which city do you want to see the data: \n")
        city = input('[chicago, new york city , washington]: ').lower()
        print()


    month = ''
    while month not in months and month != 'all':
        print('which month do you want to see the data: \n')
        month = input('[all, january, february, march, april, may, june]: ').lower()
        print()



    day = ''
    while day not in days and day != 'all':
        if month != 'all':

            print('which day of each month do you want to see the data :\n')
            day = input('[all,monday, tuesday, wednesday, thursday, friday, saturday, sunday]:').lower()
            print()
        else:

            day = input(f'\n for which day of the {month.title()} do you want to see the {city.title()} data?\n'
                        f"[all, monday, tuesday, wednesday, thursday, friday, saturday, sunday]:").lower()

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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    if month != "all":
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != "all":
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    print('Month:\t\t', df['month'].mode()[0])

    print('Day:\t\t', df['day_of_week'].mode()[0])

    print('Hour:\t\t', df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    print('start station:\t\t', df['Start Station'].mode()[0])

    print('end station:\t\t', df['End Station'].mode()[0])

    print('start & end:\t', (df['Start Station'] + df['End Station']).mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    print('Total travel time:\t\t', df['Trip Duration'].sum())

    print('Mean travel time:t\t', df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    print('total of user types:\n', df['User Type'].value_counts())

    if city == 'washington':
          print("no gender data available for washington!")
    else:
          print(f"\nTotal count per gender:\n{df['Gender'].value_counts()}")


    if city == 'washington':
          print("no data available for washington")
    else:
        print("Earliest Y.O.B.:\t\t", int(df['Birth Year'].min()))
        print("Most recent Y.O.B.:\t\t", int(df['Birth Year'].max()))
        print("Most common Y.O.B.:\t\t", int(df['Birth Year'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(city):
    filename = CITY_DATA[city]

    with open (filename)as fo:

        while True:

            raw = input('Do you want to see raw data? [yes/no]: \n').lower()

            if raw != 'yes':
                print('\n you have chosen not to see the raw data!')
                break

            else:
                for _ in range(5):

                    contents = fo.readline()

                    print(contents)
                    continue


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        raw_data(city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
