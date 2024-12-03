import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Accounts
from .backend.accounts.user_account import User_account, UnauthorizedActionError

# Create your views here.

def command_page(request):
    return render(request, 'command_page.html')

@csrf_exempt # Disabling CSRF for testing purposes, but in production, use the CSRF token
def execute_command(request):
    print('execute_command iniciado')
    
    if request.method == 'POST':
        try:
            
            print(f"Request body: {request.body}")

            data = json.loads(request.body)

            print(f"data: {data}")

            command = data.get('command')
            parameter = data.get('parameter')

            if not command or not parameter:
                print('Missing command or parameter')
                return JsonResponse({'error': 'Command or parameter missing'}, status=400)

            function_name = f'{command}_{parameter}'

            print(f"function name: {function_name}")
            
            function = globals().get(function_name)

            print(f"function: {function}")

            if function:
                
                print(f"Executing function: {function_name}")

                return function(request)
            else:
                
                print(f"Unrecognized command: {function_name}")

                return JsonResponse({'error': 'Unrecognized command'}, status=400)

        except json.JSONDecodeError as e:

            print(f"JSON Decode Error: {str(e)}"
                  )
            return JsonResponse({'error': 'Error processing JSON data'}, status=400)
        
        except Exception as e:

            print(f"Unhandled exception: {str(e)}")

            return JsonResponse({'error': f'Error: {str(e)}'}, status=500)
    else:

        print(f"Method not allowed: {request.method}")

        return JsonResponse({'error': 'HTTP method not allowed'}, status=405)
    
# Account
def add_account(request): #testado, funcional, necessita verificar lógica e segurança

    print('add_account executado')

    user = request.user

    print(f'user recebido: {user}')

    action = "create_account"

    print(f'action recebido: {action}')

    if not user.is_authenticated:
        print('user not authenticated or not loged')
        creator = None
    else:
        print('user authenticated')
        creator = user
    
    print(f'add_account user:{user}, action:{action}, creator: {creator}')

    try:
        if creator is None:
            print("creator is None")
            new_user_account = User_account()
            print('account criado')
            account_data = new_user_account.to_dict()
            print('account to dict')
            Accounts.objects.create(user_data=account_data)
            print('account colocado no accounts')
            
            print("message: Account created without authentication.")
            return JsonResponse({"message": "Account created without authentication."}, status=201)

        # Verifica se o usuário tem permissão para criar a conta
        user.check_permission(action)
        print(f"creator is {user}")
        new_user_account = User_account(creator=creator)
        print('account criado')
        account_data = new_user_account.to_dict()
        print('account to dict')
        Accounts.objects.create(user_data=account_data)
        print('account colocado no accounts')

        print("message: Account added successfully.")
        return JsonResponse({"message": "Account added successfully."}, status=201)

    except UnauthorizedActionError as e:
        # Caso o usuário não tenha permissão
        print(f"message: {str(e)}")
        return JsonResponse({"message": str(e)}, status=403)
    except Exception as e:
        # Outros erros
        print(f"message: Error: {str(e)}")
        return JsonResponse({"message": f"Error: {str(e)}"}, status=500)
    
def remove_account(request): #necessita testar e verificar lógica

    print('remove_account executado')

    user = request.user
    print(f'user recebido: {user}')

    action = "delete_account"
    print(f'action recebido: {action}')

    if not user.is_authenticated:
        print('user not authenticated or not logged')
        return JsonResponse({"message": "Authentication required to remove an account."}, status=401)

    try:
        # Verifica se o usuário tem permissão para remover a conta
        user.check_permission(action)
        print(f'Usuário autorizado para {action}')

        # Obtém o identificador da conta a ser removida
        account_id = request.GET.get('account_id')  # Supondo que o ID venha na query string
        print(f'account_id recebido: {account_id}')

        if not account_id:
            print('Nenhum account_id fornecido')
            return JsonResponse({"message": "Account ID is required."}, status=400)

        # Verifica se a conta existe
        try:
            account = Accounts.objects.get(id=account_id)
            print(f'Conta encontrada: {account}')
        except Accounts.DoesNotExist:
            print(f'Account com id {account_id} não encontrada')
            return JsonResponse({"message": "Account not found."}, status=404)

        # Verifica se o usuário tem relação com a conta antes de removê-la
        if account.user_data.get("creator") != str(user.id):
            print(f'Usuário {user.id} não é o criador da conta {account_id}')
            return JsonResponse({"message": "You do not have permission to delete this account."}, status=403)

        # Remove a conta
        account.delete()
        print(f'Account com id {account_id} removida com sucesso')

        return JsonResponse({"message": "Account removed successfully."}, status=200)

    except UnauthorizedActionError as e:
        # Caso o usuário não tenha permissão
        print(f"message: {str(e)}")
        return JsonResponse({"message": str(e)}, status=403)
    except Exception as e:
        # Outros erros
        print(f"message: Error: {str(e)}")
        return JsonResponse({"message": f"Error: {str(e)}"}, status=500)



def find_account(request):
    return JsonResponse({"message": "Find account logic will be implemented here."})

# Permission
def add_permission(request):
    return JsonResponse({"message": "Add permission logic will be implemented here."})

def remove_permission(request):
    return JsonResponse({"message": "Remove permission logic will be implemented here."})

def find_permission(request):
    return JsonResponse({"message": "Find permission logic will be implemented here."})

# Enterprise
def add_enterprise(request):
    return JsonResponse({"message": "Add enterprise logic will be implemented here."})

def remove_enterprise(request):
    return JsonResponse({"message": "Remove enterprise logic will be implemented here."})

def find_enterprise(request):
    return JsonResponse({"message": "Find enterprise logic will be implemented here."})

# Department Sector
def add_department_sector(request):
    return JsonResponse({"message": "Add department sector logic will be implemented here."})

def remove_department_sector(request):
    return JsonResponse({"message": "Remove department sector logic will be implemented here."})

def find_department_sector(request):
    return JsonResponse({"message": "Find department sector logic will be implemented here."})

# Role
def add_role(request):
    return JsonResponse({"message": "Add role logic will be implemented here."})

def remove_role(request):
    return JsonResponse({"message": "Remove role logic will be implemented here."})

def find_role(request):
    return JsonResponse({"message": "Find role logic will be implemented here."})

# Team
def add_team(request):
    return JsonResponse({"message": "Add team logic will be implemented here."})

def remove_team(request):
    return JsonResponse({"message": "Remove team logic will be implemented here."})

def find_team(request):
    return JsonResponse({"message": "Find team logic will be implemented here."})

# Service
def add_service(request):
    return JsonResponse({"message": "Add service logic will be implemented here."})

def remove_service(request):
    return JsonResponse({"message": "Remove service logic will be implemented here."})

def find_service(request):
    return JsonResponse({"message": "Find service logic will be implemented here."})

# Product
def add_product(request):
    return JsonResponse({"message": "Add product logic will be implemented here."})

def remove_product(request):
    return JsonResponse({"message": "Remove product logic will be implemented here."})

def find_product(request):
    return JsonResponse({"message": "Find product logic will be implemented here."})

# App
def add_app(request):
    return JsonResponse({"message": "Add app logic will be implemented here."})

def remove_app(request):
    return JsonResponse({"message": "Remove app logic will be implemented here."})

def find_app(request):
    return JsonResponse({"message": "Find app logic will be implemented here."})

# Module
def add_module(request):
    return JsonResponse({"message": "Add module logic will be implemented here."})

def remove_module(request):
    return JsonResponse({"message": "Remove module logic will be implemented here."})

def find_module(request):
    return JsonResponse({"message": "Find module logic will be implemented here."})

# Process
def add_process(request):
    return JsonResponse({"message": "Add process logic will be implemented here."})

def remove_process(request):
    return JsonResponse({"message": "Remove process logic will be implemented here."})

def find_process(request):
    return JsonResponse({"message": "Find process logic will be implemented here."})

# Artifact
def add_artifact(request):
    return JsonResponse({"message": "Add artifact logic will be implemented here."})

def remove_artifact(request):
    return JsonResponse({"message": "Remove artifact logic will be implemented here."})

def find_artifact(request):
    return JsonResponse({"message": "Find artifact logic will be implemented here."})

# Information
def add_information(request):
    return JsonResponse({"message": "Add information logic will be implemented here."})

def remove_information(request):
    return JsonResponse({"message": "Remove information logic will be implemented here."})

def find_information(request):
    return JsonResponse({"message": "Find information logic will be implemented here."})

# Routine
def add_routine(request):
    return JsonResponse({"message": "Add routine logic will be implemented here."})

def remove_routine(request):
    return JsonResponse({"message": "Remove routine logic will be implemented here."})

def find_routine(request):
    return JsonResponse({"message": "Find routine logic will be implemented here."})

# Person
def add_person(request):
    return JsonResponse({"message": "Add person logic will be implemented here."})

def remove_person(request):
    return JsonResponse({"message": "Remove person logic will be implemented here."})

def find_person(request):
    return JsonResponse({"message": "Find person logic will be implemented here."})

# Operand
def add_operand(request):
    return JsonResponse({"message": "Add operand logic will be implemented here."})

def remove_operand(request):
    return JsonResponse({"message": "Remove operand logic will be implemented here."})

def find_operand(request):
    return JsonResponse({"message": "Find operand logic will be implemented here."})

# Storage
def add_storage(request):
    return JsonResponse({"message": "Add storage logic will be implemented here."})

def remove_storage(request):
    return JsonResponse({"message": "Remove storage logic will be implemented here."})

def find_storage(request):
    return JsonResponse({"message": "Find storage logic will be implemented here."})