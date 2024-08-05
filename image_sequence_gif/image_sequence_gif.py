"""
Script to create a GIF from a directory of images.

Usage:
    python image_sequence_gif.py [--input INPUT_DIR] [--output OUTPUT_FILE] [--duration FRAME_DURATION] [--transition TRANSITION_FRAMES] [--crop CROP_BOX] [--delay DELAY]

Arguments:
    --input INPUT_DIR      Directory containing PNG images (default: ./input).
    --output OUTPUT_FILE   Output GIF file (default: output.gif).
    --duration FRAME_DURATION
                           Duration of each frame in milliseconds (default: 50 ms).
    --transition TRANSITION_FRAMES
                           Number of frames for the transition effect (default: 4).
    --crop CROP_BOX        Crop box for the images in the format 'left,upper,right,lower' (optional).
    --delay DELAY          Delay in milliseconds for each image before transition (default: 2000 ms).
"""

from PIL import Image
import os
import glob
import argparse


def load_images_from_directory(directory, extensions=[".png", ".jpg", ".jpeg", ".bmp"]):
    image_paths = []
    for ext in extensions:
        image_paths.extend(glob.glob(os.path.join(directory, f"*{ext}")))
    image_paths = sorted(image_paths)
    images = [Image.open(path).convert("RGBA") for path in image_paths]
    return images


def blend_images(img1, img2, alpha):
    return Image.blend(img1, img2, alpha)


def crop_image(image, crop_box):
    return image.crop(crop_box)


def create_gif(
    input_dir, output_file, frame_duration, transition_frames, crop_box, delay
):
    images = load_images_from_directory(input_dir)

    if not images:
        raise ValueError(
            "No images loaded from the input directory. Please ensure the directory contains images."
        )

    frames = []

    # Add each image with a delay and its fade transition to the next image
    for i in range(len(images)):
        img1 = crop_image(images[i], crop_box) if crop_box else images[i]
        frames.extend(
            [img1] * (delay // frame_duration)
        )  # Delay at specified frame rate

        if i < len(images) - 1:
            img2 = crop_image(images[i + 1], crop_box) if crop_box else images[i + 1]
            for alpha in range(1, transition_frames + 1):  # Transition frames
                blended = blend_images(img1, img2, alpha / transition_frames)
                frames.append(blended)

    # Add fade transition from last to first image for looping
    img1 = crop_image(images[-1], crop_box) if crop_box else images[-1]
    img2 = crop_image(images[0], crop_box) if crop_box else images[0]
    for alpha in range(1, transition_frames + 1):  # Transition frames
        blended = blend_images(img1, img2, alpha / transition_frames)
        frames.append(blended)

    # Convert frames to 'P' mode and add transparency info
    converted_frames = []
    for frame in frames:
        converted_frame = frame.convert("RGBA").convert(
            "P", palette="ADAPTIVE", colors=256
        )
        alpha = frame.getchannel("A")
        mask = Image.eval(alpha, lambda a: 255 if a <= 128 else 0)
        converted_frame.paste(255, mask)
        converted_frames.append(converted_frame)

    # Save as GIF with transparency
    converted_frames[0].save(
        output_file,
        save_all=True,
        append_images=converted_frames[1:],
        duration=frame_duration,
        loop=0,
        transparency=255,
        disposal=2,
    )


def main():
    parser = argparse.ArgumentParser(
        description="Script to create a GIF from a directory of images."
    )
    parser.add_argument(
        "--input",
        default="./input",
        help="Directory containing PNG images (default: ./input).",
    )
    parser.add_argument(
        "--output", default="output.gif", help="Output GIF file (default: output.gif)."
    )
    parser.add_argument(
        "--duration",
        type=int,
        default=50,
        help="Duration of each frame in milliseconds (default: 50 ms).",
    )
    parser.add_argument(
        "--transition",
        type=int,
        default=4,
        help="Number of frames for the transition effect (default: 4).",
    )
    parser.add_argument(
        "--crop",
        help="Crop box for the images in the format 'left,upper,right,lower' (optional).",
    )
    parser.add_argument(
        "--delay",
        type=int,
        default=2000,
        help="Delay in milliseconds for each image before transition (default: 2000 ms).",
    )

    args = parser.parse_args()

    crop_box = tuple(map(int, args.crop.split(","))) if args.crop else None

    try:
        create_gif(
            args.input,
            args.output,
            args.duration,
            args.transition,
            crop_box,
            args.delay,
        )
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
