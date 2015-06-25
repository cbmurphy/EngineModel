#!/usr/bin/python

#####################################################
# A model to describe an internal combustion engine.
# All units in Metric/SI.
# Author: Collin Murphy
# email: cbmurphy87@gmail.com
# Date Created: 6.15.2015
# Last Modified: 6.24.2015
#####################################################

# ================== standard imports =================

from camshaft import Camshaft

# ================== custom methods  ==================

def avg(*args):
    return sum(args) / len(args)

# ===================== classes ========================

class Engine(object):
    def __init__(self, number_cylinder, bore, stroke, firing_order):
        super(Engine, self).__init__()
        self.number_cylinders
        self.bore = bore
        self.stroke = stroke
        self.firing_order = firing_order
        self.operating_temp = 366  # degrees Kelvin


class Crankshaft(object):
    def __init__(self, stroke, mass, main_diameter, rod_diameter):
        super(Camshaft, self).__init__()
        self.stroke = stroke
        self.mass = mass
        self.main_diameter = main_diameter
        self.rod_diameter = rod_diameter


class Piston(object):
    '''
    Class for an engine piston. Alpha is the coefficient of thermal expansion,
    measured in 10^-6mm/K.
    '''

    def __init__(self, diameter, pin_height, alpha=22.2):
        super(Piston, self).__init__()
        self.diameter = diameter  # diameter at STP of 273.15 degrees Kelvin
        self.pin_height = pin_height


class CylinderHead(object):
    ''' Model an engine cylinder head '''

    def __init__(self, number_cylinders, number_valves):
        super(CylinderHead, self).__init__()
        self.number_cylinders = num_cyls
        self.number_valves = number_valves
        self.combustion_chamber_vol = combustion_chamber_volume


def main():

    cam = Camshaft(11.3, 294.0, (1, 5, 3, 6, 2, 4))
    print cam.firing_order
    print cam.start_lift
    print 'Degrees: lift (mm)'

    for crank_deg in range(0, 720 + 1, 10):
        lift = cam.get_lift(crank_deg, 1)
        print '%4s: %s %s' % (crank_deg, '#' * int(round(lift)), lift)

if __name__ == '__main__':
    main()
