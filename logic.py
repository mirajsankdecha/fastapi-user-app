def create_info(name, phone, age):
    try:
        user_dict=dict()
        user_dict['name']=name
        user_dict['phone']=phone
        user_dict['age']=age
        #TODO: PUT THIS ENTRY IN DB
        #raise Exception
        return True
    except Exception as e:
        print("error in creating user",e)
        return False