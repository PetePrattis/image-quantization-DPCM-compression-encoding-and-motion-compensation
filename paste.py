from PIL import Image
import image_slicer

def main(): #{
    filename = "img.jpg";

    image = Image.open(filename);
    image_two = Image.open("praxis.jpg");
    size = width, height = image.size;

    image.paste(image_two, (0,0,image_two.width,image_two.height)) #coordinates on image (0,0,640,920)

    image.show();

    del image;

#}

if(__name__ == "__main__"):#{

    main();

#}
