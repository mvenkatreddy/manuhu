from django.conf.urls import patterns, url


urlpatterns = patterns(
    'registration.views',
    url(r'^registration/$','registrationuser', name="user_registration"),
    url(r'^logout/$', 'accounts_logout', name="accounts_logout"),
    url(r'^login/$', 'accounts_login', name='accounts_login'),
    url(r'^signin/$', 'accounts_signin', name="accounts_signin"),
    url(r'^pdf/$', 'some_view', name="some_view"),
    url(r'^pdf_view/$', 'pdf_view', name="pdf_view"),
    )
