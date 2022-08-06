#from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def resume_curuculum (request):
  return HttpResponse ("""
<img src="https://i.ibb.co/d4Wp4B9/kitmedicament.jpg" />
<img src="https://i.ibb.co/xmgcR24/packmedicament.jpg" />
 """)

#un petit commentaire de cette urgence médicament codimed
