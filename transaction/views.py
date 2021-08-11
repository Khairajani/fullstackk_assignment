from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status

from .models import Transaction, TransactionItemDetail, Inventory, BranchMaster, DepartmentMaster, CompanyLedgerMaster, ArticleMaster, ColorMaster
from .serializers import TransactionSerializer, TransactionItemDetailSerializer, InventorySerializer
from datetime import datetime
import datetime

# Create your views here.
class home(APIView):
    @method_decorator(csrf_exempt)
    
    def get(self, request):
        response = {"message":"Home is working", "status":status.HTTP_200_OK}
        return Response(response)

class addtransaction(APIView):
    @method_decorator(csrf_exempt)   

    def get(self, request):
        response = {"message":"add-transaction is working. please send POST request with transaction details to add your transaction", "status":status.HTTP_200_OK}
        return Response(response)

    def post(self, request):
        try:
            data = request.data.dict()

            try:
                c_name = data['company']

                try:
                    
                    b_name = data['branch']

                    try: 
                        d_name = data['department']

                        try:
                            
                            company = CompanyLedgerMaster.objects.get(name=c_name)
                            data['company'] = company.id
                            
                            branch = BranchMaster.objects.get(short_name=b_name)
                            data['branch'] = branch.id

                            department = DepartmentMaster.objects.get(name=d_name)
                            data['department'] = department.id

                            curr_year = datetime.datetime.now().year
                            con = Constant()
                            
                            if curr_year!=con.year:
                                con.year = curr_year
                                con.cnt = 1
                            else:
                                con.cnt+=1
                            
                            data['transaction_number']= "TRN/"+str(con.cnt)+"/"+str(con.year)

                            serializer = TransactionSerializer(data=data)
                            if serializer.is_valid():
                                con.change_conf()
                                trn = serializer.save()                                
                                # trn=serializer.data
                                response = {"data":{'trn_id':trn.id,'trn_number':trn.transaction_number,'company':c_name, 'branch':b_name, 'department':d_name},"status":status.HTTP_201_CREATED}
                                return Response(response, status=status.HTTP_201_CREATED)

                            else:
                                response = {"message":serializer.errors,"status":status.HTTP_400_BAD_REQUEST}
                                return Response(response, status=status.HTTP_400_BAD_REQUEST)

                        except Exception as e:
                            
                            response = {"message":str(e),"status":status.HTTP_400_BAD_REQUEST}
                            return Response(response, status=status.HTTP_400_BAD_REQUEST)         

                    except:
                        response = {"message":{"department": ["This field is required."]}, "status" : status.HTTP_400_BAD_REQUEST}
                        return Response(response, status=status.HTTP_400_BAD_REQUEST)     
                        
                except:
                    response = {"message":{"branch": ["This field is required."]}, "status" : status.HTTP_400_BAD_REQUEST}
                    return Response(response, status=status.HTTP_400_BAD_REQUEST)    

            except:
                response = {"message":{"company": ["This field is required."]} , "status" : status.HTTP_400_BAD_REQUEST}
                return Response(response, status=status.HTTP_400_BAD_REQUEST)    
            
        except:
            response = {"message":"empty request", "status" : status.HTTP_400_BAD_REQUEST}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

class addtransactionitem(APIView):
    @method_decorator(csrf_exempt)   

    def get(self, request):
        response = {"message":"add-transaction-item working. please send POST request with item details to add items", "status" : status.HTTP_200_OK}
        return Response(response)

    def post(self, request):
        try:
            data = request.data.dict()

            try:
                t_num = data['transaction_number']

                try:
                    
                    a_name = data['article']

                    try: 
                        c_name = data['colour']

                        try:
                            transaction = Transaction.objects.get(transaction_number = t_num)
                            data['transaction_id'] = transaction.id

                            article = ArticleMaster.objects.get(name=a_name)
                            data['article'] = article.id

                            colour = ColorMaster.objects.get(article=article,name=c_name)
                            data['colour'] = colour.id

                            serializer = TransactionItemDetailSerializer(data=data)
                            if serializer.is_valid():
                                
                                trnItem = serializer.save()                                
                                # trn=serializer.data
                                response = {'data':{'trn_item_id':trnItem.id,'trn_item_article':a_name, 'trn_item_colour':c_name} , "status" : status.HTTP_201_CREATED}
                                return Response(response, status=status.HTTP_201_CREATED)

                            else:
                                response = {"message":serializer.errors, "status" : status.HTTP_400_BAD_REQUEST}
                                return Response(response, status=status.HTTP_400_BAD_REQUEST)

                        except Exception as e:
                            
                            response = {"message":str(e), "status" : status.HTTP_400_BAD_REQUEST}
                            return Response(response, status=status.HTTP_400_BAD_REQUEST)         

                    except:
                        response = {"message":{"colour": ["This field is required."]} , "status" : status.HTTP_400_BAD_REQUEST}
                        return Response(response, status=status.HTTP_400_BAD_REQUEST)     
                        
                except:
                    response = {"message":{"acticle": ["This field is required."]} , "status" : status.HTTP_400_BAD_REQUEST}
                    return Response(response, status=status.HTTP_400_BAD_REQUEST)    

            except:
                response = {"message":{"transaction_number": ["This field is required."]} , "status" : status.HTTP_400_BAD_REQUEST}
                return Response(response, status=status.HTTP_400_BAD_REQUEST)    
            
        except:
            response = {"message":"empty request", "status" : status.HTTP_400_BAD_REQUEST}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

class addinventory(APIView):
    @method_decorator(csrf_exempt)   

    def get(self, request):
        response = {"message":"add-inventory working. please send POST request with inventory details to add data to your inventory", "status" : status.HTTP_200_OK}
        return Response(response)

    def post(self, request):
        try:
            data = request.data.dict()

            try:
                t_id = data['transaction_item_id']

                try:
                    
                    a_name = data['article']

                    try: 
                        col_name = data['colour']

                        try: 
                            c_name = data['company']

                            try:
                                transaction = TransactionItemDetail.objects.get(id = t_id)
                                data['transaction_id'] = transaction.id

                                article = ArticleMaster.objects.get(name=a_name)
                                data['article'] = article.id

                                colour = ColorMaster.objects.get(article=article,name=col_name)
                                data['colour'] = colour.id

                                company = CompanyLedgerMaster.objects.get(name=c_name)
                                data['company'] = company.id

                                serializer = InventorySerializer(data=data)
                                if serializer.is_valid():
                                    
                                    invent = serializer.save()                                
                                    # trn=serializer.data
                                    response = {'data':{'invent_id':invent.id,'invent_article':a_name,'invent_colour':col_name, 'invent_company':c_name}, "status" : status.HTTP_201_CREATED}
                                    return Response(response, status=status.HTTP_201_CREATED)

                                else:
                                    response = {"message":serializer.errors, "status" : status.HTTP_400_BAD_REQUEST}
                                    return Response(response, status=status.HTTP_400_BAD_REQUEST)

                            except Exception as e:
                                response = {"message":str(e) , "status" : status.HTTP_400_BAD_REQUEST}
                                return Response(response, status=status.HTTP_400_BAD_REQUEST) 
                            
                        except:                            
                            response = {"message":{"company": ["This field is required."]}, "status" : status.HTTP_400_BAD_REQUEST}
                            return Response(response, status=status.HTTP_400_BAD_REQUEST)     

                    except:
                        response = {"message":{"colour": ["This field is required."]}, "status" : status.HTTP_400_BAD_REQUEST}
                        return Response(response, status=status.HTTP_400_BAD_REQUEST)     
                        
                except:
                    response = {"message":{"acticle": ["This field is required."]}, "status" : status.HTTP_400_BAD_REQUEST}
                    return Response(response, status=status.HTTP_400_BAD_REQUEST)    

            except:
                response = {"message":{"transaction_number": ["This field is required."]}, "status" : status.HTTP_400_BAD_REQUEST}
                return Response(response, status=status.HTTP_400_BAD_REQUEST)    
            
        except:
            response = {"message":"empty request", "status" : status.HTTP_400_BAD_REQUEST}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class gettransaction(APIView):
    @method_decorator(csrf_exempt)   

    def get(self, request):
        response = {"message":"transaction-view working. please send POST request with transaction_number to view transaction details", "status" : status.HTTP_200_OK}
        return Response(response)

    def post(self, request, format=None):
        try:
            data = request.data.dict()

            try:
                t_num = data['transaction_number']
                
                try:
                    transaction = Transaction.objects.get(transaction_number=t_num)
                    
                    try:
                        mydict = {'transaction_number':t_num, 'transaction_items':[]}
                        order_list = []
                        trn_item = TransactionItemDetail.objects.filter(transaction_id=transaction)
                        # trn_item_data = TransactionItemDetailSerializer(trn_item, many=True).data
                        
                        for order in trn_item:
                            trn_item_detail = TransactionItemDetailSerializer(order).data    
                            trn_item_detail['inventory_detail'] = []

                            cart = Inventory.objects.filter(transaction_item_id=order)
                            for c in cart:
                                cart_data = InventorySerializer(c).data    
                                trn_item_detail['inventory_detail'].append(cart_data)

                            mydict['transaction_items'].append(trn_item_detail)

                        order_list.append(mydict)
                            
                        if order_list:
                            response = {"data":order_list, "status" : status.HTTP_200_OK}              
                        else:
                            response = {"data":"inventory empty for given transaction", "status" : status.HTTP_400_BAD_REQUEST}

                        return Response(response) 

                    except Exception as e:
                        response = {"message":str(e), "status" : status.HTTP_400_BAD_REQUEST}               
                        return Response(response, status=status.HTTP_400_BAD_REQUEST)

                except:
                    response = {"message":"transaction with " + data['transaction_number'] + " not found", "status" : status.HTTP_400_BAD_REQUEST}
                    return Response(response, status=status.HTTP_400_BAD_REQUEST)

            except:
                response = {"message":{"transaction_number": ["This field is required."]}, "status" : status.HTTP_400_BAD_REQUEST}
                return Response(response, status=status.HTTP_400_BAD_REQUEST)    
            
        except:
            response = {"message":"empty request", "status" : status.HTTP_400_BAD_REQUEST}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

class deletetransaction(APIView):
    @method_decorator(csrf_exempt)   

    def get(self, request):
        response = {"message":"delete-transaction working please send POST request with transaction_number to delete the transaction", "status" : status.HTTP_200_OK}
        return Response(response)

    def post(self, request, format=None):
        try:
            data = request.data.dict()

            try:
                t_num = data['transaction_number']
                
                try:
                    transaction = Transaction.objects.get(transaction_number=t_num)
                    
                    try:
                        flag = 0
                        trn_item = TransactionItemDetail.objects.filter(transaction_id=transaction)                  
                        
                        for order in trn_item:
                            if Inventory.objects.filter(transaction_item_id=order).exists():
                                flag = 1
                                break
                        
                        if flag:
                            response = {"data":"Transation can't be deleted, as inventory exist", "status" : status.HTTP_200_OK}
                        else:
                            transaction.delete()
                            response = {"data":"Transation deleted", "status" : status.HTTP_200_OK}

                        return Response(response) 

                    except Exception as e:
                        response = {"message":str(e), "status" : status.HTTP_400_BAD_REQUEST}            
                        return Response(response, status=status.HTTP_400_BAD_REQUEST)

                except:
                    response = {"message":"transaction with " + data['transaction_number'] + " not found", "status" : status.HTTP_400_BAD_REQUEST}
                    return Response(response, status=status.HTTP_400_BAD_REQUEST)

            except:
                response = {"message":{"transaction_number": ["This field is required."]}, "status" : status.HTTP_400_BAD_REQUEST}
                return Response(response, status=status.HTTP_400_BAD_REQUEST)    
            
        except:
            response = {"message":"empty request", "status" : status.HTTP_400_BAD_REQUEST}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

class Constant:
    # file_path = os.path.join(settings.STATICFILES_DIRS,'conf.txt')

    def __init__(self):
        f = open('./static/conf.txt', "r")
        trn_num = f.read().split("\n")
        self.year,self.cnt = int(trn_num[0]), int(trn_num[1])
        
    def change_conf(self):        
        f = open('./static/conf.txt', "w")
        f.write(str(self.year)+"\n"+str(self.cnt))
        f.close()
