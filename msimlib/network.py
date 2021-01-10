import numpy


class NetModel:

    @classmethod
    def open_csv(cls):
        pass

    def __init__(self, node, init_value=0):
        self.values = numpy.empty(node)
        self.values[:] = init_value
        self.relation = []

    @property
    def nodes_count(self):
        return len(self.values)

    def connect(self):
        pass

    def concatenate(self):
        pass

    def set_init_value(self):
        pass
