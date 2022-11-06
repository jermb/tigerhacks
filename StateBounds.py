import math

def getState(coord):
    px = coord[0]
    py = coord[1]

    possible_states = {}
    for state in states:
        box = states[state]["bbox"]
        x1 = box[0] 
        y1 = box[1]
        x2 = box[2]
        y2 = box[3]
        if (px > x1 and px < x2 and py > y1 and py < y2) :
            x3 = states[state]["center"][0]
            y3 = states[state]["center"][1]
            dx = x3 - px
            dy = y3 - py

            distance_from_center = math.sqrt((dx*dx) + (dy*dy))
            possible_states[state] = distance_from_center        
    try:
        return min(possible_states, key=possible_states.get)
    except:
        raise Exception("Error: This point does not reside within a US State!")

states = {
  "Alabama": {
    "bbox": [-88.4732271, 30.108750601, -84.888245902, 35.00802804],
    "center": [-86.7892920871389, 32.8288658080717]
  },
  "Alaska": {
    "bbox": [-179.9, 51.1555978, -129.990234302, 71.4202911],
    "center": [-153.180996665583, 64.6358675746153]
  },
  "Arizona": {
    "bbox": [-114.816590087, 31.3321769, -109.0451719, 37.0037251],
    "center": [-111.422127989113, 34.2202611707236]
  },
  "Arkansas": {
    "bbox": [-94.6178591, 33.0042819, -89.640996901, 36.4997491],
    "center": [-92.4202962772624, 35.0968852383944]
  },
  "California": {
    "bbox": [-124.512924199, 32.534250901, -114.1312109, 42.0095031],
    "center": [-119.699375153073, 37.0743595873945]
  },
  "Colorado": {
    "bbox": [-109.0601871, 36.9924609, -102.0415219, 41.0034441],
    "center": [-105.604997408086, 39.1902459990462]
  },
  "Connecticut": {
    "bbox": [-73.727775086, 40.979898002, -71.7872389, 42.0505111],
    "center": [-72.7262428031069, 41.6261419326713]
  },
  "Delaware": {
    "bbox": [-75.7889221, 38.443868911, -74.952106001, 39.8395161],
    "center": [-75.5055627423557, 38.9978781537978]
  },
  "Florida": {
    "bbox": [-87.634896098, 24.430290401, -79.932394001, 31.0009681],
    "center": [-82.033629763236, 28.9444647055242]
  },
  "Georgia": {
    "bbox": [-85.605165098, 30.3557569, -80.72097521, 35.0013031],
    "center": [-83.2572560296474, 32.3305706594431]
  },
  "Hawaii": {
    "bbox": [-178.432653299, 18.816422614, -154.710447001, 28.4890016],
    "center": [-157.855676, 21.304547]
  },
  "Idaho": {
    "bbox": [-117.2430271, 41.9881819, -111.0435469, 49.0009111],
    "center": [-114.651378585904, 44.3918682454771]
  },
  "Illinois": {
    "bbox": [-91.513079099, 36.970297904, -87.0117186, 42.5854444],
    "center": [-89.2749461071049, 40.1492928594374]
  },
  "Indiana": {
    "bbox": [-88.097892099, 37.771765902, -84.7845349, 42.09822248],
    "center": [-86.2846076064882, 39.9184076479867]
  },
  "Iowa": {
    "bbox": [-96.639485099, 40.3754399, -90.140060901, 43.5011961],
    "center": [-93.4967816941637, 42.0869507820775]
  },
  "Kansas": {
    "bbox": [-102.0517691, 36.9930159, -94.5883869, 40.0031661],
    "center": [-98.7257387818225, 38.5320800989441]
  },
  "Kentucky": {
    "bbox": [-89.571201099, 36.497057901, -81.964787903, 39.147732099],
    "center": [-85.2893967376316, 37.5310880799693]
  },
  "Louisiana": {
    "bbox": [-94.0433521, 28.8334077, -88.727852605, 33.0196201],
    "center": [-92.305998069584, 30.9374993015932]
  },
  "Maine": {
    "bbox": [-71.083928099, 42.923707915, -66.8847655, 47.459854094],
    "center": [-69.2365510393463, 45.3982848479073]
  },
  "Maryland": {
    "bbox": [-79.4876511, 37.857507102, -74.950777808, 39.7230371],
    "center": [-76.8536374638244, 39.4780636707791]
  },
  "Massachusetts": {
    "bbox": [-73.508210099, 41.166766302, -69.834759002, 42.886778098],
    "center": [-71.9603257607071, 42.3204700602381]
  },
  "Michigan": {
    "bbox": [-90.439453198, 41.6961179, -82.133789, 48.370847798],
    "center": [-84.525239999781, 44.9337458924535]
  },
  "Minnesota": {
    "bbox": [-97.239063098, 43.4993609, -89.384765544, 49.3836573],
    "center": [-94.1991167709013, 46.3434063154299]
  },
  "Mississippi": {
    "bbox": [-91.655009098, 30.069093908, -88.09788791, 34.9960981],
    "center": [-89.7181678797461, 32.8566735673939]
  },
  "Missouri": {
    "bbox": [-95.774704099, 35.995744929, -89.0989679, 40.6136401],
    "center": [-92.585914899503, 38.19080239858]
  },
  "Montana": {
    "bbox": [-116.0491321, 44.357935903, -104.039693916, 49.0011001],
    "center": [-109.172599073804, 47.0725146587006]
  },
  "Nebraska": {
    "bbox": [-104.0535141, 39.9999429, -95.3082899, 43.0017071],
    "center": [-99.9595472694748, 41.8637326962585]
  },
  "Nevada": {
    "bbox": [-120.0064731, 35.001856904, -114.0394629, 42.0018421],
    "center": [-116.598821819119, 40.071120297646]
  },
  "New Hampshire": {
    "bbox": [-72.5571241, 42.6970419, -70.553456648, 45.305778099],
    "center": [-71.5783054333969, 43.6898878153712]
  },
  "New Jersey": {
    "bbox": [-75.574177881, 38.8510384, -73.870666088, 41.357607098],
    "center": [-74.3893168105238, 40.1502478924773]
  },
  "New Mexico": {
    "bbox": [-109.0504311, 31.3322309, -103.0020429, 37.0002331],
    "center": [-105.998350627305, 34.3248564900842]
  },
  "New York": {
    "bbox": [-79.8046876, 40.47714, -71.763626912, 45.0239468],
    "center": [-75.4652471468304, 42.751210955038]
  },
  "North Carolina": {
    "bbox": [-84.321821099, 33.756920004, -75.361988, 36.5881371],
    "center": [-79.3896838690365, 35.5568849207634]
  },
  "North Dakota": {
    "bbox": [-104.0490091, 45.9350909, -96.554435901, 49.0006921],
    "center": [-100.459284161645, 47.4443684021068]
  },
  "Ohio": {
    "bbox": [-84.8202931, 38.4034229, -80.5187049, 42.2935643],
    "center": [-82.7114488167578, 40.4174201146542]
  },
  "Oklahoma": {
    "bbox": [-103.0024131, 33.615832902, -94.4310139, 37.0023121],
    "center": [-97.5389608460746, 35.9015874097089]
  },
  "Oregon": {
    "bbox": [-124.70606, 41.967659102, -116.4632619, 46.301396094],
    "center": [-120.281411696945, 44.0328841608707]
  },
  "Pennsylvania": {
    "bbox": [-80.6835938, 39.7197989, -74.6895609, 42.4558877],
    "center": [-78.2907462468837, 41.0911397651497]
  },
  "Rhode Island": {
    "bbox": [-71.8945313, 41.073376105, -71.103515502, 42.01879807],
    "center": [-71.5793902557177, 41.6850953372905]
  },
  "South Carolina": {
    "bbox": [-83.353928095, 32.026706202, -78.461673368, 35.215485085],
    "center": [-80.9007732114739, 33.9184118141794]
  },
  "South Dakota": {
    "bbox": [-104.0578791, 42.479701901, -96.436554902, 45.9453701],
    "center": [-100.149201511155, 44.8688864124358]
  },
  "Tennessee": {
    "bbox": [-90.3104911, 34.9829239, -81.64689993, 36.6782551],
    "center": [-85.9823352140893, 35.9885949444454]
  },
  "Texas": {
    "bbox": [-106.6456461, 25.837290904, -93.508038901, 36.5007041],
    "center": [-98.8223185136653, 31.8039734986915]
  },
  "Utah": {
    "bbox": [-114.0528671, 36.9976569, -109.0415719, 42.0017021],
    "center": [-111.602499934826, 39.254817164782]
  },
  "Vermont": {
    "bbox": [-73.438563698, 42.7269329, -71.465049907, 45.0269505],
    "center": [-72.7473878342175, 44.0473082937196]
  },
  "Virginia": {
    "bbox": [-83.6753951, 36.5272947, -75.166797016, 39.466012097],
    "center": [-78.6190526172645, 37.6775920440554]
  },
  "Washington": {
    "bbox": [-124.861672398, 45.5435409, -116.916070902, 49.0121482],
    "center": [-120.094292506456, 48.0250054263449]
  },
  "West Virginia": {
    "bbox": [-82.644539099, 37.201539907, -77.719518927, 40.638801086],
    "center": [-80.7144445663771, 38.743259310741]
  },
  "Wisconsin": {
    "bbox": [-92.889433094, 42.4914411, -86.352539016, 47.3983493],
    "center": [-89.7639108198947, 44.7131688504626]
  },
  "Wyoming": {
    "bbox": [-111.054556, 40.9947959, -104.0522449, 45.0058151],
    "center": [-107.539857541109, 43.5444588856134]
  }
}