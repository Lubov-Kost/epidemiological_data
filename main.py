from fastapi import FastAPI, Query
import asyncio
from datetime import datetime, timezone
import random
import logging
from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - [%(levelname)s] - %(name)s - %(message)s"
)
logger = logging.getLogger("EpiDataSimulator")

app = FastAPI(
    title="Epidemiological Data Flow Simulator",
    description="Симулятор потока эпидемиологических данных в реальном времени.",
    version="1.0.0"
)

class SimulationFrequency(str, Enum):
    secondly = "secondly"
    hourly = "hourly"
    daily = "daily"
    monthly = "monthly"

class EpiDataPoint(BaseModel):
    timestamp: str = Field(description="Время генерации данных в формате ISO")
    country: str = Field(description="Страна или регион")
    disease: str = Field(description="Тип заболевания")
    new_cases: int = Field(description="Количество новых случаев за период")
    new_deaths: int = Field(description="Количество летальных исходов")

class SimulationStatus(BaseModel):
    running: bool
    interval_seconds: Optional[int] = None
    frequency_name: Optional[str] = None

class ActionResponse(BaseModel):
    status: str
    message: str

class SimulatorState:
    def __init__(self):
        self.task: Optional[asyncio.Task] = None
        self.interval: int = 60
        self.frequency_name: str = "stopped"

state = SimulatorState()

COUNTRIES = ["Brazil", "India", "Italy", "South Korea", "Argentina", "Philippines", "Palestine"]
DISEASES = ["COVID-19", "Zika Virus", "Malaria", "Dengue"]

async def generate_data_flow(interval_seconds: int):
    logger.info(f"Симуляция запущена. Интервал: {interval_seconds} сек.")
    try:
        while True:
            data = EpiDataPoint(
                timestamp=datetime.now(timezone.utc).isoformat(),
                country=random.choice(COUNTRIES),
                disease=random.choice(DISEASES),
                new_cases=random.randint(0, 5000),
                new_deaths=random.randint(0, 100)
            )
            
            logger.info(f"[DATA STREAM] {data.model_dump_json()}")
            
            await asyncio.sleep(interval_seconds)
    except asyncio.CancelledError:
        logger.info("Симуляция успешно остановлена по запросу.")
        raise
    except Exception as e:
        logger.error(f"Непредвиденная ошибка в симуляции: {e}")

@app.get("/", response_model=ActionResponse, tags=["General"])
async def read_root():
    return ActionResponse(
        status="ok", 
        message="EpiData Simulator is running. Use /docs for API documentation."
    )

@app.get("/simulate", response_model=EpiDataPoint, tags=["Simulation"], summary="Сгенерировать одну точку данных")
async def simulate_once():
    return EpiDataPoint(
        timestamp=datetime.now(timezone.utc).isoformat(),
        country=random.choice(COUNTRIES),
        disease=random.choice(DISEASES),
        new_cases=random.randint(0, 5000),
        new_deaths=random.randint(0, 100)
    )

@app.post("/start", response_model=ActionResponse, tags=["Simulation"], summary="Запустить непрерывную симуляцию")
async def start_simulation(
    frequency: SimulationFrequency = Query(
        default=SimulationFrequency.hourly,
        description="Выберите частоту генерации данных из выпадающего списка"
    )
):
    freq_map = {
        SimulationFrequency.secondly: 1,
        SimulationFrequency.hourly: 3600,
        SimulationFrequency.daily: 86400,
        SimulationFrequency.monthly: 30 * 86400,
    }
    
    interval = freq_map[frequency]

    if state.task and not state.task.done():
        state.task.cancel()

    state.interval = interval
    state.frequency_name = frequency.value
    state.task = asyncio.create_task(generate_data_flow(interval))
    
    return ActionResponse(
        status="started", 
        message=f"Simulation started with frequency: {frequency.value} ({interval}s)"
    )

@app.post("/stop", response_model=ActionResponse, tags=["Simulation"], summary="Остановить симуляцию")
async def stop_simulation():
    if state.task and not state.task.done():
        state.task.cancel()
        state.frequency_name = "stopped"
        return ActionResponse(status="stopped", message="Simulation has been stopped.")
    
    return ActionResponse(status="idle", message="No active simulation to stop.")

@app.get("/status", response_model=SimulationStatus, tags=["Simulation"], summary="Получить текущий статус")
async def get_status():
    if state.task and not state.task.done():
        return SimulationStatus(
            running=True, 
            interval_seconds=state.interval,
            frequency_name=state.frequency_name
        )
    return SimulationStatus(running=False)