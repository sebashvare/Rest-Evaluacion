from datetime import date
from django.urls import reverse
from rest_framework.decorators import api_view
from .serializer import HacerSerializer, PlaneacionSerializer
from rest_framework import viewsets
from .models import Hacer, Planeacion, Backlog, Evaluacion
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
import planeacion.variables as var

"""
Librerias EMAIL
"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class getPlaneacion(viewsets.ModelViewSet):
    queryset = Planeacion.objects.all()
    serializer_class = PlaneacionSerializer


class getHacer(viewsets.ModelViewSet):
    queryset = Hacer.objects.all()
    serializer_class = HacerSerializer


def listPlaneacion(request):
    listado_planeacion = Planeacion.objects.all()
    return render(request, "planeacion/list_planeacion.html", {"data": listado_planeacion})


def list_backlog(request):
    data = Backlog.objects.all()
    return render(request, "eventos/listar_eventos.html", {"data": data})


def list_backlog_json(request):
    data = Backlog.objects.all()
    json = serializers.serialize('json', data)
    return HttpResponse(json, content_type='application/json')


def registrar_eventos(request):
    return render(request, "eventos/registrar_eventos.html", {})


def save_eventos(request):

    if request.method == "POST":
        quienReporta = request.POST.get("quienReporta")
        print(quienReporta)
        idPuntoServicio = request.POST.get("idPuntoServicio")
        actividadEjecutar = request.POST.get("actividadEjecutar")
        fuente = request.POST.get("fuente")
        contrata = request.POST.get("contrata")
        quienResuelve = request.POST.get("quienResuelve")
        resultado_inicial = Backlog.objects.filter(
            id_punto_servicio=idPuntoServicio, estado="Pendiente")
        if not resultado_inicial:
            data = Backlog(
                fuente=quienReporta,
                reporte=actividadEjecutar,
                id_punto_servicio=idPuntoServicio,
                ejecucion=fuente,
                responsable=quienResuelve,
                contrata=contrata
            )
            data.save()
            data = Backlog.objects.all()
            agregado = "OK"
            return render(request, "eventos/listar_eventos.html", {"data": data, "info": agregado})
        else:
            data = Backlog.objects.all()
            agregado = "ERROR"
            return render(request, "eventos/listar_eventos.html", {"data": data, "info": agregado})


def registrar_planeacion(request):
    return render(request, "planeacion/formulario_planeacion.html", {})


def save_planeacion(request):
    resultado = ""

    if request.method == "POST":
        orden_ot = request.POST.get("ot")
        origen = request.POST.get("origen")
        contrata = request.POST.get("contrata")
        resultado_inicial = Planeacion.objects.filter(pk=orden_ot)
        if not resultado_inicial:
            data = Planeacion.objects.create(
                orden_trabajo=orden_ot,
                fuente=origen,
                contrata=contrata,
                fecha_programacion=date.today(),
                estado="PENDIENTE"
            )
            data.save()
            informacion_total = Planeacion.objects.all()
            resultado = "Se guardo la OT {} de manera correcta.".format(
                orden_ot)
            """
                ===================================================
                    Envio EMAIL de confirmacion de la OT
                ===================================================
            """
            mail_body = '''
            <!DOCTYPE html>

<html lang="en" xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:v="urn:schemas-microsoft-com:vml">

<head>
	<title></title>
	<meta content="text/html; charset=utf-8" http-equiv="Content-Type" />
	<meta content="width=device-width, initial-scale=1.0" name="viewport" />
	<!--[if mso]><xml><o:OfficeDocumentSettings><o:PixelsPerInch>96</o:PixelsPerInch><o:AllowPNG/></o:OfficeDocumentSettings></xml><![endif]-->
	<style>
		* {
			box-sizing: border-box;
		}

		body {
			margin: 0;
			padding: 0;
		}

		a[x-apple-data-detectors] {
			color: inherit !important;
			text-decoration: inherit !important;
		}

		#MessageViewBody a {
			color: inherit;
			text-decoration: none;
		}

		p {
			line-height: inherit
		}

		.desktop_hide,
		.desktop_hide table {
			mso-hide: all;
			display: none;
			max-height: 0px;
			overflow: hidden;
		}

		@media (max-width:660px) {
			.desktop_hide table.icons-inner {
				display: inline-block !important;
			}

			.icons-inner {
				text-align: center;
			}

			.icons-inner td {
				margin: 0 auto;
			}

			.image_block img.big,
			.row-content {
				width: 100% !important;
			}

			.mobile_hide {
				display: none;
			}

			.stack .column {
				width: 100%;
				display: block;
			}

			.mobile_hide {
				min-height: 0;
				max-height: 0;
				max-width: 0;
				overflow: hidden;
				font-size: 0px;
			}

			.desktop_hide,
			.desktop_hide table {
				display: table !important;
				max-height: none !important;
			}
		}
	</style>
</head>

<body style="background-color: #f8f8f9; margin: 0; padding: 0; -webkit-text-size-adjust: none; text-size-adjust: none;">
	<table border="0" cellpadding="0" cellspacing="0" class="nl-container" role="presentation"
		style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #f8f8f9;" width="100%">
		<tbody>
			<tr>
				<td>
					<table align="center" border="0" cellpadding="0" cellspacing="0" class="row row-1"
						role="presentation"
						style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #1aa19c;" width="100%">
						<tbody>
							<tr>
								<td>
									<table align="center" border="0" cellpadding="0" cellspacing="0"
										class="row-content stack" role="presentation"
										style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000000; background-color: #1aa19c; width: 640px;"
										width="640">
										<tbody>
											<tr>
												<td class="column column-1"
													style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; padding-top: 0px; padding-bottom: 0px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"
													width="100%">
													<table border="0" cellpadding="0" cellspacing="0"
														class="divider_block block-1" role="presentation"
														style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"
														width="100%">
														<tr>
															<td class="pad">
																<div align="center" class="alignment">
																	<table border="0" cellpadding="0" cellspacing="0"
																		role="presentation"
																		style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"
																		width="100%">
																		<tr>
																			<td class="divider_inner"
																				style="font-size: 1px; line-height: 1px; border-top: 4px solid #1AA19C;">
																				<span> </span></td>
																		</tr>
																	</table>
																</div>
															</td>
														</tr>
													</table>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
					<table align="center" border="0" cellpadding="0" cellspacing="0" class="row row-2"
						role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
						<tbody>
							<tr>
								<td>
									<table align="center" border="0" cellpadding="0" cellspacing="0"
										class="row-content stack" role="presentation"
										style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #fff; color: #000000; width: 640px;"
										width="640">
										<tbody>
											<tr>
												<td class="column column-1"
													style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; padding-top: 0px; padding-bottom: 0px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"
													width="100%">
													<table border="0" cellpadding="0" cellspacing="0"
														class="divider_block block-1" role="presentation"
														style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"
														width="100%">
														<tr>
															<td class="pad"
																style="padding-bottom:12px;padding-top:60px;">
																<div align="center" class="alignment">
																	<table border="0" cellpadding="0" cellspacing="0"
																		role="presentation"
																		style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"
																		width="100%">
																		<tr>
																			<td class="divider_inner"
																				style="font-size: 1px; line-height: 1px; border-top: 0px solid #0000000;">
																				<span> </span></td>
																		</tr>
																	</table>
																</div>
															</td>
														</tr>
													</table>
													<table border="0" cellpadding="0" cellspacing="0"
														class="image_block block-2" role="presentation"
														style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"
														width="100%">
														<tr>
															<td class="pad"
																style="padding-left:40px;padding-right:40px;width:100%;">
																<div align="center" class="alignment"
																	style="line-height:10px"><img alt="I'm an image"
																		class="big"
																		src="https://images.unsplash.com/photo-1543489816-c87b0f5f7dd4?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80"
																		style="display: block; height: auto; border: 0; width: 640px; max-width: 100%;"
																		title="I'm an image" width="640" /></div>
															</td>
														</tr>
													</table>
													<table border="0" cellpadding="0" cellspacing="0"
														class="divider_block block-3" role="presentation"
														style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"
														width="100%">
														<tr>
															<td class="pad" style="padding-top:50px;">
																<div align="center" class="alignment">
																	<table border="0" cellpadding="0" cellspacing="0"
																		role="presentation"
																		style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"
																		width="100%">
																		<tr>
																			<td class="divider_inner"
																				style="font-size: 1px; line-height: 1px; border-top: 0px solid #0000000;">
																				<span> </span></td>
																		</tr>
																	</table>
																</div>
															</td>
														</tr>
													</table>
													<table border="0" cellpadding="0" cellspacing="0"
														class="text_block block-4" role="presentation"
														style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;"
														width="100%">
														<tr>
															<td class="pad"
																style="padding-bottom:10px;padding-left:40px;padding-right:40px;padding-top:10px;">
																<div style="font-family: sans-serif">
																	<div class=""
																		style="font-size: 12px; font-family: Montserrat, Trebuchet MS, Lucida Grande, Lucida Sans Unicode, Lucida Sans, Tahoma, sans-serif; mso-line-height-alt: 14.399999999999999px; color: #555555; line-height: 1.2;">
																		<p
																			style="margin: 0; font-size: 16px; text-align: center; mso-line-height-alt: 19.2px;">
																			<span
																				style="font-size:30px;color:#f96b07;"><span
																					style="text-align:left;background-color:transparent;font-size:30px;"><span
																						style="color:#f96b07;"><strong>NOTIFICACIÓN</strong></span></span><strong
																					style="color:#f96b07;font-family:inherit;font-family:inherit;font-size:30px;">:
																				</strong><span
																					style="color:#f96b07;"><span
																						style="font-size:30px;"><strong>REVISIÓN</strong></span></span><strong
																					style="color:#f96b07;font-family:inherit;font-family:inherit;font-size:30px;">
																					CONFIABILIDAD</strong></span></p>
																	</div>
																</div>
															</td>
														</tr>
													</table>
													<table border="0" cellpadding="0" cellspacing="0"
														class="text_block block-5" role="presentation"
														style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;"
														width="100%">
														<tr>
															<td class="pad"2b303a
																style="padding-bottom:10px;padding-left:40px;padding-right:40px;padding-top:10px;">
																<div style="font-family: sans-serif">
																	<div class=""
																		style="font-size: 12px; font-family: Montserrat, Trebuchet MS, Lucida Grande, Lucida Sans Unicode, Lucida Sans, Tahoma, sans-serif; mso-line-height-alt: 18px; color: #555555; line-height: 1.5;">
																		<p
																			style="margin: 0; font-size: 14px; text-align: left; mso-line-height-alt: 22.5px;">
																			<span
																				style="color:#808389;font-size:15px;">Se
																				ha generado una OT en el
																				sistema para su respectiva
																				revision.</span></p>
																	</div>
																</div>
															</td>
														</tr>
													</table>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
					<table align="center" border="0" cellpadding="0" cellspacing="0" class="row row-3"
						role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
						<tbody>
							<tr>
								<td>
									<table align="center" border="0" cellpadding="0" cellspacing="0"
										class="row-content stack" role="presentation"
										style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000000; background-color: #f96b07; width: 640px;"
										width="640">
										<tbody>
											<tr>
												<td class="column column-1"
													style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; padding-top: 0px; padding-bottom: 0px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"
													width="100%">
													<table border="0" cellpadding="0" cellspacing="0"
														class="divider_block block-1" role="presentation"
														style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"
														width="100%">
														<tr>
															<td class="pad">
																<div align="center" class="alignment">
																	<table border="0" cellpadding="0" cellspacing="0"
																		role="presentation"
																		style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"
																		width="100%">
																		<tr>
																			<td class="divider_inner"
																				style="font-size: 1px; line-height: 1px; border-top: 4px solid #1AA19C;">
																				<span> </span></td>
																		</tr>
																	</table>
																</div>
															</td>
														</tr>
													</table>
													<table border="0" cellpadding="0" cellspacing="0"
														class="text_block block-2" role="presentation"
														style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;"
														width="100%">
														<tr>
															<td class="pad"
																style="padding-bottom:10px;padding-left:40px;padding-right:40px;padding-top:15px;">
																<div style="font-family: sans-serif">
																	<div class=""
																		style="font-size: 12px; mso-line-height-alt: 18px; color: #0000000; line-height: 1.5; font-family: Montserrat, Trebuchet MS, Lucida Grande, Lucida Sans Unicode, Lucida Sans, Tahoma, sans-serif;">
																		<p
																			style="margin: 0; font-size: 12px; mso-line-height-alt: 18px;">
																			Esta OT se genero en el sistema y se debe
																			solucionar en la brevedad del caso, por
																			favor realizar la respectiva revisión y
																			retroalimentar en el aplicativo.</p>
																	</div>
																</div>
															</td>
														</tr>
													</table>
													<table border="0" cellpadding="0" cellspacing="0"
														class="divider_block block-3" role="presentation"
														style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"
														width="100%">
														<tr>
															<td class="pad"
																style="padding-bottom:10px;padding-left:40px;padding-right:40px;padding-top:25px;">
																<div align="center" class="alignment">
																	<table border="0" cellpadding="0" cellspacing="0"
																		role="presentation"
																		style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"
																		width="100%">
																		<tr>
																			<td class="divider_inner"
																				style="font-size: 1px; line-height: 1px; border-top: 1px solid #555961;">
																				<span> </span></td>
																		</tr>
																	</table>
																</div>
															</td>
														</tr>
													</table>
													<table border="0" cellpadding="0" cellspacing="0"
														class="text_block block-4" role="presentation"
														style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;"
														width="100%">
														<tr>
															<td class="pad"
																style="padding-bottom:30px;padding-left:40px;padding-right:40px;padding-top:20px;">
																<div style="font-family: sans-serif">
																	<div class=""
																		style="font-size: 12px; font-family: Montserrat, Trebuchet MS, Lucida Grande, Lucida Sans Unicode, Lucida Sans, Tahoma, sans-serif; mso-line-height-alt: 14.399999999999999px; color: #555555; line-height: 1.2;">
																		<p
																			style="margin: 0; font-size: 14px; text-align: center; mso-line-height-alt: 16.8px;">
																			<span
																				style="color:#000000;font-size:12px;">Desarrollado
																				por Sebastian Felipe Herrera Varela 
																				Copyright © 2023</span></p>
																	</div>
																</div>
															</td>
														</tr>
													</table>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
					<table align="center" border="0" cellpadding="0" cellspacing="0" class="row row-4"
						role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
						<tbody>
							<tr>
								<td>
									<table align="center" border="0" cellpadding="0" cellspacing="0"
										class="row-content stack" role="presentation"
										style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000000; width: 640px;"
										width="640">
										<tbody>
											<tr>
												<td class="column column-1"
													style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; padding-top: 5px; padding-bottom: 5px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"
													width="100%">
													<table border="0" cellpadding="0" cellspacing="0"
														class="icons_block block-1" role="presentation"
														style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"
														width="100%">
														<tr>
															<td class="pad"
																style="vertical-align: middle; color: #9d9d9d; font-family: inherit; font-size: 15px; padding-bottom: 5px; padding-top: 5px; text-align: center;">
																<table cellpadding="0" cellspacing="0"
																	role="presentation"
																	style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"
																	width="100%">
																	<tr>
																		<td class="alignment"
																			style="vertical-align: middle; text-align: center;">
																			<!--[if vml]><table align="left" cellpadding="0" cellspacing="0" role="presentation" style="display:inline-block;padding-left:0px;padding-right:0px;mso-table-lspace: 0pt;mso-table-rspace: 0pt;"><![endif]-->
																			<!--[if !vml]><!-->
																			<table cellpadding="0" cellspacing="0"
																				class="icons-inner" role="presentation"
																				style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; display: inline-block; margin-right: -4px; padding-left: 0px; padding-right: 0px;">
																				<!--<![endif]-->
																				
																			</table>
																		</td>
																	</tr>
																</table>
															</td>
														</tr>
													</table>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
				</td>
			</tr>
		</tbody>
	</table><!-- End -->
</body>
            </html>'''

            mimemsg = MIMEMultipart()
            mimemsg['From'] = var.USERNAME
            mimemsg['To'] = var.USERNAME
            mimemsg['Subject'] = "EVALUACION - REVISION OT # {} - PENDIENTE".format(
                orden_ot)
            mimemsg.attach(MIMEText(mail_body, 'html'))
            connection = smtplib.SMTP(host='smtp.office365.com', port=587)
            connection.starttls()
            connection.login(var.USERNAME, var.PASS)
            connection.send_message(mimemsg)
            connection.quit()
            return render(request, "planeacion/list_planeacion.html", {"data": informacion_total, "info": resultado})
        else:
            print("Ya se encuentra en la BD")
            resultado = "La OT {} Ya se encuentra en la BD".format(orden_ot)
            informacion_total = Planeacion.objects.all()
            return render(request, "planeacion/list_planeacion.html", {"data": informacion_total, "info": resultado})


def list_hacer(request):
    data = Hacer.objects.all()
    return render(request, "hacer/list_hacer.html", {"data": data})


def registrar_hacer(request):
    data_planeacion = Planeacion.objects.filter(estado="PENDIENTE")
    return render(request, "hacer/registrar_hacer.html", {"data": data_planeacion})


def save_hacer(request):

    if request.method == "POST":
        orden_OT = request.POST.get("orden_OT")
        actividad_ejecutada = request.POST.get("actividad_ejecutada")
        numero_formato = request.POST.get("numero_formato")
        multiplo = request.POST.get("multiplo")
        fecha_telemedida = request.POST.get("fecha_telemedida")
        actualizacion_sistema = request.POST.get("actualizacion_sistema")
        pago_actividad = request.POST.get("pago_actividad")
        ot_final = Planeacion.objects.get(pk=orden_OT)
        ot_final.estado = "PENDIENTE EVALUACION"
        ot_final.save()
        data = Hacer(
            orden_trabajo=ot_final,
            actividad_ejecutada=actividad_ejecutada,
            numero_formato=numero_formato,
            multiplo=multiplo,
            telemedida=fecha_telemedida,
            actualizac0ion_sistema=actualizacion_sistema,
            pagar=pago_actividad
        )
        data.save()
        info = Hacer.objects.all()
        return render(request, "hacer/list_hacer.html", {"data": info})
    return render(request, "hacer/list_hacer.html", {"data": info})


def list_evaluacion(request):
    data = Planeacion.objects.filter(estado="PENDIENTE EVALUACION")
    data_evaluacion = Evaluacion.objects.all()
    return render(request, "evaluacion/listar_evaluacion.html", {"data": data, "data_evaluacion": data_evaluacion})


def registrar_evaluacion(request):
    data_evaluacion = Planeacion.objects.filter(estado="PENDIENTE EVALUACION")
    return render(request, "evaluacion/registrar_evaluacion.html", {"data": data_evaluacion})


def save_evaluacion(request):
    
    if request.method == "POST":
        orden_OT = request.POST.get("orde_OT_eva")
        primera_factura = request.POST.get("primera_factura")
        fecha_telemedida = request.POST.get("fecha_telemedida")
        conforme = request.POST.get("conforme")
        ot_final = Planeacion.objects.get(pk=orden_OT)
        ot_final.estado = "TERMINADO"
        ot_final.save()
        data = Evaluacion(
            orden_trabajo=ot_final,
            primera_factura=primera_factura,
            ultima_telemedida=fecha_telemedida,
            conforme=conforme,
        )
        data.save()
        """
		Querys: Consulto la tabla Planeacion para listar nuevamente los clientes Pendientes por estado de Evaluacion
		Querys: Consulto la tabla Evaluacion para listar todos los registros de la Evaluacion
  		"""
        data_planeacion = Planeacion.objects.filter(estado="PENDIENTE EVALUACION")
        data_evaluacion = Evaluacion.objects.all()
        info = True
        return render(request, "evaluacion/listar_evaluacion.html", {"data": data_planeacion, "data_evaluacion": data_evaluacion, "info": info})
    return render(request, "evaluacion/listar_evaluacion.html", {"data": data_planeacion, "data_evaluacion": data_evaluacion, "info": False})
