# Generated by Django 3.0.5 on 2020-08-06 19:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('followup', '0001_initial'),
        ('core', '0002_auto_20200806_1411'),
        ('auth', '0011_update_proxy_permissions'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='labfollowup',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='labfollowup',
            name='author_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='auth.Group'),
        ),
        migrations.AddField(
            model_name='labfollowup',
            name='contact_method',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.ContactMethod'),
        ),
        migrations.AddField(
            model_name='labfollowup',
            name='contact_resolution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='followup.ContactResult'),
        ),
        migrations.AddField(
            model_name='labfollowup',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Patient'),
        ),
        migrations.AddField(
            model_name='historicallabfollowup',
            name='author',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicallabfollowup',
            name='author_type',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='auth.Group'),
        ),
        migrations.AddField(
            model_name='historicallabfollowup',
            name='contact_method',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='core.ContactMethod'),
        ),
        migrations.AddField(
            model_name='historicallabfollowup',
            name='contact_resolution',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='followup.ContactResult'),
        ),
        migrations.AddField(
            model_name='historicallabfollowup',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicallabfollowup',
            name='patient',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='core.Patient'),
        ),
        migrations.AddField(
            model_name='historicalactionitemfollowup',
            name='action_item',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='core.ActionItem'),
        ),
        migrations.AddField(
            model_name='historicalactionitemfollowup',
            name='author',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicalactionitemfollowup',
            name='author_type',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='auth.Group'),
        ),
        migrations.AddField(
            model_name='historicalactionitemfollowup',
            name='contact_method',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='core.ContactMethod'),
        ),
        migrations.AddField(
            model_name='historicalactionitemfollowup',
            name='contact_resolution',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='followup.ContactResult'),
        ),
        migrations.AddField(
            model_name='historicalactionitemfollowup',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicalactionitemfollowup',
            name='patient',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='core.Patient'),
        ),
        migrations.AddField(
            model_name='actionitemfollowup',
            name='action_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.ActionItem'),
        ),
        migrations.AddField(
            model_name='actionitemfollowup',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='actionitemfollowup',
            name='author_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='auth.Group'),
        ),
        migrations.AddField(
            model_name='actionitemfollowup',
            name='contact_method',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.ContactMethod'),
        ),
        migrations.AddField(
            model_name='actionitemfollowup',
            name='contact_resolution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='followup.ContactResult'),
        ),
        migrations.AddField(
            model_name='actionitemfollowup',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Patient'),
        ),
    ]
