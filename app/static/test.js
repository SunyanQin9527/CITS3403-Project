var numberOfStudentsRemove = 0;

function sayHi(){
    alert("Hi1");
    alert("Hi2");
}

function factorial(n){
    let rec = n * factorial(n-1);
    return n * rec;
}

function removesStudent() {
    // Update the database
    numberOfStudentsRemove += 2;
    showNumberOfStudentsRemoved();
  }
  
function showNumberOfStudentsRemoved() {
    let result = prompt("Give me a number", 7);
    console.log("Result: " + result);
  }


