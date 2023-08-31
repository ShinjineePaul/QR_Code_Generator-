from importlib.metadata import version
import qrcode as qr
img=qr.make("https://www.google.com/search?q=i+love+u&rlz=1C1CHBF_enIN966IN967&sxsrf=ALiCzsYHSwascvNBH66fwI6AC1hZrJt0kA:1668833401596&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjBlN3wuLn7AhUc2DgGHcPzAr4Q_AUoAXoECAIQAw#imgrc=gvgGd2Dzq5JO7M")
img.save("Open this for 1 min of happiness!.png")


from PIL import Image
qr=qr.QRCode(version=3,error_correction=qr.constants.ERROR_CORRECT_H,box_size=10,border=4,)
qr.add_data("https://www.google.com/search?q=i+love+u&rlz=1C1CHBF_enIN966IN967&sxsrf=ALiCzsYHSwascvNBH66fwI6AC1hZrJt0kA:1668833401596&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjBlN3wuLn7AhUc2DgGHcPzAr4Q_AUoAXoECAIQAw#imgrc=gvgGd2Dzq5JO7M")
qr.make(fit=True)
img=qr.make_image(fill_color="red",back_color="pink")
img.save("Open this for 1 min of happiness!.png")