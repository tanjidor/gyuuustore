from django.db import models
from django.template.defaultfilters import slugify 
from django.urls import reverse
from django.db.models import Avg

class Produk(models.Model):
    slug = models.SlugField(blank=False, unique=True, editable=False)
    nama_produk = models.CharField(max_length=255, blank=False, null=False)
    harga = models.IntegerField(default=0)
    harga_coret = models.IntegerField(default=0)
    deskripsi1 = models.TextField(verbose_name='Deskripsi Atas', default="") # deskripsi atas
    deskripsi2 = models.TextField(verbose_name='Deskripsi Bawah', default="") # deskripsi bawah
    informasi1 = models.TextField(verbose_name='Main Informasi', default="") # informasi
    informasi2 = models.TextField(verbose_name='Bottom Left Informasi', default="") # informasi kiri bawah 
    informasi3 = models.TextField(verbose_name='Bottom Right Informasi', default="") # informasi kanan bawah
    sold = models.IntegerField(default=1)
    # thumbnail, carousel1, carousel2, carousel3, info_tambahan
    thumbnail = models.URLField(max_length=255, blank=True, null=True)
    carousel1 = models.URLField(max_length=255, blank=True, null=True)
    carousel2 = models.URLField(max_length=255, blank=True, null=True)
    carousel3 = models.URLField(max_length=255, blank=True, null=True)
    info_tambahan = models.URLField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nama_produk

    def get_absolute_url(self):
        return reverse("ecommerce:detail", kwargs={"slug": self.slug})
    
    @property
    def averagereview(self):
        return self.review_produk.aggregate(Avg('ratings'))['ratings__avg']
    
    @property
    def getReview(self):
        return self.review_produk.all().order_by('-tanggal')

    def save(self, *args, **kwargs): 
        # if not self.slug:
        self.slug = slugify(self.nama_produk)
        return super().save(*args, **kwargs)


class Review(models.Model):
    produk = models.ForeignKey(Produk, on_delete=models.CASCADE, related_name='review_produk')
    reviewers = models.CharField(max_length=255, blank=False, null=False)
    review = models.TextField()
    ratings = models.FloatField(default=0) # max 5
    tanggal = models.DateField(default='2025-01-01')

    def __str__(self):
        return self.reviewers


class Attachment(models.Model):
    nama = models.CharField(max_length=255, blank=False, null=False)
    file = models.FileField('Attachment', upload_to='attachments/', blank=True)
    url_file = models.URLField(max_length=255, blank=True, null=True)
    # file_type = models.CharField('File type', choices=AttachmentType.choices, max_length=10)
    produk = models.ForeignKey(Produk, on_delete=models.CASCADE, verbose_name='Model that uses the image field', related_name='attachment_produk')

    # depan, detail, info (nama attachment sesuaikan dengan yang diinginkan)

    def __str__(self):
        return "{}-{}".format(self.nama, self.produk.nama_produk)

    class Meta:
        verbose_name = 'Attachment'
        verbose_name_plural = 'Attachments'


# <div class="review-feedback">
#                 <span class="fa fa-star {% if product_detail.averagereview > 0 %} checked {% endif %}"></span>
#                 <span class="fa fa-star {% if product_detail.averagereview > 1 %} checked {% endif %}"></span>
#                 <span class="fa fa-star {% if product_detail.averagereview > 2 %} checked {% endif %}"></span>
#                 <span class="fa fa-star {% if product_detail.averagereview > 3 %} checked {% endif %}"></span>
#                 <span class="fa fa-star {% if product_detail.averagereview > 4 %} checked {% endif %}"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
#                 {{product_detail.averagereview | stringformat:".2f"}}
#             </div>

# <div class="rating-star">
#     <span title="{{ review.rating }}/5">
#     <!-- By default the star is full else it is empty otherwise it is half -->
#         <i class="fa fa-star{% if review.rating < 0.5%}-o{% elif review.rating >= 0.5 and review.rating < 1 %}-half-o{% endif %}" aria-hidden="true"></i>
#         <i class="fa fa-star{% if review.rating < 1.5%}-o{% elif review.rating >= 1.5 and review.rating < 2 %}-half-o{% endif %}" aria-hidden="true"></i>
#         <i class="fa fa-star{% if review.rating < 2.5%}-o{% elif review.rating >= 2.5 and review.rating < 3 %}-half-o{% endif %}" aria-hidden="true"></i>
#         <i class="fa fa-star{% if review.rating < 3.5%}-o{% elif review.rating >= 3.5 and review.rating < 4 %}-half-o{% endif %}" aria-hidden="true"></i>
#         <i class="fa fa-star{% if review.rating < 4.5%}-o{% elif review.rating >= 4.5 and review.rating < 5 %}-half-o{% endif %}" aria-hidden="true"></i>
#     </span>
#     <span><strong>( {{ review.rating }}/5 )</strong></span>
# </div> fas == full, far == empty, fas-half-alt == half

# ** order review by tgl