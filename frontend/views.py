import requests
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

API_URL = "http://127.0.0.1:8000/api"

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        response = requests.post(
            f"{API_URL}/login/",
            json={"username": username, "password": password}
        )

        if response.status_code == 200:
            tokens = response.json()
            request.session['access'] = tokens['access']
            request.session['refresh'] = tokens['refresh']
            return redirect('dashboard')

        return render(request, "frontend/login.html", {"error": "Login inválido"})

    return render(request, "frontend/login.html")

@login_required
def dashboard_view(request):
    token = request.session.get('access')

    if not token:
        return redirect('login')

    headers = {"Authorization": f"Bearer {token}"}

    response = requests.get(
        f"{API_URL}/finance/transactions/",
        headers=headers
    )

    transactions = response.json() if response.status_code == 200 else []

    return render(
        request,
        "frontend/dashboard.html",
        {"transactions": transactions}
    )

def create_transaction(request):
    token = request.session.get('access')
    if not token:
        return redirect('login')

    if request.method == "POST":
        data = {
            "description": request.POST.get("description"),
            "value": request.POST.get("value"),
            "transaction_type": request.POST.get("transaction_type"),
            "date": request.POST.get("date"),
            "is_paid": request.POST.get("is_paid") == "on"
        }

        headers = {
            "Authorization": f"Bearer {token}"
        }

        response = requests.post(
            f"{API_URL}/finance/transactions/",
            json=data,
            headers=headers
        )

        if response.status_code == 201:
            return redirect('dashboard')

    return render(request, "frontend/create_transaction.html")

def delete_transaction(request, id):
    token = request.session.get('access')
    if not token:
        return redirect('login')

    headers = {
        "Authorization": f"Bearer {token}"
    }

    requests.delete(
        f"{API_URL}/finance/transactions/{id}/",
        headers=headers
    )

    return redirect('dashboard')



