from django.db import migrations
from usuarios.models import MyUser

#UD9.3.c BEGIN
def superusuario(apps, schema_editor):
    
    MyUser.objects.create_superuser(
        email='admin@example.com',
        password='password'
    )
class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(superusuario),
    ]
#UD9.3.c END