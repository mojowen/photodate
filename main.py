from glob import glob
from exif import Image

BASE_DIR = '../../Dropbox/Harlow Photos/'

photos = glob("{}**/*.jpg".format(BASE_DIR), recursive=True)

MONTHS = {
	'January': 1,
	'February': 2,
	'March': 3,
	'April': 4,
	'May': 5,
	'June': 6,
	'July': 7,
	'August': 8,
	'September': 9,
	'October': 10,
	'November': 11,
	'December': 12,
}


def update_photo(path):
	try:
		with open(path, 'rb') as fl:
			image = Image(fl)

		[year, *rest]= path.replace(BASE_DIR, '').split('/')

		filename = rest.pop()

		month = MONTHS[rest[0] if len(rest) > 0 and rest[0] in MONTHS.keys() else 'January']
		day = int(rest[1]) if len(rest) > 1 and rest[1].isdigit() else 1

		date = "{}:{:02d}:{:02d} 00:00:00".format(year, month, day)
		image.datetime_original = date

		with open(path, 'wb') as fl:
			fl.write(image.get_file())

	except Exception as e:
		print("Could not save {} due to {}".format(path, e))


for photo in photos:
	update_photo(photo)
