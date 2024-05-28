import json
import geojson

# Load the GeoJSON data
with open('plant_species_cleaned.geojson', 'r', encoding='utf-8') as f:
    data = geojson.load(f)

# Define the traditional Squamish name mapping based on the Latin name
squamish_names = {
    "Achillea_millefolium": {"Common_Name": "Yarrow", "squamish_name": "si7semáchxw"},
    "Oplapanax_horridus": {"Common_Name": "Devil's Club", "squamish_name": "ch’átyaý"}, 
    "Rosa_nutkana": {"Common_Name": "Wild Rose", "squamish_name": "k_áĺk_ay"}, 
    "Rosa_gymnocarpa": {"Common_Name": "Wild Rose", "squamish_name": "k_áĺk_ay"}, 
    "Rosa_pisocarpa": {"Common_Name": "Wild Rose", "squamish_name": "k_áĺk_ay"}, 
    "Urtica_dioica": {"Common_Name": "Stinging Nettle", "squamish_name": "ts’ex _ ts’íx _"}, 
    "Rubus_leucodermis": {"Common_Name": "Black Cap", "squamish_name": "ts’kw’um ́áý"}, 
    "Vaccinium_ovafolium": {"Common_Name": "Blueberry", "squamish_name": "xwíxwikw’ay/iyálkpaý"}, 
    "Vaccinium_uliginosum": {"Common_Name": "Blueberry", "squamish_name": "xwíxwikw’ay/iyálkpaý"}, 
    "Vaccinium_alaskaense": {"Common_Name": "Blueberry", "squamish_name": "xwíxwikw’ay/iyálkpaý"}, 
    "Vaccinium_myrtilloides": {"Common_Name": "Blueberry", "squamish_name": "xwíxwikw’ay/iyálkpaý"}, 
    "Vaccinium_oxycoccus": {"Common_Name": "Bog Cranberry", "squamish_name": "kwemchúĺs"}, 
    "Ledum_groenlandicum": {"Common_Name": "Labrador Tea", "squamish_name": "mákwam"}, 
    "Sambucus_racemosa": {"Common_Name": "Red Elderberry", "squamish_name": "sts’iwk’"}, 
    "Vaccinium parvifolium": {"Common_Name": "Red Huckleberry", "squamish_name": "skw’ekwchsáý"}, 
    "Rubus_spectabilis": {"Common_Name": "Salmonberry", "squamish_name": "yetwánaý"}, 
    "Amelanchier_alnifolia": {"Common_Name": "Saskatoon Berry", "squamish_name": "nástam ́aý"}, 
    "Amelanchier_semiintegrifolia": {"Common_Name": "Saskatoon Berry", "squamish_name": "nástam ́aý"}, 
    "Sheperdia_canadensis": {"Common_Name": "Soapberry", "squamish_name": "sxwúsum"}, 
    "Rubus_parviflorus": {"Common_Name": "Thimbleberry", "squamish_name": "t’ákw’emaý"}, 
    "Rubus_usinus": {"Common_Name": "Trailing Blackberry", "squamish_name": "skw’elḿxw"}, 
    "Camassia_quamash": {"Common_Name": "Camas", "squamish_name": "spánanexw"}, 
    "Typha_latifolia": {"Common_Name": "Cat-tail", "squamish_name": "sts’á7ḵin"}, 
    "Epilobium_angusstifolium": {"Common_Name": "Fireweed", "squamish_name": "x_ach’t"}, 
    "Allium_cernuum": {"Common_Name": "Nodding Onion", "squamish_name": "kweláwa"}, 
    "Sagittaria_latifolia": {"Common_Name": "Wapato", "squamish_name": "xwuxwukw’últs"}, 
    "Asarum_caudatum": {"Common_Name": "Western Wild Ginger", "squamish_name": "xet’tánay"}, 
    "Fragaria_chiloensis": {"Common_Name": "Coastal Wild Strawberry", "squamish_name": "schi7i7áý"}, 
    "Polydium_glycyrrhiza": {"Common_Name": "Licorice Fern", "squamish_name": "tl’esíp"}, 
    "Pyrus_fusca": {"Common_Name": "Wild Crabapple", "squamish_name": "kwe7úpaý"}, 
    "Tricholoma_murrillianum": {"Common_Name": "Pine Mushroom"}, 
    "Prunus_emarginata": {"Common_Name": "Bitter Cherry"}, 
    "Osmaronia_cerasiformis": {"Common_Name": "Indian Plum"}, 
    "Perideria_gairgeri": {"Common_Name": "Wild Carrot"}, 
    "Lomatium_nudicaule": {"Common_Name": "Indian Consumption Plant"}, 
    "Triglochin_maritimum": {"Common_Name": "Arrow-Grass"}, 
    "Pinus_monticola": {"Common_Name": "White Pine"}, 
    "Echinodontium_tinctorium": {"Common_Name": "Indian Paint Fungus"}, 
    "Solidago_canadensis": {"Common_Name": "Golden Rod"}, 
    "Fragaria_vesca": {"Common_Name": "Woodland Strawberry"}, 
    "Sambucus_canadensis": {"Common_Name": "Common Elderberry"}, 
    "Arbutus_menziesii": {"Common_Name": "Arbutus"}, 
    "Vaccinium_membranaceum": {"Common_Name": "Mountain Bilberry"}, 
    # Add more mappings here
}

# Update each feature with the traditional Squamish name 
for feature in data['features']:
    latin_name = feature['properties']['feature_collection_name']
    if latin_name in squamish_names:
        Common_Name = squamish_names[latin_name]['Common_Name']
        feature['properties']['Common_Name'] = squamish_names[latin_name]['Common_Name']
        feature['properties']['traditional_squamish_name'] = squamish_names[latin_name]

# Save the updated GeoJSON data back to a file
with open('updated_plants.geojson', 'w', encoding='utf-8') as f:
    geojson.dump(data, f, ensure_ascii=False)

print("Traditional Squamish names added successfully.")
