import math
import packcircles as pc
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.cm import get_cmap

def FindRadii(gears : list[int], first, smallest) -> list[float]:
    radii = [gears[0] * first]
    for gear in gears[1:]:
        radii.append(gear * smallest)
        radii.append(smallest)

    return radii

def AddSpacing(radii : list[float], spacing) -> list[float]:
    return [radius + spacing for radius in radii]

def MeetsRequiredRatio (gears : list[int], threshold, efficiency) -> bool:
    ratio = gears[0]
    effective_ratio = ratio * efficiency
    for gear in gears[1:]:
        ratio *= gear
        effective_ratio *= gear * efficiency

    print("Ratio Achieved is: " + str(ratio))
    print("Effective Ratio Achieved is: " + str(effective_ratio))

    return ratio >= threshold

def CanPack(radii : list[float], size) -> tuple[bool, tuple[float], list[tuple[float]]]:
    maxX = -math.inf
    maxY = -math.inf
    minX = math.inf
    minY = math.inf

    circles = pc.pack(radii)

    for (x, y, r) in circles:
        minX = min(minX, x - r)
        minY = min(minY, y - r)
        maxX = max(maxX, x + r)
        maxY = max(maxY, y + r)

    return (maxX - minX <= size[0] and maxY - minY <= size[1]), (maxX , minX, maxY , minY), circles

def Draw(circles, size, top, left):
    fig, ax = plt.subplots()
    cmap = get_cmap('coolwarm_r')
    circles = pc.pack(radii)
    for (x,y,radius) in circles:
        patch = patches.Circle(
            (x,y),
            radius,
            color=cmap(radius/max(radii)),
            alpha=0.65
        )
        ax.add_patch(patch)

    ax.set_xlim(-1.5 * size[1], 1.5 * size[1])
    ax.set_ylim(-1.5 * size[1], 1.5 * size[1])

    ax.add_patch(patches.Rectangle((left, top - size[1]), size[0], size[1], fill=False, edgecolor='black', linewidth=2))

    plt.axis('off')

    plt.show()

if __name__ == "__main__":
    """INPUT VARIABLES"""
    # Motor:2.25 -> 1:2.25 -> 1:2.25, 1:2.25 -> 1:2.25 -> Shaft
    gears = [2.25, 2.25, 2.25, 2.25]
    draw = True

    # Small Gear Radius
    min_radius = 9
    
    # Motor Gear Radius
    first_radius_mm = 18.5/2
    
    # adding added to gears
    radius_spacing = 0.2

    # Efficiency between gear stages
    efficiency = 0.95

    # Required Gear Ratio
    threshold_gear_ratio = 48

    # Size of the sheet
    size = (210, 297)
    """END INPUT VARIABLES"""

    radii = FindRadii(gears, first_radius_mm, min_radius)
    radii = AddSpacing(radii, radius_spacing)

    MeetsRequiredRatio(gears, threshold_gear_ratio, efficiency)

    canPack, minSize, circles = CanPack(radii, size)

    print("Can Pack: " + str(canPack))
    print("Packed Size: " + str((minSize[0] - minSize[1], minSize[2] - minSize[3])))

    if draw:
        Draw(circles, size, minSize[2], minSize[1])