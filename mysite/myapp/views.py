from django.shortcuts import render

# Create your views here.
def home(request):
    import json
    import requests
    api_request=requests.get("https://api.github.com/users?since=0")
    api=json.loads(api_request.content)
    return render(request,'home.html',{"api":api})

# Create your views here.
def user(request):
    if request.method =='POST':
        import json
        import requests
        user=request.POST['user']
        user_request = requests.get("https://api.github.com/users/"+user)
        username = json.loads(user_request.content)
        return render(request,'user.html',{'username':username})
    else:
        notfound1 = "You can search githuber's profile here."
        notfound2 = "Plz input the username in the search box."
        return render(request,'user.html',{'notfound1':notfound1,'notfound2':notfound2})

