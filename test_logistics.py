from devopslib.logistics import print_cities, calculate_distance


def test_distance_btwn_points():
    assert calculate_distance(cities[0][1], cities[1][1] == 3944.422231489921)

def test_print_cities():
    assert "Dallas" in print_cities()