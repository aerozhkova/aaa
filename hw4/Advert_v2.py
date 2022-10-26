import json
import keyword


class JsonToPython:
    def __init__(self, _dict: dict):
        self._dict = _dict

    def __getattr__(self, item):
        if item.endswith('_') and keyword.iskeyword(item[:-1]):
            item = item[:-1]
        if item in self._dict:
            attr = self._dict[item]
            if isinstance(attr, dict):
                return JsonToPython(attr)
            return attr
        else:
            raise AttributeError(f'Object has no attribute {item}')

    def __str__(self):
        return str(self._dict)


class ColorizeMixin:
    def __repr__(self):
        super_repr = super().__repr__()
        try:
            return f'\033[{super().repr_color_code};40m' + \
                   super_repr + '\033[0m'
        except AttributeError:
            return super_repr


class Advert:
    repr_color_code = 33

    def __init__(self, _dict):
        self.jtp = JsonToPython(_dict)
        _ = self.price

    def __getattr__(self, item):
        return self.jtp.__getattr__(item)

    @property
    def price(self):
        price_value = 0
        try:
            price_value = self.jtp.__getattr__('price')
        except AttributeError:
            pass
        if price_value < 0:
            raise ValueError('price must be >= 0')
        return price_value

    def __repr__(self):
        return f'{self.title} | {self.price} ₽'


class ColorizedAdvert(ColorizeMixin, Advert):
    pass


if __name__ == '__main__':
    # обращение к вложенным атрибутам через точки
    # lesson_str = """{
    #               "title": "python",
    #               "price": 0,
    #               "location": {
    #                   "address": "город Москва, Лесная, 7",
    #                   "metro_stations": ["Белорусская"]
    #                   }
    # }"""
    # lesson = json.loads(lesson_str)
    # lesson_ad = Advert(lesson)
    # print(lesson_ad.location.address)

    # ошибка при отрицательной цене
    # lesson_str = '{"title": "python", "price": -1}'
    # lesson = json.loads(lesson_str)
    # lesson_ad = Advert(lesson)

    # 0 при отсутствии цены
    # lesson_str = '{"title": "python"}'
    # lesson = json.loads(lesson_str)
    # lesson_ad = Advert(lesson)
    # print(lesson_ad.price)

    # желтый цвет текста при выводе
    lesson_str = """{
      "title": "Вельш-корги",
      "price": 1000,
      "class": "dogs",
      "location": {
        "address": "поселок санатория Тишково, 25"
      }
    }"""
    lesson = json.loads(lesson_str)
    corgi = Advert(lesson)
    corgi_colored = ColorizedAdvert(lesson)
    print(corgi)
    print(corgi_colored)
    print(corgi_colored.class_)
