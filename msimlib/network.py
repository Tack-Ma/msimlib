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

    @property
    def edge_count(self):
        return len(self.relation)

    @property
    def relation_array(self):
        arr = numpy.zeros((self.edge_count, self.nodes_count))
        for i, relation in enumerate(self.relation):
            arr[i][relation[0]] = -1
            arr[i][relation[1]] = 1
        return arr

    def connect(self, relation: list):
        self.relation.append(relation)

    def concatenate(self):
        pass

    def set_init_value(self):
        pass
