#!/usr/bin/env python
from logistics import calculate_distance
import click

# Build a click group
@click.group()
def cli():
    """Tool for calculating total distance between a list of cities"""


# Build a click command
@cli.command("total")
@click.argument("cities", nargs=-1)
def total(cities):
    """calculate the total distance between a list of cities"""
    print(calculate_distance(cities))


# invoke the click command
if __name__ == "__main__":
    cli()
