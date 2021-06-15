import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'datacenter.settings')
django.setup()

from mysite.models import Post

for i in range(3):
    newdata = Post(title="標題{}".format(i+4),
                   body="內文{}".format(i+4))
    newdata.save()