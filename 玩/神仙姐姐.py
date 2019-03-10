from PIL import Image
import sys,array
def fill_image(image):
    width, height = image.size
    new_image_length = width if width > height else height
    new_image = image.new(image.mode,(new_image_length,new_image_length),color = 'white')
    if width > height:
        new_image.paste(image,(0,int((new_image_length - height)/2)))
    else:
        new_image.paste(image, (int((new_image_length - width)/2),0))
        return new_image

def cut_image(image):
    width, height = image.size
    item_width = int(width / 3)
    box_list = []
    for i in range(0,3):
        for j in range(0,3):
            box = (j*item_width,i*item_width,(j+1)+item_width)
            box_list.append(box)
    image_list = [image.crop(box) for box in box_list]
    return image_list
def save_image(image_list):
    index = 1
    for image in image_list:
        image.save(str(index) + '.png','PNG')
        index += 1

if __name__ == '__main__':
    file_path = r"C:\Users\13436\PycharmProjects\learnpy\venv\神仙姐姐.jpg"
    image = Image.open(file_path)
    image = fill_image(image)
    image_list = cut_image(image)
    save_image(image_list)

#img = Image.open(path) #打开图片
#img_array = np.array(img) #将图片装换为数组
#wc = WordCloud(
#    background_color='white',
#   width=1000,
#    height=300,
 #   mask=img_array,
  #  font_path=font,
#).generate_from_text(string)#绘制图片


