import numpy


class Polygon:

    @classmethod
    def rectangle(cls, h, b, shift=(0, 0)):
        rect = numpy.array([
            [-b / 2 + shift[0], -h / 2 + shift[1]],
            [-b / 2 + shift[0],  h / 2 + shift[1]],
            [ b / 2 + shift[0],  h / 2 + shift[1]],
            [ b / 2 + shift[0], -h / 2 + shift[1]],
        ])
        return Polygon(rect)

    def __init__(self, plots):
        self.plots = plots

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    @property
    def x(self):
        return self.plots[:, 0]

    @property
    def y(self):
        return self.plots[:, 1]

    @property
    def A(self):
        return numpy.sum(self._diff[:, 0] * self._average[:, 1])

    @property
    def G(self):
        return self.S / self.A

    @property
    def Io(self):
        return numpy.sum(self.Io_detail, axis=1)

    @property
    def Ig(self):
        return self.Io - self.A * self.G**2

    @property
    def S(self):
        return numpy.sum(self.S_detail, axis=1)
        # return numpy.prod(self._average, axis=1) @ self._diff * numpy.array([1, -1])

    @property
    def l(self):
        return numpy.sqrt(self._diff[:, 0]**2 + self._diff[:, 1]**2)

    @property
    def _diff(self):
        return numpy.roll(self.plots, -1, axis=0) - self.plots

    @property
    def _average(self):
        return self._sub_nx / 2

    @property
    def _x1y1(self):
        return numpy.prod(self.plots, axis=1)

    @property
    def _x2y2(self):
        return numpy.roll(self._x1y1, -1)

    @property
    def _x1y2(self):
        return self.plots[:, 0] * numpy.roll(self.plots[:, 1], -1)

    @property
    def _x2y1(self):
        return numpy.roll(self.plots[:, 0], -1, axis=0) * self.plots[:, 1]

    @property
    def _sq(self):
        return self.plots**2

    @property
    def _x1sq(self):
        return self._sq[:, 0]

    @property
    def _y1sq(self):
        return self._sq[:, 1]

    @property
    def _x2sq(self):
        return numpy.roll(self._x1sq, -1)

    @property
    def _y2sq(self):
        return numpy.roll(self._y1sq, -1)

    @property
    def _nx(self):
        return self.plots * numpy.roll(self.plots, -1, axis=0)

    @property
    def _sub_nx(self):
        return self.plots + numpy.roll(self.plots, -1, axis=0)

    @property
    def _x1x2(self):
        return self._nx[:, 0]

    @property
    def _y1y2(self):
        return self._nx[:, 1]

    @property
    def Iy_detail(self):
        return 1 / 4 * self._diff[:, 1] * self._sub_nx[:, 0] * (self._x2sq + self._x1sq) \
               - 1 / 3 * (self._x1y2 - self._x2y1) * (self._x1sq + self._x1x2 + self._x2sq)
        # return - 1 / 3 * (self._x1y2 - self._x2y1) * (self._x1sq + self._x1x2 + self._x2sq)\
        #        - 1 / 4 * (self._x1y1 - self._x1y2 + self._x2y1 - self._x2y2)

    @property
    def Ix_detail(self):
        return -1 * (1 / 4 * self._diff[:, 0] * self._sub_nx[:, 1] * (self._y2sq + self._y1sq)
                     + 1 / 3 * (self._x1y2 - self._x2y1) * (self._y1sq + self._y1y2 + self._y2sq))
        # return - 1 / 3 * (self._x2y1 - self._x1y2) * (self._y1sq + self._y1y2 + self._y2sq) \
        #        - 1 / 4 * (self._x1y1 + self._x1y2 - self._x2y1 - self._x2y2)

    @property
    def Io_detail(self):
        return numpy.stack([self.Ix_detail, self.Iy_detail])

    @property
    def _Sy_detail(self):
        return 1 / 3 * self._diff[:, 1] * (self._x2sq + self._x1x2 + self._x1sq) \
               - 1 / 2 * (self._x1y2 - self._x2y1) * self._sub_nx[:, 0]

    @property
    def _Sx_detail(self):
        return - 1 * (1 / 3 * self._diff[:, 0] * (self._y2sq + self._y1y2 + self._y1sq)
                      + 1 / 2 * (self._x1y2 - self._x2y1) * self._sub_nx[:, 1])

    @property
    def S_detail(self):
        return numpy.stack([self._Sx_detail, self._Sy_detail])

    def reverse(self):
        return Polygon(numpy.roll(self.plots[::-1], 1, axis=0))
