from schema import factory
from schema import Country


contr1 = Country (country_name = "Equador", region_id=3)
contr2 = Country (country_name = "Eswatini", region_id=2)
contr3 = Country (country_name = "Fartland", region_id=4)
contr4 = Country(country_name="Incelland", region_id=5)

session = factory()
session.add(contr1)
session.add(contr2)
session.add(contr3)
session.add(contr4)
session.commit()