from django.shortcuts import render
from django.views.generic import TemplateView
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import ensure_csrf_cookie


from .models import Human
# Create your views here.

class List(TemplateView):
    template_name = 'human_list.html'

    def get(self, request):
        all_humans = Human.objects.all()
        the_first_two = Human.objects.all()[:2]

        workers_google = Human.objects.filter(company='google')
        filtered = Human.objects.filter(birth__year=2020)

        ordered = Human.objects.all().order_by('birth')
        sorted = Human.objects.all().filter(birth__year__gte=2015).order_by('birth')
        sorted_salary = Human.objects.filter(salary__gte=100, salary__lte=3000).order_by('-salary')

        ctx = {
            'all_humans': all_humans,
            'the_first_two': the_first_two,
            'workers_google': workers_google,
            'filtered': filtered,
            'ordered': ordered,
            'sorted': sorted,
            'sorted_salary': sorted_salary,
        }

        return render(request, self.template_name, ctx)

        # @csrf_exempt 
        # @ensure_csrf_cookie
    def post(self, request):
        # print('\n\n')
        # print('\n post')
        # print(request)
        query = request.POST['search']
        # print(query)
        result_list = Human.objects.filter(company=query)
        print(result_list)

        if result_list.count() != 0:
            context = {
                'result_list': result_list,
                'query': query,
            }
        else:
            context = {
                'empty': "ничего не найдено",
                'query': query,
            }
        print(context)
        return render(request, 'result.html', context)
            


