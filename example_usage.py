"""Example projecting coordinate to UTM."""
from client import UTMProjection

def main():
    res = UTMProjection.latlon_to_utm(40.7128, -74.0060)
    print("New York City UTM Projection:")
    print(f"  Zone: {res['zone']}{res['hemisphere']}")
    print(f"  Easting: {res['easting']} m")
    print(f"  Northing: {res['northing']} m")

if __name__ == "__main__":
    main()
