var heapq = require("./heapq");

var hq = new heapq();
hq.push(1, 1);
hq.push(2, 2);
hq.push(3, 3);
console.log(hq.q);

hq.pop();

console.log(hq.q);
