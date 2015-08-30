var sum = 0;
var i;

for (i = 2; i < process.argv.length; i++) {
    sum += +process.argv[i];
}

console.log(sum);
