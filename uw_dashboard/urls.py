from django.conf.urls import url, include

from .views import Homepage, UploadView, LoginView, AddUserView, MapView, LogoutView, SearchResultsView, SearchPage, SetPasswordView, Profile, DeleteUserView

urlpatterns = [
    url(r'^$', Homepage.as_view(), name='index'),
    url(r'^homepage.html$', Homepage.as_view(), name='homepage'),
    url(r'^upload.html$', UploadView.as_view(), name="upload"),
    url(r'^login.html$', LoginView.as_view(), name="login"),
    url(r'^logout.html$', LogoutView.as_view(), name="logout"),
    url(r'^addUser.html$', AddUserView.as_view(), name="addUser"),
    url(r'^map.html$', MapView.as_view(), name="map"),
    url(r'^searchResults.html$', SearchResultsView.as_view(), name='search-results'),
    url(r'^search-page.html$', SearchPage.as_view(), name='search-page'),
    url(r'^resetPassword.html$', SetPasswordView.as_view(), name="resetPassword"),
    url(r'^profile.html$', Profile.as_view(), name="profile"),
    url(r'^deleteUser.html$', DeleteUserView.as_view(), name="deleteUser"),
]
