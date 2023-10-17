# Trilateration on an Oblate Spheroid (Earth) in Python

This Python code demonstrates how to perform trilateration on an oblate spheroid, such as the Earth. Trilateration is a method for determining an unknown location based on the distances from that location to known points.

The code takes three known points, their latitudes, longitudes, altitudes, and distances to an unknown point. It then calculates the latitude, longitude, and altitude of the unknown point using the Earth's oblate spheroid model.

## Dependencies

This code uses the following Python libraries:

- `math`: For mathematical calculations.
- `numpy`: For numerical operations.

Make sure to import these libraries before running the code.

## Usage

### Download the Repository

You can download the repository in one of the following ways:

#### Using Git

1. Clone the repository using Git by running the following command:

    ```bash
    git clone https://github.com/your-username/trilateration.git
    ```

#### Downloading from the Website

1. Visit the GitHub repository page at [https://github.com/d4v1-sudo/trilateration](https://github.com/d4v1-sudo/trilateration.git).
2. Click the "Code" button and select "Download ZIP" to download the repository as a ZIP file.
3. Extract the contents of the ZIP file to your local machine.

### Install the Required Libraries

Before running the code, you need to install the necessary Python libraries. Open a terminal or command prompt and navigate to the project directory.

1. Run the following command to install the required libraries using pip:

    ```bash
    pip install -r requirements.txt
    ```

### Run the Code

1. In the terminal or command prompt, navigate to the project directory where you downloaded the repository.

2. Run the Python script by executing the following command:

    ```bash
    python3 trilateration.py
    ```

3. Follow the prompts to provide the coordinates and altitudes of reference points A, B, and C, as well as the distances from an unknown point to each of these points.

4. The script will calculate and print the geographic coordinates of the unknown point.

## Code Explanation

- The code converts the geodetic coordinates (latitude, longitude, and altitude) of the input points into Earth-Centered, Earth-Fixed (ECEF) coordinates.

- It calculates the normal of the plane formed by the three known points by taking the cross product of vectors AB and AC.

- The distances to each known point from the trilateration point are computed using the dot product with the normal vector.

- Finally, the code calculates the ECEF coordinates of the trilateration point and converts them back into geodetic coordinates to obtain the latitude, longitude, and altitude.

## Improvements

You can enhance this code by adding more comments to explain the calculations in detail and by validating the input values to ensure they are within valid ranges.

To reuse the geodetic-to-ECEF or ECEF-to-geodetic conversion functions in other projects, it's a good practice to place them in a separate module and import them.

## Note

Ensure that you have installed the `numpy` library if it's not already installed on your system.

This code is a valuable tool for determining the location of an unknown point on the Earth's surface based on distance measurements from known reference points.

## License

This project is licensed under the [MIT License](LICENSE).
