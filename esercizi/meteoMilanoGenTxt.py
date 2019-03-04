import numpy as np
import matplotlib.pyplot as plt

fileName = 'MeteoMilano.csv'
# [0]  CET
#      Temperatura maxC
#      Temperatura mediaC
#      Temperatura minC
#      Punto di rugiadaC
#      MeanDew PointC
#      Min DewpointC
#      Max Umidità
#      Mean Umidità
# [9]  Min Umidità
#      Max Pressione a livello del marehPa
#      Mean Pressione a livello del marehPa
#      Min Pressione a livello del marehPa
#      Max VisibilitàKm
#      Mean VisibilitàKm
#      Min VisibilitàkM
#      Max Velocità del ventoKm/h
#      Mean Velocità del ventoKm/h
#      Max Velocità RafficaKm/h
# [19] Precipitazionimm
#      CloudCover
#      Eventi
#      WindDirDegrees

# matriceAuto = np.genfromtxt(fileName)
# matriceAuto = np.genfromtxt(fileName, delimiter=',')
# matriceAuto = np.genfromtxt(fileName, delimiter=',', skip_header=1)
matriceAuto = np.genfromtxt(fileName, delimiter=',', skip_header=1, dtype=int)
print matriceAuto[:5,:]

