import azure.functions as func
import logging
from ..services.car_service import list_available_cars
from ..utils.database import get_db_connection

app = func.FunctionApp()

@app.function_name(name="ListCars")
@app.route(route="cars", methods=["GET"], auth_level=func.AuthLevel.ANONYMOUS)
def list_cars(req: func.HttpRequest) -> func.HttpResponse:
    try:
        conn = get_db_connection()
        cars = list_available_cars(conn)
        return func.HttpResponse(
            body=cars.to_json(orient="records"),
            mimetype="application/json",
            status_code=200
        )
    except Exception as e:
        logging.error(f"Erro ao listar carros: {str(e)}")
        return func.HttpResponse(
            body='{"error": "Erro interno no servidor"}',
            mimetype="application/json",
            status_code=500
        )
