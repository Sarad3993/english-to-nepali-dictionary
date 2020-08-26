from django.shortcuts import render
from bs4 import BeautifulSoup 
import requests # to send GET requests 
 

def engtonepdict(request):
    if request.method == 'POST':
        word = request.POST['word']
        context = {'q':word}
        req = requests.get('https://www.englishnepalidictionary.com/',params=context).text
        soup = BeautifulSoup(req,'html.parser')
        nepali_meaning = soup.find(class_='search-result').h3.text.strip()
        context_view = {'nepali_meaning':nepali_meaning}
        return render(request,'index.html',context_view)
    return render(request,'index.html')
