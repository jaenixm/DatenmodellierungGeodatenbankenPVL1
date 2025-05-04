from math import sqrt, sin, cos, radians, atan2

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def eukl_dist(self, other):
        dx = other.x - self.x
        dy = other.y - self.y
        return sqrt(dx**2 + dy**2)

    def area(self):
        return 0   

class GeographicPoint(Point):
    def __init__(self, latitude, longitude):
        super().__init__(latitude, longitude)  # Vererbung zeigen
        self.latitude = latitude
        self.longitude = longitude

    def harvesine(self, other):
        # Radius der Erde in Kilometern
        r = 6371
        
        # Umrechnung in Radiant
        phi1 = radians(self.latitude)
        phi2 = radians(other.latitude)
        delta_phi = radians(other.latitude - self.latitude)
        delta_lambda = radians(other.longitude - self.longitude)

        # Harvesine-Formel
        a = sin(delta_phi / 2)**2 + cos(phi1) * cos(phi2) * sin(delta_lambda / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        d = r * c
        return d
    
if __name__ == "__main__":
    p1 = Point(0, 0)
    p2 = Point(3, 4)
    print("Euklidische Distanz:", p1.eukl_dist(p2))
    print("Fläche von p1:", p1.area())

    gp1 = GeographicPoint(53.551086, 9.993682)  # Hamburg
    gp2 = GeographicPoint(-36.848461, 174.763336)   # Auckland

    print("Harvesine Distanz:", gp1.harvesine(gp2), "km")

    # Vererbung zeigen
    print("MRO:", GeographicPoint.mro())

        
