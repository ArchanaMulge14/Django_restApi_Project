from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    dob = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email

class Paragraph(models.Model):
    text = models.TextField()
    user_id = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    def save(self, *args, **kwargs):
        # Tokenize text and index words against paragraph ID
        super().save(*args, **kwargs)
        words = self.text.lower().split()
        for word in words:
            # Create or update index for word
            WordIndex.objects.update_or_create(
                word=word,
                defaults={'paragraph_id': self.id}
            )

class WordIndex(models.Model):
    word = models.CharField(max_length=255)
    paragraph = models.ForeignKey(Paragraph, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('word', 'paragraph')


def tokenize_and_index_paragraph(paragraph):
    words = paragraph.text.lower().split()
    for word in words:
        WordIndex.objects.update_or_create(
            word=word,
            paragraph=paragraph
        )

def search_paragraphs_by_word(word):
    # Convert the word to lowercase
    word = word.lower()

    # Search for the word in WordIndex and get the top 10 paragraphs
    paragraphs = (Paragraph.objects.filter(wordindex__word=word)
                  .annotate(word_count=models.Count('wordindex'))
                  .order_by('-word_count')[:10])
    
    return paragraphs
