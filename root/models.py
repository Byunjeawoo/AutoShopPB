from django.db import models

class UserUpload(models.Model):
    uploadedFile = models.FileField(upload_to="")
    dateTimeOfUpload = models.DateTimeField(auto_now=True)

class UploadFormModel(models.Model):
    uploadedFile = models.FileField(upload_to="")
    password = models.TextField(default='0000')

#상품주문번호 / 구매자명 / 상품명 / 옵션 / 수량 / 주문일시 / 총 주문 금액
class realtp(models.Model):
    orderNumber = models.IntegerField(default=0, unique=True)
    consumerName = models.TextField(default='')
    productName = models.TextField(default='')
    optionName = models.TextField(default='')
    orderCount = models.IntegerField(default=0)
    sellTime = models.TimeField(default='')
    sellTotalMoney = models.IntegerField(default=0)

    def __int__(self):
        return self.orderNumber
