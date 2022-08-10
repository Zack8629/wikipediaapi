import wikipediaapi
import re


def wiki():
    wiki_wiki = wikipediaapi.Wikipedia('ru')

    page = wiki_wiki.page('Категория:Женские имена')

    def get_animal_categories(categorymembers, level=0, max_level=1):
        for cat in categorymembers.values():
            yield cat
            if cat.ns == wikipediaapi.Namespace.CATEGORY and level < max_level:
                get_animal_categories(cat.categorymembers, level=level + 1, max_level=max_level)

    names = get_animal_categories(page.categorymembers)

    with open('names.txt', 'w', encoding='utf-8') as f:
        for val in names:
            pattern = r'[А-Я]'

            name = str(val).title().split()[0]

            first_letter = name[0]
            if not re.search(pattern, first_letter):
                continue

            f.writelines(f"'{name}', ")

wiki()
