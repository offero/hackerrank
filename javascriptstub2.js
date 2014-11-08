var readline = require('readline');

var rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.on('line', function (cmd) {
  console.log('You just typed: '+cmd);
  rl.prompt(); // continue the prompt
});

rl.on("close", function() {
    process.exit(0);
});

// rl.question("", function(answer) {
//   // TODO: Log the answer in a database
//   console.log("Thank you for your valuable feedback:", answer);

//   rl.close();
// });

rl.prompt(); // ask the user for input
