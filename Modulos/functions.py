def generate_report(main_tank, external_tank, hydrogen_tank):
    print(f"""Fuel report:
        Main Tank: {main_tank}
        External Tank: {external_tank}
        Hydrogen Tank: {hydrogen_tank}
        """)
    
# generate_report(25, 40, 3.5)

from datetime import timedelta, datetime

def arrival_time(hours=51):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime("Arrival: %A %H:%M")

# print(arrival_time())

def sequence_time(*args):
    total_minutes = sum(args)
    if total_minutes < 60:
        return f"Total time to launch is {total_minutes} minutes"
    else:
        return f"Total time to launch is {total_minutes/60} hours"
    
# print(sequence_time(10, 14, 18))

def crew_members(**kwargs):
    print(f"{len(kwargs)} astronauts assigned for this mission:")
    for title, name in kwargs.items():
        print(f"{title}: {name}")

# crew_members(captain="Neil Armstrong", pilot="Buzz Aldrin", command_pilot="Michael Collins")

def fuel_report(**fuel_tanks):
    for tank in fuel_tanks:
        print(f"{tank}: {fuel_tanks[tank]}")

fuel_report(main_tank=300, hydrogen_tank=60, emergency_tank=24.4)