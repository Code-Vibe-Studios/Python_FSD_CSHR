// for loop 
for (let i = 0; i < 5; i++) {
    console.log(i);
}

//while loop
let i = 0;
while (i < 5) {
    console.log(i);
    i++;
}

//do while loop
let j = 0;
do {
    console.log(j);
    j++;
} while (j < 5);

//for of loop
const arr = ["a", "b", "c"];
for (let i of arr) {
    console.log(i);
}

//for in loop
const obj = {
    name: "John",
    age: 30
};  
for (let i in obj) {
    console.log(i + ":" + obj[i]);
}