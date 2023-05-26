

import barcode
from barcode.writer import ImageWriter
#number = '5901234123457'
number = 'A800-A3424'
#barcode_format = barcode.get_barcode_class('code39')

# Now, let's create an object of EAN13 class and
# pass the number with the ImageWriter() as the
# writer
#my_code = EAN13(number, writer=ImageWriter())
#my_code = barcode_format(number, writer=ImageWriter())
#my_code = barcode.get('code39',number,writer=ImageWriter(),add_checksum=False)
barcode_writer = ImageWriter()
my_code = barcode.codex.Code39( number, barcode_writer,  add_checksum=False)
print(my_code)
# Our barcode is ready. Let's save it.
my_code.save("new_code3")



