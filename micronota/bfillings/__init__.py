r'''
Application Wrappers
====================

.. currentmodule:: micronota.bfillings

This module (:mod:`micronota.bfillings`) provides wrappers of `class`
for external bioinformatic tools such as `Prodigal`, `HMMer`, etc.
It also has the util functions built upon those wrappers to predict genes,
search for homologues, etc.


Classes
-------

.. autosummary::
   :toctree: _autosummary


Functions
---------

.. autosummary::
   :toctree: _autosummary

   predict_genes
   cmpress_cm
   cmscan_fasta
   hmmpress_hmm
   hmmscan_fasta
   make_db
   search_protein_homologs

'''

# ----------------------------------------------------------------------------
# Copyright (c) 2015--, micronota development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
# ----------------------------------------------------------------------------


from .prodigal import predict_genes
from .infernal import cmpress_cm, cmscan_fasta
from .hmmer import hmmpress_hmm, hmmscan_fasta
from .diamond import make_db, search_protein_homologs


__all__ = ['predict_genes',
           'cmpress_cm', 'cmscan_fasta',
           'hmmpress_hmm', 'hmmscan_fasta',
           'make_db', 'search_protein_homologs']
