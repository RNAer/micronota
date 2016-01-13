# ----------------------------------------------------------------------------
# Copyright (c) 2015--, micronota development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
# ----------------------------------------------------------------------------

import click

from ..annotate import AnnotateWF


@click.command()
@click.option('-i', '--input_fp', type=click.File('r'),
              required=True,
              help='Input file path.')
@click.option('-o', '--output_dir', type=click.File('w'),
              required=True,
              help='Output directory path.')
@click.option('--min_len', type=int, default=100,
              required=True,
              help='Seq shorter than this will not be annotated.')
@click.option('--cpu', type=int, default=1,
              help='Number of CPU cores to use.')
@click.option('--config', type=click.File('r'),
              help=('Config file to fine tune the wrapped annotation tools. '
                    'Its format is defined in https://docs.python.org/3/'
                    'library/configparser.html#supported-ini-file-structure'))
@click.pass_context
def cli(ctx, input_fp, output_dir, min_len, sense, antisense):
    '''Annotate prokaryotic sequences.

    By default, it will annotate both +/- strands.'''
    sequences = ''
    options = {'rc=': False}
    wf = AnnotateWF(state=sequences, options=options, min_len=min_len)

