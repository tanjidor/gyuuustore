from .models import Produk, Review, Attachment

def clone(instance, i):
    instance.pk = None
    instance.nama_produk = 'produk baru' + str(i)
    instance.save()
    return instance

def clone1(instance, produk):
    instance.pk = None
    instance.produk = produk
    instance.save()
    return instance

# instance = Produk.objects.last()
# related_objects = instance.review_produk.all()
# cloned_instance = clone(instance)

# for related_object in related_objects:
#     related_object.meeting = cloned_instance
#     clone(related_object)


def kopi():
    instance = Produk.objects.get(pk=1)
    related_objects = instance.review_produk.all()
    print(related_objects)
    for i in range(20):
        cloned_instance = clone(instance, i)

        for related_object in related_objects:
            fak = clone1(related_object, cloned_instance)
            print(fak)
            print(fak.produk)
        print(f'kopi {i} berhasil')
        