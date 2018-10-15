# -*- coding: utf-8 -*-

"""Console script for glean_parser."""

from pathlib import Path
import sys

import click

from . import translate as mod_translate


@click.command()
@click.argument(
    'input',
    type=click.Path(
        exists=True,
        dir_okay=False,
        file_okay=True,
        readable=True,
    ),
    nargs=-1
)
@click.option(
    '--output',
    '-o',
    type=click.Path(
        dir_okay=True,
        file_okay=False,
        writable=True,
    ),
    nargs=1,
    required=True,
)
@click.option(
    '--format',
    '-f',
    type=click.Choice(mod_translate.OUTPUTTERS.keys()),
    required=True,
)
def translate(input, format, output):
    """
    Translate metrics.yaml files to other formats.
    """
    mod_translate.translate(
        [Path(x) for x in input],
        format,
        Path(output)
    )


@click.group()
def main(args=None):
    """Command line utility for glean_parser."""
    pass


main.add_command(translate)


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
