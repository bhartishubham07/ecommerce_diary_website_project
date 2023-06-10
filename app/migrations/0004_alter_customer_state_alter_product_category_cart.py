# Generated by Django 4.1.7 on 2023-06-02 06:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0003_alter_product_category_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(choices=[('Delhi', 'Delhi'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Odisha', 'Odisha'), ('Manipur', 'Manipur'), ('Haryana', 'Haryana'), ('Mizoram', 'Mizoram'), ('Andhra Pradesh', 'Andhra Pradesh'), ('Bihar', 'Bihar'), ('Rajasthan', 'Rajasthan'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Nagaland', 'Nagaland'), ('Gujarat', 'Gujarat'), ('Kerala', 'Kerala'), ('Karnataka', 'Karnataka'), ('Uttarakhand', 'Uttarakhand'), ('Tamil Nadu', 'Tamil Nadu'), ('Chhattisgarh', 'Chhattisgarh'), ('Meghalaya', 'Meghalaya'), ('Sikkim', 'Sikkim'), ('Maharashtra', 'Maharashtra'), ('Uttar Pradesh', 'Uttar Pradesh'), ('Punjab', 'Punjab'), ('Jharkhand', 'Jharkhand'), ('Telangana', 'Telangana'), ('West Bengal', 'West Bengal'), ('Assam', 'Assam'), ('Goa', 'Goa'), ('Tripura', 'Tripura'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Jammu and Kashmir', 'Jammu and Kashmir')], max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('GH', 'Ghee'), ('LS', 'Lassi'), ('CR', 'Curd'), ('PN', 'Paneer'), ('ML', 'Milk'), ('MS', 'Milkshake'), ('IC', 'Ice-cream'), ('CZ', 'Cheese')], max_length=2),
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
