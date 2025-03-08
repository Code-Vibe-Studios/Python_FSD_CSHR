let employee = {
    name: "Mounish",
    age: 32,
    position: "Developer",
    salary: 10000
};

let info = document.getElementById("employee-details");
info.innerHTML = `Name: ${employee.name}, Age: ${employee.age}, Position: ${employee.position}, Salary: ${employee.salary}`;


