from fastapi import HTTPException, status, APIRouter
from pydantic import BaseModel
from mysql.connector import Error

from connections import mydbProyectoLocal, cursorLocal
#from connections import mydbProyectoCleaver,cursorCleaver

clientesRTR = APIRouter()
cursorClientes = cursorLocal
mydbproy = mydbProyectoLocal


#mydbproy = mydbProyectoCleaver
#cursorClientes = cursorCleaver

class clientes(BaseModel):
    nombres_y_apellidos: str
    direccion: str
    telefono: str
    numero_documento: str
    correo: str

@clientesRTR.get("/clientes", status_code=status.HTTP_302_FOUND)
async def get_clientes():
    selectALL_query = "SELECT * FROM clientes"
    cursorClientes.execute(selectALL_query)
    results = cursorClientes.fetchall()
    return results

@clientesRTR.get("/clientes/{id_cliente}", status_code=status.HTTP_200_OK)
def get_clientes_by_id(id_cliente:int):
    select_query = "SELECT * FROM clientes WHERE id_cliente = %s"
    cursorClientes.execute(select_query, (id_cliente,))
    results = cursorClientes.fetchone()
    if results:
        return results
    else:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    
@clientesRTR.post("/clientescrear", status_code=status.HTTP_201_CREATED)
def insert_clientes(clientes: clientes):
    insert_query="""
    INSERT INTO clientes( nombres_y_apellidos, direccion, telefono, numero_documento, correo)
    VALUES ( %s, %s, %s, %s, %s)"""
    values = (clientes.nombres_y_apellidos,clientes.direccion,clientes.telefono,clientes.numero_documento,clientes.correo)
    
    try:
        cursorClientes.execute(insert_query, values)
        mydbproy.commit()
    except Error as error:
        raise HTTPException(status_code=400, detail=f"Error: {error}")
    return {"message": "Cliente creado exitosamente"}