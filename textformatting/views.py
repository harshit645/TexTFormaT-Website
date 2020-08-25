#THIS FILE IS CREATED BY ME

from django.http import HttpResponse
from django.shortcuts import render

def Homepage(request):
    return render(request,"indexboots.html")


def textanalyze(request):
    djtext=request.POST.get("text","default")
    button1=request.POST.get("check1","off")
    button2=request.POST.get("check2","off")
    button3=request.POST.get("check3","off")
    button4=request.POST.get("check4","off")
    button5=request.POST.get("check5","off")
    button6=request.POST.get("check6","off")

    if button1=="on":
        analyzetext=""
        punctuations='''{}-!"#$%&'()*+,./:;<=>?@\^_`|\[]'''
        for char in djtext:
            if char not in punctuations:
                analyzetext=analyzetext+char
                
        dict={'purpose':'Remove Punctuations','analyze':analyzetext}
        return render(request,"textanalyzerboots.html",dict)


    elif button2=="on":
        analyzetext=""
        analyzetext=djtext.upper()
        dict={'purpose':'UpperCase String','analyze':analyzetext}
        return render(request,"textanalyzerboots.html",dict)


    elif button3=="on":
        analyzetext=""
        analyzetext=djtext.lower()
        dict={'purpose':'LowerCase String','analyze':analyzetext}
        return render(request,"textanalyzerboots.html",dict)

    elif button4=="on":
        count=0
        for char in djtext:
            count=count+1
        
        dict={'purpose':'Character Count','analyze':count}
        return render(request,"textanalyzerboots.html",dict)


    elif button5=="on":
        analyzetext=""
        analyzetext=djtext[::-1]
        
        dict={'purpose':'Reverse the String','analyze':analyzetext}
        return render(request,"textanalyzerboots.html",dict)
    
    elif button6=="on":
        analyzetext=""
        analyzetext=" ".join(djtext.split())
                 
        dict={'purpose':'Remove Extraspaces','analyze':analyzetext}
        return render(request,"textanalyzerboots.html",dict)


      
    # if we do not tick any of the checkbox then we get the error only 
    else:
        return render(request,"error.html")


    
