// Data Types
/* 

String
Number
Boolean
Undefined

Object: 
    Array
    Null
    Literal Object

*/

/* let const var */
/* 
let varName = value;
*/

let nombre = "John";
let apellido = 'Doe'
let nombreCompleto = `${nombre} ${apellido}`

let edad = 42
let precio = 10.50
let temp = -5.5

let users = null;
let posts;

let numeros = [1, 2, 3, 4]
//let nombres = array("Hugo", "Paco", "Luis")

//nombres[0]
numeros.push(5)
numeros.pop()

console.log(numeros)
console.log(typeof numeros)

let persona = {
    nombre: 'John',
    apellido: 'Doe'
}

console.log(persona.nombre)
console.log(persona["apellido"])

persona["edad"] = 0

console.log(persona)