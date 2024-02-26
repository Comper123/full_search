from yandex_map.yandex_map import (
    search_business, 
    get_coordinates,
    show_map,
    get_map,
    del_map,
    generate_spn,
    get_territory
)
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("adres")

territory = get_territory(parser.parse_args().adres)
coords = get_coordinates(parser.parse_args().adres)

image = get_map(coords, spn=generate_spn(territory), pt=f"{coords[0]},{coords[1]},blm")
show_map(image)
del_map(image)