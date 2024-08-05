<div align="center">
  <h1>Image Sequence GIF 🎞️</h1>
</div>

<p>
  <code>image-sequence-gif</code> is a script that creates a GIF from a sequence of images in a specified directory. The script supports multiple image formats and allows for various customizable options, including frame duration, transition effects, cropping, and delay.
</p>

## ❓ Why?

If you have multiple images that you’d like to combine into a single animated GIF, this script can help you stitch them together. Whether you have a collection of random images or a series you’d like to turn into a timelapse, this script will convert a directory of images into an animated GIF. Also because I needed this for my [dotfiles](https://github.com/epilande/dotfiles) repo demo.

## ✨ Features

- 🖼️ Supports multiple image formats (PNG, JPG, JPEG, BMP)
- ⏱️ Customizable frame duration and transition effects
- ✂️ Optional cropping of images
- ⏲️ Adjustable delay between frames
- 🖌️ Generates a GIF with transparency

## 📋 Requirements

- 🐍 Python 3.x
- 🖼️ Pillow

## 🔧 Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/epilande/image-sequence-gif.git
   cd image-sequence-gif
   ```

2. Install the required dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```

3. Install the package:
   ```bash
   pip install .
   ```

## 🚀 Usage

```bash
image-sequence-gif [--input INPUT_DIR] [--output OUTPUT_FILE] [--duration FRAME_DURATION] [--transition TRANSITION_FRAMES] [--crop CROP_BOX] [--delay DELAY]
```

### 📌 Arguments

- `--input INPUT_DIR`: Directory containing images (default: `./input`).
- `--output OUTPUT_FILE`: Output GIF file (default: `output.gif`).
- `--duration FRAME_DURATION`: Duration of each frame in milliseconds (default: 50 ms).
- `--transition TRANSITION_FRAMES`: Number of frames for the transition effect (default: 4).
- `--crop CROP_BOX`: Crop box for the images in the format `left,upper,right,lower` (optional).
- `--delay DELAY`: Delay in milliseconds for each image before transition (default: 2000 ms).

### 📖 Examples

1. Basic usage with default settings:

   ```bash
   image-sequence-gif
   ```

2. Specify custom input and output files:

   ```bash
   image-sequence-gif --input ./my_images --output my_gif.gif
   ```

3. Set custom frame duration and delay:

   ```bash
   image-sequence-gif --duration 100 --delay 3000
   ```

4. Include a transition effect between frames:

   ```bash
   image-sequence-gif --transition 4
   ```

5. Crop images before creating the GIF:
   ```bash
   image-sequence-gif --crop 100,50,3500,2000
   ```

## 📦 Import in Another Script

You can also import the `create_gif` function from `image_sequence_gif` and call it programmatically in another Python script:

```python
from image_sequence_gif import create_gif

input_dir = "./input"
output_file = "output.gif"
frame_duration = 50
transition_frames = 4
crop_box = (110, 70, 3570, 2240)  # Set to None if no cropping is needed
delay = 2000

create_gif(input_dir, output_file, frame_duration, transition_frames, crop_box, delay)
```
