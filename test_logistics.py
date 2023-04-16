from devopslib.logistics import print_cities, calculate_distance, cities


def test_distance_btwn_points():
    assert (
        calculate_distance(
            cities["New York City, New York"], cities["Los Angeles, California"]
        )
        == 3944.422231489921
    )


def test_print_cities(capsys):
    print_cities()
    captured = capsys.readouterr()
    assert "Dallas, Texas" in captured.out
