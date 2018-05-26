from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.shortcuts import render ,get_object_or_404 ,redirect
from .forms import PostForm
from .models import Post

# Create your views here.


def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            #success message
            messages.success(request,'successfully created')
            return HttpResponseRedirect(instance.get_absolute_url())
        else:
            messages.error(request,'not successfully created')
    # Post, generate a blank form
    form = PostForm()
    return render(request,'post_form.html',{'form':form})


# that all for testing purposes
#     form = PostForm()
#     if request.method == 'POST':
#         # POST, generate form with data from the request
#         form = PostForm(request.POST)
#         # check if it's valid:
#         if form.is_valid():
#             instance = form.save(commit=False)
#             print(form.cleaned_data.get("title"))
#             instance.save()
#             return HttpResponseRedirect(render(request,'success_post.html',{'msg':'the form has been submitted!'}))
#         else:
#             #GET, generate blank form:
#             form = PostForm()
#     return render(request,'post_form.html',{'form':form})
#
#     # if request.method == 'POST':
#     #     print(request.POST.get("title"))
#     #     print(request.POST.get("content"))
#
#     # if request.user.is_authenticated:
#     #     context = {
#     #         'title': 'my user create'
#     #     }
#     # else:
#     #     context = {
#     #         'title': 'create'
#     #     }
# #
# # def post_success(request):
# #     context = {'msg':'your form data has been processed successfully!',}
# #     return render(request,'success_post.html',context)

def post_detail(request, id=None):
    queryset = Post.objects.all()
    instance = get_object_or_404(Post, id = id)
    # if request.user.is_authenticated:
    #     context = {
    #         'title': 'my user detail'
    #     }
    # else:
    #     context = {
    #         'title': 'Detail'
    #     }

    context = {
        'instance' : instance,
        'title': instance.title,
        'list_set': queryset,
    }
    return render(request,'post_detail.html',context)

def post_list(request):
    query_list = Post.objects.all() #.order_by("-timestamp")
    paginator = Paginator(query_list, 5)  # Show 10 contacts per page

    page = request.GET.get('page')
    queryset = paginator.get_page(page)

    # if request.user.is_authenticated:
    #     context = {
    #         'title': 'my user List',
    #
    #     }
    # else:
    #     context = {
    #         'title': instance.title,
    #         'content':instance.content
    #     }

    context = {
        'obj_list' : queryset,
        'title': 'List',


    }
    return render(request,'post_list.html',context)

def post_update(request,id=None):
    instance = get_object_or_404(Post, id = id)

    form = PostForm(request.POST or None, request.FILES or None ,instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        #success message
        messages.success(request,'Item Saved')
        return HttpResponseRedirect(instance.get_absolute_url())
    # Post, generate a blank form
    context = {
        'instance':instance,
        'title':instance.title,
        'form':form,
    }
    return render(request,'post_form.html',context)

def post_delete(request, id = None):
    instance = get_object_or_404(Post, id = id)
    instance.delete()
    #
    # if request.user.is_authenticated:
    #     context = {
    #         'title': 'my user delete'
    #     }
    # else:
    #     context = {
    #         'title': 'delete'
    #     }
    messages.success(request, 'successfully deleted')
    return redirect("posts:list")
