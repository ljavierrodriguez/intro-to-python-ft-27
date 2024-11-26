// Functions

/* 

Funciones Declarativas
--------------------------
*/
function saludar(){
    console.log("Hola")
}

saludar()

/* 
Funciones Expresivas
--------------------------- 
*/

const saludar = function(){
    console.log("Hola")
}


saludar();


/* 
Funciones Flecha
---------------------------- 
*/

const saludar = () => {
    console.log("Hola")
}

saludar();

/* 
Funcion Anidada
---------------------------
 */

function exterior(){
    let nombre = "John Doe";

    function interior(){
        console.log(`Hola, ${nombre}`)
    }

    interior()
}

exterior()

/* Parametros */


function sumar(a, b = 10){
    return a + b
}

sumar(10) // 20
sumar(5, 15) // 20