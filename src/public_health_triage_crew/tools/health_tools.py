"""
Custom tools for the Public Health Triage Advisor
"""

import requests
import json
from typing import Dict, List, Optional
from crewai.tools import tool

class HealthTools:
    """Collection of health-related tools"""
    
    @staticmethod
    def get_weather_health_risk(location: str) -> str:
        """Get weather-based health risks for a location"""
        try:
            # Mock weather API call (replace with real API)
            weather_data = {
                "temperature": 28,
                "humidity": 75,
                "air_quality": "moderate"
            }
            
            risks = []
            if weather_data["temperature"] > 30:
                risks.append("Heat stress risk - stay hydrated")
            if weather_data["humidity"] > 80:
                risks.append("High humidity - increased infection risk")
            if weather_data["air_quality"] == "poor":
                risks.append("Poor air quality - respiratory issues")
            
            return f"Weather health risks for {location}: {'; '.join(risks) if risks else 'No significant risks'}"
        except Exception as e:
            return f"Unable to get weather data: {str(e)}"
    
    @staticmethod
    def get_disease_outbreak_info(location: str) -> str:
        """Get current disease outbreak information"""
        try:
            # Mock outbreak data (replace with real API)
            outbreaks = {
                "Lagos": ["Malaria", "Dengue"],
                "Kano": ["Measles"],
                "Port Harcourt": ["Cholera"]
            }
            
            if location in outbreaks:
                return f"Current outbreaks in {location}: {', '.join(outbreaks[location])}"
            else:
                return f"No major outbreaks reported in {location}"
        except Exception as e:
            return f"Unable to get outbreak data: {str(e)}"
    
    @staticmethod
    def get_phc_locations(location: str) -> str:
        """Get nearby Primary Health Centre locations"""
        try:
            # Mock PHC data (replace with real geolocation API)
            phc_data = {
                "Lagos": [
                    {"name": "Lagos Island PHC", "distance": "2.3km", "rating": "4.5"},
                    {"name": "Victoria Island PHC", "distance": "3.1km", "rating": "4.2"}
                ],
                "Kano": [
                    {"name": "Kano Central PHC", "distance": "1.8km", "rating": "4.0"}
                ]
            }
            
            if location in phc_data:
                phcs = phc_data[location]
                result = f"Nearby PHCs in {location}:\n"
                for phc in phcs:
                    result += f"- {phc['name']} ({phc['distance']}, Rating: {phc['rating']}/5)\n"
                return result
            else:
                return f"PHC locations for {location} not available"
        except Exception as e:
            return f"Unable to get PHC locations: {str(e)}"
    
    @staticmethod
    def get_medicine_prices(medicine_name: str, location: str) -> str:
        """Get current medicine prices"""
        try:
            # Mock medicine price data (replace with real API)
            prices = {
                "paracetamol": {"Lagos": "₦150-₦300", "Kano": "₦120-₦250"},
                "amoxicillin": {"Lagos": "₦500-₦1200", "Kano": "₦400-₦1000"},
                "malaria_meds": {"Lagos": "₦800-₦2000", "Kano": "₦700-₦1800"}
            }
            
            if medicine_name.lower() in prices and location in prices[medicine_name.lower()]:
                return f"{medicine_name} price in {location}: {prices[medicine_name.lower()][location]}"
            else:
                return f"Price data for {medicine_name} in {location} not available"
        except Exception as e:
            return f"Unable to get medicine prices: {str(e)}"

@tool("weather_health_risk")
def weather_health_risk(location: str) -> str:
    """Get weather-based health risks for a specific location"""
    return HealthTools.get_weather_health_risk(location)


@tool("disease_outbreak_info")
def disease_outbreak_info(location: str) -> str:
    """Get current disease outbreak information for a location"""
    return HealthTools.get_disease_outbreak_info(location)


@tool("phc_locations")
def phc_locations(location: str) -> str:
    """Find nearby Primary Health Centre locations"""
    return HealthTools.get_phc_locations(location)


@tool("medicine_prices")
def medicine_prices(medicine_name: str, location: str) -> str:
    """Get current medicine prices in a specific location"""
    return HealthTools.get_medicine_prices(medicine_name, location)


def create_health_tools():
    """Create and return health-related tools"""
    return [
        weather_health_risk,
        disease_outbreak_info,
        phc_locations,
        medicine_prices,
    ]

