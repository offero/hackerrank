process.stdin.resume();

process.stdin.setEncoding("utf8");

process.stdin.on("data", function(input) {
    console.log("Data: " + input.trim());
});

process.stdin.on("end", function() {
    // fires on EOF
    console.log("END");
});
