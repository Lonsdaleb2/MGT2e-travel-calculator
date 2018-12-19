import math

def start():

    planet = (input(
        "Enter distance (eg: 100km), or a UWP number if approaching/departing a planetary jump point : "))
    speed = (input("What's your ships speed rating?  "))
    traveltime(planet, speed)


def traveltime(planet, speed):

    planet_size = {
        "0": 1000,
        "1": 1600,
        "2": 3200,
        "3": 4800,
        "4": 6400,
        "5": 8000,
        "6": 9600,
        "7": 11200,
        "8": 12800,
        "9": 14400,
        "A": 16000
    }

    if "km" in planet:
        planet = planet.replace("km", "")
        planet_out = int(planet)
        jump = False

    elif planet in planet_size:
        planet_out = planet_size.get(planet)
        planet_out = (planet_out*100)
        jump = True


    travelmaths(planet_out, speed, jump)

def travelmaths(planet_out, speed, jump):
    speed = int(speed)
    #print(planet_out, speed)

    distance_sum = (planet_out*100)
    a = round((distance_sum/speed),9)

    root_subject = math.sqrt(a)
    a = (root_subject * 2)

    seconds = a

    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    if jump == False:
        print("Distance to target (d/h/m/s): \n" + "%d:%d:%02d:%02d" % (d, h, m, s) + "\n"
              + "(Travelling " + str(planet_out) + "km @ "  + str(speed) + "G)")
    if jump == True:
        print("Distance to/from jump point (d/h/m/s): \n" + "%d:%d:%02d:%02d" % (d, h, m, s) + "\n"
              + "(Travelling " + str(planet_out) + "km @ " + str(speed) + "G)")





start()