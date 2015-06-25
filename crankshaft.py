#!/usr/bin/python

#####################################################
# A model to describe an I.C.E. crankshaft.
# All units in Metric/SI.
# Author: Collin Murphy
# email: cbmurphy87@gmail.com
# Date Created: 6.15.2015
# Last Modified: 6.24.2015
#####################################################

# ================== standard imports =================

from camshaft import Camshaft

# ================== custom methods  ==================

class Crankshaft(object):

    """ Class for an I.C.E. crankshaft. """

    def __init__(self, stroke, mass, main_diameter, rod_diameter):
        super(Camshaft, self).__init__()
        self.stroke = stroke
        self.mass = mass
        self.main_diameter = main_diameter
        self.rod_diameter = rod_diameter


def main():
    pass

if __name__ == '__main__':
    main()
