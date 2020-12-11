from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Language, Paradigm, Programmer
from .serializers import LanguageSerializer, ParadigmSerializer, ProgrammerSerializer
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

from .models import UserDetails, AccountDetails, TransactionAmounts



# Create your views here.
class LanguageView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class ParadigmView(viewsets.ModelViewSet):
    queryset = Paradigm.objects.all()
    serializer_class = ParadigmSerializer


class ProgrammerView(viewsets.ModelViewSet):
    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializer

def index(request):
    return render(request, 'paymentapp/index.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            newuser = AccountDetails.objects.create(
                username = username,
                accountName = username,
                accountNumber = 1,
                linked = True,
                balance = 100000
            )
            newuser.save()
            return redirect('index')
    else: 
        form = UserCreationForm()
    
    context = {'form': form}
    return render(request, 'registration/register.html', context)

def addinfo(request):
    pass

def transfer(request):
    username = None
    username = request.user.username
    if request.method == 'POST':
        recipient = request.POST['recipient']
        amount = float(request.POST['transaction_amount'])
        transaction = TransactionAmounts.objects.create(
            sender = username,
            receiver = recipient,
            amount = amount
        )
        transaction.save()
        sender_object = AccountDetails.objects.get(username=username)
        recipient_object = AccountDetails.objects.get(username=recipient)
        sender_object.balance = float(sender_object.balance) - amount
        recipient_object.balance = float(recipient_object.balance) + amount
        sender_object.save()
        recipient_object.save()
        return redirect('/history/')

    else: 
        return render(request, "paymentapp/transfer.html",{
        "username": username
        })
        
def balance(request):
    username = request.user.username
    user_object = AccountDetails.objects.get(username=username)
    balance = user_object.balance
    return render(request, "paymentapp/balance.html",{
        "username": username,
        "balance": balance
        })

def history(request):
    username = request.user.username
    num_transactions = TransactionAmounts.objects.all().count()
    sent_amounts = []
    received_amounts = []

    for id in range(1, num_transactions + 1):
        selected_transaction = TransactionAmounts.objects.get(id=str(id))
        if selected_transaction.sender == username:
            sent_amount = selected_transaction.receiver, selected_transaction.amount, selected_transaction.date.strftime("%Y:%m:%d")
            sent_amounts.append(sent_amount)
        elif selected_transaction.receiver == username:
            received_amount = selected_transaction.sender, selected_transaction.amount, selected_transaction.date.strftime("%Y:%m:%d")
            received_amounts.append(received_amount)
    
    return render(request, "paymentapp/history.html",{
        "sent_amounts": sent_amounts,
        "received_amounts": received_amounts
    })