#!/usr/bin/env python

# Copyright (C) 2006-2017  Music Technology Group - Universitat Pompeu Fabra
#
# This file is part of Essentia
#
# Essentia is free software: you can redistribute it and/or modify it under
# the terms of the GNU Affero General Public License as published by the Free
# Software Foundation (FSF), either version 3 of the License, or (at your
# option) any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the Affero GNU General Public License
# version 3 along with this program. If not, see http://www.gnu.org/licenses/

from essentia_test import *
import essentia.streaming as estr


class TestCoverSongSimilarity(TestCase):

    sim_matrix = array([[1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1],
                        [0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1],
                        [1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1],
                        [1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0],
                        [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1]])
    expected_distance = 1.732

    def testEmpty(self):
        self.assertComputeFails(CoverSongSimilarity(), [])

    def testRegressionStandard(self):
        sim = CoverSongSimilarity()
        score_matrix, distance = sim.compute(self.sim_matrix)
        self.assertAlmostEqualFixedPrecision(self.expected_distance, distance)
        warn = "Expected shape of output score_matrix is %s, instead of %s" % (self.sim_matrix.shape, score_matrix.shape)
        self.assertEqual(score_matrix.shape[0], self.sim_matrix.shape[0], warn)
        self.assertEqual(score_matrix.shape[1], self.sim_matrix.shape[1], warn)

    def testInvalidParam(self):
        self.assertConfigureFails(CoverSongSimilarity(), { 'distanceType': 'test' })
        self.assertConfigureFails(CoverSongSimilarity(), { 'alignmentType': 'test' })


suite = allTests(TestCoverSongSimilarity)

if __name__ == '__main__':
    TextTestRunner(verbosity=2).run(suite)

