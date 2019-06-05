# A very simple class modelling coffee beans


class CoffeeBean:

    def __init__(self, origin, country, tasting_notes):
        self._origin = origin
        self._country = country
        self._tasting_notes = tasting_notes

    def origin(self):
        return self._origin

    def country(self):
        return self._country

    def tasting_notes(self):
        return self._tasting_notes

    def __str__(self):
        return "{origin} ({country}): \n* {tasting_notes}".format(
            origin=self.origin(),
            country=self.country(),
            tasting_notes='\n* '.join(self.tasting_notes()))


bean = CoffeeBean("Chumeca La Trinidad",
                  "Costa Rica",
                  ['caramel', 'chocolate', 'berry fruit'])
print(bean)
