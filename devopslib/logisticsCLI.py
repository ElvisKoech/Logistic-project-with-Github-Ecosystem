#!/usr/bin/env python
from devopslib.logistics import (
    calculate_distance,
    print_cities,
    get_city_coordinates,
    travel_time,
)
import click


@click.group()
def cli() -> None:
    """Logistics command-line"""


@cli.command("cities")
def cities() -> None:
    """Print the list of cities"""
    click.echo(click.style("List of cities", fg="green"))
    for city in print_cities():
        click.echo(click.style(city, fg="blue"))


@cli.command("distance")
@click.argument("city1")
@click.argument("city2")
def distance(city1, city2):
    """calculate the distance between two cities

     Example:
    ./logisticsCLI.py distance "New York" "Los Angeles"

    """
    click.echo(click.style("Distance between two cities", fg="green"))
    click.echo(
        click.style(
            f"{calculate_distance(get_city_coordinates(city1), get_city_coordinates(city2))} miles",
            fg="blue",
        )
    )


# build a click command to estimate the tarvel time between two cities by car
# assume the speed is 60mphs per hour
@cli.command("travel")
@click.argument("city1")
@click.argument("city2")
@click.option("--speed", default=60, help="speed in mph")
def travel(city1, city2, speed):
    """calculate the travel time between two cities

    Example:
    "./logisticsCLI.py travel "New York" "Los Angeles" --speed 60

    """
    click.echo(click.style("Travel time between two cities", fg="green"))
    click.echo(
        click.style(
            f"{travel_time(city1, city2, speed)} hours",
            fg="blue",
        )
    )


if __name__ == "__main__":
    cli.add_command(cities)
    cli.add_command(distance)
    cli()
