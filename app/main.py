from fastapi import FastAPI
from app.database import engine, Base
from app.routers import route, bus, ticket
from app.auth import routes as auth_routes


app = FastAPI(title="TransitPRO",
    version="1.0.0",
    description="API for managing buses, routes, and ticket bookings")

app.include_router(route.router, prefix="/api/v1/routes", tags=["Routes"])
app.include_router(bus.router, prefix="/api/v1/buses", tags=["Buses"])
app.include_router(ticket.router, prefix="/api/v1/tickets", tags=["Tickets"])
app.include_router(auth_routes.router, prefix="/api/v1/auth", tags=["Authentication"])

