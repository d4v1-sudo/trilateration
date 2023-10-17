import math
import numpy

# Polar and equatorial radii of the Earth in meters
polar_radius = 6356752
equatorial_radius = 6378137

LatA = math.radians(float(input("Latitude of point A: ")))
LonA = math.radians(float(input("Longitude of point A: ")))
AltA = float(input("Altitude of point A (in meters): "))
DistA = float(input("Your distance to point A (in meters): ")

LatB = math.radians(float(input("Latitude of point B: ")))
LonB = math.radians(float(input("Longitude of point B: ")))
AltB = float(input("Altitude of point B (in meters): "))
DistB = float(input("Your distance to point B (in meters): ")

LatC = math.radians(float(input("Latitude of point C: ")))
LonC = math.radians(float(input("Longitude of point C: ")))
AltC = float(input("Altitude of point C (in meters): "))
DistC = float(input("Your distance to point C (in meters): ")

# Convert geodetic coordinates (latitude, longitude, and altitude) to ECEF coordinates
def geodetic_to_ecef(lat, lon, alt):
    N = equatorial_radius / math.sqrt(1 - (polar_radius / equatorial_radius) ** 2 * math.sin(lat) ** 2)
    x = (N + alt) * math.cos(lat) * math.cos(lon)
    y = (N + alt) * math.cos(lat) * math.sin(lon)
    z = (N * (1 - (polar_radius / equatorial_radius) ** 2) + alt) * math.sin(lat)
    return x, y, z

xA, yA, zA = geodetic_to_ecef(LatA, LonA, AltA)
xB, yB, zB = geodetic_to_ecef(LatB, LonB, AltB)
xC, yC, zC = geodetic_to_ecef(LatC, LonC, AltC)

AB = numpy.array([xB - xA, yB - yA, zB - zA])
AC = numpy.array([xC - xA, yC - yA, zC - zA])

# Calculate the cross product of vectors AB and AC to obtain the normal of the plane formed by the points.
N = numpy.cross(AB, AC)
N /= numpy.linalg.norm(N)  # Normalize the normal.

# Use the dot product to find the distances in the direction of each point.
dA = numpy.dot(N, numpy.array([xA, yA, zA]))
dB = numpy.dot(N, numpy.array([xB, yB, zB]))
dC = numpy.dot(N, numpy.array([xC, yC, zC]))

# Use the distances to calculate the coordinates of the trilateration point.
x_trilateration = (dA * xA + dB * xB + dC * xC) / (dA + dB + dC)
y_trilateration = (dA * yA + dB * yB + dC * yC) / (dA + dB + dC)
z_trilateration = (dA * zA + dB * zB + dC * zC) / (dA + dB + dC)

# Now you have the ECEF coordinates of the trilateration point on the oblate spheroid.
# You can convert these ECEF coordinates into geodetic coordinates (latitude, longitude, and altitude)
# to obtain the location in terms of Earth's latitude and longitude.

# Function to convert ECEF coordinates to geodetic coordinates
def ecef_to_geodetic(x, y, z):
    p = math.sqrt(x ** 2 + y ** 2)
    theta = math.atan2(z * equatorial_radius, p * polar_radius)
    latitude = math.atan2((z + polar_radius * polar_radius * polar_radius * math.sin(theta) * math.sin(theta) * math.sin(theta)),
                         (p - equatorial_radius * equatorial_radius * equatorial_radius * math.cos(theta) * math.cos(theta) * math.cos(theta)))
    longitude = math.atan2(y, x)
    N = equatorial_radius / math.sqrt(1 - polar_radius * polar_radius * math.sin(latitude) * math.sin(latitude))
    altitude = p / math.cos(latitude) - N
    return math.degrees(latitude), math.degrees(longitude), altitude

# Convert the ECEF coordinates of the trilateration point to geodetic coordinates
lat_trilateration, lon_trilateration, alt_trilateration = ecef_to_geodetic(x_trilateration, y_trilateration, z_trilateration)

print(f"Latitude of trilateration: {lat_trilateration} degrees")
print(f"Longitude of trilateration: {lon_trilateration} degrees")
print(f"Altitude of trilateration: {alt_trilateration} meters")
