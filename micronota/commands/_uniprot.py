# ----------------------------------------------------------------------------
# Copyright (c) 2015--, micronota development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
# ----------------------------------------------------------------------------

import gzip
from logging import getLogger

import click

from ..database.uniprot import add_metadata


logger = getLogger(__name__)


@click.command()
@click.argument('infile', type=click.Path(), nargs=-1)
@click.argument('outfile', type=click.Path(),  nargs=1)
@click.pass_context
def cli(ctx, infile, outfile):
    '''Create UniProt protein cross-ref database.

    Example:
    micronota _uniprot uniprot_sprot.xml.gz uniprot_trembl.xml.gz <out_dir>/<uniprot.sql>

    '''
    click.echo('=======+')
    n = 0
    for fp in infile:
        if fp.endswith('.gz'):
            with gzip.open(fp) as f:
                n += add_metadata(f, outfile)
        else:
            with open(fp) as f:
                n += add_metadata(f, outfile)
    logger.info('Parsed %d records from %r' % (n, infile))
