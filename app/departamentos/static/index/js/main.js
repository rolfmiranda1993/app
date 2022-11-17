/*$( document ).ready(function() {
    // Handler for .ready() called.
    alert('Todo bien');
  });*/


function eliminarEquipo(id) {
  document.getElementById("id_equipo_eliminar").value = id;
}

function eliminarArea(id) {
  document.getElementById("id_area_eliminar").value = id;
}

function marcarBajado(id) {
  document.getElementById("id_trabajo_materiales").value = id;
}

function editarEquipo(id, area, codigo, descripcion) {
  document.getElementById("id_equipo_editar").value = id;
  document.getElementById("area_editar").value = area;
  document.getElementById("codigo_editar").value = codigo;
  document.getElementById("descripcion_editar").value = descripcion;
}

function editarProduct(id, precio, descripcion, costo, cantidad, categoria, servicio) {
  document.getElementById("id_producto_editar").value = id;
  document.getElementById("precio_editar").value = precio;
  document.getElementById("descripcion_editar").value = descripcion;
  document.getElementById("costo_editar").value = costo;
  document.getElementById("cantidad_editar").value = cantidad;
  document.getElementById("categoria_editar").value = categoria;
  if (servicio=='True'){
    document.getElementById('servicio_editar').checked=true;
  }
}

function historialPreventivo(id,solicitadoh,supervisado,responsable, subtotalpiezas, subtotalmo, fecha) {
  
  document.getElementById("hist_preventivo_editar").value = id;
  document.getElementById("hist_solicitadoh").value = solicitadoh;
  document.getElementById("hist_supervisadoh").value = supervisado;
  document.getElementById("hist_responsable").value = responsable;
  document.getElementById("hist_subtotalpiezas").value = subtotalpiezas;
  document.getElementById("hist_subtotalmo").value = subtotalmo;
  document.getElementById("hist_fecha_programada_editar").value = fecha;
}

function editarPreventivo(id, fecha, contacto, piezas, actividades, comentarios, total) {
  
  document.getElementById("id_preventivo_editar").value = id;
  document.getElementById("fecha_editar").value = fecha;
  document.getElementById("contacto_editar").value = contacto;
  document.getElementById("actividades_editar").value = actividades;
  document.getElementById("comentarios_editar").value = comentarios;
  document.getElementById("piezas_editar").value = piezas;
  document.getElementById("total_editar").value = total;
}

function editarCorrectivo(id, equipo, fecha, solicitado, estado, responsable, actividades, subtotalmo, supervisado, falla) {
  
  document.getElementById("id_correctivo_editar").value = id;
  document.getElementById("equipo_editar").value = equipo;
  document.getElementById("fecha_editar").value = fecha;
  document.getElementById("actividades_editar").value = actividades;
  document.getElementById("solicitadoc_editar").value = solicitado;
  document.getElementById("estado_editar").value = estado;
  document.getElementById("responsablec_editar").value = responsable;
  document.getElementById("subtotalmo_editar").value = subtotalmo;
  document.getElementById("supervisadoc_editar").value = supervisado;
  document.getElementById("falla_editar").value = falla;
}

function eliminarCorrectivo(id) {
  document.getElementById("id_correctivo_eliminar").value = id;
}

function historialCorrectivo(id,solicitadoh,supervisado,responsable, subtotalpiezas, subtotalmo, fecha) {
  
  document.getElementById("hist_correctivo_editar").value = id;
  document.getElementById("hist_solicitadoh").value = solicitadoh;
  document.getElementById("hist_supervisadoh").value = supervisado;
  document.getElementById("hist_responsable").value = responsable;
  document.getElementById("hist_subtotalpiezas").value = subtotalpiezas;
  document.getElementById("hist_subtotalmo").value = subtotalmo;
  document.getElementById("hist_fecha_programada_editar").value = fecha;
}

function eliminarPreventivo(id) {
  document.getElementById("id_preventivo_eliminar").value = id;
}

function eliminarProducto(id) {
  document.getElementById("id_producto_eliminar").value = id;
}

function editarPersonal(id,nombre_usuario, contraseña, rol, vinculacion,tipo_usuario) {
  document.getElementById("id_personal_editar").value = id;
  document.getElementById("nombre_usuario_editar").value = nombre_usuario;
  document.getElementById("contraseña_editar").value = contraseña;
  document.getElementById("rol_editar").value = rol;
  document.getElementById("vinculacion_editar").value = vinculacion;
  document.getElementById("tipo_usuario_editar").value = tipo_usuario;
}

function editarMiembro(id,nombres,apellidos,numero_de_documento,fecha_de_nacimiento,telefono_particular,telefono_corporativo,mail_particular,mail_corporativo,fecha_de_ingreso,fecha_de_salida,motivo_de_salida,cargo,notas_adicionales,contribuyente_set,estado_civil,hijos,genero) {
  document.getElementById("id_personal_editar").value = id;
  document.getElementById("nombre_editar").value = nombres;
  document.getElementById("apellido_editar").value = apellidos;
  document.getElementById("numero_de_documento_editar").value = numero_de_documento;
  document.getElementById("fecha_de_nacimiento_editar").value = fecha_de_nacimiento;
  document.getElementById("telefono_particular_editar").value = telefono_particular;
  document.getElementById("telefono_corporativo_editar").value = telefono_corporativo;
  document.getElementById("mail_particular_editar").value = mail_particular;
  document.getElementById("mail_corporativo_editar").value = mail_corporativo;
  document.getElementById("fecha_de_ingreso_editar").value = fecha_de_ingreso;
  document.getElementById("fecha_de_salida_editar").value = fecha_de_salida;
  document.getElementById("motivo_de_salida_editar").value = motivo_de_salida;
  document.getElementById("cargo_editar").value = cargo;
  document.getElementById("notas_adicionales_editar").value = notas_adicionales;
  document.getElementById("contribuyente_set_editar").value = contribuyente_set;
  document.getElementById("estado_civil_editar").value = estado_civil;
  document.getElementById("hijos_editar").value = hijos;
  document.getElementById("genero_editar").value = genero;
}

function editarCliente(id,nombre_de_la_empresa,numero_de_ruc,nombre_del_nexo,telefono_del_nexo,mail_del_nexo,nombre_contacto_pagos,telefono_contacto_pagos,mail_contacto_pagos,fecha_de_vinculacion,notas_adicionales,forma_de_pago_habitual,banco,titular_de_la_cuenta,tipo_de_cuenta,numero_de_cuenta,documento_de_cuenta) {
  document.getElementById("id_personal_editar").value = id;
  document.getElementById("nombre_de_la_empresa_editar").value = nombre_de_la_empresa;
  document.getElementById("numero_de_ruc_editar").value = numero_de_ruc;
  document.getElementById("nombre_del_nexo_editar").value = nombre_del_nexo;
  document.getElementById("telefono_del_nexo_editar").value = telefono_del_nexo;
  document.getElementById("mail_del_nexo_editar").value = mail_del_nexo;
  document.getElementById("nombre_contacto_pagos_editar").value = nombre_contacto_pagos;
  document.getElementById("telefono_contacto_pagos_editar").value = telefono_contacto_pagos;
  document.getElementById("mail_contacto_pagos_editar").value = mail_contacto_pagos;
  document.getElementById("fecha_de_vinculacion_editar").value = fecha_de_vinculacion;
  document.getElementById("notas_adicionales_editar").value = notas_adicionales;
  document.getElementById("forma_de_pago_habitual_editar").value = forma_de_pago_habitual;
  document.getElementById("banco_editar").value = banco;
  document.getElementById("titular_de_la_cuenta_editar").value = titular_de_la_cuenta;
  document.getElementById("tipo_de_cuenta_editar").value = tipo_de_cuenta;
  document.getElementById("numero_de_cuenta_editar").value = numero_de_cuenta;
  document.getElementById("documento_de_cuenta_editar").value = documento_de_cuenta;
}

function editarRubro(id, area, nombre) {
  document.getElementById("id_personal_editar").value = id;
  document.getElementById("area_editar").value = area;
  document.getElementById("nombre_editar").value = nombre;
}

function editarDepartamento(id, nombre, jerarquia) {
  document.getElementById("id_personal_editar").value = id;
  document.getElementById("nombre_editar").value = nombre;
  document.getElementById("jerarquia_editar").value = jerarquia;
}

function editarTarea(id,nombre,descrpcion,fecha_entrega,hora_entrega,responsable) {
  document.getElementById("id_personal_editar").value = id;
  document.getElementById("nombre_editar").value = nombre;
  document.getElementById("descripcion_editar").value = descrpcion;
  document.getElementById("fecha_entrega_editar").value = fecha_entrega;
  document.getElementById("hora_entrega_editar").value = hora_entrega;
  document.getElementById("responsable_editar").value = responsable;
}

function editarEgreso(id,rubro,forma_de_pago,tipo_de_pago,nombre_de_pago,titular_de_pago,monto_de_pago,responsable) {
  document.getElementById("id_personal_editar").value = id;
  document.getElementById("rubro_editar").value = rubro;
  document.getElementById("forma_de_pago_editar").value = forma_de_pago;
  document.getElementById("tipo_de_pago_editar").value = tipo_de_pago;
  document.getElementById("nombre_de_pago_editar").value = nombre_de_pago;
  document.getElementById("titular_de_pago_editar").value = titular_de_pago;
  document.getElementById("monto_de_pago_editar").value = monto_de_pago;
  document.getElementById("responsable_editar").value = responsable;
}

function editarIngreso(id,rubro,forma_de_pago,tipo_de_cobro,nombre_de_pago,titular_de_pago,monto_de_pago,responsable) {
  document.getElementById("id_personal_editar").value = id;
  document.getElementById("rubro_editar").value = rubro;
  document.getElementById("forma_de_pago_editar").value = forma_de_pago;
  document.getElementById("tipo_de_cobro_editar").value = tipo_de_cobro;
  document.getElementById("nombre_de_pago_editar").value = nombre_de_pago;
  document.getElementById("titular_de_pago_editar").value = titular_de_pago;
  document.getElementById("monto_de_pago_editar").value = monto_de_pago;
  document.getElementById("responsable_editar").value = responsable;
}

function eliminarPersonal(id) {
  document.getElementById("id_personal_eliminar").value = id;
}

function borrarContent(){
  document.getElementById("search").value = "";
}

function seleccionarCliente(id, nombre){
 document.getElementById("id_cliente").value = id;
 document.getElementById("cliente").value = nombre;
}

function activarEspera(){
  const btn = document.getElementById("btn");
  btn.innerHTML = 'Generando ... <span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>';
  btn.disabled = true;
}

$(document).ready(function () {

  $('#myTable').DataTable({
    "language": {
      "url": "../static/index/js/idiom.json"},
    "lengthMenu": [[10, 25, 50], [10, 25, 50]],
    dom: 'Bfrtip',
    buttons: [
      { extend: 'csv' },
      { extend: 'print'},
    ]
  });
  $('#table2').DataTable({
    "language": {
      "url": "../static/index/js/idiom.json"},
    "lengthMenu": [[10, 25, 50], [10, 25, 50]],
    dom: 'Bfrtip',
    buttons: [
      { extend: 'csv' },
      { extend: 'print'},
    ]
  });
  $('#table3').DataTable({
    "language": {
      "url": "../static/index/js/idiom.json"},
    "lengthMenu": [[10, 25, 50], [10, 25, 50]],
    dom: 'Bfrtip',
    buttons: [
      { extend: 'csv' },
      { extend: 'print'},
    ]
  });
});
 