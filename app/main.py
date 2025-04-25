from fastapi import FastAPI
from app.database import engine, Base
from app.routers import route, bus, ticket


app = FastAPI(title="Bus Ticketing API",
    version="1.0.0",
    description="API for managing buses, routes, and ticket bookings")

app.include_router(route.router, prefix="/api/v1/routes", tags=["Routes"])
app.include_router(bus.router, prefix="/api/v1/buses", tags=["Buses"])
app.include_router(ticket.router, prefix="/api/v1/tickets", tags=["Tickets"])

