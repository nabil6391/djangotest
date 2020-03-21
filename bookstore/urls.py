from rest_framework.routers import SimpleRouter
from bookstore import views


router = SimpleRouter()

router.register(r'genre', views.GenreViewSet, 'Genre')
router.register(r'language', views.LanguageViewSet, 'Language')
router.register(r'book', views.BookViewSet, 'Book')
router.register(r'bookinstance', views.BookInstanceViewSet, 'BookInstance')
router.register(r'author', views.AuthorViewSet, 'Author')

urlpatterns = router.urls
