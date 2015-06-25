#!/usr/bin/python

###########################################################
# A model to describe an internal combustion engine.
# All units in Metric/SI.
# Author: Collin Murphy
# email: cbmurphy87@gmail.com
# Date Created: 6.15.2015
# Last Modified: 6.24.2015
###########################################################

# ================= standard imports ======================

import sys

# ================== custom imports =======================

from camshaft import Camshaft
from crankshaft import Crankshaft
from cylinderhead import CylinderHead
from piston import Piston

# ===================== classes ===========================

class Engine(object):

    """
    Class for an Internal Combustion Engine (I.C.E.).
    The following units are used, unless noted otherwise:
        rotational angle: entered in degrees, but converted to rad
        rotational velocity: radians per second (rad/s)
        rotational acceleration: radians per second ^ 2 (rad/s^2)
        length: millimeters (mm)
        volume: cubic centimeters (cc)
        temperature: Kelvin (K)
    """

    def __init__(self, bore, stroke, firing_order, **kwargs):

        """
        Initialize an Engine instance

        :param number_cylinder: number of cylinders
        :param bore: bore in mm
        :param stroke: stroke in mm
        :param firing_order: firing order of cylinders
        :param cam_lift: cam lift in mm
        :param cam_duration: cam duration in crankshaft degrees
        :param cam_overlap: cam overlap in crankshaft degrees
        """

        super(Engine, self).__init__()
        self.run = False
        self.number_cylinders = len(firing_order)
        self.bore = bore
        self.stroke = stroke
        self.firing_order = firing_order
        self.operating_temp = 366  # degrees Kelvin

        ################# initialize engine components ###############

        # define requirements
        requirements = {
            'camshaft': {'lift', 'duration'},
            'crankshaft': {'main_diameter', 'rod_diameter', 'mass', 'moment'},
            'piston': {'diameter', 'mass', 'pin_height'}
        }
        # gather other parameters
        engine_parameters = {
            'number_cylinders': self.number_cylinders,
            'bore': bore,
            'stroke': stroke,
            'firing_order': firing_order
        }
        # check each component and its requirements
        for component, requires in requirements.items():
            if component in kwargs:
                missing = set(kwargs.get(component, {})).difference(requires)
                if missing:
                    print 'Must provide%s for %s' % (', '.join(missing),
                                                     component)
                    sys.exit()

        cam_kwargs = kwargs.get('camshaft')
        cam_kwargs.update({'firing_order':engine_parameters['firing_order']})
        self.camshaft = Camshaft(**cam_kwargs)
        return
        self.crankshaft = Crankshaft(**kwargs.get('crankshaft', None))
        self.piston = Piston(**kwargs.get('piston', None))

    def _hidden_method(self):
        print 'You found me!'

def main():

    camshaft = {
        'lift': 11.3,
        'duration': 294
    }
    crankshaft = {
        'main_diameter': 45,
        'rod_diameter': 30,
        'mass': 10000,
        'moment': 500,
    }
    piston = {
        'diameter': 86.5,
        'mass': 350,
        'pin_height': 30
    }

    engine = Engine(bore=86.5, stroke=86.5, firing_order=(1,5,6,3,4,2),
                    camshaft=camshaft, crankshaft=crankshaft,
                    piston=piston)

    print dir(engine)
    print engine._hidden_method()
    for crank_deg in range(0, 720 + 1, 10):
        lift = engine.camshaft.get_lift(crank_deg, 1)
        print '%4s: %s %s' % (crank_deg, '#' * int(round(lift)), lift)

if __name__ == '__main__':
    main()
