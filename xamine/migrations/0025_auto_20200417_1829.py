# Generated by Django 3.0.5 on 2020-04-17 22:29

from django.db import migrations


def add_data_list(apps, schema_editor):
    levels = [
        'Referral Placed',
        'Checked In',
        'Imaging Complete',
        'Analysis Complete',
        'Archived'
    ]
    add_data(apps, schema_editor, app='xamine', model='Level', items=levels)

    groups = [
        'Administrators',
        'Physicians',
        'Radiologists',
        'Receptionists',
        'Technicians'
    ]
    add_data(apps, schema_editor, app='auth', model='Group', items=groups)

    modalities = [
        'MRI',
        'X-Ray',
        'CAT Scan',
    ]
    add_data(apps, schema_editor, app='xamine', model='ModalityOption', items=modalities)


def add_data(apps, schema_editor, app, model, items):
    model = apps.get_model(app, model)
    db_alias = schema_editor.connection.alias

    item_objs = []
    for item in items:
        if not model.objects.using(db_alias).filter(name=item).exists():
            item_objs.append(model(name=item))

    model.objects.using(db_alias).bulk_create(item_objs)


class Migration(migrations.Migration):

    dependencies = [
        ('xamine', '0024_auto_20200417_1829'),
    ]

    operations = [
        migrations.RunPython(add_data_list),
    ]
