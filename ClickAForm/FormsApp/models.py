from django.db import models


class FormTemplate(models.Model):
    title = models.CharField(max_length=200)
    flow_id = models.IntegerField()


class IdType(models.Model):
    name = models.CharField(max_length=200)
    hebrew_value = models.CharField(max_length=200)


class Field(models.Model):
    field_type = models.CharField(max_length=200)
    id_type = models.ForeignKey(IdType)


class FormTemplateField(models.Model):
    form_template_id = models.ForeignKey(FormTemplate)
    field_id = models.ForeignKey(Field)


class User(models.Model):
    name = models.CharField(max_length=200)


class FormInstance(models.Model):
    form_template_id = models.ForeignKey(FormTemplate)
    flow_instance_id = models.IntegerField()
    user_id = models.ForeignKey(User)


class FormInstanceFieldValue(models.Model):
    form_instance_id = models.ForeignKey(FormInstance)
    form_field_id = models.ForeignKey(FormTemplateField)
    value = models.CharField(max_length=200)

