from django.shortcuts import render, redirect
from .models import LoginCMSInfo


def loginCMS(request):
    # Eğer kullanıcı zaten giriş yaptıysa, ana sayfaya yönlendir
    if 'user_authenticated' in request.session:
        return redirect('cmsDashboard')  # Dashboard'a yönlendir

    # Kullanıcı giriş yapmadıysa, login sayfasını göster
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Kullanıcı doğrulama
        try:
            user = LoginCMSInfo.objects.get(username=username, password=password)
            # Giriş başarılı, oturum açma
            request.session['user_authenticated'] = True
            return redirect('cmsDashboard')  # Giriş başarılıysa dashboard'a yönlendir
        except LoginCMSInfo.DoesNotExist:
            # Kullanıcı bulunamadıysa hata mesajı
            return render(request, 'loginCMS.html', {'error': 'Geçersiz kullanıcı adı veya parola!'})

    return render(request, 'loginCMS.html')

def logoutCMS(request):
    # Oturum bilgisini temizle
    request.session.flush()
    return redirect('loginCMS')  # Kullanıcıyı login sayfasına yönlendir
