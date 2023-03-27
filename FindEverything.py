from FindGearRatio import FindGearRatio, calculate_worst_case_radius
from CheckRatio import  AddSpacing, FindRadii, MeetsRequiredRatio, CanPack, Draw


if __name__ == "__main__":

    """INPUT VARIABLES"""
    # Motor:2.25 -> 1:2.25 -> 1:2.25, 1:2.25 -> 1:2.3 -> Shaft
    gears = [2.25, 2.25, 2.25, 2.3]
    draw = True

    # Small Gear Radius
    min_radius = 9
    
    # Motor Gear Radius
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

    """END INPUT VARIABLES"""

    print("Gears: ", gears)
    print("Efficiency: ", efficiency)
    print("No of Stages: ", len(gears))
    print("")

    shaft_radius_corrected = (shaft_diameter_mm + shaft_tolerance_mm) / 2
    worst_case_radius = calculate_worst_case_radius(string_holder_length,shaft_radius_corrected, string_length_mm, string_thickness_mm)

    gear_ratio, gear_ratio_with_efficiency = FindGearRatio(friction_coefficient, incline_deg, weight_kg, motor_torque_gcm, worst_case_radius, len(gears), efficiency)
    print("Optimal Gear Ratio: ", gear_ratio)
    print("Optimal Gear Ratio with Efficiency: ", gear_ratio_with_efficiency)
    
    radii = FindRadii(gears, first_radius_mm, min_radius)
    radii = AddSpacing(radii, radius_spacing)
    
    print("Meets Required Ratio: " + str(MeetsRequiredRatio(gears, gear_ratio_with_efficiency)))

    canPack, minSize, circles = CanPack(radii, size)

    print("Can Pack: " + str(canPack))
    print("Packed Size: " + str((minSize[0] - minSize[1], minSize[2] - minSize[3])))

    if draw:
        Draw(radii, size, minSize[2], minSize[1])