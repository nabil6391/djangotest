from rest_framework.routers import SimpleRouter
from incubator import views


router = SimpleRouter()

router.register(r'app', views.AppViewSet, 'App')
router.register(r'user', views.UserViewSet, 'User')
router.register(r'applike', views.AppLikeViewSet, 'AppLike')
router.register(r'seerahtopic', views.SeerahTopicViewSet, 'SeerahTopic')
router.register(r'seerahquestion', views.SeerahQuestionViewSet, 'SeerahQuestion')
router.register(r'dictionary', views.DictionaryViewSet, 'Dictionary')

urlpatterns = router.urls
