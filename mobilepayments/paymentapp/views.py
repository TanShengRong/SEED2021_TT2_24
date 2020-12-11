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
            return redirect('index')
    else: 
        form = UserCreationForm()
    
    context = {'form': form}
    return render(request, 'registration/register.html', context)

def addinfo(request):
    pass

def transfer(request):
    username = None
    if request.user.is_authenticated():
        username = request.user.username
        if request.method == 'POST':
            sender = int(request.POST['id'])
            recipient = int(request.POST['Recipient'])
            amount = float(request.POST['amount'])
            transaction = transaction.TransactionAmounts.create(
                senderID = sender,
                receiverID = recipient,
                amount = amount
            )
            transaction.save()
        else: 




def search(request):
    if request.method == "POST":
        query = request.POST['q']
        entries = util.list_entries()
        if util.get_entry(query):
            return HttpResponseRedirect(f"/{query}")
        else:
            possible_entries = []
            for entry in entries:
                if query in entry:
                    possible_entries.append(entry)
            return render(request, "encyclopedia/searchresults.html", {
            "entries": possible_entries
            })
    else:
        return render(request, "encyclopedia/index.html")
            

    else:
        pass #Redirect

        
def balance(request):
    pass

def history(request):
    pass

def mybids(request):
    user = request.user.username
    num_bids = Bids.objects.all().count()
    bidders = []
    item_ids = []
    list_items = []
    
    for i in range(1, num_bids + 1):
        SelectedObject = Bids.objects.get(id=i)
        if SelectedObject.bidder == user:
            item_id = SelectedObject.item_id
            if item_id not in item_ids:
                item_ids.append(item_id)

    for id in item_ids:
        SelectedObject = Listing.objects.get(id=str(id))
        list_item = id, SelectedObject.item_name, SelectedObject.seller, SelectedObject.price, SelectedObject.imageurl
        list_items.append(list_item)
    return render(request, "auctions/mybids.html",{
        "listings": list_items
    })    