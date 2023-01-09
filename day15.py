import re

# Parse input
sensors, beacons = [], []
with open('test.txt') as sensors_signals:
    for sensor_signal in sensors_signals.readlines():
        positions = re.findall(r'x=(-?[0-9]*), y=(-?[0-9]*)', sensor_signal)
        sensor, beacon = [list(map(int, position)) for position in positions]
        sensors.append(sensor)
        beacons.append(beacon)

# Manhattan distance
def manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

distance_sensor_beacon = [manhattan(*sensor_beacon) 
             for sensor_beacon in list(zip(sensors, beacons))]

# Grid dimensions
sensor_range = []
for sensor, d in zip(sensors, distance_sensor_beacon):
    sensor_range += [(sensor[0] + d, sensor[1]),
                     (sensor[0] - d, sensor[1]),
                     (sensor[0], sensor[1] + d),
                     (sensor[0], sensor[1] - d)]

coordinates_list = list(zip(*sensor_range))
left = min(coordinates_list[0])
right = max(coordinates_list[0])
top = min(coordinates_list[1])
down = max(coordinates_list[1])

# Iterate over the grid
grid = []
for y in range(top, down + 1):
    grid.append([])
    for x in range(left, right + 1):
        cell = [x, y]
        distance_cell_sensor = [manhattan(cell, sensor) for sensor in sensors]
        # Calculate if cell-sensor distance is smaller than beacon-sensor distance
        in_range = any([distances[0] >= distances[1] 
         for distances in zip(distance_sensor_beacon, distance_cell_sensor)])

        if cell in beacons or in_range:
            grid[-1].append(True)
        else:
            grid[-1].append(False)
        
###########
PROBLEMAS CON LA EXTENSIÓN DEL GRID
##########
grid[11]
x = -2
y = 10
for distances in zip(distance_sensor_beacon, distance_cell_sensor):
    print(distances)


g = []
g.append([])
g[-1].append(True)
