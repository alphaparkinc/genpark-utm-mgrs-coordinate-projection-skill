"""Universal Transverse Mercator (UTM) Map Projection.
100% Python Standard Library.
"""

import math

class UTMProjection:
    """Projects WGS-84 (Lat, Lon) to UTM (Easting, Northing, Zone)."""
    @staticmethod
    def latlon_to_utm(lat, lon):
        zone = int((lon + 180.0) / 6.0) + 1
        lon_origin = (zone - 1) * 6.0 - 180.0 + 3.0
        
        phi = math.radians(lat)
        lam = math.radians(lon)
        lam0 = math.radians(lon_origin)
        
        a = 6378137.0
        f = 1.0 / 298.257223563
        e2 = 2.0 * f - f**2
        e_prime_sq = e2 / (1.0 - e2)
        k0 = 0.9996
        
        N = a / math.sqrt(1.0 - e2 * math.sin(phi)**2)
        T = math.tan(phi)**2
        C = e_prime_sq * math.cos(phi)**2
        A = (lam - lam0) * math.cos(phi)
        
        M = a * ((1.0 - e2/4.0 - 3.0*e2**2/64.0 - 5.0*e2**3/256.0) * phi
                 - (3.0*e2/8.0 + 3.0*e2**2/32.0 + 45.0*e2**3/1024.0) * math.sin(2.0*phi)
                 + (15.0*e2**2/256.0 + 45.0*e2**3/1024.0) * math.sin(4.0*phi)
                 - (35.0*e2**3/3072.0) * math.sin(6.0*phi))
                 
        easting = k0 * N * (A + (1.0 - T + C) * A**3 / 6.0 + (5.0 - 18.0*T + T**2 + 72.0*C - 58.0*e_prime_sq) * A**5 / 120.0) + 500000.0
        northing = k0 * (M + N * math.tan(phi) * (A**2 / 2.0 + (5.0 - T + 9.0*C + 4.0*C**2) * A**4 / 24.0 + (61.0 - 58.0*T + T**2 + 600.0*C - 330.0*e_prime_sq) * A**6 / 720.0))
        if lat < 0:
            northing += 10000000.0
            
        return {
            "zone": zone,
            "easting": round(easting, 2),
            "northing": round(northing, 2),
            "hemisphere": "N" if lat >= 0 else "S"
        }
