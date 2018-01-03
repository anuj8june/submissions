var data = [0, 1, 2, 'stop', 2, 0, 1, 'stop']
for(var i = data.length - 1; i >= 0; i--) {
    if(data[i] == 0) {
       data.splice(i, 1);
    }
}
console.log(data)