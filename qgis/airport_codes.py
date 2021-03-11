with open("/Users/acryan/Desktop/airports.csv","w") as output_file:
    for f in layer.getFeatures():
        geom = f.geometry()
        line = f"{f['name']},{f['iata_code']},{geom.asPoint().y():.2f},{geom.asPoint().x():.2f}\n"
        o=output_file.write(line)