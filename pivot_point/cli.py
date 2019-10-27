# -*- coding: utf-8 -*-
import sys
import click
from pivot_point import helpers


@click.command()
@click.argument("high")
@click.argument("low")
@click.argument("close")
def main(high, low, close):
    """Console script for pivot_point."""
    h = float(high)
    l = float(low)
    c = float(close)
    pp = helpers.pp(h, c, l)
    click.echo(helpers.r2(pp, h, l))
    click.echo(helpers.r1(pp, l))
    click.echo(pp)
    click.echo(helpers.s1(pp, h))
    click.echo(helpers.s2(pp, h, l))
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
