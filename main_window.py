from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont


CANVAS_WIDTH = 960
CANVAS_HEIGHT = 540

class MainWindow:

    def __init__(self):
        self.window = Tk()
        self.window.title("Image Watermarking App")
        self.window.minsize(width=1100, height=700)
        self.window.config(padx=100, pady=50)
        self.canvas = Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white", highlightthickness=0)
        self.canvas.grid(column=0, row=0, columnspan=3)
        self.image = Image.open("Logo.jpg").convert('RGB')
        self.image_for_canvas = ImageTk.PhotoImage(file="Logo.jpg")
        self.img_on_canvas = self.canvas.create_image((480, 270), image=self.image_for_canvas)

        # ------ Buttons ------
        self.add_btn = Button(text="Load image", command=self.load_image)
        self.add_btn.grid(column=0, row=2)
        self.process_btn = Button(text="Add watermark", command=self.add_watermark)
        self.process_btn.grid(column=1, row=2)
        self.save_btn = Button(text="Save", command=self.save_image)
        self.save_btn.grid(column=2, row=2)

        self.window.mainloop()

    def load_image(self):
        try:
            file_path = filedialog.askopenfile().name
        except AttributeError:
            return
        self.image = Image.open(file_path).convert('RGB')
        img_resized = self.image.resize((CANVAS_WIDTH, CANVAS_HEIGHT))
        self.image_for_canvas = ImageTk.PhotoImage(img_resized)
        self.canvas.itemconfig(self.img_on_canvas, image=self.image_for_canvas)

    def save_image(self):
        files = [('JPEG', ('*.jpg', '*.jpeg', '*.jpe', '*.jfif')),
                 ('PNG', '*.png'),
                 ('BMP', '*.bmp'),
                 ('GIF', '*.gif')]
        a = filedialog.asksaveasfilename(filetypes=files, defaultextension="*.jpg")
        self.image.save(a)

    def add_watermark(self):
        if self.image.width < self.image.height:
            font = ImageFont.truetype("Fonts/bastliga-one/Bastliga One.ttf", size=int(0.05 * self.image.width))
            print(f"1 {font.size}, {self.image.width} x {self.image.height}")
        else:
            font = ImageFont.truetype("Fonts/bastliga-one/Bastliga One.ttf", size=int(0.1 * self.image.height))
            print(f"2 {font.size}, {self.image.width} x {self.image.height}")
        d = ImageDraw.Draw(self.image)
        d.text((int(self.image.width * 0.75), int(self.image.height * 0.93)), "Photo by Franciszek Walczak", fill="black", anchor="ms", font=font)
        img_resized = self.image.resize((CANVAS_WIDTH, CANVAS_HEIGHT))
        self.image_for_canvas = ImageTk.PhotoImage(img_resized)
        self.canvas.itemconfig(self.img_on_canvas, image=self.image_for_canvas)
