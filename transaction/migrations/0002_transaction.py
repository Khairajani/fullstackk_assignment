# Generated by Django 3.1.1 on 2021-08-11 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_number', models.CharField(blank=True, max_length=50)),
                ('transaction_status', models.CharField(choices=[('PE', 'Pending'), ('CO', 'Complete'), ('CL', 'Close')], default='PE', max_length=2)),
                ('remarks', models.CharField(blank=True, max_length=64)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transaction.branchmaster')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transaction.companyledgermaster')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transaction.departmentmaster')),
            ],
        ),
    ]