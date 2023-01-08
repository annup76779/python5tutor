import random
import numpy as np

# # the state of seed
random.seed(123)

simulation_count = 10000
no_of_seats = 189

fare = {
    "s": 249,
    "p": 349
}

s_mean = 150
p_mean = 100
s_deviation = 30
p_deviation = 40


# Question 1
def first_simulation():
    demand_of_standard_seats = int(np.random.normal(s_mean, s_deviation))
    demand_of_premium_seats = int(np.random.normal(p_mean, p_deviation))
    return demand_of_premium_seats * fare['p'] + demand_of_standard_seats * fare['s']


sum_of_revenue = 0
for _ in range(simulation_count):
    sum_of_revenue += first_simulation()

expected_revenue = sum_of_revenue / simulation_count
print("Expected Revenue without any limit of bookings: ", expected_revenue)


def second_simulation(booking_limit):
    demand_of_standard_seats = int(np.random.normal(s_mean, s_deviation))
    demand_of_premium_seats = int(np.random.normal(p_mean, p_deviation))
    # get the total number of requirement of the seats
    total_demand_of_seats = demand_of_standard_seats + demand_of_premium_seats

    # if the total number of requests for standard is greater than limit
    # we need to deduct the booking of standard demands
    if demand_of_standard_seats > booking_limit:
        revenue_generated = booking_limit * fare["s"] + demand_of_premium_seats * fare['p']
    else:
        revenue_generated = demand_of_standard_seats * fare["s"] + demand_of_premium_seats * fare['p']

    return revenue_generated


sum_of_revenue = 0
for _ in range(simulation_count):
    sum_of_revenue += second_simulation(110)

expected_revenue = sum_of_revenue / simulation_count
print("Expected Revenue with a limit of bookings as 110: ", expected_revenue)
