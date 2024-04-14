from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from pydantic import BaseModel
from models.models import prediction


app = FastAPI(
    title='Сar predition price'
)

templates = Jinja2Templates(directory="frontend")

app.mount(
    "/frontend",
    StaticFiles(directory="frontend"),
    name="frontend-static"
)

@app.get('/predict/', response_class=HTMLResponse)
def main(request: Request):
    return templates.TemplateResponse("test.html", {"request" : request})

@app.post('/predict/')
def predict_price(request: Request, year: int = Form(...), vehicle_type: str = Form(...), 
                  drivetrain: str = Form(...), transmission: str = Form(...), 
                   engine_hp: int = Form(...), highway: int = Form(...), city: int = Form(...)):

    # global pred

    imput_dict = {'year' : year, 'vehicle_type' : vehicle_type, 'drivetrain' : drivetrain,
                   'transmission' : transmission, 'engine_hp' : engine_hp,
                   'highway': highway , 'city': city}

    year = imput_dict['year']
    vehicle_type = imput_dict['vehicle_type']
    drivetrain = imput_dict['drivetrain']
    transmission = imput_dict['transmission']
    engine_hp = imput_dict['engine_hp']
    highway = imput_dict['highway']
    city = imput_dict['city']

    pred = int(prediction([[year, vehicle_type, drivetrain, transmission, engine_hp, highway, city]]))
    pred = '{0:,}'.format(pred).replace(',', ' ')
    pred = str(pred) + " rub."

    return templates.TemplateResponse('test.html', context={'request': request, 'pred': pred})
    



