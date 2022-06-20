from django.shortcuts import render
from urllib.parse import parse_qs
from checker import Check

# Create your views here.

def form_view(request):
    if request.method == "GET":
        return render(request, "form.html")
    else:
        secret_nums = [2, 4, 6, 8]
        context_line = request.POST.get("numbers")
        context = {
            'secret_nums' : [2, 4, 6, 8],
            'bulls': 0,
            'cows': 0,
        }
        if context_line:
            context_str = context_line.split()
            nums = []
            try:
                for i in context_str:
                    i = int(i)
                    nums.append(i)
                    try:
                        nums_checked = Check()
                        if nums_checked.checker_list(nums):
                            context['nums'] = nums
                            return render(request, "form.html", context)
                    except ValueError:
                        context['response_line'] = "Please make sure you enter 4 numbers from 1 to 9 and don't repeat them"
                        return render(request, "form.html", context)
            except ValueError:
                context['response_line'] = "Please enter 4 numbers, not text"
                return render(request, "form.html", context)
        else:
            context['response_line'] = "Empty request is sent"
            return render(request, "form.html", context)





