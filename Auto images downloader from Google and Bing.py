Type = input("Welche Fotos willst du henderladen (Foto_type)?")
zahl = int(input("Wie viele Fotos ?"))


from google_images_download import google_images_download
from bing_image_downloader import downloader

response = google_images_download.googleimagesdownload()
arguments = {"keywords":"aeroplane, school bus, dog in front of house",
             "limit":10,"print_urls":False}
paths = response.download(arguments)


print(paths)

downloader.download(f"{Type}", limit=int(f"{zahl}"),  output_dir='dataset',
                    adult_filter_off=True, force_replace=False, timeout=60)
