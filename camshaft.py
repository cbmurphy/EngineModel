#!/usr/bin/python

###########################################################
# A model to describe an I.C.E. camshaft
# All units in Metric/SI.
# Author: Collin Murphy
# email: cbmurphy87@gmail.com
# Date Created: 6.15.2015
# Last Modified: 6.24.2015
###########################################################

# ================= standard imports ======================

from math import sin, pi, radians as rad
import sys

# ================== custom imports  ======================

from enginemethods import *

# ===================== classes ===========================

class Camshaft(object):

    """
    Class for an I.C.E. camshaft.
    All units of rotational angle are entered in degrees, but are converted
     to radians for computations.
    All units of length are in mm.
    """

    def __init__(self, lift, duration, firing_order, advance=0):

        """
        Initialize a Camshaft instance

        :param lift: camshaft lift measured in mm
        :param duration: crank degrees between valve opening and closing
        :param firing_order: list of cylinder numbers in order of firing pattern
        :param  advance[optional]: camshaft (not crankshaft) degrees of advance
            - Positive means valve opens sooner than when piston is at TDC
            - Negative means valve opens later than when piston is at TDC
        """

        super(Camshaft, self).__init__()
        self.lift = lift
        self.duration = rad(duration)
        self.number_cylinders = len(firing_order)
        self.firing_order = firing_order
        self.advance = rad(advance)
        self.amplitude = None
        self.start_lift = tuple(rad(720 / self.number_cylinders * (cyl - 1))
                           for cyl in self.firing_order)

        # run methods to solve for parameters
        self.solve_amplitude()

    def solve_amplitude(self, error=0.001):

        """
        Solve for the amplitude of the sin curve to describe cam lift
        using an iterative bisection method.

        :param error[optional]: error which will stop the solver

        :rtype : None
        """

        low = self.lift
        high = 2 * self.lift
        mid = avg(low, high)
        for x in range(10000):
            mid = avg(low, high)
            f_mid = mid * sin(.5 * (pi - self.duration / 2)) - (mid - self.lift)
            if abs(f_mid) <= error:
                break
            if f_mid > 0:
                low = mid
            elif f_mid < 0:
                high = mid
        else:
            print 'Could not solve for amplitude'
            sys.exit()

        self.amplitude = mid

    def get_lift(self, crank_degrees, cylinder_number):

        """
        Get valve lift in mm at camshaft degrees for cylinder number
        cylinder_number.

        :param crank_degrees: degrees of crankshaft where lift is to be found
        :param cylinder_number: number of cylinder of which to find lift

        :rtype : float
        """

        # if cylinder_number is out of range, return None
        if not 0 < cylinder_number <= self.number_cylinders:
            return None

        # normalize crank_degrees
        crank_degrees %= 720
        crank_rad = rad(crank_degrees)

        return max(0, self.amplitude * sin(.5 * (crank_rad + pi -
                    self.duration / 2- self.start_lift[cylinder_number - 1] -
                    self.advance)) - (self.amplitude - self.lift))


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
