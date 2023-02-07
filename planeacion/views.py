from datetime import date
from django.urls import reverse
from rest_framework.decorators import api_view
from .serializer import HacerSerializer, PlaneacionSerializer
from rest_framework import viewsets
from .models import Hacer, Planeacion, Backlog
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
        agregado = True
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
            resultado = "Se guardo la OT {} de manera correcta.".format(orden_ot)
            """
                ===================================================
                    Envio EMAIL de confirmacion de la OT
                ===================================================
            """
            mail_body = """
            <!DOCTYPE html>

<html
  lang="en"
  xmlns:o="urn:schemas-microsoft-com:office:office"
  xmlns:v="urn:schemas-microsoft-com:vml"
>
  <head>
    <title></title>
    <meta content="text/html; charset=utf-8" http-equiv="Content-Type" />
    <meta content="width=device-width, initial-scale=1.0" name="viewport" />
    
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
        line-height: inherit;
      }

      .desktop_hide,
      .desktop_hide table {
        mso-hide: all;
        display: none;
        max-height: 0px;
        overflow: hidden;
      }

      @media (max-width: 670px) {
        .desktop_hide table.icons-inner,
        .social_block.desktop_hide .social-table {
          display: inline-block !important;
        }

        .icons-inner {
          text-align: center;
        }

        .icons-inner td {
          margin: 0 auto;
        }

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
		.container {
			display: flex;
			justify-content: center;
			align-items: center;
			height:800px ;
		}
    </style>
  </head>
  <body
    style="
      background-color: #f5f5f5;
      margin: 0;
      padding: 0;
      -webkit-text-size-adjust: none;
      text-size-adjust: none;
    "
  >
<div class="container">
	<table
	border="0"
	cellpadding="0"
	cellspacing="0"
	class="nl-container"
	role="presentation"
	style="
	  mso-table-lspace: 0pt;
	  mso-table-rspace: 0pt;
	  background-color: #f5f5f5;
	"
	width="100%"
  >
	<tbody>
	  <tr>
		<td>
		  <table
			align="center"
			border="0"
			cellpadding="0"
			cellspacing="0"
			class="row row-1"
			role="presentation"
			style="
			  mso-table-lspace: 0pt;
			  mso-table-rspace: 0pt;
			  background-position: top center;
			  background-repeat: repeat;
			"
			width="100%"
		  >
			<tbody>
			  <tr>
				<td>
				  <table
					align="center"
					border="0"
					cellpadding="0"
					cellspacing="0"
					class="row-content stack"
					role="presentation"
					style="
					  mso-table-lspace: 0pt;
					  mso-table-rspace: 0pt;
					  color: #000000;
					  width: 650px;
					"
					width="650"
				  >
					<tbody>
					  <tr>
						<td
						  class="column column-1"
						  style="
							mso-table-lspace: 0pt;
							mso-table-rspace: 0pt;
							font-weight: 400;
							text-align: left;
							vertical-align: top;
							padding-top: 5px;
							padding-bottom: 5px;
							border-top: 0px;
							border-right: 0px;
							border-bottom: 0px;
							border-left: 0px;
						  "
						  width="100%"
						>
						  <div
							class="spacer_block"
							style="
							  height: 51px;
							  line-height: 51px;
							  font-size: 1px;
							"
						  >
							 
						  </div>
						</td>
					  </tr>
					</tbody>
				  </table>
				</td>
			  </tr>
			</tbody>
		  </table>
		  <table
			align="center"
			border="0"
			cellpadding="0"
			cellspacing="0"
			class="row row-2"
			role="presentation"
			style="mso-table-lspace: 0pt; mso-table-rspace: 0pt"
			width="100%"
		  >
			<tbody>
			  <tr>
				<td>
				  <table
					align="center"
					border="0"
					cellpadding="0"
					cellspacing="0"
					class="row-content stack"
					role="presentation"
					style="
					  mso-table-lspace: 0pt;
					  mso-table-rspace: 0pt;
					  color: #000000;
					  width: 650px;
					"
					width="650"
				  >
					<tbody>
					  <tr>
						<td
						  class="column column-1"
						  style="
							mso-table-lspace: 0pt;
							mso-table-rspace: 0pt;
							font-weight: 400;
							text-align: left;
							padding-left: 15px;
							padding-right: 15px;
							vertical-align: top;
							padding-top: 5px;
							padding-bottom: 5px;
							border-top: 0px;
							border-right: 0px;
							border-bottom: 0px;
							border-left: 0px;
						  "
						  width="100%"
						>
						  <table
							border="0"
							cellpadding="0"
							cellspacing="0"
							class="image_block block-1"
							role="presentation"
							style="
							  mso-table-lspace: 0pt;
							  mso-table-rspace: 0pt;
							"
							width="100%"
						  >
							<tr>
							  <td
								class="pad"
								style="
								  width: 100%;
								  padding-right: 0px;
								  padding-left: 0px;
								"
							  >
								<div
								  align="center"
								  class="alignment"
								  style="line-height: 10px"
								>
								  <img
									src="https://www.celsia.com/wp-content/uploads/2021/09/12001200p4871EDNmain2678logo-censia-naranja-200.jpg"
									style="
									  display: block;
									  height: auto;
									  border: 0;
									  width: 130px;
									  max-width: 100%;
									"
									title="Social Hug Logo"
									width="130"
								  />
								</div>
							  </td>
							</tr>
						  </table>
						  <table
							border="0"
							cellpadding="0"
							cellspacing="0"
							class="text_block block-3"
							role="presentation"
							style="
							  mso-table-lspace: 0pt;
							  mso-table-rspace: 0pt;
							  word-break: break-word;
							"
							width="100%"
						  >
							<tr>
							  <td
								class="pad"
								style="
								  padding-bottom: 10px;
								  padding-left: 10px;
								  padding-right: 10px;
								  padding-top: 30px;
								"
							  >
								<div style="font-family: sans-serif">
								  <div
									class=""
									style="
									  font-family: Tahoma, Verdana, Segoe,
										sans-serif;
									  font-size: 12px;
									  mso-line-height-alt: 24px;
									  color: #f96b07;
									  line-height: 2;
									"
								  >
									<p
									  style="
										margin: 0;
										font-size: 12px;
										text-align: center;
										mso-line-height-alt: 84px;
									  "
									>
									  <span style="font-size: 42px">
										<strong><span style="font-size: 42px">Modulo Planeacion</span></strong>
									</span>
									</p>
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
		  <table
			align="center"
			border="0"
			cellpadding="0"
			cellspacing="0"
			class="row row-3"
			role="presentation"
			style="mso-table-lspace: 0pt; mso-table-rspace: 0pt"
			width="100%"
		  >
			<tbody>
			  <tr>
				<td>
				  <table
					align="center"
					border="0"
					cellpadding="0"
					cellspacing="0"
					class="row-content"
					role="presentation"
					style="
					  mso-table-lspace: 0pt;
					  mso-table-rspace: 0pt;
					  background-color: #e4e9ed;
					  color: #333;
					  width: 650px;
					"
					width="650"
				  >
					<tbody>
					  <tr>
						<td
						  class="column column-1"
						  style="
							mso-table-lspace: 0pt;
							mso-table-rspace: 0pt;
							font-weight: 400;
							text-align: left;
							vertical-align: top;
							border-top: 0px;
							border-right: 0px;
							border-bottom: 0px;
							border-left: 0px;
						  "
						  width="25%"
						>
						  <table
							border="0"
							cellpadding="0"
							cellspacing="0"
							class="image_block block-2"
							role="presentation"
							style="
							  mso-table-lspace: 0pt;
							  mso-table-rspace: 0pt;
							"
							width="100%"
						  >
							<tr>
							  <td
								class="pad"
								style="
								  width: 100%;
								  padding-right: 0px;
								  padding-left: 0px;
								"
							  >
								<div
								  align="center"
								  class="alignment"
								  style="line-height: 10px"
								>
								  <img
									alt="CEO"
									src="https://www.celsia.com/wp-content/uploads/2021/09/12001200p4871EDNmain2678logo-censia-naranja-200.jpg"
									style="
									  display: block;
									  height: 150px;
									  border: 0;
									  width: 150px;
									  max-width: 100%;
									"
									title="CEO"
									width="122"
								  />
								</div>
							  </td>
							</tr>
						  </table>
						</td>
						<td
						  class="column column-2"
						  style="
							mso-table-lspace: 0pt;
							mso-table-rspace: 0pt;
							font-weight: 400;
							text-align: left;
							vertical-align: top;
							border-top: 0px;
							border-right: 0px;
							border-bottom: 0px;
							border-left: 0px;
						  "
						  width="75%"
						>
						  <table
							border="0"
							cellpadding="0"
							cellspacing="0"
							class="text_block block-2"
							role="presentation"
							style="
							  mso-table-lspace: 0pt;
							  mso-table-rspace: 0pt;
							  word-break: break-word;
							"
							width="100%"
						  >
							<tr>
							  <td
								class="pad"
								style="
								  padding-bottom: 25px;
								  padding-left: 10px;
								  padding-right: 10px;
								  padding-top: 20px;
								"
							  >
								<div style="font-family: sans-serif">
								  <div
									class=""
									style="
									  font-family: Tahoma, Verdana, Segoe,
										sans-serif;
									  font-size: 12px;
									  mso-line-height-alt: 18px;
									  color: #625050;
									  line-height: 1.5;
									"
								  >
									<p
									  style="
										margin: 0;
										font-size: 14px;
										text-align: left;
										mso-line-height-alt: 21px;
									  "
									>
									  <span
										style="
										  color: #1a6eff;
										  font-size: 14px;
										"
										><strong><span style="font-size: 22px;">Orden de trabajo : <span>{}</span></span></strong></span>
									</p>
									<p
									  style="
										margin: 0;
										font-size: 14px;
										text-align: left;
										mso-line-height-alt: 27px;
									  "
									>
									  <span style="font-size: 18px;">Se registro una OT para su revision y su</span>
									</p>
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
		  <table
			align="center"
			border="0"
			cellpadding="0"
			cellspacing="0"
			class="row row-4"
			role="presentation"
			style="mso-table-lspace: 0pt; mso-table-rspace: 0pt"
			width="100%"
		  >
			<tbody>
			  <tr>
				<td>
				  <table
					align="center"
					border="0"
					cellpadding="0"
					cellspacing="0"
					class="row-content stack"
					role="presentation"
					style="
					  mso-table-lspace: 0pt;
					  mso-table-rspace: 0pt;
					  color: #000000;
					  width: 650px;
					"
					width="650"
				  >
					<tbody>
					  <tr>
						<td
						  class="column column-1"
						  style="
							mso-table-lspace: 0pt;
							mso-table-rspace: 0pt;
							font-weight: 400;
							text-align: left;
							vertical-align: top;
							padding-top: 5px;
							padding-bottom: 5px;
							border-top: 0px;
							border-right: 0px;
							border-bottom: 0px;
							border-left: 0px;
						  "
						  width="100%"
						>
						  <div
							class="spacer_block"
							style="
							  height: 60px;
							  line-height: 60px;
							  font-size: 1px;
							"
						  >
							 
						  </div>
						</td>
					  </tr>
					</tbody>
				  </table>
				</td>
			  </tr>
			</tbody>
		  </table>
		  <table
			align="center"
			border="0"
			cellpadding="0"
			cellspacing="0"
			class="row row-5"
			role="presentation"
			style="
			  mso-table-lspace: 0pt;
			  mso-table-rspace: 0pt;
			  background-color: #f96b07;
			"
			width="100%"
		  >
			<tbody>
			  <tr>
				<td>
				  <table
					align="center"
					border="0"
					cellpadding="0"
					cellspacing="0"
					class="row-content"
					role="presentation"
					style="
					  mso-table-lspace: 0pt;
					  mso-table-rspace: 0pt;
					  color: #333;
					  width: 650px;
					"
					width="650"
				  >
					<tbody>
					  <tr>
						<td
						  class="column column-1"
						  style="
							mso-table-lspace: 0pt;
							mso-table-rspace: 0pt;
							font-weight: 400;
							text-align: left;
							vertical-align: top;
							border-top: 0px;
							border-right: 0px;
							border-bottom: 0px;
							border-left: 0px;
						  "
						  width="50%"
						>
						  <table
							border="0"
							cellpadding="0"
							cellspacing="0"
							class="text_block block-2"
							role="presentation"
							style="
							  mso-table-lspace: 0pt;
							  mso-table-rspace: 0pt;
							  word-break: break-word;
							"
							width="100%"
						  >
							<tr>
							  <td
								class="pad"
								style="
								  padding-bottom: 15px;
								  padding-left: 10px;
								  padding-right: 10px;
								  padding-top: 15px;
								"
							  >
								<div style="font-family: sans-serif">
								  <div
									class=""
									style="
									  font-family: Tahoma, Verdana, Segoe,
										sans-serif;
									  font-size: 12px;
									  mso-line-height-alt: 14.399999999999999px;
									  color: #ffffff;
									  line-height: 1.2;
									"
								  >
									<p
									  style="
										margin: 0;
										font-size: 12px;
										mso-line-height-alt: 14.399999999999999px;
									  "
									>
									  <span style="font-size: 30px">
										<strong><span style="font-size: 20px">Transmision y Distribucion</span></strong>
									</span>
									  
									</p>
								  </div>
								</div>
							  </td>
							</tr>
						  </table>
						</td>
						<td
						  class="column column-2"
						  style="
							mso-table-lspace: 0pt;
							mso-table-rspace: 0pt;
							font-weight: 400;
							text-align: left;
							vertical-align: top;
							border-top: 0px;
							border-right: 0px;
							border-bottom: 0px;
							border-left: 0px;
						  "
						  width="50%"
						>
						  <table
							border="0"
							cellpadding="0"
							cellspacing="0"
							class="social_block block-2"
							role="presentation"
							style="
							  mso-table-lspace: 0pt;
							  mso-table-rspace: 0pt;
							"
							width="100%"
						  >
							<tr>
							  <td
								class="pad"
								style="
								  padding-bottom: 15px;
								  padding-left: 10px;
								  padding-right: 10px;
								  padding-top: 15px;
								  text-align: center;
								"
							  >
								<div align="center" class="alignment">
								  <table
									border="0"
									cellpadding="0"
									cellspacing="0"
									class="social-table"
									role="presentation"
									style="
									  mso-table-lspace: 0pt;
									  mso-table-rspace: 0pt;
									  display: inline-block;
									"
									width="141px"
								  >
									<tr>
									  <td style="padding: 0 15px 0 0px">
										<a
										  href="https://twitter.com/"
										  target="_blank"
										  ><img
											alt="Twitter"
											height="32"
											src="static/assets/img/twitter2x.png"
											style="
											  display: block;
											  height: auto;
											  border: 0;
											"
											title="Twitter"
											width="32"
										/></a>
									  </td>
									  <td style="padding: 0 15px 0 0px">
										<a
										  href="https://instagram.com/"
										  target="_blank"
										  ><img
											alt="Instagram"
											height="32"
											src="static/assets/img/instagram2x.png"
											style="
											  display: block;
											  height: auto;
											  border: 0;
											"
											title="Instagram"
											width="32"
										/></a>
									  </td>
									  <td style="padding: 0 15px 0 0px">
										<a
										  href="https://www.linkedin.com/"
										  target="_blank"
										  ><img
											alt="LinkedIn"
											height="32"
											src="static/assets/img/linkedin2x.png"
											style="
											  display: block;
											  height: auto;
											  border: 0;
											"
											title="LinkedIn"
											width="32"
										/></a>
									  </td>
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
		  <table
			align="center"
			border="0"
			cellpadding="0"
			cellspacing="0"
			class="row row-6"
			role="presentation"
			style="
			  mso-table-lspace: 0pt;
			  mso-table-rspace: 0pt;
			  background-color: #f96b07;
			"
			width="100%"
		  >
			<tbody>
			  <tr>
				<td>
				  <table
					align="center"
					border="0"
					cellpadding="0"
					cellspacing="0"
					class="row-content stack"
					role="presentation"
					style="
					  mso-table-lspace: 0pt;
					  mso-table-rspace: 0pt;
					  color: #000000;
					  width: 650px;
					"
					width="650"
				  >
					<tbody>
					  <tr>
						<td
						  class="column column-1"
						  style="
							mso-table-lspace: 0pt;
							mso-table-rspace: 0pt;
							font-weight: 400;
							text-align: left;
							vertical-align: top;
							padding-top: 30px;
							padding-bottom: 30px;
							border-top: 0px;
							border-right: 0px;
							border-bottom: 0px;
							border-left: 0px;
						  "
						  width="100%"
						>
						  <table
							border="0"
							cellpadding="10"
							cellspacing="0"
							class="text_block block-1"
							role="presentation"
							style="
							  mso-table-lspace: 0pt;
							  mso-table-rspace: 0pt;
							  word-break: break-word;
							"
							width="100%"
						  >
							<tr>
							  <td class="pad">
								<div style="font-family: sans-serif">
								  <div
									class=""
									style="
									  font-family: Tahoma, Verdana, Segoe,
										sans-serif;
									  font-size: 12px;
									  mso-line-height-alt: 14.399999999999999px;
									  color: #ffffff;
									  line-height: 1.2;
									"
								  >
									<p style="margin: 0;
										font-size: 14px;
										mso-line-height-alt: 16.8px;
									  "
									>
									  <em>Elaborado por Sebastian Felipe Herrera Varela - Analisis demanda</em>
									</p>
									<p
									  style="
										margin: 0;
										font-size: 14px;
										mso-line-height-alt: 16.8px;
									  "
									>
									  Celsia 2023 © all rights reserved
									</p>
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
		  <table
			align="center"
			border="0"
			cellpadding="0"
			cellspacing="0"
			class="row row-7"
			role="presentation"
			style="mso-table-lspace: 0pt; mso-table-rspace: 0pt"
			width="100%"
		  >
			<tbody>
			  <tr>
				<td>
				  <table
					align="center"
					border="0"
					cellpadding="0"
					cellspacing="0"
					class="row-content stack"
					role="presentation"
					style="
					  mso-table-lspace: 0pt;
					  mso-table-rspace: 0pt;
					  color: #000000;
					  width: 650px;
					"
					width="650"
				  >
					<tbody>
					  <tr>
						<td
						  class="column column-1"
						  style="
							mso-table-lspace: 0pt;
							mso-table-rspace: 0pt;
							font-weight: 400;
							text-align: left;
							vertical-align: top;
							padding-top: 5px;
							padding-bottom: 5px;
							border-top: 0px;
							border-right: 0px;
							border-bottom: 0px;
							border-left: 0px;
						  "
						  width="100%"
						>
						  <table
							border="0"
							cellpadding="0"
							cellspacing="0"
							class="icons_block block-1"
							role="presentation"
							style="
							  mso-table-lspace: 0pt;
							  mso-table-rspace: 0pt;
							"
							width="100%"
						  >
							<tr>
							  <td
								class="pad"
								style="
								  vertical-align: middle;
								  color: #9d9d9d;
								  font-family: inherit;
								  font-size: 15px;
								  padding-bottom: 5px;
								  padding-top: 5px;
								  text-align: center;
								"
							  >
								<table
								  cellpadding="0"
								  cellspacing="0"
								  role="presentation"
								  style="
									mso-table-lspace: 0pt;
									mso-table-rspace: 0pt;
								  "
								  width="100%"
								>
								  <tr>
									<td
									  class="alignment"
									  style="
										vertical-align: middle;
										text-align: center;
									  "
									>
									  <!--[if vml]><table align="left" cellpadding="0" cellspacing="0" role="presentation" style="display:inline-block;padding-left:0px;padding-right:0px;mso-table-lspace: 0pt;mso-table-rspace: 0pt;"><![endif]-->
									  <!--[if !vml]><!-->
									  <table
										cellpadding="0"
										cellspacing="0"
										class="icons-inner"
										role="presentation"
										style="
										  mso-table-lspace: 0pt;
										  mso-table-rspace: 0pt;
										  display: inline-block;
										  margin-right: -4px;
										  padding-left: 0px;
										  padding-right: 0px;
										"
									  >
										<!--<![endif]-->
										<tr>
										  
										</tr>
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
  </table>
</div>
    <!-- End -->
  </body>
</html>
""".format(orden_ot)
            
            mimemsg = MIMEMultipart()
            mimemsg['From']= var.USERNAME
            mimemsg['To']=var.USERNAME
            mimemsg['Subject']="EVALUACION - REVISION OT {} - PENDIENTE".format(orden_ot)
            mimemsg.attach(MIMEText(mail_body, 'html'))
            connection = smtplib.SMTP(host='smtp.office365.com', port=587)
            connection.starttls()
            connection.login(var.USERNAME,var.PASS)
            connection.send_message(mimemsg)
            connection.quit()

            

            
            return render(request, "planeacion/list_planeacion.html", {"data": informacion_total, "info": resultado})
        else:
            print("Ya se encuentra en la BD")
            resultado = "La OT {} Ya se encuentra en la BD".format(orden_ot)
            informacion_total = Planeacion.objects.all()
            return render(request, "planeacion/list_planeacion.html", {"data": informacion_total, "info": resultado})
