from typing import Hashable, List
import matplotlib.pyplot as plt
import networkx as nx


def dfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Функция выполняет обход в глубину и возвращает список узлов в порядке посещения.
    В данной задаче порядок обхода графа левосторонний или правосторонний не важен,
    главное соблюсти порядок обхода в ширину.

    :param g: Граф NetworkX, по которому нужно совершить обход
    :param start_node: Стартовый узел, откуда нужно начать обход
    :return: Список узлов в порядке посещения.
    """
    ...  # TODO реализовать обход в глубину

    visited = {node: False for node in g.nodes}
    path = []

    def rec_dfs(current_node):

        visited[current_node] = True
        path.append(current_node)

        for neighbor in g.neighbors(current_node):
            if not visited[neighbor]:
                rec_dfs(neighbor)

    rec_dfs(start_node)

    return path







if __name__ == '__main__':

    graph = nx.Graph()
    graph.add_nodes_from("ABCDEFG")
    graph.add_edges_from([('A', 'B'),
                         ('A', 'C'),
                         ('C', 'F'),
                          ('B', 'E'),
                          ('E', 'G'),
                          ('B', 'D'),
                          ])
    #
    # nx.draw(graph, with_labels=True, font_weight='bold')
    # plt.show()
# print(dfs(graph,'A'))
