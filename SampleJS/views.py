from django.shortcuts import render
from django.http import JsonResponse

from forms import RegistrationForm, StudentForm


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
    common_form = RegistrationForm(request.POST or None)
    result = {
        'status': 'ok',
        'message': {
        }
    }
    if not common_form.is_valid():
        result['status'] = 'error'
        result['message']['common'] = common_form.errors

    if 'role' in request.POST:
        if request.POST['role'] == 'student':
            student_form = StudentForm(request.POST or None)
            if not student_form.is_valid():
                result['status'] = 'error'
                result['message']['student'] = student_form.errors

        if request.POST['role'] == 'teacher':
            # ....
            teacher_result = {}
            if teacher_result:
                result['message']['teacher'] = teacher_result

    # {
    #     'message': {
    #         'common': {
    #             'username': ['This field is required'],
    #             'password': ['This field is required'],
    #         },
    #         'student': {
    #             'age': ['Value is too small']
    #         },
    #         'teacher': {
    #
    #         }
    #     }
    # }
    return JsonResponse(result)
