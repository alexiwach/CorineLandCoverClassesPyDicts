# dictionairies corine land cover classes after the Updated CLC  nomenclature
# guidelines (10/05/2019): for details see 
# https://land.copernicus.eu/content/corine-land-cover-nomenclature-guidelines/html/

corine_level_1_dict = {
    1: 'Artificial Surfaces',
    2: 'Agricultural Areas',
    3: 'Forests and Semi-Natural Areas',
    4: 'Wetlands',
    5: 'Water Bodies',
}

corine_level_2_dict = {
    # Artificial surfaces
    11: 'Urban fabric',
    12: 'Industrial, commercial, and transport units',
    13: 'Mine, dump, and construction sites',
    14: ' Artificial, non-agricultural vegetated areas',
    
    # Agricultural areas
    21: 'Arable land',
    22: 'Permanent crops',
    23: 'Pastures',
    24: 'Heterogeneous agricultural areas',
    
    # Forest and seminatural areas
    31: 'Forests',
    32: 'Shrub and/or herbaceous vegetation associations',
    33: 'Open spaces with little or no vegetation',
    
    # Wetlands
    41: 'Inland wetlands',
    42: 'Coastal wetlands',
    
    # Water bodies
    51: 'Inland waters',
    52: 'Marine waters',
}

corine_level_3_dict = {
    # Urban fabric
    111: 'Continuous urban fabric',
    112: 'Discontinuous urban fabric',
    
    # Industrial, comercial and transport units
    121: 'Industrial or commercial units',
    122: 'Road and rail networks and associated land',
    123: 'Port areas',
    124: 'Airports',
    
    # Mine, dump and construction sites
    131: 'Mineral extraction sites',
    132: 'Dump sites',
    133: 'Construction sites',
    
    # Artificial, non-agricultural vegetated areas
    141: 'Green urban areas',
    142: 'Sport and leisure facilities',
    
    # Arable land
    211: 'Non-irrigated arable land',
    212: 'Permanently irrigated land',
    213: 'Rice fields',
    
    # Permanent crops
    221: 'Vineyards',
    222: 'Fruit trees and berry plantations',
    223: 'Olive groves',
    
    # Pastures
    231: 'Pastures',
    
    # Heterogeneous agricultural areas
    241: 'Annual crops associated with permanent crops',
    242: 'Complex cultivation patterns',
    243: 'Land principally occupied by agriculture, with significant areas of natural vegetation',
    244: 'Agro-forestry areas',
    
    # Forest
    311: 'Broad-leaved forest',
    312: 'Coniferous forest',
    313: 'Mixed forest',
    
    # Shrub and/or herbaceous vegetation associations
    321: 'Natural grassland',
    322: 'Moors and heathland',
    323: 'Sclerophyllous vegetation',
    324: 'Transitional woodland/shrub',
    
    # Open spaces with little or no vegetation
    331: 'Beaches, dunes, sands',
    332: 'Bare rock',
    333: 'Sparsely vegetated areas',
    334: 'Burnt areas',
    335: 'Glaciers and perpetual snow',
    
    # Inland wetlands
    411: 'Inland marshes',
    412: 'Peatbogs',
    
    # Coastal wetlands
    421: 'Salt marshes',
    422: 'Salines',
    423: 'Intertidal flats',
    
    # Inland waters
    511: 'Water courses',
    512: 'Water bodies',
    
    # Marine waters
    521: 'Coastal lagoons',
    522: 'Estuaries',
    523: 'Sea and ocean',
}

# tests
if __name__ == '__main__':

  test_inputs = [4, 32, 123, 3, 42, 333]
  test_outputs = [
      'Wetlands',
      'Shrub and/or herbaceous vegetation associations',
      'Port areas',
      'Forest and seminatural areas',
      'Coastal wetlands',
      'Sparsely vegetated areas'
    ]
  dicts = [
      corine_level_1_dict,
      corine_level_2_dict,
      corine_level_3_dict,
      corine_level_1_dict,
      corine_level_2_dict,
      corine_level_3_dict,
      ]

  for i in range(3):
    if not dicts[i][test_inputs[i]] == test_outputs[i]:
      msg = 'error w/in dict' + str(i + 1) + 'at key' + str(test_inputs[i])
      raise ValueError(msg)
