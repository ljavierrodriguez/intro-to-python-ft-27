// Object Oriented Programming (Programacion Orientada a Objetos)

let persona = {
    nombre: '',
    apellido: '',
    saludar(){},
    comer: () => {}
}

class Persona { // this
    nombre = ""
    apellido = ""
    edad = ""

    constructor(nombre, apellido){
        this.nombre = nombre
        this.apellido = apellido
    }

    saludar(){
        console.log("Soy una persona")
    }
    comer(){}
    hablar(){}
}

let persona1 = new Persona("John", "Doe")
let persona2 = new Persona("Jane", "Doe")
let persona3 = new Persona("Mickey", "Mouse")

console.log(person1.saludar())
console.log(person2.hablar())

class Estudiante extends Persona {
    calificaciones = []
    saludar(){
        console.log("Soy un estudiante")
    }
}

let estudiante1 = new Estudiante()
console.log(estudiante1.nombre)
console.log(estudiante1.apellido)
console.log(estudiante1.saludar())