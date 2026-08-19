from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.core.paginator import Paginator

from .forms import ImageForm
from .models import Comment, Follow, Image, Like


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})

@login_required
def home(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            picture = form.save(commit=False)
            picture.user = request.user
            picture.save()
            return redirect("home")

    else:
        form = ImageForm()

    images = (
        Image.objects
        .select_related("user")
        .prefetch_related("likes", "comments__user")
        .order_by("-date")
    )

    # 12 posts per page
    paginator = Paginator(images, 12)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    liked_image_ids = set(
        Like.objects.filter(
            user=request.user,
            image__in=page_obj.object_list
        ).values_list("image_id", flat=True)
    )

    return render(
        request,
        "myapp/home.html",
        {
            "img": page_obj.object_list,
            "form": form,
            "liked_image_ids": liked_image_ids,
            "page_obj": page_obj,
        },
    )


@login_required
def toggle_like(request, image_id):
    if request.method != "POST":
        return redirect("home")

    image = get_object_or_404(Image, id=image_id)
    like, created = Like.objects.get_or_create(user=request.user, image=image)
    if not created:
        like.delete()

    return redirect(request.META.get("HTTP_REFERER") or "home")


@login_required
def add_comment(request, image_id):
    if request.method == "POST":
        image = get_object_or_404(Image, id=image_id)
        text = request.POST.get("text", "").strip()
        if text:
            Comment.objects.create(user=request.user, image=image, text=text[:500])

    return redirect(request.META.get("HTTP_REFERER") or "home")

@login_required
def profile(request, username):
    profile_user = get_object_or_404(User, username=username)

    images = (
        Image.objects
        .filter(user=profile_user)
        .prefetch_related("likes", "comments__user")
        .order_by("-date")
    )

    liked_image_ids = set(
        Like.objects
        .filter(user=request.user, image__in=images)
        .values_list("image_id", flat=True)
    )

    return render(
        request,
        "myapp/profile.html",
        {
            "profile_user": profile_user,
            "img": images,
            "liked_image_ids": liked_image_ids,
        },
    )

@login_required
def search_users(request):
    query = request.GET.get("q", "").strip()

    users = User.objects.filter(
        username__icontains=query
    ) if query else User.objects.none()

    return render(
        request,
        "myapp/search.html",
        {
            "query": query,
            "users": users,
        },
    )

@login_required
def delete_image(request, image_id):
    if request.method != "POST":
        return redirect("home")

    image = get_object_or_404(Image, id=image_id)

    # Only the owner can delete the photo
    if image.user != request.user:
        return redirect("home")

    image.delete()

    return redirect(request.META.get("HTTP_REFERER") or "home")

@login_required
def delete_comment(request, comment_id):
    if request.method != "POST":
        return redirect("home")

    comment = get_object_or_404(Comment, id=comment_id)

    # Only the comment author can delete it
    if comment.user != request.user:
        return redirect("home")

    comment.delete()

    return redirect(request.META.get("HTTP_REFERER") or "home")