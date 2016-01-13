# ----------------------------------------------------------------------------
# Copyright (c) 2015--, micronota development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
# ----------------------------------------------------------------------------


from skbio.workflow import Workflow, method, requires

from .bfillings import predict_genes


class AnnotateWF(Workflow):
    '''Annotation workflow.'''
    def initialize_state(self, seq):
        self.state = seq

    @method(priority=100)
    def check_length(self):
        if len(self.state) < self.min_len:
            self.failed = True

    @method(priority=70)
    @requires(option='gene', values=True)
    def cds(self):
        '''Identify CDS.'''
        predict_genes()

    @method(priority=60)
    @requires(option='uniref', values=True)
    def search_uniref(self):
        '''Identify homologs and get metadata from them.'''
        pass

    @method(priority=50)
    @requires(option='tigrfam', values=True)
    def search_tigrfam(self):
        '''Identify homologs and get metadata from them.'''
        pass

    @method(priority=80)
    def ncrna(self):
        '''Identify ncRNA.'''
        pass

    @method(priority=90)
    @requires(option='trna', values=True)
    def trna(self):
        '''Identify tRNA and tmRNA.'''

