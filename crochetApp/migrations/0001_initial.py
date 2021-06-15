# Generated by Django 3.2.3 on 2021-06-15 06:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Acct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acctType', models.CharField(default='General', max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postTitle', models.CharField(max_length=255)),
                ('postContent', models.TextField()),
                ('postCreatedAt', models.DateTimeField(auto_now_add=True)),
                ('postUpdatedAt', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemName', models.CharField(max_length=45)),
                ('itemDescription', models.TextField()),
                ('itemPrice', models.DecimalField(decimal_places=2, max_digits=5)),
                ('itemImg', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topicName', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=45)),
                ('lastName', models.CharField(max_length=45)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('username', models.CharField(max_length=45)),
                ('password', models.CharField(max_length=45)),
                ('userCreatedAt', models.DateTimeField(auto_now_add=True)),
                ('userUpdatedAt', models.DateTimeField(auto_now=True)),
                ('acct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='crochetApp.acct')),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('replyText', models.TextField()),
                ('replyCreatedAt', models.DateTimeField(auto_now_add=True)),
                ('replyUpdatedAt', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='crochetApp.user')),
                ('replyPost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='thePost', to='crochetApp.post')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address1', models.CharField(max_length=255, null=True)),
                ('address2', models.CharField(default='Null', max_length=255)),
                ('city', models.CharField(max_length=255, null=True)),
                ('state', models.CharField(max_length=255, null=True)),
                ('zipCode', models.IntegerField(null=True)),
                ('image', models.ImageField(default='default.jpg', upload_to='profileImgs')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='crochetApp.user')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='postLike',
            field=models.ManyToManyField(related_name='likes', to='crochetApp.User'),
        ),
        migrations.AddField(
            model_name='post',
            name='postTopic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topics', to='crochetApp.topic'),
        ),
        migrations.AddField(
            model_name='post',
            name='poster',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='crochetApp.user'),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('totalPrice', models.DecimalField(decimal_places=2, max_digits=7)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='crochetApp.user')),
                ('itemsOrdered', models.ManyToManyField(related_name='items', to='crochetApp.Product')),
                ('shipping', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='address', to='crochetApp.profile')),
            ],
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('updatedOn', models.DateTimeField(auto_now=True)),
                ('content', models.TextField()),
                ('createdOn', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to='crochetApp.user')),
            ],
            options={
                'ordering': ['-createdOn'],
            },
        ),
    ]
