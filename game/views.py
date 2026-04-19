from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Product, Conversation, ChatMessage


# 🏠 HOME
def home(request):
    products = Product.objects.all()

    search = request.GET.get('search')
    category = request.GET.get('category')

    if search:
        products = products.filter(name__icontains=search)

    if category:
        products = products.filter(category=category)

    return render(request, 'game/home.html', {'products': products})


# ➕ ADD PRODUCT
@login_required
def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        category = request.POST.get('category')
        image = request.FILES.get('image')

        Product.objects.create(
            name=name,
            price=price,
            category=category,
            image=image,
            owner=request.user
        )

        return redirect('home')

    return render(request, 'game/add.html')


# 🛒 ADD TO CART
def add_to_cart(request, id):
    cart = request.session.get('cart', [])

    id = int(id)

    if id not in cart:
        cart.append(id)

    request.session['cart'] = cart
    return redirect('home')


# 🛒 CART
def cart(request):
    cart = request.session.get('cart', [])

    products = Product.objects.filter(id__in=cart)
    total = sum(p.price for p in products)

    return render(request, 'game/cart.html', {
        'products': products,
        'total': total
    })


# ❌ REMOVE FROM CART (FIXED)
def remove_from_cart(request, id):
    cart = request.session.get('cart', [])

    try:
        id = int(id)
        if id in cart:
            cart.remove(id)
    except:
        pass

    request.session['cart'] = cart
    return redirect('cart')


# 🔐 REGISTER
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'game/register.html', {'form': form})


# 🔐 LOGIN
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request, 'game/login.html', {'form': form})


# 🔓 LOGOUT
def logout_view(request):
    logout(request)
    return redirect('home')


# 🗑️ DELETE PRODUCT
@login_required
def delete_product(request, id):
    product = get_object_or_404(Product, id=id)

    if product.owner == request.user:
        product.delete()

    return redirect('home')


# 🔍 PRODUCT DETAIL
def product_detail(request, id):
    product = get_object_or_404(Product, id=id)

    return render(request, 'game/detail.html', {
        'product': product
    })


# 💳 CHECKOUT → สร้างแชทกับ seller
@login_required
def checkout(request):
    cart = request.session.get('cart', [])
    products = Product.objects.filter(id__in=cart)

    for p in products:
        convo = Conversation.objects.filter(
            user1=request.user,
            user2=p.owner,
            product=p
        ).first()

        if not convo:
            convo = Conversation.objects.create(
                user1=request.user,
                user2=p.owner,
                product=p
            )

        ChatMessage.objects.create(
            conversation=convo,
            sender=request.user,
            text=f"สนใจสินค้า: {p.name}"
        )

    request.session['cart'] = []
    return redirect('chat_list')


# 📩 CHAT LIST
@login_required
def chat_list(request):
    chats = Conversation.objects.filter(user1=request.user) | Conversation.objects.filter(user2=request.user)

    return render(request, 'game/chat_list.html', {
        'chats': chats
    })


# 💬 CHAT DETAIL
@login_required
def chat_detail(request, id):
    convo = get_object_or_404(Conversation, id=id)

    messages = ChatMessage.objects.filter(conversation=convo)

    if request.method == 'POST':
        text = request.POST.get('text')

        if text:
            ChatMessage.objects.create(
                conversation=convo,
                sender=request.user,
                text=text
            )

        return redirect('chat_detail', id=id)

    return render(request, 'game/chat_detail.html', {
        'convo': convo,
        'messages': messages
    })

@login_required
def seller_inbox(request):
    # ดึงแชททั้งหมดที่ user เป็น "seller"
    chats = Conversation.objects.filter(user2=request.user).order_by('-id')

    return render(request, 'game/seller_inbox.html', {
        'chats': chats
    })

@login_required
def buy_now(request, id):
    product = get_object_or_404(Product, id=id)

    # หา / สร้างห้องแชท
    convo = Conversation.objects.filter(
        user1=request.user,
        user2=product.owner,
        product=product
    ).first()

    if not convo:
        convo = Conversation.objects.create(
            user1=request.user,
            user2=product.owner,
            product=product
        )

    # ส่งข้อความอัตโนมัติ
    ChatMessage.objects.create(
        conversation=convo,
        sender=request.user,
        text=f"สนใจสินค้า: {product.name}"
    )

    return redirect('chat_detail', id=convo.id)