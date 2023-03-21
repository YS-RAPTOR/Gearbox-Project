import math

def FindGearRatio(friction_coefficient, incline_deg, weight_kg, motor_torque_gcm, shaft_radius):
    # Calculate the minimum force required to move the box up the incline
    incline_rad = math.radians(incline_deg)
    weight = weight_kg * 9.81
    normal_force = weight * math.cos(incline_rad)
    friction_force = normal_force * friction_coefficient
    min_force = weight * math.sin(incline_rad) + friction_force
    
    motor_torque_Nm = (motor_torque_gcm / (1000 * 100)) *9.81
    
    # Torque = Force * Radius
    Torque_to_move_box = min_force * (shaft_radius/1000)
    print("Torque to move box: ", Torque_to_move_box)

    return Torque_to_move_box / motor_torque_Nm

def calculate_worst_case_radius(wrap_around_length, wrap_around_initial_radius, string_length_mm, string_thickness_mm):
    no_of_lengthwise_wraps = math.floor(wrap_around_length / string_thickness_mm)
    
    length = string_length_mm
    radius = wrap_around_initial_radius

    while length > 0:
        for _ in range(no_of_lengthwise_wraps):
            circumference = 2 * math.pi * radius
            length -= circumference
        radius += string_thickness_mm

    return radius

if __name__ == "__main__":
    friction_coefficient = 0.45
    incline_deg = 45
    weight_kg = 5
    motor_torque_gcm = 80
    shaft_diameter_mm = 6
    shaft_tolerance_mm = 0.2
    shaft_radius_corrected = (shaft_diameter_mm + shaft_tolerance_mm) / 2
    length_between_bolts_mm = 50

    string_length_mm = 1000
    string_thickness_mm = 1
    string_rotation_window_percentage = 0.4

    print("Gear Ratio: ", FindGearRatio(friction_coefficient, incline_deg, weight_kg, motor_torque_gcm, calculate_worst_case_radius(length_between_bolts_mm * string_rotation_window_percentage,shaft_radius_corrected, string_length_mm, string_thickness_mm)))










