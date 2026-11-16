"""
physics.py
COS 101 Assignment - Question 2: Interactive Physics Calculator with While Loop
"""

def calculate_force():
    mass = float(input("Enter mass (kg): "))
    acceleration = float(input("Enter acceleration (m/s²): "))
    force = mass * acceleration
    print(f"-> Result: Force = {force} N\n")

def calculate_kinetic_energy():
    mass = float(input("Enter mass (kg): "))
    velocity = float(input("Enter velocity (m/s): "))
    ke = 0.5 * mass * (velocity ** 2)
    print(f"-> Result: Kinetic Energy = {ke} J\n")

def calculate_potential_energy():
    mass = float(input("Enter mass (kg): "))
    height = float(input("Enter height (m): "))
    gravity = 9.8  # standard gravity
    pe = mass * gravity * height
    print(f"-> Result: Potential Energy = {pe} J\n")

def calculate_velocity():
    u = float(input("Enter initial velocity (m/s): "))
    a = float(input("Enter acceleration (m/s²): "))
    t = float(input("Enter time (s): "))
    v = u + (a * t)
    print(f"-> Result: Final Velocity = {v} m/s\n")

def calculate_ohm_voltage():
    current = float(input("Enter current (Amps): "))
    resistance = float(input("Enter resistance (Ohms): "))
    voltage = current * resistance
    print(f"-> Result: Voltage = {voltage} V\n")

def main():
    print("=== Interactive Physics Calculator ===")
    
    while True:
        print("\nSelect a formula to calculate:")
        print("1. Force (F = m * a)")
        print("2. Kinetic Energy (KE = 0.5 * m * v^2)")
        print("3. Potential Energy (PE = m * g * h)")
        print("4. Final Velocity (v = u + a * t)")
        print("5. Ohm's Law Voltage (V = I * R)")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            calculate_force()
        elif choice == '2':
            calculate_kinetic_energy()
        elif choice == '3':
            calculate_potential_energy()
        elif choice == '4':
            calculate_velocity()
        elif choice == '5':
            calculate_ohm_voltage()
        elif choice == '6':
            print("Exiting calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose between 1 and 6.")
            continue
            
        cont = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if cont not in ['yes', 'y']:
            print("Exiting calculator. Goodbye!")
            break

if __name__ == "__main__":
    main()
  
