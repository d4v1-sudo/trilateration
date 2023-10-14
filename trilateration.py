import math
import numpy

earthR = 6371
LatA = float(input("Latitude of point A: "))
LonA = float(input("Longitude of point A: "))
AltA = float(input("Altitude of point A (in kilometers): "))
DistA = float(input("Your distance to point A (in kilometers): "))
print()
LatB = float(input("Latitude of point B: "))
LonB = float(input("Longitude of point B: "))
AltB = float(input("Altitude of point B (in kilometers): "))
DistB = float(input("Your distance to point B (in kilometers): "))
print()
LatC = float(input("Latitude of point C: "))
LonC = float(input("Longitude of point C: "))
AltC = float(input("Altitude of point C (in kilometers): "))
DistC = float(input("Your distance to point C (in kilometers): "))
print()

# Using an authalic sphere
# If using an ellipsoid, this step is slightly different
# Convert geodetic Latitude/Longitude to ECEF (Earth-Centered, Earth-Fixed) coordinates (xyz)
#   1. Convert Latitude/Longitude to radians
#   2. Convert Latitude/Longitude (in radians) to ECEF
xA = (earthR + AltA) * (math.cos(math.radians(LatA)) * math.cos(math.radians(LonA)))
yA = (earthR + AltA) * (math.cos(math.radians(LatA)) * math.sin(math.radians(LonA)))
zA = (earthR + AltA) * (math.sin(math.radians(LatA)))

xB = (earthR + AltB) * (math.cos(math.radians(LatB)) * math.cos(math.radians(LonB)))
yB = (earthR + AltB) * (math.cos(math.radians(LatB)) * math.sin(math.radians(LonB)))
zB = (earthR + AltB) * (math.sin(math.radians(LatB)))

xC = (earthR + AltC) * (math.cos(math.radians(LatC)) * math.cos(math.radians(LonC)))
yC = (earthR + AltC) * (math.cos(math.radians(LatC)) * math.sin(math.radians(LonC)))
zC = (earthR + AltC) * (math.sin(math.radians(LatC)))

P1 = numpy.array([xA, yA, zA])
P2 = numpy.array([xB, yB, zB])
P3 = numpy.array([xC, yC, zC])

# From Wikipedia
# Transform to get circle 1 at the origin
# Transform to get circle 2 on the x-axis
ex = (P2 - P1) / (numpy.linalg.norm(P2 - P1))
i = numpy.dot(ex, P3 - P1)
ey = (P3 - P1 - i * ex) / (numpy.linalg.norm(P3 - P1 - i * ex))
ez = numpy.cross(ex, ey)
d = numpy.linalg.norm(P2 - P1)
j = numpy.dot(ey, P3 - P1)

# From Wikipedia
# Plug and chug using the above values
x = (pow(DistA, 2) - pow(DistB, 2) + pow(d, 2)) / (2 * d)
y = ((pow(DistA, 2) - pow(DistC, 2) + pow(i, 2) + pow(j, 2)) / (2 * j)) - ((i / j) * x)

# Only one case shown here
z = numpy.sqrt(pow(DistA, 2) - pow(x, 2) - pow(y, 2))  # Height

# triPt is an array with ECEF x, y, z of the trilateration point
triPt = P1 + x * ex + y * ey + z * ez

# Convert back to Latitude/Longitude from ECEF
# Convert to degrees
lat = math.degrees(math.asin(triPt[2] / (earthR + AltA)))
lon = math.degrees(math.atan2(triPt[1], triPt[0]))

print(lat, lon)