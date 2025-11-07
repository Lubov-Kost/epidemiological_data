from fastapi import FastAPI
import asyncio
from datetime import datetime
import random

app = FastAPI(title="Data Flow Simulator")

# Глобальная переменная для хранения задачи
current_task = None

async def simulate_data_flow(interval_seconds: int):
    """
    Симуляция потока данных с заданной частотой дискретизации.
    """
    print(f"[INFO] Simulation started with interval = {interval_seconds} sec")
    try:
        while True:
            data = {
                "timestamp": datetime.utcnow().isoformat(),
                "value": round(random.uniform(0, 100), 2),
            }
            print(f"[DATA] {data}")
            await asyncio.sleep(interval_seconds)
    except asyncio.CancelledError:
        print("[INFO] Simulation stopped.")
        raise

@app.get("/")
def read_root():
    """
    Приветственное сообщение.
    """
    return {"message": "Hello, FastAPI! Use /docs to interact with the simulator."}


@app.get("/simulate")
async def simulate_once():
    """
    Разовая симуляция данных — просто возвращает случайное значение.
    """
    data = {
        "timestamp": datetime.utcnow().isoformat(),
        "value": round(random.uniform(0, 100), 2),
    }
    return {"status": "success", "data": data}


@app.post("/start")
async def start_simulation(frequency: str = "hourly"):
    """
    Запуск симуляции данных.
    frequency: "hourly", "daily", "monthly", "custom" и т.п.
    """
    global current_task

    # Определяем частоту (в секундах)
    freq_map = {
        "hourly": 3600,
        "daily": 86400,
        "monthly": 30 * 86400,
    }
    interval = freq_map.get(frequency, 60)  # по умолчанию — 1 минута

    # Если уже идёт симуляция — останавливаем
    if current_task and not current_task.done():
        current_task.cancel()

    # Запускаем новую задачу
    current_task = asyncio.create_task(simulate_data_flow(interval))
    return {"status": "started", "interval_seconds": interval}


@app.post("/stop")
async def stop_simulation():
    """
    Остановка симуляции.
    """
    global current_task
    if current_task and not current_task.done():
        current_task.cancel()
        return {"status": "stopping"}
    return {"status": "no active simulation"}


@app.get("/status")
async def get_status():
    """
    Проверка состояния симуляции.
    """
    if current_task and not current_task.done():
        return {"running": True}
    return {"running": False}
