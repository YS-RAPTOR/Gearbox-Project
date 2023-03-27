import math

def FindGearRatio(friction_coefficient, incline_deg, weight_kg, motor_torque_gcm, shaft_radius, no_of_gears, efficiency = 1 ):
    # Calculate the minimum force required to move the box up the incline
    incline_rad = math.radians(incline_deg)
    weight = weight_kg * 9.81
    normal_force = weight * math.cos(incline_rad)
    friction_force = normal_force * friction_coefficient

    total_efficiency = efficiency ** no_of_gears

    min_force = weight * math.sin(incline_rad) + friction_force
    min_force_efficiency = min_force / total_efficiency

    motor_torque_Nm = (motor_torque_gcm / (1000 * 100)) *9.81
    
    # Torque = Force * Radius
    Torque_to_move_box = min_force * (shaft_radius/1000)
    Torque_to_move_box_efficiency = min_force_efficiency * (shaft_radius/1000)

    print("Torque to move box: ", Torque_to_move_box)

    if(efficiency != 1):
        print(f"Torque to move box with {100 * efficiency}% efficiency between stages:", Torque_to_move_box_efficiency)

    return (Torque_to_move_box / motor_torque_Nm, Torque_to_move_box_efficiency / motor_torque_Nm)

def calculate_worst_case_radius(wrap_around_length, wrap_around_initial_radius, string_length_mm, string_thickness_mm):
    no_of_lengthwise_wraps = math.floor(wrap_around_length / string_thickness_mm)
    
    length = string_length_mm
    radius = wrap_around_initial_radius

    while length > 0:
        for _ in range(no_of_lengthwise_wraps):
            circumference = 2 * math.pi * radius
            length -= circumference

            if length < 0:
                break

        radius += string_thickness_mm

    return radius

if __name__ == "__main__":
    """INPUT VARIABLES"""
    # Test bench Info
    friction_coefficient = 0.45
    incline_deg = 45
    weight_kg = 5

    # Motor Info
    motor_torque_gcm = 80

    # Shaft Info
    shaft_diameter_mm = 6
    shaft_tolerance_mm = 0.2

    # String Info
    string_length_mm = 1000
    string_thickness_mm = 0.165
    string_holder_length = 20

    """END INPUT VARIABLES"""

    shaft_radius_corrected = (shaft_diameter_mm + shaft_tolerance_mm) / 2
    worst_case_radius = calculate_worst_case_radius(string_holder_length,shaft_radius_corrected, string_length_mm, string_thickness_mm)

    print("Gear Ratio: ", FindGearRatio(friction_coefficient, incline_deg, weight_kg, motor_torque_gcm, worst_case_radius, 1 )[0])










