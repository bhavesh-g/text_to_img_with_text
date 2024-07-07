# Image Text Renderer

This Python script generates images containing text, encodes the images in base64 format, and provides HTML `<img>` tags for easy embedding. It can be particularly useful in preventing users from copying text during online exams by converting the text into images, which are harder to copy using Chrome Developer Tools or other similar methods.

## Features
- Loads configuration from a YAML file.
- Wraps text to fit within specified image dimensions.
- Generates images with wrapped text.
- Encodes images in base64 format.
- Saves image paths and HTML `<img>` tags in a JSON file.

## Requirements
- Python 3.x
- `Pillow` library
- `PyYAML` library

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/imagetextrenderer.git
   cd imagetextrenderer
   ```

2. Install the required packages:
   ```bash
   pip install pillow pyyaml
   ```

## Configuration

Create a `config.yaml` file in the root directory with the following structure:

```yaml
font_path: 'path/to/font.ttf'
font_size: 15
output_width: 800
output_height: 200
wrap_factor: 7
output_json_file: 'output_html_tags.json'
```

- `font_path`: Path to the TTF font file to use.
- `font_size`: Font size for the text.
- `output_width`: Width of the output image.
- `output_height`: Height of the output image.
- `wrap_factor`: Factor to determine text wrapping width.
- `output_json_file`: Name of the output JSON file containing HTML img tags.

## Input Data

Create an `input.yaml` file in the root directory with the text data to be converted into images:

```yaml
example1: |
  This is an example text.
  It will be wrapped and rendered into an image.
example2: |
  Another example text.
  This text will also be rendered into a separate image.
```

## Usage

Run the script using the following command:

```bash
python script.py
```

This will generate images for the provided text data, encode them in base64, and save the HTML `<img>` tags in the specified JSON file.

## Output

The output will be a JSON file (default: `output_html_tags.json`) containing the HTML `<img>` tags for the generated images. You can embed these tags in your HTML files to display the images.

## Example

If the `input.yaml` contains:

```yaml
example1: |
  Hello, this is a test.
```

The output JSON will contain something like:

```json
{
  "example1": "<img src=\"data:image/png;base64,....\" alt=\"example1\">"
}
```

You can then use the generated HTML `<img>` tags in your web pages to display the images.

## Use Case in Online Exam Cheat Prevention

By converting exam questions and important text into images, you can prevent users from copying the text directly, even if they use Chrome Developer Tools to bypass other copy-paste restrictions. This method ensures that the text is only viewable as an image, making it more difficult to extract the text content.

## License

This project is licensed under the MIT License.
