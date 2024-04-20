
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import HomepageView, DalleGenerationView, InteractionDetailView, GeneratorView, ProductViewSet

router = SimpleRouter()
router.register('product', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', HomepageView.as_view(), name='home-page'),  # home page
    path('generate/', DalleGenerationView.as_view(), name='generate'), # this is the url path to the generate images
    path('generate/<int:pk>', InteractionDetailView.as_view(), name='interaction_detail'),
    path('sidebar', GeneratorView.as_view(), name='sidebar'),
    # path('product', ProductViewset.as_view()),
    # path('product/<int:pk>', ProductDetail.as_view()),
]
