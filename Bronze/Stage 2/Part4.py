def points_in_circle(r, coordinates):
    count = 0
    for x, y in coordinates:
        if x**2 + y**2 <= r**2:
            count += 1
    return count

# input 1
print(points_in_circle(100, [[30, 40], [60, 80], [70, 70], [100, 0], [0, 100], [-50, -50], [-80, 60], [120, 10], [10, -120], [0, 0]]))
# input 2
print(points_in_circle(50, [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50], [-30, -40], [25, 40], [-60, -60], [5, 12], [-10, -10]]))
# input 3
print(points_in_circle(25, [[24, 7], [7, 24], [0, 0], [18, 15], [-20, -10], [-5, -5], [12, -16], [13, 24], [-25, 0], [26, 0]]))
