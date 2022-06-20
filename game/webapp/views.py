from django.shortcuts import render
from urllib.parse import parse_qs
from webapp.checker import Check

# Create your views here.

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
                print(context)
                return render(request, "form.html", context)


