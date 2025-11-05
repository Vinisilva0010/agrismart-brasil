"""
AgriSmart Brasil - Multi-Agent System
Agents package initialization
"""

from .climate_monitor import ClimateMonitorAgent
from .crop_analyzer import CropAnalyzerAgent
from .water_optimizer import WaterOptimizerAgent
from .yield_predictor import YieldPredictorAgent
from .farm_manager import FarmManagerAgent

__all__ = [
    "ClimateMonitorAgent",
    "CropAnalyzerAgent",
    "WaterOptimizerAgent",
    "YieldPredictorAgent",
    "FarmManagerAgent",
]

