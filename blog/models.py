from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

from config import settings


# Create your models here.

class CustomUser(AbstractUser):
    username = models.CharField(max_length=50, unique=True, null=True, blank=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(null=True, blank = True)
    address = models.CharField(max_length=100, null=True, blank=True)

class Category(models.Model):
    title = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title

class Article(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    photo = models.ImageField(upload_to="articles/", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    publish = models.BooleanField(default=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    def get_photo(self):
        try:
            return self.photo.url
        except:
            return "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMwAAADACAMAAAB/Pny7AAAAM1BMVEX///+/v7+8vLz8/Pz5+fnt7e3ExMTHx8fPz8/h4eHw8PD29vbY2Njn5+fMzMzU1NS2trYNfAMMAAAEIUlEQVR4nO2c2ZqjIBBGI+573v9pOyZMVHZaC6rn+8/ltAonlFAUmTweAAAAAAAAAFDNPWfqMkZmaEXBF9FVkGEJZLgCGa5AhiuQ4Qpkvjcz4DaZJXeW3PdTc5OMmGJupWE8deiSTNT2gQTISCBDCWQkkKEEMhLIUAIZCWQogYwEMpRARgIZSpLJpFBNIVMOU/F8scxRj48ngcy4yoKWEO1MOkD0MvWyXyWannJwyGWG5lz2pCyvUctU3bkeLUR9T8dNUMv0am1dLL8JtGoIedmoZfSDAjHHtCGZuyHgKmKZUT/0EGtMGx+qrgj5CIhltCh70UZPz+UkxBrQNWKZyXQcFS0zPAvRBsTZX5Apt3ZE778tg0wTK/N+iGhG74XEMrVhAlhi2tieIe/zL1DEMpU+MKKPaeP1CNlKwBRAvc6s+tD4w+XEHqneoaGWGQrFJjY5q9vwO8kTzVnJzZa4gRmX/dbW1ztymW3BO7qEpCUHpuMH4csC6PczZf+NNPGMHJdHfdpANJ6rU2ybx7X5fH9iic0xx/MG4un5KNIUNMa5n6Y5MsLeg3p+4TxTAOtSU61OhZ4pIL9Mbf1m+Lhoi5R7wc0uU3WN5U1Sg2xjcTaSW2ab6yw2daPLNM4sILfM0BY2G9NX89zb1Mwy5SfzMtmYNqmvLMA1O2eW+W4RNBtTkG24poC8MtX3CerYVEthxrURyCtzCCXFxrjf3ppxTQFZZYbj/adIswWZu52sMqcssmh3m7GzuTjLNDll1K3ON9JMy+V+mX0KyCgzqqH0fR/Oib96lb2TGWUmvZ/t26YyFA4O2KeARDKGv82Gd/w9Ns4gc7aUaD/Tawv3aFxINpu9hGGRsWYBaWT6olP/avv429odZIWjFpBE5rX7Fcr+vb7yPzxs5whJZPr3s4//UtpW+CBstYAkBY13WUIcI22+4mKtBaSQkRnY4TTTsCGOwzw0Kb7U8K9eJDrZB9/k68WSBSSQmfeL1o+NPY0MlTHXAuhljiEl3jbl1SCzHdbQy8ynXmyRdu3tlz3NIlMqC8pSja40MhjTFJD6SOMVad4VPgTjFEAu40m0fo2pq9QyN7wfFgwJGrFMeXUStrPq7RHL0A2MqRZALEM3MEWhJ2i0MrPehdswdJZUxlqWvAW9QE0qczWf9DCpvaWUqeylvDvQpwBKGeKB0U8ECGXUL87eznd/lEDGVBi72UaJMzqZy1vjABnlsIZOZlg7cqZUMo8yAecWc5823wpkJJChBDISyFACGQlkKIGM5P+VYfBjbXN/14+1sQMyXIEMVyDDFchwBTJcgQxXIMMVyHAFMlyBDFcgwxXIcAUyXIEMVyDDFchwBTJcgQxXIMMVyHAFMlyBDFcgw5VYma7hTMgPie9UQ82ZoF/fBwAAAAAAAIC/ww/JmYESURpw2wAAAABJRU5ErkJggg=="
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={"pk":self.pk})

class Comment(models.Model):
    description = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return self.description