# UTM Coordinate Map Projection Skill

Conformal map projection algorithm mapping the WGS-84 curved ellipsoid surface to a 2D Cartesian grid plane.

```mermaid
flowchart LR
    LatLon["Geodetic (Latitude, Longitude)"] --> Zone["Determine 6° Longitudinal Zone (1..60)"]
    Zone --> Meridian["Compute Meridian Distance M on WGS-84 Ellipsoid"]
    Meridian --> EastNorth["Compute False Easting (500km) & Northing"]
    EastNorth --> Grid["2D UTM Coordinates (Zone, Easting, Northing)"]
```

## Features
- **100% Python Standard Library**: High-order Taylor series truncation.
- **Standard Cartographic Output**: Compatible with global GIS mapping services.
