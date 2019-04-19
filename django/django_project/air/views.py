#-*- coding:utf-8 -*-
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.conf import settings
from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from air.models import City, Region, Comment, Counter
from .forms import TellForm, GenForm, UploadForm
from django.views.generic.edit import FormView
from django.contrib import messages
import os, random, glob, datetime
#from PIL import Image, ImageDraw, ImageFont
from django.core.mail import EmailMessage, send_mail

def index(request):
    cities=City.objects.all()
    return render(request, 'index.html', locals())
    
def intro(request):
    return render(request,'intro.html', locals())
  
class IndexView(ListView):

    model = City
    template_name = 'NewTemIndex01N.html'
    context_object_name = 'cities' 
    
    def get_context_data(self,**kwargs):
        
        return super(IndexView, self).get_context_data(rr=Region.objects.all(), **kwargs)

def tellus(request):    
    message = " If you have any idea please feel free to tell us. "
    inhere = Counter.objects.get(id=4) #東引最後+1
    inhere.night6 = inhere.night6 + 1
    inhere.save()
    if request.method == 'POST':
        form = TellForm(request.POST)
        if form.is_valid():
            message = " Thanks for your feedback"
            visitor = form.cleaned_data['visitor']
            content = form.cleaned_data['content']
            email = form.cleaned_data['email']            
            
            mail_body = u'''
            姓名: {}
            信箱: {}
            意見: {}
            '''.format(visitor, email, content)
            
            #mailgun = EmailMultiAlternatives( '來自future image的反饋', mail_body, email, ['fennics1@gmail.com']) #主旨 內容 寄件人 收件人
            mailgun = EmailMessage( '來自future image的反饋', mail_body, email, ['mixtureq.tw@gmail.com'])
            mailgun.content_subtype = 'html'
            mailgun.send()
            
            Comment.objects.create(
            visitor = form.cleaned_data['visitor'],
            content = form.cleaned_data['content'],
            email = form.cleaned_data['email'],
            date_time = timezone.now(),)
            form = TellForm()
        else:
            message = '內容不正確YO'
    else:
        form = TellForm()

    return render(request, 'comment.html', locals())
 
"""
class TellView(FormView):
    form_class = TellForm 
    template_name = 'comment.html'
    success_url = '/tellus/'
    initial = {'content': u'香蕉00'}
    #model = Restaurant
    #context_object_name = 'r'
    
    def form_valid(self, form):
        Comment.objects.create(
            visitor = form.cleaned_data['visitor'],
            content = form.cleaned_data['content'],
            email = form.cleaned_data['email'],
            date_time = timezone.now(),)
            
        return self.render_to_response(self.get_context_data(form=self.form_class(initial=self.initial)))
"""         
            
"""        
    def get_context_data(self, **kwargs):
        self.object = self.get_object()
        return super(CommentView, self).get_context_data(object=self.object, **kwargs)
 
    @method_decorator(user_passes_test(user_can_comment, login_url='/accounts/login/'))
    def dispatch(self, request, *args, **kwargs):
        return super(CommentView, self).dispatch(request, *args, **kwargs)
"""
    
def local(request, city):
    try: 
        thecity=City.objects.get(english_name=city)
        id = thecity.id
        nextcity = City.objects.get(id=id+1)
        if id-1:
            prevcity = City.objects.get(id=id-1)
    except: 
        return HttpResponseRedirect("/")
    thecity.click = thecity.click + 1
    thecity.save()
    comment = Comment.objects.order_by('-date_time')
    aaa = ['01','02','03','04','05','06','07','08']   
    #rr = Region.objects.all()
    date_time = datetime.datetime.now()

    """判斷時間
    try:
        counter = Counter.objects.get(city=thecity)
    except:
        Counter.objects.create(city=thecity)
        return HttpResponseRedirect("/local/{}/{}".format(regionid, city))

    if date_time.day == 10:
        counter = Counter.objects.get(city=thecity)
        counter.night4 = counter.night4 + 1
    elif date_time.day == 11:
        if date_time.hour < 12:
            counter.morning5 = counter.morning5+1
        if date_time.hour > 12 and date_time.hour < 18:
            counter.afternoon5 = counter.afternoon5 + 1
        if date_time.hour < 24:
            counter.night5 = counter.night5 + 1
    else:
        if date_time.hour < 12:
            counter.morning6 = counter.morning6+1
        if date_time.hour > 12 and date_time.hour < 18:
            counter.afternoon6 = counter.afternoon6 + 1
        if date_time.hour < 24:
            counter.night6 = counter.night6 + 1
    counter.save()"""
    
    return render(request, "taipei_0816.html", locals())   
    
"""
def gen(request):
    messages.get_messages(request)
    backfiles = glob.glob(os.path.join(settings.BASE_DIR, 'static/backimages/*.jpg'))
    if request.method=='POST':
        ff=GenForm(request.POST)
        if ff.is_valid():
            saved_filename = mergepic(request.POST.get('backfile'),
                                      request.POST.get('msg'),
                                      int(request.POST.get('font_size')),
                                      int(request.POST.get('x')),
                                      int(request.POST.get('y')))
    else:
        ff = GenForm(backfiles)
        
    return render(request, "gen.html", locals())   

def mergepic(image_file, msg, font_size, x, y):
    fill = (0,0,0,255)
    image_file=Image.open(image_file)
    im_w,im_h = image_file.size
    im0 = Image.new('RGBA', (1,1))
    dw0 = ImageDraw.Draw(im0)
    font = ImageFont.truetype(os.path.join(settings.BASE_DIR, 'ACQUAINT.TTF'), font_size)
    fn_w, fn_h = dw0.textsize(msg,font=font)
    im = Image.new('RGBA', (fn_w, fn_h), (255,0,0,0))
    dw =ImageDraw.Draw(im)
    dw.text((0,0), msg, font=font, fill=fill)
    image_file.paste(im, (x, y), im)
    saved_filename = '456.jpg'
    image_file.save(os.path.join(settings.BASE_DIR, "media", saved_filename))
    return saved_filename
    
def save_backfile(f):
    target = os.path.join(settings.BASE_DIR, "media", '741.jpg')
    with open(target, 'wb') as des:
        for chunk in f.chunks():
            des.write(chunk)
    return os.path.basename(target)
    
def vip(request):
    messages.get_messages(request)
    custom_backfile = None
    if 'custom_backfile' in request.session:
        if len(request.session.get('custom_backfile')) > 0:
            custom_backfile = request.session.get('custom_backfile')

    if request.method=='POST':
        if 'change_backfile' in request.POST:
            upload_form = UploadForm(request.POST, request.FILES)
            if upload_form.is_valid():
                custom_backfile = save_backfile(request.FILES['file'])
                request.session['custom_backfile'] = custom_backfile
                messages.add_message(request, messages.SUCCESS, "檔案上傳成功！")
                return HttpResponseRedirect('/vip/')
            else:
                messages.add_message(request, messages.WARNING, "檔案上傳失敗！")
                return HttpResponseRedirect('/vip/')
        else:
            form = GenForm(request.POST)
            if custom_backfile is None:
                back_file = os.path.join(settings.BASE_DIR, 'static/backimages/back1.jpg')
            else:
                back_file = os.path.join(settings.BASE_DIR, 'media', custom_backfile)
            saved_filename = mergepic(back_file,
                                      request.POST.get('msg'), 
                                      int(request.POST.get('font_size')),
                                      int(request.POST.get('x')),
                                      int(request.POST.get('y')))
    else:
        form = GenForm()
        upload_form = UploadForm()

    return render(request, "gen.html", locals()) 
"""