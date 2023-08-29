import numpy as np
geoPositions = {
    "Agder": {
        "Length": 100,
        "Width": 100,
        "Municipalities": {
            "Arendal": (),
            "Grimstad": (),
            "Lillesand": (),
            "Risor": (),
            "Tvsedestrand": (),
            "Froland": (),
            "Birkenes": (),
            "Evje og Hornnes": (),
            "Gjerstad": (),
            "Vegårshei": (),
            "Amli": (),
            "Valle": (),
            "Iveland": (),
            "Bygland": (),
            "Bykle": ()
        }
    }
}

print(geoPositions["Agder"]["Municipalities"]["Arendal"])
print(np.zeros((10,2)))

demandByProvince = np.array([2144636, 1702321, 1651337, 1152372, 8296265, 4082799, 848626, 3505345, 3029488, 6066878, 12176541])/10
print(demandByProvince)