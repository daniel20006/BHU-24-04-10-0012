
# Formula a: Force (F = ma)
def calculate_force(mass, acceleration):
    force = mass * acceleration
    return force


# Formula b: Kinetic Energy (KE = 0.5mv^2)
def calculate_kinetic_energy(mass, velocity):
    kinetic_energy = 0.5 * mass * (velocity ** 2)
    return kinetic_energy


# Formula c: Potential Energy (PE = mgh)
def calculate_potential_energy(mass, gravity, height):
    potential_energy = mass * gravity * height
    return potential_energy


# Formula d: Momentum (p = mv)
def calculate_momentum(mass, velocity):
    momentum = mass * velocity
    return momentum


# Formula e: Distance (d = vt)
def calculate_distance(velocity, time):
    distance = velocity * time
    return distance


# Formula f: Velocity (v = d/t)
def calculate_velocity(distance, time):
    velocity = distance / time
    return velocity


# Formula g: Acceleration (a = Δv/Δt)
def calculate_acceleration(initial_velocity, final_velocity, time):
    acceleration = (final_velocity - initial_velocity) / time
    return acceleration


def main():
    print(" GOLDEN Physics Formulas Calculator")
    print("-------------------------------")

    while True:
        print("Choose a formula:")
        print("a. Force (F = ma)")
        print("b. Kinetic Energy (KE = 0.5mv^2)")
        print("c. Potential Energy (PE = mgh)")
        print("d. Momentum (p = mv)")
        print("e. Distance (d = vt)")
        print("f. Velocity (v = d/t)")
        print("g. Acceleration (a = Δv/Δt)")
        print("h. Quit")

        choice = input("Enter the number of your chosen formula: ")

        if choice == "a":
            mass = float(input("Enter mass (kg): "))
            acceleration = float(input("Enter acceleration (m/s^2): "))
            force = calculate_force(mass, acceleration)
            print(f"Force: {force} N")

        elif choice == "b":
            mass = float(input("Enter mass (kg): "))
            velocity = float(input("Enter velocity (m/s): "))
            kinetic_energy = calculate_kinetic_energy(mass, velocity)
            print(f"Kinetic Energy: {kinetic_energy} J")

        elif choice == "c":
            mass = float(input("Enter mass (kg): "))
            gravity = float(input("Enter gravity (m/s^2): "))
            height = float(input("Enter height (m): "))
            potential_energy = calculate_potential_energy(mass, gravity, height)
            print(f"Potential Energy: {potential_energy} J")

        elif choice == "d":
            mass = float(input("Enter mass (kg): "))
            velocity = float(input("Enter velocity (m/s): "))
            momentum = calculate_momentum(mass, velocity)
            print(f"Momentum: {momentum} kg*m/s")

        elif choice == "e":
            velocity = float(input("Enter velocity (m/s): "))
            time = float(input("Enter time (s): "))
            distance = calculate_distance(velocity, time)
            print(f"Distance: {distance} m")

        elif choice == "f":
            distance = float(input("Enter distance (m): "))
            time = float(input("Enter time (s): "))
            velocity = calculate_velocity(distance, time)
            print(f"Velocity: {velocity} m/s")

        elif choice == "g":
            initial_velocity = float(input("Enter initial velocity (m/s): "))
            final_velocity = float(input("Enter final velocity (m/s): "))
            time = float(input("Enter time (s): "))
            acceleration = calculate_acceleration(initial_velocity, final_velocity, time)
            print(f"Acceleration: {acceleration} m/s^2")

        elif choice == "h":
            break

        else:
            print("Invalid choice. Please choose a valid formula.")


if __name__ == "__main__":
    main()


