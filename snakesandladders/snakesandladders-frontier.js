function toInt(x) { return x | 0; }

// function objContains(ob, x) { return ob[x] === true; }
function objContains(ob, x) { return ob[x] !== undefined; }

function findsteps(edges, start, stop) {
    var V = {};
    var F = {};
    var Fnew;
    var i, j, v;
    F[start] = true;
    var steps = 0;
    while(!objContains(F, stop)) {
        steps++;
        Fnew = {};
        // console.log(F);
        for(i in F){ if(F.hasOwnProperty(i)) {
            i = toInt(i);
            if(i === stop){ return steps; }
            V[i] = true;  // visit node
            // set the new frontier
            for(j=1; j<=6; j++) {
                v = i+j;
                // don't go past the end
                if(v > 100){ break; }
                // move through a ladder/snake
                if(objContains(edges, v)) { v = edges[v]; }
                // if we have yet to visit this node, add it to the next fontier
                if(!objContains(V, v)){ Fnew[v] = true; }
            }
        }}
        F = Fnew;
    }
    return steps;
}

function play(edges){
    var start = 1;
    var stop = 100;
    // console.log(edges);
    var nsteps = findsteps(edges, start, stop);
    console.log(nsteps);
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
        console.log("lines: " + lines.length);
        console.log("trials: " + trials);
        for(i in lines){
            console.log(lines[i]);
        }
        process.exit(1);
    }

    lineno = 0;
    for(i=0; i<trials; i++){
        lineno++;
        edges = {};

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
            a = toInt(edge[0]);
            b = toInt(edge[1]);
            edges[a] = b;
        }

        // next line is a list of the snake edges
        lineno++;
        snakeedges = lines[lineno].trim().split(" ");

        for(j in snakeedges){
            edge = snakeedges[j].split(',');
            a = toInt(edge[0]);
            b = toInt(edge[1]);
            edges[a] = b;
        }
        play(edges);
    }
    process.exit(0);
}

/*
var fs = require('fs');
var _input = fs.readFileSync('snakesandladders.1.txt',
                             {encoding: 'ascii'});
processData(_input);
*/

process.stdin.resume();
process.stdin.setEncoding("ascii"); // utf8

var _input = "";

process.stdin.on("data", function (input) {
    // "data" fires on Enter key
    // console.log("Data: " + input);
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
