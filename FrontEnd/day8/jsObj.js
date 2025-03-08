let person = {
    name: "John",
    age: 30,
    city: "New York",

    start : function(){
        console.log("I am starting");
    }
};

console.log(person); // prints complete obj
console.log(person.name); // prints "John"

person["name"] = "Jane";  // change the value of "name" key

delete person.city;  // delete the "city" key

person.start(); // call the "start" method