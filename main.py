from fastapi import FastAPI, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI
from database import engine, Base


# Инициализация FastAPI
app = FastAPI()

# Подключение статических файлов (например, CSS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Подключение шаблонов
templates = Jinja2Templates(directory="templates")


@app.get("/")
def read_root(request: Request):
    # Отправка данных в шаблон index.html
    return templates.TemplateResponse("index.html", {"request": request, "title": "Cafe Management System"})


# Страница создания клиента
@app.get("/create_client")
def create_client(request: Request):
    return templates.TemplateResponse("client_form.html", {"request": request})


# Страница создания товара
@app.get("/create_product")
def create_product(request: Request):
    return templates.TemplateResponse("product_form.html", {"request": request})


# Страница создания заказа
@app.get("/create_order")
def create_order(request: Request):
    return templates.TemplateResponse("order_form.html", {"request": request})


# Обработчик отправки отзыва
@app.post("/submit")
async def handle_form(input_name: str = Form(...), feedback: str = Form(...)):
    print(f"Получено имя: {input_name}, отзыв: {feedback}")
    return RedirectResponse(url="/", status_code=303)


# Обработчик создания клиента
@app.post("/submit_client")
async def submit_client(name: str = Form(...)):
    print(f"Добавлен клиент: Имя={name}")
    # Здесь можно добавить логику сохранения клиента в базу данных
    return RedirectResponse(url="/", status_code=303)


# Обработчик создания товара
@app.post("/submit_product")
async def submit_product(name: str = Form(...), description: str= Form(...), price: float = Form(...), quantity: int = Form(...)):
    print(f"Добавлен товар: Название={name},Описание={description} Цена={price}, Количество={quantity}")
    # Здесь можно добавить логику сохранения товара в базу данных
    return RedirectResponse(url="/", status_code=303)


# Обработчик создания заказа
@app.post("/submit_order")
async def submit_order(order_id: str = Form(...), product_name: str = Form(...), quantity: int = Form(...), customer_name: str = Form(...)):
    print(f"Создан заказ: Клиент ID={order_id}, Товар ID={product_name}, Количество={quantity}, Кастомное имя={customer_name}")
    # Здесь можно добавить логику сохранения заказа в базу данных
    return RedirectResponse(url="/", status_code=303)
