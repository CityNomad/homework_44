from django.shortcuts import render
from urllib.parse import parse_qs

# Create your views here.

def form_view(request):
    if request.method == "GET":
        return render(request, "form.html")
    else:
        secret_nums = [2, 4, 6, 8]
        context_line = request.POST.get("numbers")
        context_str = context_line.split()
        nums = []
        try:
            for i in context_str:
                i = int(i)
                nums.append(i)
        except ValueError:
            response = "Please enter 4 numbers, not text"
            return render(request, "form.html", response)
        print(nums)
        # if context_line:
        #     numbers_str = context_line["numbers"][0].split()
        #     print(numbers_str)



