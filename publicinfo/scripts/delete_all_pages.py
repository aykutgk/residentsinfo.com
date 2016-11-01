from person.models import Page

def delete_all():
    objs = Page.objects.all()
    for obj in objs:
        obj.delete()

delete_all()
