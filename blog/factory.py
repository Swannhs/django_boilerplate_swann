from blog import models
import factory


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Post

    title = factory.Faker('sentence')
    content = factory.Faker('text')
