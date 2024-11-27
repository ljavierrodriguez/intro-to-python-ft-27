// Loops
/* 

for(counter; condition; increment){
    codigo
}

for(indice in collection){
    codigo
}

for(value of collection){
    codigo
}

while(condition){
    codigo
}

do {
    codigo
} while (condition)


*/

let numeros = [1, 2, 3, 4]

for(let i = 1; i <= 10; i++){
    console.log(i)
}

for(let indice in numeros){
    console.log(indice) // 0 1 2 3
}

for(let value of numeros){
    console.log(value) // 1 2 3 4
}


let i = 1;
while (i <= 10){
    console.log(i)
    i++
}