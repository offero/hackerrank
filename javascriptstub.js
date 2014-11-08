function processData(input) {
    //Enter your code here
}

process.stdin.resume();
process.stdin.setEncoding("ascii"); // utf8

var _input = "";

process.stdin.on("data", function (input) {
    // "data" fires on Enter key
    _input += input;
});

process.stdin.on("end", function () {
    // An empty or no STDIN stream is detected by the 'end' event
    processData(_input);
});
