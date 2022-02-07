"""

Joey Del Guercio
Lab 3: nested loops and accumulators

"""

def traffic_analysis():
    total_cars = 0
    total_roads = 0
    n_roads = eval(input('How many roads were surveyed? '))
    for roads in range(1, n_roads+1):
        day_cars = 0
        print('How many days was road', roads, 'surveyed', end='?')
        n_days = eval(input())
        for days in range(1, n_days+1):
            print('How many cars traveled on day', days, end='?')
            cars = eval(input())
            day_cars += cars
        print('Road', roads, 'average vehicles per day:', day_cars / n_days)
        total_cars += day_cars
    total_roads += n_roads
    print('Total number of vehicles traveled on all roads:', total_cars)
    print('Average number of vehicles per road:', total_cars/total_roads)

traffic_analysis()