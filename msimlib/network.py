import numpy


class NetModel:

    @classmethod
    def open_csv(cls):
        # TODO: csv読み込みの定義
        pass

    @classmethod
    def by_node_names(cls, name_list):

        # TODO: list以外のエラー処理の追加
        if type(name_list) is not list:
            raise ValueError('not list')

        model = NetModel(len(name_list))
        model.names = name_list
        return model

    def __init__(self, node, init_value=0):
        self.values = numpy.empty(node)
        self.set_init_value(init_value)
        self.relation = []
        self.names = ['NoName' for i in range(node)]

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

    def set_init_value(self, values):
        self.values[:] = values
