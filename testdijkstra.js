var dijkstra = require('./dijkstra');
var edges, path;

edges = {
    0: [1],
    1: [2, 3, 4],
    2: [],
    3: [5, 6],
    4: [],
    5: [],
    6: [5]
};
path = dijkstra(edges, 0, 5);
console.log(path);
path = dijkstra(edges, 0, 6);
console.log(path);

edges = {
    0: [1],
    1: [2, 3, 4, 6],
    2: [],
    3: [5, 6],
    4: [],
    5: [],
    6: [5]
};
path = dijkstra(edges, 0, 5);
console.log(path);
path = dijkstra(edges, 0, 6);
console.log(path);
