import Image
import Extraction
import db
import arduino_work

while True:
    print("in loop")
    if arduino_work.check_image_button() is True:
        print("photo")
        file, datetim = Image.take_photo()
        if file:
            # filepath = './Images/'+file
            # print(filepath)
            filepath = './image1.jpg'
            result = Extraction.get_num(filepath)
            plate = result[0][1]
            print(plate)
            db.insert_id(plate, datetim)

            if db.check_resident(plate) is True:
                arduino_work.set_barrier()
            else:
                print("no open")
                arduino_work.check_barrier_button()
