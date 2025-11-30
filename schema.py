from typing import List, Optional, Dict, Any, Literal, Annotated
import operator
from pydantic import BaseModel, Field
from datetime import datetime

# === Agent Types ===
AgentType = Literal["router", "local_specialist", "global_researcher", "synthesizer", "booking"]

# === 1. Vehicle & Database Schemas ===
class VehicleSpecs(BaseModel):
    vehicle_id: str
    name: str
    brand: str
    model: str
    year: int
    type: str
    price: float
    mileage: float
    fuel_type: str
    transmission: str
    engine_cc: int
    power: str
    torque: str
    seating: int
    features: List[str] = Field(default_factory=list)
    safety_rating: Optional[float] = None
    warranty_years: int
    colors_available: List[str] = Field(default_factory=list)
    stock_status: str

# === 2. Tool Request Schemas ===
class InventorySearchRequest(BaseModel):
    budget_max: Optional[float] = None
    vehicle_type: Optional[str] = None
    fuel_type: Optional[str] = None
    seating_min: Optional[int] = None
    brand: Optional[str] = None
    sort_by: Optional[str] = None

class FinancingCalculation(BaseModel):
    vehicle_price: float
    down_payment: float = 0.0
    loan_term_months: int = 60
    interest_rate: float = 9.0

class ComparisonRequest(BaseModel):
    vehicle_ids: List[str]

class DealOffer(BaseModel):
    vehicle_id: str
    vehicle_name: str
    final_price: float
    discount_applied: float
    valid_until: datetime

class Message(BaseModel):
    role: str 
    content: str
    timestamp: datetime = Field(default_factory=datetime.now)
    metadata: Dict[str, Any] = Field(default_factory=dict)

class CustomerProfile(BaseModel):
    name: Optional[str] = None
    budget_max: Optional[float] = None
    preferences: List[str] = Field(default_factory=list)
    usage_type: Optional[str] = None

# ==========================================
# 🚨 STATE DEFINITION
# ==========================================
class ConversationState(BaseModel):
    # 'operator.add' allows Parallel Workers to both write to messages at the same time
    messages: Annotated[List[Message], operator.add] = Field(default_factory=list)
    
    # Router Decisions
    tool_used: str = "CHAT"
    parallel_query_1: Optional[str] = None
    parallel_query_2: Optional[str] = None
    
    # Booking Details (For Human-in-the-Loop)
    booking_details: Optional[str] = None