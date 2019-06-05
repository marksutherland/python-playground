class Fruit:

    def __init__(self, seeds, flesh, skin):
        self._seeds = seeds
        self._flesh = flesh
        self._skin = skin

    @property
    def seeds(self):
        return self._seeds

    @property
    def flesh(self):
        return self._flesh

    @property
    def skin(self):
        return self._skin

    def __str__(self):
        return "{name}: I have {skin} skin, {flesh} flesh and {seeds} seeds".format(
            name=self.__class__.__name__,
            skin=self.skin,
            flesh=self.flesh,
            seeds=self.seeds
        )


class Apple(Fruit):
    def __init__(self, colour):
        super().__init__(
            seeds="small black pips",
            flesh="pale and crunchy",
            skin="firm yet thin, {}".format(colour)
        )


class Braeburn(Apple):
    def __init__(self):
        super().__init__('red with green patches')


class Bramley(Apple):
    def __init__(self):
        super().__init__('green')


class Orange(Fruit):
    def __init__(self):
        super().__init__(
            seeds="pale, wrinkly pips",
            flesh="juicy, gelatinous, orange",
            skin="thick, orange rind"
        )


class Tomato(Fruit):
    def __init__(self):
        super().__init__(
            seeds="small and round with a gelatinous case",
            flesh="thin and watery",
            skin="soft and red"
        )


print(Braeburn())
print(Bramley())
print(Orange())
print(Tomato())
