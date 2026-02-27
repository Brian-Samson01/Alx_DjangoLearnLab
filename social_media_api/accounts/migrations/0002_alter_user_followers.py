from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='followers',
            field=models.ManyToManyField(
                blank=True,
                related_name='following',
                symmetrical=False,
                to='accounts.user',
            ),
        ),
    ]
