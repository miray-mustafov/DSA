def createGraph(projects, dependencies):
    projectGraph = {}
    for project in projects:
        projectGraph[project] = []
    for pair in dependencies:
        projectGraph[pair[0]].extend(pair[1])
    return projectGraph


projects = ['a', 'b', 'c', 'd', 'e', 'f']
dependencies = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]

my_graph = createGraph(projects, dependencies)


def getProjectsWithDependancies(graph):
    prwithdep = set()
    for project in graph:
        prwithdep = prwithdep.union(graph[project])
    return prwithdep



def findBuildOrder(graph, projects):
    dependant = getProjectsWithDependancies(graph)
    build_order = []
    while dependant:
        for pr in projects:
            if pr not in dependant and pr in graph:
                graph.pop(pr)
                build_order.append(pr)
        dependant = getProjectsWithDependancies(graph)
    for key in graph.keys():
        build_order.append(key)
    return build_order

print(findBuildOrder(my_graph, projects))
