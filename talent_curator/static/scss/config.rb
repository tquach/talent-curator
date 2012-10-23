# Require any additional compass plugins here.
require "compass-colors"

# Set this to the root of your project when deployed:
http_path = "/static"
http_stylesheets_path = http_path + "/css"
http_images_path = http_path + "/img"
http_javascripts_path = http_path + "/js"
http_fonts_path = http_path + "/font"

site_root = "../"
css_dir = site_root + "css"
sass_dir = "."
images_dir = site_root + "img"
font_dir = site_root + "font"
javascripts_dir = site_root + "js"

# To enable relative paths to assets via compass helper functions. Uncomment:
relative_assets = true
output_style = :compressed 