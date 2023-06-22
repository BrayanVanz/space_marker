from math import sqrt
summer_triangle = {"deneb" : (420, 160), "altair" : (680, 140), "vega" : (110, 320)}

key_list = list(summer_triangle.keys())

for i, v in enumerate(key_list):
    try:
        x1, y1 = summer_triangle[key_list[i]]
        x2, y2 = summer_triangle[key_list[i+1]]
        dist = sqrt((x2 - x1)**2 + (y2 - y1)**2)
        print(dist)
    except:
        break