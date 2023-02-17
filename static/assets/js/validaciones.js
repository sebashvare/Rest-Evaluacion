// Variables
var informacion_data = "";
var quienReporta = "";
var actividadEjecutar = "";
var id_punto_servicio = 0;
var fuente_reporta = "";
var contrata = "";
var quienResuelve = "";

envio_informacion = document.getElementById("guardar-info");



// Funciones

function habilitarButton() {

    envio_informacion.disabled = true;
}
/*
  Deshabilitamos el boton para enviar la informacion asi estamos seguros
  que el formulario se lleno correctamente.
*/
document.addEventListener("DOMContentLoaded", function () {
    habilitarButton();
});

/*
Deshabilito el campo quien resuelve ya que dependiendo de la actividad a actividadEjecutar
esta tendra un responsable.
*/
document.getElementById("quienResuelve").disabled = true;

// Segun la actividad a ejecutar seleccionamos la el grupo encargado para que ejecute la actividad, por defecto confiiabilidad debe enterarse de la avctividad.

document.getElementById("actividadEjecutar").onchange = function () {
    actividadEjecutar = document.getElementById("actividadEjecutar").value;

    if (actividadEjecutar.length > 0) {
        document.getElementById("quienResuelve").value = "Confiabilidad";
        quienResuelve = document.getElementById("quienResuelve").value = "Confiabilidad";
        document.getElementById("quienResuelve").disabled = false;
        console.log("Actividad a Ejecutar: " + actividadEjecutar + " \nQuien Resuelve la actividad: " + quienResuelve)
    }
};
// Capturo el campo quien reporta
document.getElementById("quienReporta").onchange = function () {
    quienReporta = document.getElementById("quienReporta").value;
}
// Capturar id_punto_servicio
document.getElementById("idPuntoServicio").onchange = function () {
    id_punto_servicio = document.getElementById("idPuntoServicio").value;
    console.log(id_punto_servicio)
}

// Capturar actividad a fuente
document.getElementById("fuente").onchange = function () {
    fuente_reporta = document.getElementById("fuente").value;
}

// Capturar actividad a contrata
document.getElementById("contrata").onchange = function () {
    contrata = document.getElementById("contrata").value;
    if (quienReporta.length == 0 || idPuntoServicio.length == 0 || actividadEjecutar.length == 0 || fuente.length == 0 || contrata.length == 0 || quienResuelve.length == 0) {
        envio_informacion.disabled = true
    }
    else {
        console.log(quienReporta)
        console.log(actividadEjecutar)
        console.log(id_punto_servicio)
        console.log(fuente_reporta)
        console.log(contrata)
        console.log(quienResuelve)
        envio_informacion.disabled = false
    }
}

function validacionFormularioPlaneacion() {
    let ordenTrabajo = document.forms["formulario_planeacion"]["ot"].value;
    let origen = document.forms["formulario_planeacion"]["origen"].value;
    let contrata = document.forms["formulario_planeacion"]["contrata"].value;
    if (ordenTrabajo.length <= 0) {
        document.getElementById("mensajeValidacionOT").innerHTML = "* Pendiente por diligenciar"
        return false;
    } else {
        document.getElementById("mensajeValidacionOT").innerHTML = ""
        if (origen.length <= 0) {
            document.getElementById("mensajeValidacionOrigen").innerHTML = "* Pendiente por diligenciar"
            return false;
        } else {
            document.getElementById("mensajeValidacionOrigen").innerHTML = ""
            if (contrata.length <= 0) {
                document.getElementById("mensajeValidacionContrata").innerHTML = "* Pendiente por diligenciar"
                return false;
            }
        }
    }

}

function validacion_formulario_hacer() {
    let ordenTrabajo = document.forms["hacer"]["orden_OT"].value;
    let actividad_ejecutada = document.forms["hacer"]["actividad_ejecutada"].value;
    let numero_formato = document.forms["hacer"]["numero_formato"].value;
    let multiplo = document.forms["hacer"]["multiplo"].value;
    let fecha_telemedida = document.forms["hacer"]["fecha_telemedida"].value;
    let actualizacion_sistema = document.forms["hacer"]["actualizacion_sistema"].value;
    let pago_actividad = document.forms["hacer"]["pago_actividad"].value;


    if (ordenTrabajo.length <= 0) {
        alert("Pendiente Diligenciar Orden de Trabajo")
        return false;
    }
    if (actividad_ejecutada.length <= 0) {
        alert("Pendiente Diligenciar Actividad Ejecutada")
        return false;
    }

    if (numero_formato.length <= 0) {
        alert("Pendiente Diligenciar Numero de Formato")
        return false;
    }
    if (multiplo.length <= 0) {
        alert("Pendiente Diligenciar multiplo")
        return false;
    }
    if (fecha_telemedida.length <= 0) {
        alert("Pendiente Diligenciar ultima fecha telemedida")
        return false;
    }
    if (actualizacion_sistema.length <= 0) {
        alert("Pendiente Diligenciar actualizacion sistema")
        return false;
    }
    if (pago_actividad.length <= 0) {
        alert("Pendiente Diligenciar pago actividad")
        return false;
    }

}



function validacion_formulario_evaluacion(){
    let ot = document.forms["pruebas"]["orde_OT_eva"].value;
    let primera_factura = document.forms["pruebas"]["primera_factura"].value;
	let fecha_telemedida = document.forms["pruebas"]["fecha_telemedida"].value;
	let conforme = document.forms["pruebas"]["conforme"].value;
    if (ot.length <= 0) {
        alert("Pendiente Diligenciar Orden de Trabajo")
        return false;
    }
    if (primera_factura.length <= 0) {
        alert("Pendiente Diligenciar Primera Factura")
        return false;
    }
    if (fecha_telemedida.length <= 0) {
        alert("Pendiente Diligenciar Fecha Telemedida")
        return false;
    }
    if (conforme.length <= 0) {
        alert("Pendiente Diligenciar campo conforme")
        return false;
    }
}