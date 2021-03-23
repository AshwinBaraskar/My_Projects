from django.http import HttpResponse
import datetime


def datetime_info(request):
    date = datetime.datetime.now()
    h = int(date.strftime("%H"))
    msg = '<h1>Hello Word Very '
    if h < 12:
        msg = msg + "Good Morning"
    if h < 16:
        msg = msg + "Good Afternoon"
    if h < 21:
        msg = msg + "Good evening"
    else:
        msg = msg + "Good Night"

    msg = msg + '<br> Now server time is ' + str(date) + '</h1>'
    return HttpResponse(msg)
