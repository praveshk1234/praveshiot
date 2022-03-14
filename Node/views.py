from django.shortcuts import render
from .models import Node
# Create your views here.
def nodelist(request):
    nodes = Node.objects.all()
    context = {'nodes': nodes}
    return render(request,'nodelist.html',context)
def nodedetail(request,pk):
    errors=""
    nodeobj = Node.objects.get(id=pk)
    buttonvalue = request.POST.get('keybutton')
    if 'On' == buttonvalue:
        buttonvalue = True
        print(buttonvalue)
        
    elif 'Off' == buttonvalue:
        buttonvalue = False
        print(nodeobj.current_status)
    else:
        errors =" device have error"
    nodeobj.current_status = buttonvalue
    nodeobj.save()
    print(nodeobj.current_status)
    context ={'error':errors}
    return render(request,'nodedetail.html',context)