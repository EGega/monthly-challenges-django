from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
  "january": "Eat no meat for the entire month!",
  "february": "Walk for at least 20 minutes every day",
  "march": "Work and learn Django well",
  "april": "Try not to tell a single lie during the first two weeks",
  "may": "Visit two countries",
  "june": "Get a new job",
  "july": "Buy a new house",
  "august": "Go to the maldives",
  "september": "Make a very long hiking tour",
  "october": "Do not consume sugar at all",
  "november": "Go to the gym everyday",
  "december": "Get rid of social media usage at all",
}

# Create your views here.

# def january(request):
#   return HttpResponse("Eat no meat for two weeks")

# def february(request):
#   return HttpResponse("Work for 20 minutes each day")

# def march(request):
#   return HttpResponse("Do not touch your phone")
def index(request):
  # response_date = """ this is a very hardcoded and not useful way of doing things
  # <ul>
  #   <li> <a href="/challenges/january">January<a/></li>
  #   <li> <a href="/challenges/february">February<a/></li>
  #   <li> <a href="/challenges/march">March<a/></li>
  #   <li> <a href="/challenges/april">April<a/></li>
  #   <li> <a href="/challenges/may">May<a/></li>
  # </ul>
  # """
  list_items = ""
  months = list(monthly_challenges.keys())
  for month in months:
    month_path = reverse("month-challenge", args=[month])
    list_items += f'<li> <a href="{month_path}" target="_blank">{month.capitalize()}<a/></li>'
  response_date = f"<ul>{list_items}</ul>"
  return HttpResponse(response_date)


def monthly_challenge_by_number(request, month):
  months = list(monthly_challenges.keys())
  
  if month > len(months):
    return HttpResponseNotFound("The only accepted months are from 1-12")
  redirect_month = months[month - 1]
  redirect_path = reverse("month-challenge", args=[redirect_month])
  return HttpResponseRedirect(redirect_path)
  

def monthly_challenge(request, month):
   try:
    challenge_text = monthly_challenges[month]
    response_data = f"<h1>{challenge_text}</h1>"
    return HttpResponse(response_data)
   except:
    return HttpResponseNotFound("<h1 style='color: red'>It seems like you entered a wrong value</h1>")

  