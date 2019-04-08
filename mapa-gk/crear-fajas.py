from qgis.core import *
#--80 Char Rule-----------------------------------------------------------------

# Este script crea los geojson correspondientes a los rectángulos y meridianos
# de gaja, necesarios para generar el mapa de fajas Gauss Krugger. El geojson
# de Pais tiene como origen: http://www.ign.gob.ar/archivos/sig250/geojson/pais.zip
# Se le cortaron las partes de antártida, se simplifico con el algoritmo de
# Douglas-nosequien (tolerancia 4km), y se eliminaron los poligonos de menos de
# 16km^2

# supply path to qgis install location
QgsApplication.setPrefixPath("/usr", True)

# create a reference to the QgsApplication, setting the
# second argument to False disables the GUI
qgs = QgsApplication([], False)

# load providers
qgs.initQgis()

arriba = -20
abajo = -60

anillos= []
mcs = []
etiquetas = []

for centro in [-54,-57,-60,-63,-66,-69,-72][::-1]:
    derecha, izquierda = centro + 1.5, centro - 1.5
    puntos = [[arriba,izquierda],[arriba,derecha],
            [abajo,derecha],[abajo,izquierda],[arriba,izquierda]]
    #
    borde = []
    #
    for (x0,y0),(x1,y1) in zip(puntos[:-1],puntos[1:]):
        largo = (x1-x0)+(y1-y0)
        print(largo)
        print((x0,y0),(x1,y1))
        if largo < 0:
            largo = -largo
            signo = -1
        else:
            signo = 1
        for i in range(int(largo/0.1)):
            if x0 == x1:
                x = x0
                y = y0 + 0.1 * i*signo
            else:
                x = x0 + 0.1 * i*signo
                y = y0
            pt = [y,x]
            borde.append(pt)
        borde.append([y1,x1])
    #
    anillos.append(QgsLineString([QgsPoint(*i) for i in borde]))

    mc = []
    for i in range(int((arriba-abajo+2)/0.1)):
        x = centro
        y = 0.1*i + abajo - 1
        mc.append([x,y])

    mcs.append(QgsLineString([QgsPoint(*i) for i in mc]))

    etiquetas.append(QgsPoint(centro,arriba))

wgs=QgsCoordinateReferenceSystem("epsg:4326")
gk4=QgsCoordinateReferenceSystem("epsg:5346")

tr = QgsCoordinateTransform(wgs,gk4,QgsProject.instance())

fajas = QgsVectorLayer('Polygon?crs=epsg:5346&field=faja:int','fajas','memory')

merid = QgsVectorLayer('LineString?crs=epsg:5346&field=faja:int','fajas','memory')

etiqs = QgsVectorLayer('Point?crs=epsg:5346&field=mc:double','fajas','memory')

campos = fajas.dataProvider().fields()

with edit(fajas):
    for faja,anillo in enumerate(anillos):
        feat = QgsFeature(campos)
        feat['faja'] = faja
        anillo.transform(tr)
        geom = QgsPolygon()
        geom.setExteriorRing(anillo)
        feat.setGeometry(geom)
        fajas.addFeature(feat)

with edit(merid):
    for faja,mc in enumerate(mcs):
        feat = QgsFeature(campos)
        feat['faja'] = faja
        mc.transform(tr)
        feat.setGeometry(mc)
        merid.addFeature(feat)

campos = etiqs.dataProvider().fields()

with edit(etiqs):
    for mc,punto in enumerate(etiquetas):
        feat = QgsFeature(campos)
        feat['mc'] = punto.x()
        punto.transform(tr)
        feat.setGeometry(punto)
        etiqs.addFeature(feat)

error = QgsVectorFileWriter.writeAsVectorFormat(fajas, "/home/javier/Carto/git-repos/apuntes-src/mapa-gk/fajas.geojson", "UTF-8", gk4 , "geojson")
error = QgsVectorFileWriter.writeAsVectorFormat(merid, "/home/javier/Carto/git-repos/apuntes-src/mapa-gk/meridianos.geojson", "UTF-8", gk4 , "geojson")
error = QgsVectorFileWriter.writeAsVectorFormat(etiqs, "/home/javier/Carto/git-repos/apuntes-src/mapa-gk/etiquetas.geojson", "UTF-8", gk4 , "geojson")
