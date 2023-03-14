/**
 *  Script de validdacion para el formulario de Confiabiilidad
 * 
 */


document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("confiabilidad_promedio_tension").readOnly = true;
    document.getElementById("confiabilidad_corrientes_promedio").readOnly = true;
    document.getElementById("promedio_angulo").readOnly = true;
});

/**
 *  Calcular el promedio de las Tensiones
 *  confiabilidad_tension_a
 *  confiabilidad_tension_b
 *  confiabilidad_tension_c
 */


document.getElementById("tipo_medida").onchange = function () {
    valor = document.getElementById("tipo_medida").value;
    if (valor == 2) {

        document.getElementById("confiabilidad_tension_b").readOnly = true;
        document.getElementById("confiabilidad_corrientes_b").readOnly = true;
        document.getElementById("angulo_ib").readOnly = true;
        document.getElementById("confiabilidad_tension_a").value = 0;
        document.getElementById("confiabilidad_tension_b").value = 0;
        document.getElementById("confiabilidad_tension_c").value = 0;
        document.getElementById("confiabilidad_promedio_tension").value = 0;
        // Corrientes
        document.getElementById("confiabilidad_corrientes_a").value = 0;
        document.getElementById("confiabilidad_corrientes_b").value = 0;
        document.getElementById("confiabilidad_corrientes_c").value = 0;
        document.getElementById("confiabilidad_corrientes_promedio").value = 0;
        // Angulos
        document.getElementById("angulo_ia").value = 0;
        document.getElementById("angulo_ib").value = 0;
        document.getElementById("angulo_ic").value = 0;
        document.getElementById("promedio_angulo").value = 0;



    } else {
        document.getElementById("confiabilidad_tension_b").readOnly = false;
        document.getElementById("confiabilidad_corrientes_b").readOnly = false;
        document.getElementById("angulo_ib").readOnly = false;
        document.getElementById("confiabilidad_tension_a").value = 0;
        document.getElementById("confiabilidad_tension_b").value = 0;
        document.getElementById("confiabilidad_tension_c").value = 0;
        document.getElementById("confiabilidad_promedio_tension").value = 0;
        // Corrientes
        document.getElementById("confiabilidad_corrientes_a").value = 0;
        document.getElementById("confiabilidad_corrientes_b").value = 0;
        document.getElementById("confiabilidad_corrientes_c").value = 0;
        document.getElementById("confiabilidad_corrientes_promedio").value = 0;
        // Angulos
        document.getElementById("angulo_ia").value = 0;
        document.getElementById("angulo_ib").value = 0;
        document.getElementById("angulo_ic").value = 0;
        document.getElementById("promedio_angulo").value = 0;

    }
}

document.getElementById("confiabilidad_tension_a").onchange = function () {
    valor = document.getElementById("tipo_medida").value;
    if (valor == 2) {
        tension_a = document.getElementById("confiabilidad_tension_a").value;
        tension_c = document.getElementById("confiabilidad_tension_c").value;
        document.getElementById("confiabilidad_tension_b").value = 0;
        if (tension_c.length == 0) {
            tension_c = 0;
        }
        promedio = (parseInt(tension_a) + parseInt(tension_c)) / 2;
        document.getElementById("confiabilidad_promedio_tension").value = promedio;
    } else {
        tension_a = document.getElementById("confiabilidad_tension_a").value;
        tension_b = document.getElementById("confiabilidad_tension_b").value;
        tension_c = document.getElementById("confiabilidad_tension_c").value;
        if (tension_b.length == 0) {
            tension_b = 0;
        }
        if (tension_c.length == 0) {
            tension_c = 0;
        }
        promedio = (parseInt(tension_a) + parseInt(tension_b) + parseInt(tension_c)) / 3
        document.getElementById("confiabilidad_promedio_tension").value = promedio
    }

}

document.getElementById("confiabilidad_tension_b").onchange = function () {
    tension_a = document.getElementById("confiabilidad_tension_a").value;
    tension_b = document.getElementById("confiabilidad_tension_b").value;
    tension_c = document.getElementById("confiabilidad_tension_c").value;
    if (tension_a.length == 0) {
        tension_a = 0;
    }
    if (tension_c.length == 0) {
        tension_c = 0;
    }
    promedio = (parseInt(tension_a) + parseInt(tension_b) + parseInt(tension_c)) / 3
    document.getElementById("confiabilidad_promedio_tension").value = promedio

}
document.getElementById("confiabilidad_tension_c").onchange = function () {
    valor = document.getElementById("tipo_medida").value;
    if (valor == 2) {
        tension_a = document.getElementById("confiabilidad_tension_a").value;
        tension_c = document.getElementById("confiabilidad_tension_c").value;
        document.getElementById("confiabilidad_tension_b").value = 0;
        if (tension_a.length == 0) {
            tension_a = 0;
        }
        promedio = (parseInt(tension_a) + parseInt(tension_c)) / 2;
        document.getElementById("confiabilidad_promedio_tension").value = promedio;
    } else {
        tension_a = document.getElementById("confiabilidad_tension_a").value;
        tension_b = document.getElementById("confiabilidad_tension_b").value;
        tension_c = document.getElementById("confiabilidad_tension_c").value;
        if (tension_b.length == 0) {
            tension_b = 0;
        }
        if (tension_c.length == 0) {
            tension_c = 0;
        }
        promedio = (parseInt(tension_a) + parseInt(tension_b) + parseInt(tension_c)) / 3
        document.getElementById("confiabilidad_promedio_tension").value = promedio
    }
}
/**
 *  Validacioon Corrientes
 */

document.getElementById("confiabilidad_corrientes_a").onchange = function () {
    valor = document.getElementById("tipo_medida").value;
    if (valor == 2) {
        corrientes_a = document.getElementById("confiabilidad_corrientes_a").value;
        corrientes_c = document.getElementById("confiabilidad_corrientes_c").value;
        if (corrientes_c.length == 0) {
            corrientes_c = 0;
        }
        promedio = (parseInt(corrientes_a) + parseInt(corrientes_c)) / 2;
        document.getElementById("confiabilidad_promedio_tension").value = promedio;
    } else {
        corriente_a = document.getElementById("confiabilidad_corrientes_a").value;
        corriente_b = document.getElementById("confiabilidad_corrientes_b").value;
        corriente_c = document.getElementById("confiabilidad_corrientes_c").value;
        if (corriente_b.length == 0) {
            corriente_b = 0;
        }
        if (corriente_c.length == 0) {
            corriente_c = 0;
        }
        promedio = (parseInt(corriente_a) + parseInt(corriente_b) + parseInt(corriente_c)) / 3;
        document.getElementById("confiabilidad_corrientes_promedio").value = promedio;
    }

}

document.getElementById("confiabilidad_corrientes_b").onchange = function () {
    corriente_a = document.getElementById("confiabilidad_corrientes_a").value;
    corriente_b = document.getElementById("confiabilidad_corrientes_b").value;
    corriente_c = document.getElementById("confiabilidad_corrientes_c").value;
    if (corriente_a.length == 0) {
        corriente_a = 0;
    }
    if (corriente_c.length == 0) {
        corriente_a = 0;
    }
    promedio = (parseInt(corriente_a) + parseInt(corriente_b) + parseInt(corriente_c)) / 3
    document.getElementById("confiabilidad_corrientes_promedio").value = promedio

}
document.getElementById("confiabilidad_corrientes_c").onchange = function () {
    valor = document.getElementById("tipo_medida").value;
    if (valor == 2) {
        corriente_a = document.getElementById("confiabilidad_corrientes_a").value;
        corriente_c = document.getElementById("confiabilidad_corrientes_c").value;
        if (corriente_a.length == 0) {
            corriente_a = 0;
        }
        promedio = (parseInt(corriente_a) + parseInt(corriente_c)) / 2;
        document.getElementById("confiabilidad_corrientes_promedio").value = promedio;
    } else {
        corriente_a = document.getElementById("confiabilidad_corrientes_a").value;
        corriente_b = document.getElementById("confiabilidad_corrientes_b").value;
        corriente_c = document.getElementById("confiabilidad_corrientes_c").value;
        if (corriente_a.length == 0) {
            corriente_a = 0;
        }
        if (corriente_b.length == 0) {
            corriente_b = 0;
        }
        promedio = (parseInt(corriente_a) + parseInt(corriente_b) + parseInt(corriente_c)) / 3
        document.getElementById("confiabilidad_corrientes_promedio").value = promedio
    }
}

/**
 * 
 *  Validacion Angulos
 * 
 */

document.getElementById("angulo_ia").onchange = function () {
    valor = document.getElementById("tipo_medida").value;
    if (valor == 2) {
        angulo_ia = document.getElementById("angulo_ia").value;
        angulo_ic = document.getElementById("angulo_ic").value;
        if (angulo_ic.length == 0) {
            angulo_ic = 0;
        }
        promedio = (parseInt(angulo_ia) + parseInt(angulo_ic)) / 2;
        document.getElementById("promedio_angulo").value = promedio;
    } else {
        angulo_ia = document.getElementById("angulo_ia").value;
        angulo_ib = document.getElementById("angulo_ib").value;
        angulo_ic = document.getElementById("angulo_ic").value;
        if (angulo_ib.length == 0) {
            angulo_ib = 0;
        }
        if (angulo_ic.length == 0) {
            angulo_ic = 0;
        }
        promedio = (parseInt(angulo_ia) + parseInt(angulo_ib) + parseInt(angulo_ic)) / 3;
        document.getElementById("promedio_angulo").value = promedio;
    }

}

document.getElementById("angulo_ib").onchange = function () {
    angulo_ia = document.getElementById("angulo_ia").value;
    angulo_ib = document.getElementById("angulo_ib").value;
    angulo_ic = document.getElementById("angulo_ic").value;
    if (angulo_ia.length == 0) {
        angulo_ia = 0;
    }
    if (angulo_ic.length == 0) {
        angulo_ic = 0;
    }
    promedio = (parseInt(angulo_ia) + parseInt(angulo_ib) + parseInt(angulo_ic)) / 3
    document.getElementById("promedio_angulo").value = promedio

}
document.getElementById("angulo_ic").onchange = function () {
    valor = document.getElementById("tipo_medida").value;
    if (valor == 2) {
        angulo_ia = document.getElementById("angulo_ia").value;
        angulo_ic = document.getElementById("angulo_ic").value;
        if (angulo_ia.length == 0) {
            angulo_ia = 0;
        }
        promedio = (parseInt(angulo_ia) + parseInt(angulo_ic)) / 2;
        document.getElementById("promedio_angulo").value = promedio;
    } else {
        angulo_ia = document.getElementById("angulo_ia").value;
        angulo_ib = document.getElementById("angulo_ib").value;
        angulo_ic = document.getElementById("angulo_ic").value;
        if (angulo_ia.length == 0) {
            angulo_ia = 0;
        }
        if (angulo_ib.length == 0) {
            angulo_ib = 0;
        }
        promedio = (parseInt(angulo_ia) + parseInt(angulo_ib) + parseInt(angulo_ic)) / 3
        document.getElementById("promedio_angulo").value = promedio
    }
}


function validacion_formulario_confiabilidad() {
    let ot = document.forms["confiabilidad_form"]["confiabilidad_OT"].value;
    let confiabilidad_tension_a = document.forms["confiabilidad_form"]["confiabilidad_tension_a"].value;
    let confiabilidad_tension_b = document.forms["confiabilidad_form"]["confiabilidad_tension_b"].value;
    let confiabilidad_tension_c = document.forms["confiabilidad_form"]["confiabilidad_tension_c"].value;
    let confiabilidad_promedio_tension = document.forms["confiabilidad_form"]["confiabilidad_promedio_tension"].value;
    let confiabilidad_corrientes_a = document.forms["confiabilidad_form"]["confiabilidad_corrientes_a"].value;
    let confiabilidad_corrientes_b = document.forms["confiabilidad_form"]["confiabilidad_corrientes_b"].value;
    let confiabilidad_corrientes_c = document.forms["confiabilidad_form"]["confiabilidad_corrientes_c"].value;
    let confiabilidad_corrientes_promedio = document.forms["confiabilidad_form"]["confiabilidad_corrientes_promedio"].value;
    let angulo_ia = document.forms["confiabilidad_form"]["angulo_ia"].value;
    let angulo_ib = document.forms["confiabilidad_form"]["angulo_ib"].value;
    let angulo_ic = document.forms["confiabilidad_form"]["angulo_ic"].value;
    let promedio_angulo = document.forms["confiabilidad_form"]["promedio_angulo"].value;
    let fechaHora = document.forms["confiabilidad_form"]["fechaHora"].value;
    let canales = document.forms["confiabilidad_form"]["validacion_canales"].value;
    let file = document.forms["confiabilidad_form"]["formFile"].value;


    // Validaciones
    if (ot.length <= 0) {
        alert("Pendiente Diligenciar Orden de Trabajo")
        return false;
    }
    if (confiabilidad_tension_a.length <= 0) {
        alert("Pendiente Diligenciar Tension A")
        return false;
    }
    if (confiabilidad_tension_b.length <= 0) {
        alert("Pendiente Diligenciar Tension B")
        return false;
    }
    if (confiabilidad_tension_c.length <= 0) {
        alert("Pendiente Diligenciar Tension C")
        return false;
    }
    if (confiabilidad_promedio_tension.length <= 0) {
        alert("Pendiente Diligenciar Promedio Tension")
        return false;
    }
    if (confiabilidad_corrientes_a.length <= 0) {
        alert("Pendiente Diligenciar Corriente A")
        return false;
    }
    if (confiabilidad_corrientes_b.length <= 0) {
        alert("Pendiente Diligenciar Corriente B")
        return false;
    }
    if (confiabilidad_corrientes_c.length <= 0) {
        alert("Pendiente Diligenciar Corriente C")
        return false;
    }
    if (confiabilidad_corrientes_promedio.length <= 0) {
        alert("Pendiente Diligenciar Promedio Corrientes")
        return false;
    }
    if (angulo_ia.length <= 0) {
        alert("Pendiente Diligenciar Angulo IA")
        return false;
    }
    if (angulo_ib.length <= 0) {
        alert("Pendiente Diligenciar Angulo IB")
        return false;
    }
    if (angulo_ic.length <= 0) {
        alert("Pendiente Diligenciar Angulo IC")
        return false;
    }
    if (promedio_angulo.length <= 0) {
        alert("Pendiente Diligenciar Promedio Angulos")
        return false;
    }
    if (fechaHora.length <= 0) {
        alert("Pendiente Diligenciar Fecha y Hora")
        return false;
    }
    if (canales.length <= 0) {
        alert("Pendiente Diligenciar Archivo Adjunto")
        return false;
    }
    if (file.length <= 0) {
        alert("Pendiente Diligenciar Archivo Adjunto")
        return false;
    }

}
