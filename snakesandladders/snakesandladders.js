function toInt(x) { return x | 0; }

function heapq() {
    this.q = [];

    // our heap logic is based on 1-based indexing, so each of these
    // operations adds 1 to the 0-based index, computes the related node
    // as 1-based index, and then subtracts 1 to get back the 0-based index.
    // IE. `2*0` would *NOT* give us the left child's position of the root.
    //     But, `2*1 - 1` does. Likewise, `2*0 + 1` does *NOT* give us the
    //     right child's position, but `(2*1 + 1) - 1` does.
    this.leftchild  = function(i) { return (2*(i+1))-1; };
    this.rightchild = function(i) { return (2*(i+1)+1)-1; };
    this.parent     = function(i) { return toInt((i+1)/2)-1; };

    this.score      = function(i) { return this.q[i][1]; };

    this.swap = function(i, j) {
        var _t = this;
        var tmp = _t.q[i];
        _t.q[i] = _t.q[j];
        _t.q[j] = tmp;
    };

    this.upheapify = function(i){
        var _t = this;
        var p = _t.parent(i);
        while(p >= 0 && _t.score(p) > _t.score(i)){
            _t.swap(p, i);
            i = p;
            p = _t.parent(i);
        }
        return i;
    };

    this.push = function(val, score){
        if(score === undefined) { throw "Undefined score."; }
        var _t = this;
        _t.q.push([val, score]);
        _t.upheapify(_t.q.length-1);
    };

    this.downheapify = function(i){
        var _t = this;
        var minchild;
        var l, r;
        // console.log("downheapify: " + _t.q);
        while(i<_t.q.length){
            l = _t.leftchild(i);
            r = _t.rightchild(i);
            if(l >= _t.q.length){
                // we are at the bottom
                return i;
            }
            // console.log("l: " + l + " i: " + i);
            if(r >= _t.q.length){
                if (_t.score(l) < _t.score(i)){
                    _t.swap(i, l);
                    i = l;
                }else{
                    return i;
                }
            }
            // both left child and right child exist
            else{
                // find the smaller valued child and move it up
                // so the invariant still holds
                minchild = _t.score(l) < _t.score(r) ? l : r;
                if(_t.score(minchild) < _t.score(i)){
                    _t.swap(i, minchild);
                    i = minchild;
                }else{
                    // con't go any farther
                    return i;
                }
            }
        }
    };

    this.pop = function(){
        var _t = this;
        // swap the last and the first value, putting the smallest value
        // at the end of the array
        var l = _t.q.length;
        _t.swap(0, l-1);
        var val = _t.q.pop();
        _t.downheapify(0);
        return val;
    };
}

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

function play(edges){
    var start = 1;
    var stop = 100;
    // console.log(edges);
    var path = dijkstra(edges, start, stop);
    // console.log(path);
    console.log(path.length-1);
}

function processData(input) {
    // console.log("Input:");
    // console.log(input);
    //Enter your code here
    var lines = input.trim().split(/\r\n|[\n\r\u0085\u2028\u2029]/g);
    // console.log("number of lines: " + lines.length);
    var trials = toInt(lines[0]);
    var i, nm, ladderedges, snakeedges, nladders, nsnakes;
    var j, edges, a, b, edge, lineno;

    if((lines.length-1) % 3 !== 0){
        console.log("Error. Invalid number of input lines.");
        process.exit(1);
    }

    lineno = 0;
    for(i=0; i<trials; i++){
        lineno++;
        edges = {};

        // first, make all the original edges possible for each spot
        // via a roll of the dice.
        for(j=1; j<=100; j++){
            // make an edge from each node to the 6 nodes ahead.
            a = j;
            if(edges[a] === undefined){ edges[a] = []; }
            for(b=a+1; b<=a+6; b++){
                if(b > 100) { break; }
                edges[a].push(b);
            }
        }

        // first line of the trial is the number of ladders and snakes
        nm = lines[lineno].trim().split(",");
        nladders = toInt(nm[0]);
        nsnakes = toInt(nm[1]);

        // console.log("nladders: " + nladders + " nsnakes: " + nsnakes);

        // next line is a list of the ladder edges
        lineno++;
        ladderedges = lines[lineno].trim().split(" ");  // first space separated

        for(j in ladderedges){
            edge = ladderedges[j].trim().split(",");   // second comma separated
            // console.log("ladderedge: " + edge);
            a = toInt(edge[0]);
            b = toInt(edge[1]);
            // all nodes that can get to a, can get directly to b
            // if(edges[a] === undefined){ edges[a] = []; }
            // edges[a].push(b);
            edges[a] = []; // ladder nodes have no edges
            for(var k = 1; k <= 100; k++){
                var idx = edges[k].indexOf(a);
                if(idx >= 0){
                    edges[k][idx] = b;
                }
            }
        }

        // next line is a list of the snake edges
        lineno++;
        snakeedges = lines[lineno].trim().split(" ");

        for(j in snakeedges){
            edge = snakeedges[j].split(',');
            // console.log("snakeedge: " + edge);
            a = toInt(edge[0]);
            b = toInt(edge[1]);
            // if(edges[a] === undefined){ edges[a] = []; }
            // edges[a].push(b);
            // edges[a] = [b];
            edges[a] = []; // snake nodes have no edges
            for(var k = 1; k <= 100; k++){
                var idx = edges[k].indexOf(a);
                if(idx >= 0){
                    edges[k][idx] = b;
                }
            }
        }
        play(edges);
    }
    process.exit(0);
}

process.stdin.resume();
process.stdin.setEncoding("ascii"); // utf8

var _input = "";

process.stdin.on("data", function (input) {
    // "data" fires on Enter key
    if(input.trim() === ""){
        processData(_input);
    }else{
        _input += input;
    }
});

process.stdin.on("end", function () {
    // An empty or no STDIN stream is detected by the 'end' event
    processData(_input);
});
