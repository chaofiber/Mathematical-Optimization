from PIL import Image as PILimg
from matplotlib import image as MPLimg
from matplotlib import cm as cm
from matplotlib import pyplot as plt

def read_image(file):
    # open file as grayscale image
    img = PILimg.open(file).convert("L")
    # return it converted to an integer array
    return MPLimg.pil_to_array(img).astype(int)

def plot_image(img):
    # setup plot and show
    plt.figure(figsize = (7,7))
    plt.imshow(img, cmap = cm.gray)
    plt.show()

def polygonal_selection(coord, shape):
    from PIL import Image, ImageDraw
    import matplotlib
    # create image of given size
    img_polygon = Image.new("L", (shape[1], shape[0]))
    # draw polygon using given coordinates
    img_draw = ImageDraw.Draw(img_polygon)
    img_draw.polygon(coord, fill="white", outline="white")
    # convert to array, scale down to 0/1 image and cast to type int
    return (matplotlib.image.pil_to_array(img_polygon)/255).astype(int)

def plot_selection(img, sel):
    # plots selection with slight blue background
    
    def entry(i, j):
        # returns right color - either blue or grayscale image value
        if sel[i][j] == 0: 
            return [170, 240, 240] 
        else:
            return [img[i][j], img[i][j], img[i][j]]
    
    # construct selection image, plot and show it
    selection = [ [ entry(i,j) for j in range(img.shape[1]) ] for i in range(img.shape[0]) ]
    plt.figure(figsize = (7,7))
    plt.imshow(selection)
    plt.show()