from rest_framework.routers import SimpleRouter
from hadith import views


router = SimpleRouter()

router.register(r'book', views.BookViewSet, 'Book')
router.register(r'chapter', views.ChapterViewSet, 'Chapter')
router.register(r'collection', views.CollectionViewSet, 'Collection')
router.register(r'hadith', views.HadithViewSet, 'Hadith')
router.register(r'scholars', views.ScholarsViewSet, 'Scholars')
router.register(r'hadithnarrators', views.HadithNarratorsViewSet, 'HadithNarrators')
router.register(r'relatedhadiths', views.RelatedHadithsViewSet, 'RelatedHadiths')

urlpatterns = router.urls
