from src.question_2.PID import PIDController
import time, random


def main(initial_aperture, initial_pressure, max_iterations=100):

    # Initialise PID controller
    pid = PIDController(P=1.2, I=1.0, D=0.001, target_value=initial_pressure)

    aperture = initial_aperture  # Initial aperture size
    pressure = initial_pressure  # Initial pressure

    # Run simulation
    for i in range(1, max_iterations):

        # Update the aperture size based on the pressure reading
        aperture = pid.update(pressure)

        # Clamp the aperture size between 0% and 100%
        if aperture > 1:
            aperture = 1
        elif aperture < 0:
            aperture = 0

        # randomise pressure in the range [-0.5*(P1), 0.5*(1-P1)]
        fluctuation = random.uniform(-0.5 * aperture, 0.5 * (1.0 - aperture))
        pressure += fluctuation

        # Random delay between 0 and 2 seconds
        delay = random.uniform(0, 2)
        time.sleep(delay)


if __name__ == "__main__":
    initial_aperture = 0.5
    initial_pressure = 2.0

    main(initial_aperture, initial_pressure)
