from django.db.models import query
from Banking_System.models import Customer, TransactionHistory
from django.shortcuts import redirect, render
from django.contrib import messages

# Create your views here.
def indexPage(request):
    return render(request,'index.html')

def customers(request):
    Customers=Customer.objects.all()
    return render(request,'customers.html',{'customers':Customers})

def transfer(request):
    Customers=Customer.objects.all()
    return render(request,'transfermoney.html',{'customers':Customers})

def transfernow(request,myid):
    # messages.success(request, 'Welcome To Transaction Page')
    transact=Customer.objects.filter(id=myid)
    Customers=Customer.objects.all()


    if request.method == "POST":
        sendername=request.POST.get('from')
        receivername=request.POST.get('to')
        amount=request.POST.get('amount')
      
        try:
            amount = int(amount)

        except:
            print("enter amount")

        for i in Customers:
            if(i.name==receivername):
                j=i
                receiverid=i.id
                break

        for i in Customers:

            if amount>=i.balance:
                messages.error(request,'Invalid Data,   You have exceeded the maximum transaction limit set by your bank!!')
                break

            if i.name==sendername and amount<i.balance and amount>0:
                avail_bal1=i.balance-amount
                avail_bal2=j.balance+amount

                try:
                    query1=Customer(id=i.id,name=i.name,email=i.email,balance=avail_bal1)

                    query2=Customer(id=receiverid,name=j.name,email=j.email,balance=avail_bal2)

                    query3=TransactionHistory(senderName=sendername,receiverName=receivername,amount=amount)

                    query1.save()
                    query2.save()
                    query3.save()

                    return redirect('/transactionhistory')

                except:
                    messages.error(request, 'Transaction Failed')
                    print("Transaction Failed")
                    break

            else:
                print("Invalid Data")
            
    return render(request,'transfernow.html',{'transact':transact,'customers':Customers})


def history(request):
    TransactionDetail=TransactionHistory.objects.all()
    return render(request,'transactionhistory.html',{'transactiondetail':TransactionDetail})

