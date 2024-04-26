# Generated by Django 4.2.11 on 2024-04-26 21:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categories',
            options={'verbose_name': 'категория', 'verbose_name_plural': 'категории'},
        ),
        migrations.AlterField(
            model_name='categories',
            name='name',
            field=models.CharField(max_length=150, unique=1, verbose_name='название'),
        ),
        migrations.AlterField(
            model_name='categories',
            name='slug',
            field=models.SlugField(blank=1, max_length=200, null=1, unique=1, verbose_name='добавочный url'),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=1, verbose_name='название')),
                ('slug', models.SlugField(blank=1, max_length=200, null=1, unique=1, verbose_name='добавочный url')),
                ('description', models.TextField(blank=1, null=1, verbose_name='описание')),
                ('image', models.ImageField(blank=1, null=1, upload_to='goods_imgs')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=7, verbose_name='цена')),
                ('discount', models.DecimalField(decimal_places=2, default=0.0, max_digits=7, verbose_name='скидка')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='кол-во')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.categories')),
            ],
            options={
                'verbose_name': 'продукт',
                'verbose_name_plural': 'продукты',
                'db_table': 'product',
            },
        ),
    ]
