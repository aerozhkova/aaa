class BasePokemon:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def __str__(self):
        return f'{self.name}/{self.category}'


class EmojiMixin:
    emojid = {'grass': '🌿', 'fire': '🔥', 'water': '🌊', 'electric': '⚡'}

    def __str__(self):
        text = super().__str__()
        for category, emoji in self.emojid.items():
            text = text.replace(category, emoji)

        return text


class Pokemon(EmojiMixin, BasePokemon):
    pass


if __name__ == '__main__':
    pikachu = Pokemon(name='Pikachu', category='electric')
    print(pikachu)
