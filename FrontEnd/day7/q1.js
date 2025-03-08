function add(a,b){
    return a + b;
}

console.log(add(8,3));

for(let i = 0; i < 11; i++){
    if(i%2==0){
        console.log(i);
    }
}


const numbers = [12,34,5,645,2,34545,346,36345,363,3426,536,3567,56,2,52,43,4124];
console.log(Math.max(...numbers));
