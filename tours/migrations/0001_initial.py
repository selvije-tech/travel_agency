# Generated by Django 3.2.8 on 2021-10-30 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Continent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('North America', 'North America'), ('South America', 'South America'), ('Europe', 'Europe'), ('Asia', 'Asia'), ('Antartica', 'Antartica'), ('Africa', 'Africa'), ('Oceania', 'Oceania')], max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('standard', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('city_of_hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='city_of_hotel', to='tours.city')),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('date_of_departure', models.DateTimeField()),
                ('date_of_retur', models.DateTimeField()),
                ('number_of_days', models.IntegerField()),
                ('type_of_accomodation', models.CharField(choices=[('bed & breakfast', 'BB'), ('half board', 'HB'), ('full board', 'FB'), ('all inclusive', 'AI')], max_length=255)),
                ('price_for_an_adult', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price_for_a_chield', models.DecimalField(decimal_places=2, max_digits=10)),
                ('number_of_places_for_adults', models.IntegerField()),
                ('number_of_places_for_children', models.IntegerField()),
                ('from_airport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_airport', to='tours.airport')),
                ('from_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_city', to='tours.city')),
                ('to_airport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_airport', to='tours.airport')),
                ('to_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_city', to='tours.city')),
                ('to_hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_hotel', to='tours.hotel')),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('participiant_details', models.CharField(max_length=255)),
                ('amount', models.IntegerField()),
                ('purchase_trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchase_trip', to='tours.trip')),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('continent_of_country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='continent_of_country', to='tours.continent')),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='country_of_city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='country_of_city', to='tours.country'),
        ),
        migrations.AddField(
            model_name='airport',
            name='city_of_airport',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='city_of_airport', to='tours.city'),
        ),
    ]