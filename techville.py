def move_forward():
    print("moving forward")

def turn(direction):
    print(f"turning {direction}")

def start_engine():
    print("starting engine")

def stop_engine():
    print("stopping engine")

def follow_roundabout(exit_number):
    print(f"taking exit number {exit_number} from the roundabout")

start_engine()

destination = input("Where do you want to go? ")

# Seznam destinací, které vyžadují pohyb vpřed
move_forward_destinations = ["library", "tech park", "hospital", "mall", "airport", "university", "stadium"]

if destination in move_forward_destinations:
    move_forward()

    if destination == "library":
        turn("left")
        print("we arrived at the library")

    elif destination == "tech park":
        turn("right")
        print("we arrived at tech park")

    elif destination == "hospital":
        follow_roundabout(1)
        print("we arrived at the hospital")

    elif destination == "mall":
        follow_roundabout(2)
        print("we arrived at the mall")

    elif destination == "airport":
        follow_roundabout(3)
        print("we arrived at the airport")

    elif destination == "university":
        follow_roundabout(4)
        turn("left")
        print("we arrived at the university")

    elif destination == "stadium":
        follow_roundabout(4)
        turn("right")
        print("we arrived at the stadium")

else:
    print("error message")

stop_engine()