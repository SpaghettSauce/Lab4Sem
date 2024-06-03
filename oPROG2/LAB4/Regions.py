from schema import factory
from schema import Region

session = factory()

regions = ["Africa", "Asia", "Europe",
           "Oceania", "North America",
           "South America"]

for reg in regions:
    r = Region()
    r.region_name = reg
    session.add(r)

session.commit()
