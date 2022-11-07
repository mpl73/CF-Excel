from django.shortcuts import render, redirect
from . import models
from . import forms

def home(request):
    return render(request, 'home.html')

def gastos(request):
    gastos = models.Gasto.objects.filter()
    context = {
        'gastos': gastos,
    }
    return render(request, 'gastos.html', context)

def cartoes(request):
    cartoes = models.Cartao.objects.all()
    context = {
        'cartoes': cartoes,
    }
    return render(request, 'cartoes.html', context)

def novo_cartao(request):
    if request.method == 'GET':
        form = forms.CartaoForm()
        context = {
            'form': form,
        }
        return render(request, 'novo_cartao.html', context)
    if request.method == 'POST':
        vnome = request.POST.get('nome')
        vbanco = request.POST.get('banco')
        vnumero = request.POST.get('numero')
        vfechamento = request.POST.get('fechamento')
        vvencimento = request.POST.get('vencimento')
        models.Cartao.objects.create(
            nome = vnome,
            banco = vbanco,
            numero = vnumero,
            fechamento = vfechamento,
            vencimento = vvencimento
        )

        cartoes = models.Cartao.objects.all()
        context = {
            'cartoes': cartoes,
        }
        return redirect('cartoes')

def editar_cartao(request, id):
    if request.method == 'GET':
        cartao = models.Cartao.objects.get(id=id)
        context = {
            'cartao': cartao,
        }
        return render(request, 'editar_cartao.html', context)
    if request.method == 'POST':
        cartao = models.Cartao.objects.get(id=id)

        vnome = request.POST.get('nome')
        vbanco = request.POST.get('banco')
        vnumero = request.POST.get('numero')
        vfechamento = request.POST.get('fechamento')
        vvencimento = request.POST.get('vencimento')

        cartao.nome = vnome
        cartao.banco = vbanco
        cartao.numero = vnumero
        cartao.fechamento = vfechamento
        cartao.vencimento = vvencimento

        cartao.save()

        cartoes = models.Cartao.objects.all()
        context = {
            'cartoes': cartoes,
        }
        return redirect('cartoes')

def deletar_cartao(request, id):
    cartao = models.Cartao.objects.get(id=id)
    cartao.delete()
    
    cartoes = models.Cartao.objects.all()
    context = {
        'cartoes': cartoes,
    }
    return redirect('cartoes')

