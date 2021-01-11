import numpy


def model_concat(model1, model2):
    new_model = NetModel.by_node_names(model1.names + model2.names)
    shift_relation_arr = numpy.array(model2.relation) + model1.nodes_count
    new_model.relation = model1.relation + shift_relation_arr.tolist()
    return new_model


class NetModel:

    @classmethod
    def open_csv(cls):
        # TODO: csv読み込みの定義
        pass

    @classmethod
    def by_node_names(cls, name_list):
        if type(name_list) is not list:
            raise ValueError('not list')

        model = NetModel(len(name_list))
        model.names = name_list
        return model

    @classmethod
    def by_name_and_sub(cls, name='NoName', n=3):
        return NetModel.by_node_names([f'{name}_{sub}' for sub in range(n)])

    def __init__(self, node, init_value=0):
        self.values = numpy.empty(node)
        self.set_init_value(init_value)
        self.relation = []
        self.names = ['NoName' for i in range(node)]

    def __add__(self, other):
        return self.concat(other)

    @property
    def nodes_count(self):
        return len(self.values)

    @property
    def edge_count(self):
        return len(self.relation)

    @property
    def relation_array(self):
        if self.edge_count == 0:
            return numpy.array([])
        arr = numpy.zeros((self.edge_count, self.nodes_count))
        for i, relation in enumerate(self.relation):
            arr[i][relation[0]] = -1
            arr[i][relation[1]] = 1
        return arr

    def is_name_unique(self):
        if len(set(self.names)) == len(self.names):
            return True
        return False

    def is_relation_exist(self, relation: list):
        try:
            self.relation.index(relation)
        except ValueError:
            return False
        else:
            return True

    def connect(self, relation: list):
        if not self.is_name_unique():
            raise ValueError('node name is not unique')
        num_relation = [self.names.index(name) for name in relation]
        if self.is_relation_exist(num_relation):
            raise ValueError('relation is already existing')
        self.relation.append(num_relation)

    def concat(self, model2):
        return model_concat(self, model2)

    def set_init_value(self, values):
        self.values[:] = values

    def delta(self):
        return numpy.dot(self.relation_array, self.values)

    def check_relation(self):
        return [[self.names[relation[0]], self.names[relation[1]]] for relation in self.relation]
