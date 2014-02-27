from django.shortcuts import render

from django.http import HttpResponse
from polls.models import Poll, Choice
from django.template import RequestContext, loader
# Create your views here.

def index_old(request):
    latest_poll_list=Poll.objects.order_by("-pub_date")[:5]
    template=loader.get_template(r"polls/index.html")
    context=RequestContext(request,{
        "latest_poll_list":latest_poll_list.reverse(), # reversed additionally
    })
    return HttpResponse(template.render(context))
##    output=r"<br>".join([p.question for p in latest_poll_list])
##    return HttpResponse(output)

def index(request):
    latest_poll_list=Poll.objects.order_by("-pub_date")[:5]
    context={"latest_poll_list":latest_poll_list}
    return render(request,r"polls/index.html",context)

def detail(request,poll_id):
    return HttpResponse("Here are the details of poll %s" % poll_id)

def vote(request,poll_id):
    return HttpResponse("You voted for poll %s" % poll_id)

def results(request,poll_id):
    return HttpResponse("Here are the results of Poll %s" % poll_id)