from django.shortcuts import render
from django.http import JsonResponse

from forms import RegistrationForm


# class Promise:
#     def __init__(self, url, method, data):
#         # ask server...
#         if method == 'POST':
#             requests.posts('....')
#         else:
#             requests.get(....)
#         # wait for response
#         self.complete(...)
#
#     def complete(self, result):
#         if result == 200:
#             self.done_callback()
#         else:
#             self.fail_callback()
#
#     def done(self, done_callback):
#         self.done_callback = done_callback
#
#     def fail(self, fail_callback):
#         self.fail_callback = fail_callback
#
# class JQuery:
#     def ajax(self, args):
#         url = args['url']
#         method = args['method']
#         data = args['data']
#         return Promise(url, method, data)

def index(request):
    ctx = {

    }
    return render(request, 'index.html', ctx)


def register(request):
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        print('Success!!!')
        return JsonResponse({
            'status': 'ok'
        })

    return JsonResponse({
        'status': 'error',
        'message': form.errors,
    })
