from django.shortcuts import render
from django.http import JsonResponse
from google import genai

client = genai.Client(api_key = 'AIzaSyAJ8nwGpP1WPl8CAuZPTwSSzQtc3KZti9w')

# Create your views here.
def index(request):
    return render(request, 'index.html')

def response(request):
    if request.method == 'POST':
        message = request.POST.get('message', '')

        answer = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=message
        )
        ans = answer.text.replace('**', '')
        ans = ans.replace('###', '\n\n')
        ans = ans.replace('*', '\n\n')

        return JsonResponse({'response' : ans})
    return JsonResponse({ 'response' : 'Invalid request'}, status = 400)



