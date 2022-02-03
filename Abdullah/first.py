from math import sqrt
import csv

def get_truck_one_velocity(m1, m2, v2, cv):
    """
    Parameters:
    
        m1: mass of truck 1
        m2: mass of truck 2
        v2: velocity of truck 2
        cv: collision velocity
    """
    collision_momentum = (m1 + m2) * cv 
    v1 = (sqrt((
        (collision_momentum ** 2) - (m2 * v2) ** 2
    ))/ m1) # v1 in m/s square

    return round(v1, 4)

def get_raw_velocity(file):
    reader = csv.reader(file)
    next(reader) #skiping the first row of the csv
    raw_velocity = open("RawVelocity.txt", "w")
    velocity_ticket = open("Velocity1SpeedingTicket.txt", "w")
    ticket_lst = []
    for line in reader:
        id, t1m, t2m, v2, cv = line
        final_velocity = get_truck_one_velocity(
            float(t1m), float(t2m), float(v2), float(cv)
        )
        raw_velocity.write(str(final_velocity)+"m/s\n")
        velocity_in_km = final_velocity * 3.6
        if velocity_in_km > 50:
            charge = round((velocity_in_km - 50) * 12.5, 2)
            ticket_lst.append(
                [id, velocity_in_km, charge]
            )
            
        raw_velocity.flush()
    raw_velocity.close()

    ticket_lst.sort(key = lambda x: x[-1])

    for ticket in ticket_lst:
        id, velocity_in_km, charge = ticket
        velocity_ticket.write(
            "In Collision ID#"+id+": The Vehicle was going "+str(velocity_in_km)+"km/hr and will be charged: $"+str(charge)+".\n"
        )
        velocity_ticket.flush()
    velocity_ticket.close()


filename = input("Enter the filename of the collision csv: ")

file = open(filename+".csv", 'r')

get_raw_velocity(file) # making the RawVelocity.txt from the data given in the collision csv file

file.close()