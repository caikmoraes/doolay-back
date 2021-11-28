from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
from setores.models import Setor
from saude.models import ListaSintomas, EstadoSaude, Sintoma, EstadoSintomaItem
from saude.serializers import EstadoSaudeSerializer, EstadoSaudeNestedSerializer, ListaSintomasSerializer, SintomaSerializer, EstadoSintomaItemSerializer
import datetime
import io
from django.http import FileResponse, HttpResponse
from reportlab.pdfgen import canvas
from reportlab.rl_config import defaultPageSize
import matplotlib
from matplotlib import pyplot as plt
import numpy as np
import math

matplotlib.use('Agg')

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + datetime.timedelta(n)

def relatorio_registros_diarios(request, date_inicio, date_final):
    date_format = "%Y-%m-%d"
    date_format_output = "%d/%m/%Y"
    dt_inicio = datetime.datetime.strptime(date_inicio, date_format)
    dt_final = datetime.datetime.strptime(date_final, date_format)
    query = EstadoSaude.objects.filter(date__range=(dt_inicio, dt_final))
    n_registros = query.count()
    
    ## creating PDF

    PAGE_WIDTH  = defaultPageSize[0]
    PAGE_HEIGHT = defaultPageSize[1]

    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    p.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT-100, "Relatório de Registros Díarios")
    spacing = PAGE_HEIGHT-500
    for single_date in daterange(dt_inicio, dt_final):
        countage = query.filter(date=single_date).count()
        date_out = single_date.strftime(date_format_output)
        p.drawString(100, spacing, f"{date_out}: {countage} registros ")
        spacing += 25
    p.showPage()
    p.save()

    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename=f'relatorio_registros_{date_inicio}to{date_final}.pdf')


def plot_registros_diarios(request, date_inicio, date_final):

    date_format = "%Y-%m-%d"
    date_format_output = "%d/%m/%Y"
    dt_inicio = datetime.datetime.strptime(date_inicio, date_format)
    dt_final = datetime.datetime.strptime(date_final, date_format)
    query = EstadoSaude.objects.filter(date__range=(dt_inicio, dt_final))
    n_registros = query.count()

    objects = [date for date in daterange(dt_inicio, dt_final)]
    print(objects)
    y_pos = np.arange(len(objects))
    qty = []
    for single_date in objects:
        countage = query.filter(date=single_date).count()
        qty.append(countage)

    xlabels = [f"{date.day}/{date.month}/{date.year}" for date in daterange(dt_inicio, dt_final)]
    new_list = range(math.floor(min(qty)), math.ceil(max(qty))+1)
    plt.bar(y_pos, qty, align='center', alpha=0.5)
    plt.tight_layout()
    plt.xticks(y_pos, xlabels, rotation=45)
    plt.yticks(new_list)
    plt.ylabel('Registros')
    plt.xlabel('Datas')
    plt.title(f'Registros Diários')
    response = HttpResponse(content_type="image/png")
    plt.savefig(response, format="png")
    return response


def relatorio_nok_diarios(request, date_inicio, date_final):
    date_format = "%Y-%m-%d"
    date_format_output = "%d/%m/%Y"
    dt_inicio = datetime.datetime.strptime(date_inicio, date_format)
    dt_final = datetime.datetime.strptime(date_final, date_format)
    query = EstadoSaude.objects.filter(date__range=(dt_inicio, dt_final))
    n_registros = query.count()
    
    ## creating PDF

    PAGE_WIDTH  = defaultPageSize[0]
    PAGE_HEIGHT = defaultPageSize[1]

    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    p.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT-100, "Relatório de NOKs Díarios")
    spacing = PAGE_HEIGHT-500
    for single_date in daterange(dt_inicio, dt_final):
        countage_nok = query.filter(date=single_date.date(), estado="NOK").count()
        countage = query.filter(date=single_date.date()).count()
        date_out = single_date.strftime(date_format_output)
        if countage != 0:
            percentage = (countage_nok/countage) * 100 
        else:
            percentage = 0
        p.drawString(75, spacing, f"{date_out}: {countage_nok} registros contados como NOK, totalizando {percentage}% dos registros totais.")
        spacing += 25
    p.showPage()
    p.save()

    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename=f'relatorio_noks_{date_inicio}_{date_final}.pdf')

def plot_noks_diarios_valor(request, date_inicio, date_final):

    date_format = "%Y-%m-%d"
    date_format_output = "%d/%m/%Y"
    dt_inicio = datetime.datetime.strptime(date_inicio, date_format)
    dt_final = datetime.datetime.strptime(date_final, date_format)
    query = EstadoSaude.objects.filter(date__range=(dt_inicio, dt_final))
    n_registros = query.count()

    objects = [date for date in daterange(dt_inicio, dt_final)]
    print(objects)
    y_pos = np.arange(len(objects))
    qty = []
    for single_date in objects:
        countage_nok = query.filter(date=single_date.date(), estado="NOK").count()
        qty.append(countage_nok)

    xlabels = [f"{date.day}/{date.month}/{date.year}" for date in daterange(dt_inicio, dt_final)]
    new_list = range(math.floor(min(qty)), math.ceil(max(qty))+1)
    plt.bar(y_pos, qty, align='center', alpha=0.5)
    plt.xticks(y_pos, xlabels)
    plt.yticks(new_list)
    plt.ylabel('Registros')
    plt.xlabel('Datas')
    plt.title(f'NOKs Diários')
    response = HttpResponse(content_type="image/png")
    plt.savefig(response, format="png")
    return response

def plot_noks_diarios_percentage(request, date_inicio, date_final):

    date_format = "%Y-%m-%d"
    date_format_output = "%d/%m/%Y"
    dt_inicio = datetime.datetime.strptime(date_inicio, date_format)
    dt_final = datetime.datetime.strptime(date_final, date_format)
    query = EstadoSaude.objects.filter(date__range=(dt_inicio, dt_final))
    n_registros = query.count()

    objects = [date for date in daterange(dt_inicio, dt_final)]
    print(objects)
    y_pos = np.arange(len(objects))
    qty = []
    for single_date in objects:
        countage_nok = query.filter(date=single_date.date(), estado="NOK").count()
        countage = query.filter(date=single_date.date()).count()
        date_out = single_date.strftime(date_format_output)
        if countage != 0:
            percentage = (countage_nok/countage) * 100 
        else:
            percentage = 0
        qty.append(percentage)

    xlabels = [f"{date.day}/{date.month}/{date.year}" for date in daterange(dt_inicio, dt_final)]
    new_list = range(math.floor(min(qty)), math.ceil(max(qty))+1)
    plt.bar(y_pos, qty, align='center', alpha=0.5)
    plt.xticks(y_pos, xlabels)
    plt.ylabel('Registros')
    plt.xlabel('Datas')
    plt.title(f'NOKs Diários')
    response = HttpResponse(content_type="image/png")
    plt.savefig(response, format="png")
    return response

def relatorio_registros_setor(request, date_inicio, date_final):
    date_format = "%Y-%m-%d"
    date_format_output = "%d/%m/%Y"
    dt_inicio = datetime.datetime.strptime(date_inicio, date_format)
    dt_final = datetime.datetime.strptime(date_final, date_format)
    query = EstadoSaude.objects.filter(date__range=(dt_inicio, dt_final))
    n_registros = query.count()
    
    ## creating PDF

    PAGE_WIDTH  = defaultPageSize[0]
    PAGE_HEIGHT = defaultPageSize[1]

    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    p.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT-100, "Relatório de Registros Díarios por Setor")
    spacing = PAGE_HEIGHT-220
    setores = Setor.objects.all()
    for single_date in daterange(dt_inicio, dt_final):
        new_query = query.filter(date=single_date)
        countage = query.filter(date=single_date).count()
        date_out = single_date.strftime(date_format_output)
        p.drawCentredString(100, spacing, f"{date_out}:")
        spacing += 25
        for setor in setores:
            estado_por_setor = new_query.filter(user__setor__id=setor.pk).count()
            p.drawString(120, spacing-70, f"{setor.nome} tem {estado_por_setor} registros")
            spacing += 25
    p.showPage()
    p.save()

    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename=f'relatorio_setor_{date_inicio}_{date_final}.pdf')


def plot_registros_setor(request, date_inicio, date_final, pk_setor):

    date_format = "%Y-%m-%d"
    date_format_output = "%d/%m/%Y"
    dt_inicio = datetime.datetime.strptime(date_inicio, date_format)
    dt_final = datetime.datetime.strptime(date_final, date_format)
    query = EstadoSaude.objects.filter(date__range=(dt_inicio, dt_final))
    n_registros = query.count()

    objects = [date for date in daterange(dt_inicio, dt_final)]
    print(objects)
    y_pos = np.arange(len(objects))
    qty = []
    for single_date in objects:
        countage = query.filter(date=single_date, user__setor__id=pk_setor).count()
        qty.append(countage)

    xlabels = [f"{date.day}/{date.month}/{date.year}" for date in daterange(dt_inicio, dt_final)]
    new_list = range(math.floor(min(qty)), math.ceil(max(qty))+1)
    plt.bar(y_pos, qty, align='center', alpha=0.5)
    plt.xticks(y_pos, xlabels)
    plt.yticks(new_list)
    plt.ylabel('Registros')
    plt.xlabel('Datas')
    plt.title(f'Registros Diários')
    response = HttpResponse(content_type="image/png")
    plt.savefig(response, format="png")
    return response


def relatorio_registros_setor_percentage(request, date_inicio, date_final):
    date_format = "%Y-%m-%d"
    date_format_output = "%d/%m/%Y"
    dt_inicio = datetime.datetime.strptime(date_inicio, date_format)
    dt_final = datetime.datetime.strptime(date_final, date_format)
    query = EstadoSaude.objects.filter(date__range=(dt_inicio, dt_final))
    n_registros = query.count()
    
    ## creating PDF

    PAGE_WIDTH  = defaultPageSize[0]
    PAGE_HEIGHT = defaultPageSize[1]

    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    p.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT-100, "Relatório de Registros Díarios por Setor")
    spacing = PAGE_HEIGHT-220
    setores = Setor.objects.all()
    for single_date in daterange(dt_inicio, dt_final):
        new_query = query.filter(date=single_date)
        countage = query.filter(date=single_date).count()
        date_out = single_date.strftime(date_format_output)
        p.drawCentredString(100, spacing, f"{date_out}:")
        spacing += 25
        for setor in setores:
            estado_por_setor = new_query.filter(user__setor__id=setor.pk).count()
            nok_por_setor = new_query.filter(user__setor__id=setor.pk, estado="NOK").count()
            if estado_por_setor != 0:
                percentage = math.floor((nok_por_setor/estado_por_setor) * 100)
            else:
                percentage = 0 
            p.drawString(120, spacing-70, f"{setor.nome} tem {estado_por_setor} registros NOK, totalizando {percentage}% do total")
            spacing += 25
    p.showPage()
    p.save()

    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename=f'relatorio_nok_setor_{date_inicio}_{date_final}.pdf')

class ListaSintomasViewSet(viewsets.ModelViewSet):
    queryset = ListaSintomas.objects.all()
    serializer_class = ListaSintomasSerializer


class SintomaViewSet(viewsets.ModelViewSet):
    queryset = Sintoma.objects.all()
    serializer_class = SintomaSerializer


class EstadoItemSintomaViewSet(viewsets.ModelViewSet):
    queryset = EstadoSintomaItem.objects.all()
    serializer_class = EstadoSintomaItemSerializer


class EstadoSaudeViewSet(viewsets.ModelViewSet):
    queryset = EstadoSaude.objects.all()
    serializer_class = EstadoSaudeSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return EstadoSaudeSerializer
        else:
            return EstadoSaudeNestedSerializer


class EstadoSaudeDetail(APIView):
    queryset = EstadoSaude.objects.all()
    serializer_class = EstadoSaudeSerializer

    def get(self, request, user_pk, format=None):
        obj = self.queryset.filter(user_id=user_pk)
        serializer = self.serializer_class(obj, many=True)
        return Response(serializer.data)
