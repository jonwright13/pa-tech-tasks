import time


class PIDController:
    def __init__(self, P, I, D, target_value):
        """
        Initialise the controller with assigned values
        """
        self.Kp = P  # Proportional gain
        self.Ki = I  # Integral gain
        self.Kd = D  # Derivative gain

        # Initialise last time and last error values
        self.last_time = time.time()
        self.last_error = 0.0

        # Reset response terms
        self.PTerm = 0.0
        self.ITerm = 0.0
        self.DTerm = 0.0

        # Set min/max range for integral windup
        self.windup_guard = 20.0

        # Sets target value
        self.setPoint = target_value

    def update(self, measurement):
        """
        Calculate PID value for a given measurement
        """

        # Calculate change in time
        self.current_time = time.time()
        delta_time = self.current_time - self.last_time

        # Calculate change in error
        error = self.setPoint - measurement
        delta_error = error - self.last_error

        # Calculate response terms
        self.PTerm = self.Kp * error  # Proportional response
        self.ITerm += error * delta_time  # Integral response
        self.DTerm = (
            (delta_error / delta_time) if delta_time > 0 else 0.0
        )  # Derivative response

        # Clamp ITerm between the windup range
        self.ITerm = max(min(self.ITerm, self.windup_guard), -self.windup_guard)

        # Store error and time for next iteration
        self.last_error = error
        self.last_time = self.current_time

        # Combine P, I, D terms and return the control output
        return self.PTerm + (self.Ki * self.ITerm) + (self.Kd * self.DTerm)
