#!/usr/bin/python

#####################################################
# A model to describe an I.C.E. piston.
# All units in Metric/SI.
# Author: Collin Murphy
# email: cbmurphy87@gmail.com
# Date Created: 6.15.2015
# Last Modified: 6.24.2015
#####################################################

# ================== standard imports =================

from camshaft import Camshaft

# ================== custom methods  ==================

class Piston(object):

    """
    Class for an engine piston.
    Alpha is the coefficient of thermal expansion, measured in 10^-6mm/K.
    """

    def __init__(self, diameter, mass, pin_height, alpha=22.2):
        super(Piston, self).__init__()
        self.diameter = diameter  # diameter at STP of 273.15 degrees Kelvin
        self.pin_height = pin_height


def main():
    pass

if __name__ == '__main__':
    main()
