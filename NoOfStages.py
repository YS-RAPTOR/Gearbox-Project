from FindGearRatio import FindGearRatio, calculate_worst_case_radius
from CheckRatio import  AddSpacing, FindRadii, MeetsRequiredRatio, CanPack, Draw


if __name__ == "__main__":

    """INPUT VARIABLES"""
    initial_stage = 1.5
    added_ratio = 1.75
    

    # Small Gear Radius
    min_radius = 9
    
    # Motor Gear Raius
    first_radius_mm = 18.5/2

    # adding added to gears
    radius_spacing = 0.2

    # Efficiency between gear stages
    efficiency = 0.95

    # Size of the sheet
    size = (210, 297)

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
    i = 0

    gears = [initial_stage]
    canPack = True
    meets_ratio = False 

    while not meets_ratio or i > 100:

        """END INPUT VARIABLES"""
        shaft_radius_corrected = (shaft_diameter_mm + shaft_tolerance_mm) / 2
        worst_case_radius = calculate_worst_case_radius(string_holder_length,shaft_radius_corrected, string_length_mm, string_thickness_mm)

        gear_ratio, gear_ratio_with_efficiency = FindGearRatio(friction_coefficient, incline_deg, weight_kg, motor_torque_gcm, worst_case_radius, len(gears), efficiency)
        
        radii = FindRadii(gears, first_radius_mm, min_radius)
        radii = AddSpacing(radii, radius_spacing)

        meets_ratio = MeetsRequiredRatio(gears, gear_ratio_with_efficiency)
        print("Required Ratio: ", gear_ratio_with_efficiency)

        # canPack, minSize, circles = CanPack(radii, size)
        gears.append(added_ratio)
        i += 1

    print("")

    print("Optimal Gear Ratio: ", gears[:-1])
    print("Gear Ratio: ", gear_ratio)
    print("Gear Ratio with Efficiency: ", gear_ratio_with_efficiency)
    print("No of Stages: ", len(gears[:-1]))
    print("Length of Gears: ", len(gears[:-1]) * 3)
