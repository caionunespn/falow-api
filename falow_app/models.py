from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
  name = models.CharField(verbose_name="Nome", db_column = "name", max_length=300, blank = False, null = False)
  user = models.OneToOneField(User, verbose_name="Usuário", db_column="user", on_delete=models.CASCADE, blank=True, null=True)
  profile_photo = models.ImageField(verbose_name="Foto", db_column="profile_photo", max_length=250, blank= True, null=True, default=None, upload_to='user/profile_photos')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    db_table = "profile"
    verbose_name = "Perfil"
    verbose_name_plural = "Perfis"

  def __str__(self):
    return self.name

class Post(models.Model):
  description = models.CharField(verbose_name="Postagem", db_column = "description", max_length = 5000, blank = False, null = False)
  profile = models.ForeignKey(Profile, verbose_name = "Perfil", db_column = "profile", on_delete=models.CASCADE, blank = False, null = False)
  comments_count = models.IntegerField(verbose_name="Número de comentários", db_column = "comments_count", blank = True, null = True, default = 0)
  likes_count = models.IntegerField(verbose_name="Número de curtidas", db_column = "likes_count", blank = True, null = True, default = 0)

  class Meta:
    db_table = "post"
    verbose_name = "Postagem"
    verbose_name_plural = "Postagens"

  def __str__(self):
    return self.name

class Like(models.Model):
  user = models.ForeignKey(User, verbose_name="Usuário", db_column="user", on_delete=models.CASCADE, blank=True, null=True)
  post = models.ForeignKey(Post, verbose_name="Postagem", db_column="post", on_delete=models.CASCADE, blank=True, null=True)

  class Meta:
      db_table = "like"
      verbose_name = "Curtida"
      verbose_name_plural = "Curtidas"

  def __str__(self):
    return self.name

class Comment(models.Model):
  user = models.ForeignKey(User, verbose_name="Usuário", db_column="user", on_delete=models.CASCADE, blank=True, null=True)
  post = models.ForeignKey(Post, verbose_name="Postagem", db_column="post", on_delete=models.CASCADE, blank=True, null=True)
  description = models.CharField(verbose_name="Comentário", db_column = "description", max_length = 5000, blank = False, null = False)
  
  class Meta:
      db_table = "comment"
      verbose_name = "Comentário"
      verbose_name_plural = "Comentários"

  def __str__(self):
    return self.name