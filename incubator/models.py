from django.db import models


# Create your models here.
class App(models.Model):
    name = models.CharField(
        max_length=200,
        help_text="App name"
    )

    def likes(self):
        return AppLike.objects.filter(app_id=self.id).count()

    likes.short_description = 'Likes'

    def __str__(self):
        return self.name
        pass


class User(models.Model):
    id = models.CharField(primary_key=True, help_text="Unique ID for this particular book across whole library",
                          max_length=200)
    email = models.EmailField(blank=True)
    fcm_token = models.CharField(max_length=200, blank=True)
    android_version = models.CharField(max_length=2, blank=True)
    pass

    def __str__(self):
        return str(self.id)

    pass


class AppLike(models.Model):
    app_id = models.ForeignKey(App, on_delete=models.CASCADE)
    uid = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['app_id', 'uid'], name='App and User are unique together')
        ]

    def __str__(self):
        return str(self.uid.id) + " likes " + self.app_id.name

    pass


class SeerahTopic(models.Model):
    name = models.CharField(
        max_length=200,
        help_text="Topic name"
    )

    def __str__(self):
        return self.name
        pass


class SeerahQuestion(models.Model):
    topic_id = models.ForeignKey(SeerahTopic, on_delete=models.CASCADE)

    question = models.CharField(
        max_length=200,
        help_text="Topic name"
    )
    answer = models.TextField()

    def __str__(self):
        return self.question
        pass


class Dictionary(models.Model):
    word = models.CharField(
        max_length=200,
        help_text="Arabic Word"
    )
    word_diacless = models.CharField(
        max_length=200,
        help_text="Arabic Word Diacless"
    )
    description = models.TextField()

    def __str__(self):
        return self.word
        pass


def fetchArticles():
    import csv
    import os
    path = "C:\\Users\HP\Desktop"
    os.chdir(path)
    print(path)
    from incubator.models import SeerahTopic
    with open('topics.csv', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        print(reader.fieldnames)
        for row in reader:
            print("there was a problem with line")
            p = SeerahTopic(id=row['topic_id'], name=row['topic_name'])
            p.save()
    exit()
