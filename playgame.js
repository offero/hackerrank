/*
https://www.hackerrank.com/challenges/play-game/editorial
*/

function toInt(x) { return x | 0; }

function lineSplit(txt) {
    return txt.trim().split(/\r\n|[\n\r\u0085\u2028\u2029]/g);
}

function wsSplit(txt) {
    return txt.trim().split(/\s+/);
}

function pad(txt, n, sep) {
    if(sep === undefined){ sep = " "; }
    var val = ((new Array(n)).join(sep) + txt).slice(-n);
    // console.log("|" + val + "|");
    return val;
}

function padArray(arr, n, sep) {
    // var mlen = 0;
    var res = [];
    arr.forEach(function(x) {
        res.push(pad(x, n, sep));
    });
    return res;
}

function maxEltLen() {
    var mlen = 0;
    var y;
    var args = Array.prototype.slice.call(arguments);
    args.forEach(function(arr) {
        arr.forEach(function(x) {
            y = x.toString();
            if(y.length > mlen) { mlen = y.length; }
        });
    });
    return mlen;
}

function calcArrMax(arr){
    var rev = arr.slice().reverse();
    var arrSum = [],
        arrMaxScore = [],
        val;

    rev.reduce(function(p, c, i, a) {
        val = p+c; // sum so far
        arrSum.push(val);
        if(i===0){ arrMaxScore.push(c); }
        else if(i===1 || i===2){ arrMaxScore.push(c + arrMaxScore[i-1]); }
        else{
            arrMaxScore.push(Math.max(
                //case 1: choose 1
                c + (arrSum[i-1] - arrMaxScore[i-1]),
                //case 2: choose 2
                (c + rev[i-1]) + (arrSum[i-2] - arrMaxScore[i-2]),
                //case 3: choose 3
                (c + rev[i-1] + rev[i-2]) + (arrSum[i-3] - arrMaxScore[i-3])
            ));
        }
        return val;
    }, 0);

    arrMaxScore.reverse();
    return arrMaxScore;
}

/*
 * player = 1 for me, 2 for other.
 * call function again with the new array with our selections taken
 * return player 1's accumulated score always
 */

function play(arr, arrMaxScore, player) {
    var mlen;
    var take, minScore, i;
    var start = 1;
    var end = 3;
    var score = 0;
    var taken = 0;

    mlen = maxEltLen(arrMaxScore, arr) + 1;

    while((arr.length-taken) > 0){
        take = minScore = i = undefined;

        // console.log("Array:      " + padArray(arr, mlen).join(""));
        // console.log("Max Scores: " + padArray(arrMaxScore, mlen).join(""));
        // console.log("Sums:       " + padArray(arrSum, mlen).join(""));

        if((arr.length-taken) <= 3){
            // If there are only 3 or fewer items left, take them all!
            take = arr.length-taken;
        }else{
            // be picky about which we take; minimize the other player's possibles
            // score.
            for(i=start; i<=end; i++){
                if(minScore === undefined || arrMaxScore[taken+i] < minScore){
                    take = i;
                    minScore = arrMaxScore[taken+i];
                }
            }
        }

        // console.log("taken: " + taken);
        // console.log("take: " + take);

        if(player === 1){
            score += arr.slice(taken, taken+take).reduce(
                                    function(p, c, i, a){ return p+c; });
            // console.log("Our score: " + score);
        }

        taken += take;

        player = player === 1 ? 2 : 1;
        // arr = arr.slice(take);
        // arrMaxScore = arrMaxScore.slice(take);
    }
    return score;
}

function processData(input) {
    // console.log("Input:");
    // console.log(input);
    var lines = lineSplit(input);
    var trials = toInt(lines[0]);
    var n, arr, ans;

    lineno = 0;
    for(i=0; i<trials; i++){
        lineno++;
        // first is the number of elements
        n = toInt(lines[lineno].trim());
        // then, the list of elements
        lineno++;
        arr = [];
        wsSplit(lines[lineno]).forEach(function(x){ arr.push(toInt(x)); });
        ans = play(arr, calcArrMax(arr), 1);
        console.log(ans);
    }
    process.exit(0);
}

process.stdin.resume();
process.stdin.setEncoding("utf8"); // "ascii", "utf8"

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
