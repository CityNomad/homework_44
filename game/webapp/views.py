from django.shortcuts import render
from urllib.parse import parse_qs
from webapp.checker import Check

# Create your views here.


res_list = []

def form_view(request):
    context = {
    }

    if request.method == "GET":
        return render(request, "form.html")
    else:
        context_line = request.POST.get("numbers")
        if context_line:
            context_str = context_line.split()
            game = Check()
            error = game.checker_list(context_str)
            if error:
                context["error"] = error
                return render(request, "form.html", context)
            else:
                result = game.get_result()
                context["result"] = result
                context['entered_nums'] = context_line
                response_line = f'You have entered: {context_line}.'
                result_line = " ".join([result, response_line])
                res_list.append(result_line)
                return render(request, "form.html", context)

def history_view(request):

    context = {"results": res_list,}

    if request.method == "GET":
        return render(request, "history.html", context)