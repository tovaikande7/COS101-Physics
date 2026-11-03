"""
physics.py
COS 101 Assignment: 5 Physics Formulas implemented in Python.
"""

def calculate_force(mass, acceleration):
    """Calculates Force (F = m * a) in Newtons."""
    return mass * acceleration

def calculate_kinetic_energy(mass, velocity):
    """Calculates Kinetic Energy (KE = 0.5 * m * v^2) in Joules."""
    return 0.5 * mass * (velocity ** 2)

def calculate_potential_energy(mass, height, gravity=9.8):
    """Calculates Gravitational Potential Energy (PE = m * g * h) in Joules."""
    return mass * gravity * height

def calculate_velocity(initial_velocity, acceleration, time):
    """Calculates Final Velocity (v = u + a * t) in m/s."""
    return initial_velocity + (acceleration * time)

def calculate_ohm_voltage(current, resistance):
    """Calculates Voltage using Ohm's Law (V = I * R) in Volts."""
    return current * resistance

if __name__ == "__main__":
    print("--- Physics Formulas Calculator ---")
    print(f"Force (m = 10 kg, a = 2 m/s²): {calculate_force(10, 2)} N")
    print(f"Kinetic Energy (m = 5 kg, v = 4 m/s): {calculate_kinetic_energy(5, 4)} J")
    print(f"Potential Energy (m = 2 kg, h = 10 m): {calculate_potential_energy(2, 10)} J")
    print(f"Final Velocity (u = 0, a = 3, t = 5): {calculate_velocity(0, 3, 5)} m/s")
    print(f"Voltage (I = 2 A, R = 5 ohms): {calculate_ohm_voltage(2, 5)} V")
  
