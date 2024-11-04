from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.urls import reverse
from .forms import SaleForm
from .forms import Walletform
from django.db import models
from .models import Transaction

# Static wallet for demonstration purposes
wallet = {
    'rial': 1000000000,  # Example amount in rials
    'gold': 0  # Example initial amount in gold
}

def buy(request):
    price_per_gram = 4000000  # Static price per gram in rials
    if request.method == 'POST':
        form = SaleForm(request.POST)
        if form.is_valid():
            rial_amount = form.cleaned_data.get('rial_amount')
            gold_amount = form.cleaned_data.get('gold_amount')
            if rial_amount:
                if wallet['rial'] >= float(rial_amount):
                    gold_amount = float(rial_amount) / price_per_gram
                    #wallet['rial'] -= float(rial_amount)
                    #wallet['gold'] += gold_amount
                    # Redirect to 'buyfactor' with variables
                    return redirect(
                        reverse('sales:buyfactor') + f'?rial_amount={rial_amount}&gold_amount={gold_amount}&price_per_gram={price_per_gram}'
                    )
                else:
                    form.add_error('rial_amount', 'Not enough rial in the wallet.')
            elif gold_amount:
                rial_amount = float(gold_amount) * price_per_gram
                if wallet['rial'] >= rial_amount:
                    #wallet['rial'] -= rial_amount
                    #wallet['gold'] += float(gold_amount)
                    # Redirect to 'buyfactor' with variables
                    return redirect(
                        reverse('sales:buyfactor') + f'?rial_amount={rial_amount}&gold_amount={gold_amount}&price_per_gram={price_per_gram}'
                    )
                else:
                    form.add_error('gold_amount', 'Not enough rial in the wallet.')
    else:
        form = SaleForm()

    return render(request, 'sales/buyingPage.html', {'form': form, 'wallet': wallet, 'price_per_gram': price_per_gram})

def sell(request):
    price_per_gram = 3800000  # Static price per gram in rials
    if request.method == 'POST':
        form = SaleForm(request.POST)
        if form.is_valid():
            rial_amount = form.cleaned_data.get('rial_amount')
            gold_amount = form.cleaned_data.get('gold_amount')
            if gold_amount:
                if wallet['gold'] >= float(gold_amount):
                    rial_amount = float(gold_amount) * price_per_gram
                    #wallet['gold'] -= float(gold_amount)
                    #wallet['rial'] += rial_amount
                    # Redirect to 'sellfactor' with variables
                    return redirect(
                        reverse('sales:sellfactor') + f'?rial_amount={rial_amount}&gold_amount={gold_amount}&price_per_gram={price_per_gram}'
                    )
                else:
                    form.add_error('gold_amount', 'Not enough gold in the wallet.')
            elif rial_amount:
                gold_amount = float(rial_amount) / price_per_gram
                if wallet['gold'] >= gold_amount:
                    #wallet['gold'] -= gold_amount
                    #wallet['rial'] += float(rial_amount)
                    # Redirect to 'sellfactor' with variables
                    return redirect(
                        reverse('sales:sellfactor') + f'?rial_amount={rial_amount}&gold_amount={gold_amount}&price_per_gram={price_per_gram}'
                    )
                else:
                    form.add_error('rial_amount', 'Not enough gold in the wallet.')
    else:
        form = SaleForm()

    return render(request, 'sales/sellingPage.html', {'form': form, 'wallet': wallet, 'price_per_gram': price_per_gram})

def buyfactor(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        rial_amount = float(request.POST.get('rial_amount'))
        gold_amount = float(request.POST.get('gold_amount'))
        price_per_gram = float(request.POST.get('price_per_gram'))
        if action == 'confirm':
            # Check if the user has enough rial in the wallet
            if wallet['rial'] >= rial_amount:
                # Update the wallet
                wallet['rial'] -= rial_amount
                wallet['gold'] += gold_amount
                
                transaction = Transaction.objects.create(
                    #user=request.user,
                    transaction_type='buy_gold',
                    seller='Goldis',
                    rial_amount=rial_amount,
                    gold_amount=gold_amount,
                    price_per_gram=price_per_gram
                )
                return redirect('sales:wallet')
            else:
                # Not enough funds, show an error
                error_message = 'موجودی ریال در کیف پول کافی نیست.'
                context = {
                    'rial_amount': rial_amount,
                    'gold_amount': gold_amount,
                    'price_per_gram': price_per_gram,
                    'error_message': error_message,
                }
                return render(request, 'sales/goldBuyFactor.html', context)
        elif action == 'cancel':
            return redirect('home:home')  # Redirect to home page
    else:
        rial_amount = request.GET.get('rial_amount')
        gold_amount = request.GET.get('gold_amount')
        price_per_gram = request.GET.get('price_per_gram')
        context = {
            'rial_amount': rial_amount,
            'gold_amount': gold_amount,
            'price_per_gram': price_per_gram,
        }
        return render(request, 'sales/goldBuyFactor.html', context)

def sellfactor(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        rial_amount = float(request.POST.get('rial_amount'))
        gold_amount = float(request.POST.get('gold_amount'))
        price_per_gram = float(request.POST.get('price_per_gram'))
        if action == 'confirm':
            # Check if the user has enough gold in the wallet
            if wallet['gold'] >= gold_amount:
                # Update the wallet
                wallet['gold'] -= gold_amount
                wallet['rial'] += rial_amount

                transaction = Transaction.objects.create(
                    #user=request.user,
                    transaction_type='sell_gold',
                    seller='Goldis',
                    rial_amount=rial_amount,
                    gold_amount=gold_amount,
                    price_per_gram=price_per_gram
                )
                
                return redirect('sales:wallet')
            else:
                # Not enough gold, show an error
                error_message = 'موجودی طلای شما کافی نیست.'
                context = {
                    'rial_amount': rial_amount,
                    'gold_amount': gold_amount,
                    'price_per_gram': price_per_gram,
                    'error_message': error_message,
                }
                return render(request, 'sales/goldSellFactor.html', context)
        elif action == 'cancel':
            return redirect('home:home')  # Redirect to home page
    else:
        rial_amount = request.GET.get('rial_amount')
        gold_amount = request.GET.get('gold_amount')
        price_per_gram = request.GET.get('price_per_gram')
        context = {
            'rial_amount': rial_amount,
            'gold_amount': gold_amount,
            'price_per_gram': price_per_gram,
        }
        return render(request, 'sales/goldSellFactor.html', context)

def wallet_view(request):
    if request.method == 'POST':
        form = Walletform(request.POST)
        if form.is_valid():
            rial_amount = form.cleaned_data.get('rial_amount')
            action = request.POST.get('action')
            request.session['rial_amount'] = float(rial_amount)
            if action == 'deposit':
                return redirect('sales:deposit')
            elif action == 'withdraw':
                if wallet['rial'] >= float(rial_amount):
                    return redirect('sales:withdraw')
                else:
                    form.add_error('rial_amount', 'Not enough rial in the wallet.')
    else:
        form = Walletform()

    context = {
        'form': form,
        'rial_amount': wallet['rial'],
        'gold_amount': wallet['gold'],
    }
    return render(request, 'sales/wallet.html', context)

def deposit(request):
    rial_amount = request.session.get('rial_amount')
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'confirm':
           # Update the wallet
            wallet['rial'] += float(rial_amount)
            # Create a Transaction record
            transaction = Transaction.objects.create(
                #user=request.user,
                transaction_type='deposit',
                rial_amount=rial_amount,
                #card_id=6037111100002222,
            )
            return redirect('sales:wallet')
        elif action == 'cancel':
            return redirect('home:home')  # Redirect to home page

    context = {
        'current_rial': wallet['rial'],
        'rial_amount': rial_amount,
        'gold_amount': wallet['gold'],
    }
    return render(request, 'sales/deposit.html', context)

def withdraw(request):
    rial_amount = request.session.get('rial_amount')
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'confirm':
            # Update the wallet
            wallet['rial'] -= float(rial_amount)
            # Create a Transaction record
            transaction = Transaction.objects.create(
                #user=request.user,
                transaction_type='withdrawal',
                rial_amount=rial_amount,
                #card_id=6037111100002222,
            )
            return redirect('sales:wallet')
        elif action == 'cancel':
            return redirect('home:home')  # Redirect to home page

    context = {
        'current_rial': wallet['rial'],
        'rial_amount': rial_amount,
        'gold_amount': wallet['gold'],
    }
    return render(request, 'sales/withdraw.html', context)

def transactions(request):
    #.filter(user=request.user)
    transactions_list = Transaction.objects.order_by('-date', '-time')
    
    context = {
        'transactions': transactions_list,
    }

    return render(request, 'sales/transition.html', context)