import Image
import Extraction
import db
import arduino_work

while True:
    print("Started....")
    if arduino_work.check_image_button() is True:
        print("Taking Photo...")
        file, datetim = Image.take_photo()
        if file:
            filepath = './Images/'+file
            print(filepath)
            # filepath = './image2.jpg'
            result = Extraction.get_num(filepath)
            plate = result[0][1]
            print(plate)
            db.insert_id(plate, datetim)

            if db.check_resident(plate) is True:
                arduino_work.set_barrier()
            else:
                print("Not the resident")
                print("Press button to open...")
                arduino_work.check_barrier_button()
