import os
import crud
import model
import server

os.system("drop closet_db")
os.system("create closet_db")

if __name__ == "__main__":

    model.connet_to_db(server.app)
    server.app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= True
    


    model.db.create_all()

    sock = crud.create_sock()
    model.db.session.add(sock)
    model.db.session.commit()

    shoe = crud.create_shoe()
    model.db.session.add(shoe)
    model.db.session.commit()

    jacket = crud.create_jacket()
    model.db.session.add(jacket)
    model.db.session.commit()

    pant = crud.create_pant()
    model.db.session.add(pant)
    model.db.session.commit()

    shirt = crud.create_shirt()
    model.db.session.add(shirt)
    model.db.session.commit()



    