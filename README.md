# Trilateration

This is a geospatial trilateration algorithm that calculates the geographic coordinates (latitude and longitude) of an unknown point based on known distances to three reference points (A, B, and C) and their geographic coordinates.

## Requirements

- Python 3
- Libraries: `math` and `numpy`

## Usage

1. Download or clone this repository.

To clone use:

  ```bash
  git clone https://github.com/d4v1-sudo/trilateration.git
```
<br>
  If you download the repository, unzip de .zip file.
<br>
2. Run the Python script:
  
  ```bash
  python3 trilateration.py
  ```
<br>
3. Provide the coordinates and altitudes of reference points A, B, and C, as well as the distances from an unknown point to each of these points when prompted.
<br>
4. The script will calculate and print the geographic coordinates of the unknown point.

## Example

```bash
Latitude of point A: 40.7128
Longitude of point A: -74.0060
Altitude of point A (in kilometers): 0
Your distance to point A (in kilometers): 10

Latitude of point B: 34.0522
Longitude of point B: -118.2437
Altitude of point B (in kilometers): 0
Your distance to point B (in kilometers): 15

Latitude of point C: 51.5074
Longitude of point C: -0.1278
Altitude of point C (in kilometers): 0
Your distance to point C (in kilometers): 20

38.9079, -77.0373
```
This is an example of input and output for the algorithm.

## Notes

- **Make sure to provide coordinates in decimal degrees and distances in kilometers.**:
- **This algorithm assumes the Earth is an authalic sphere (not an ellipsoid). If you are working with an ellipsoid, the formulas may be different**:

## License

This project is licensed under the [MIT License](LICENSE).
