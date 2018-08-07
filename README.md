# gal
Tiny web gallery with progressive-loading images.

### Requirements:

- Yarn
- Python 3.5


### Usage:

    git clone https://github.com/bedekelly/gal .gal && bash .gal/run.sh
    # Serving images from current directory
    

### Remove:

    rm -r .gal


### Notes:

This works by generating low-resolution previews of photos, applying a Gaussian blur, and serving the resulting blurred previews as data-urls. These data-urls are paired with the URLs for the real images. When the real image is loaded, the preview is faded out.


### Future work:

This likely won't get any.
