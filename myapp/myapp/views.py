from django.http import HttpResponse
import os
import time
import subprocess

def htop_view(request):
    # Set your name and get system details
    name = "Manoj Bhaskar Reddy Kovvuri"  # Replace with your actual name
    username = os.getenv("USER") or "system_username"
    server_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    top_output = subprocess.getoutput("top -b -n 1")

    # Prepare HTML response
    html = f"""
    <h1>/htop</h1>
    <p>Name: {name}</p>
    <p>Username: {username}</p>
    <p>Server Time (IST): {server_time}</p>
    <pre>{top_output}</pre>
    """
    return HttpResponse(html)

