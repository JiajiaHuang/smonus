import os
import time

import django
from django.utils import timezone

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SMONU.settings")  # project_name 项目名称
django.setup()
from blog.models import TagsModels


def add_tag_to_sql(tags):
    tags_list = eval(tags)
    print(tags_list)
    for tag in tags_list:
        print(tag['value'])

        try:
            tag_model = TagsModels.objects.get(tags_name=tag['value'], )
            tag_model.tags_numb += 1
            tag_model.save()
        except:
            tag_model = TagsModels.objects.create(tags_name=tag['value'], tags_numb=1, )
            tag_model.save()
    return True


def subtraction_tag_to_sql(tags):
    tags_list = eval(tags)
    for tag in tags_list:
        try:
            tag_model = TagsModels.objects.get(tags_name=tag['value'], )
            tag_model.tags_numb -= 1
            if tag_model.tags_numb <= 0:
                tag_model.delete()
            else:
                tag_model.save()
        except:
            print(tag)

    return True


if __name__ == '__main__':
    subtraction_tag_to_sql('[{"value":"ass"},{"value":"sax"}]')
