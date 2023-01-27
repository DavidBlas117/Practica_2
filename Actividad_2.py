from fastapi import FastAPI 
from pydantic import BaseModel
app= FastAPI()

class User(BaseModel):
    Passenger_Id:int
    Survived:int
    pClass:int
    Name:str
    sex:str
    Age:int

#Creamos un objeto en forma de lista con diferentes usuarios (Esto sería una base de datos)  
users_list= [User(Passenger_Id=1,Survived=0,pClass=3,Name="Braund, Mr. Owen Harris", sex="male", Age="22"),
             User(Passenger_Id=2,Survived=1,pClass=1,Name="Cumings, Mrs. John Bradley (Florence Briggs Thayer)", sex="female", Age="38"),
             User(Passenger_Id=3,Survived=1,pClass=3,Name="Heikkinen, Miss. Laina", sex="female", Age="26"),
             User(Passenger_Id=4,Survived=1,pClass=1,Name="Futrelle, Mrs. Jacques Heath (Lily May Peel)", sex="female", Age="35"),
             User(Passenger_Id=5,Survived=0,pClass=3,Name="Allen, Mr. William Henry", sex="male", Age="35"),
             User(Passenger_Id=6,Survived=0,pClass=3,Name="Moran, Mr. James", sex="male", Age="0"),
             User(Passenger_Id=7,Survived=0,pClass=2,Name="McCarthy, Mr. Timothy J", sex="male", Age="54"),
             User(Passenger_Id=8,Survived=0,pClass=3,Name="Palsson, Master. Gosta Leonard", sex="male", Age="2"),
             User(Passenger_Id=9,Survived=1,pClass=3,Name="	Johnson, Mrs. Oscar W (Elisabeth Vilhelmina Berg)", sex="female", Age="27"),
             User(Passenger_Id=10,Survived=1,pClass=1,Name="Nasser, Mrs. Nicholas (Adele Achem)", sex="female", Age="14"),
             User(Passenger_Id=11,Survived=1,pClass=3,Name="Sandstrom, Miss. Marguerite Rut", sex="female", Age="4"),
             User(Passenger_Id=12,Survived=1,pClass=3,Name="Bonnell, Miss. Elizabeth", sex="female", Age="58"),
             User(Passenger_Id=13,Survived=0,pClass=3,Name="Saundercock, Mr. William Henry", sex="male", Age="20"),
             User(Passenger_Id=14,Survived=0,pClass=2,Name="Andersson, Mr. Anders Johan", sex="	male", Age="39"),
             User(Passenger_Id=15,Survived=0,pClass=3,Name="Vestrom, Miss. Hulda Amanda Adolfina", sex="female", Age="14"),
             User(Passenger_Id=16,Survived=1,pClass=2,Name="Hewlett, Mrs. (Mary D Kingcome)", sex="female", Age="55"),
             User(Passenger_Id=17,Survived=0,pClass=3,Name="Rice, Master. Eugene", sex="male", Age="2"),
             User(Passenger_Id=18,Survived=1,pClass=3,Name="Williams, Mr. Charles Eugene", sex="male", Age="00"),
             User(Passenger_Id=19,Survived=0,pClass=2,Name="Vander Planke, Mrs. Julius (Emelia Maria Vandemoortele)", sex="female", Age="31"),
             User(Passenger_Id=20,Survived=1,pClass=3,Name="Masselmani, Mrs. Fatima", sex="female", Age="00"),
             User(Passenger_Id=21,Survived=0,pClass=2,Name="Fynney, Mr. Joseph J", sex="male", Age="35"),
             User(Passenger_Id=22,Survived=1,pClass=2,Name="Beesley, Mr. Lawrence", sex="male", Age="34"),
             User(Passenger_Id=23,Survived=1,pClass=3,Name="McGowan, Miss. Anna ", sex="female", Age="15"),
             User(Passenger_Id=24,Survived=1,pClass=1,Name="Sloper, Mr. William Thompson", sex="male", Age="28"),
             User(Passenger_Id=25,Survived=0,pClass=3,Name="Palsson, Miss. Torborg Danira", sex="female", Age="30")]

@app.get("/usersclass")
async def usersclass():
    return (users_list)
 # En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000/usersclass/


 #post 
@app.post("/userclass/")
async def userclass(user:User):

    found=False
    for index, saved_user in enumerate(users_list):
       if saved_user.Passenger_Id == user.Passenger_Id:
          return {"ERROR: el usuario ya exixte"}
    else:
     users_list.append(user)  
    return user

@app.put("/usersclass/")
async def usersclass(user:User):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(users_list):
        if saved_user.Passenger_Id == user.Passenger_Id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           users_list[index] = user  #accedemos al indice de la lista que hemos encontrado y actualizamos con el nuevo usuario
           found=True
           
    if not found:
        return {"error":"No se ha actualizado el usuario"}
    else:
        return user
    
    #http://127.0.0.1:8000/usersclass/
    
    
        #***Delete
@app.delete("/usersclass/{id}")
async def usersclass(Passenger_Id:int):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(users_list):
        if saved_user.Passenger_Id ==Passenger_Id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           del users_list[index]  #Eliminamos al indice de la lista que hemos encontrado 
           found=True
           return "El registro se ha eliminado"
       
    if not found:
        return {"error":"No se ha eliminado el usuario"}