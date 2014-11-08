var heapq = require('./heapq');

/*
 * TODO: Add edge weights. For now, assumes weight of 1 for each edge.
 */
function dijkstra(edges, start, stop){
    var pred = {};      // predecessor to a node
    pred[start] = null;
    var finished = {};  // index of completed nodes (cycle protection)
    var costs = {};
    var queue = new heapq();
    var neighbors, i, v, w, cost, tmp;

    function getPath(v){
        var path = [v];
        while(v !== start && v !== undefined){
            v = pred[v];
            path.push(v);
        }
        return path.reverse();
    }

    queue.push(start, 0);
    while(queue.q.length > 0){
        // console.log(queue.q);
        tmp = queue.pop();
        v = tmp[0];
        cost = tmp[1];

        // if(v === stop){ return getPath(v); }

        neighbors = edges[v];
        for(i in neighbors){
            w = neighbors[i];
            if(!finished[w]){
                if(costs[w] === undefined || cost+1 < costs[w]){
                    costs[w] = cost+1;
                    pred[w] = v;
                    queue.push(w, cost+1);  // weight of 1 for now
                }
            }
        }
        finished[v] = true;
    }

    return getPath(stop);
}

module.exports = dijkstra;
