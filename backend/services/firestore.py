"""
Firestore Service
Handles all database operations with Google Cloud Firestore
"""

import os
from typing import Dict, Any, List, Optional
from datetime import datetime
from google.cloud import firestore
from google.oauth2 import service_account


class FirestoreService:
    """Service for interacting with Google Cloud Firestore."""
    
    def __init__(self):
        """Initialize Firestore client."""
        # Check if running in Cloud Run or local
        credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
        
        if credentials_path and os.path.exists(credentials_path):
            credentials = service_account.Credentials.from_service_account_file(
                credentials_path
            )
            self.db = firestore.Client(credentials=credentials)
        else:
            # Use default credentials in Cloud Run
            self.db = firestore.Client()
    
    # ===== FARM OPERATIONS =====
    
    async def create_farm(self, farm_id: str, farm_data: Dict[str, Any]) -> Dict[str, Any]:
        """Create a new farm record."""
        farm_data['created_at'] = datetime.utcnow()
        farm_data['updated_at'] = datetime.utcnow()
        
        self.db.collection('farms').document(farm_id).set(farm_data)
        
        return {"status": "success", "farm_id": farm_id}
    
    async def get_farm(self, farm_id: str) -> Optional[Dict[str, Any]]:
        """Get farm data by ID."""
        doc = self.db.collection('farms').document(farm_id).get()
        
        if doc.exists:
            return doc.to_dict()
        return None
    
    async def update_farm(self, farm_id: str, updates: Dict[str, Any]) -> Dict[str, Any]:
        """Update farm data."""
        updates['updated_at'] = datetime.utcnow()
        
        self.db.collection('farms').document(farm_id).update(updates)
        
        return {"status": "success", "farm_id": farm_id}
    
    async def list_farms(self, user_id: Optional[str] = None) -> List[Dict[str, Any]]:
        """List all farms, optionally filtered by user."""
        query = self.db.collection('farms')
        
        if user_id:
            query = query.where('user_id', '==', user_id)
        
        docs = query.stream()
        
        farms = []
        for doc in docs:
            farm_data = doc.to_dict()
            farm_data['id'] = doc.id
            farms.append(farm_data)
        
        return farms
    
    # ===== CROP OPERATIONS =====
    
    async def add_crop(self, farm_id: str, crop_data: Dict[str, Any]) -> Dict[str, Any]:
        """Add a crop to a farm."""
        crop_data['created_at'] = datetime.utcnow()
        crop_data['farm_id'] = farm_id
        
        doc_ref = self.db.collection('crops').document()
        doc_ref.set(crop_data)
        
        return {"status": "success", "crop_id": doc_ref.id}
    
    async def get_crops(self, farm_id: str) -> List[Dict[str, Any]]:
        """Get all crops for a farm."""
        docs = self.db.collection('crops').where('farm_id', '==', farm_id).stream()
        
        crops = []
        for doc in docs:
            crop_data = doc.to_dict()
            crop_data['id'] = doc.id
            crops.append(crop_data)
        
        return crops
    
    async def update_crop(self, crop_id: str, updates: Dict[str, Any]) -> Dict[str, Any]:
        """Update crop data."""
        updates['updated_at'] = datetime.utcnow()
        
        self.db.collection('crops').document(crop_id).update(updates)
        
        return {"status": "success", "crop_id": crop_id}
    
    # ===== ANALYSIS HISTORY =====
    
    async def save_analysis(self, analysis_type: str, analysis_data: Dict[str, Any]) -> Dict[str, Any]:
        """Save an analysis result."""
        analysis_data['type'] = analysis_type
        analysis_data['timestamp'] = datetime.utcnow()
        
        doc_ref = self.db.collection('analyses').document()
        doc_ref.set(analysis_data)
        
        return {"status": "success", "analysis_id": doc_ref.id}
    
    async def get_analyses(
        self,
        farm_id: str,
        analysis_type: Optional[str] = None,
        limit: int = 50
    ) -> List[Dict[str, Any]]:
        """Get analysis history for a farm."""
        query = self.db.collection('analyses').where('farm_id', '==', farm_id)
        
        if analysis_type:
            query = query.where('type', '==', analysis_type)
        
        query = query.order_by('timestamp', direction=firestore.Query.DESCENDING).limit(limit)
        
        docs = query.stream()
        
        analyses = []
        for doc in docs:
            analysis_data = doc.to_dict()
            analysis_data['id'] = doc.id
            analyses.append(analysis_data)
        
        return analyses
    
    # ===== SENSOR DATA =====
    
    async def save_sensor_data(self, farm_id: str, sensor_data: Dict[str, Any]) -> Dict[str, Any]:
        """Save sensor readings."""
        sensor_data['farm_id'] = farm_id
        sensor_data['timestamp'] = datetime.utcnow()
        
        doc_ref = self.db.collection('sensor_data').document()
        doc_ref.set(sensor_data)
        
        return {"status": "success", "data_id": doc_ref.id}
    
    async def get_sensor_data(
        self,
        farm_id: str,
        sensor_type: Optional[str] = None,
        hours: int = 24
    ) -> List[Dict[str, Any]]:
        """Get recent sensor data."""
        from datetime import timedelta
        
        cutoff_time = datetime.utcnow() - timedelta(hours=hours)
        
        query = self.db.collection('sensor_data').where('farm_id', '==', farm_id)
        query = query.where('timestamp', '>=', cutoff_time)
        
        if sensor_type:
            query = query.where('sensor_type', '==', sensor_type)
        
        query = query.order_by('timestamp', direction=firestore.Query.DESCENDING)
        
        docs = query.stream()
        
        data = []
        for doc in docs:
            sensor_reading = doc.to_dict()
            sensor_reading['id'] = doc.id
            data.append(sensor_reading)
        
        return data
    
    # ===== IRRIGATION SCHEDULES =====
    
    async def save_irrigation_schedule(
        self,
        farm_id: str,
        schedule_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Save an irrigation schedule."""
        schedule_data['farm_id'] = farm_id
        schedule_data['created_at'] = datetime.utcnow()
        
        doc_ref = self.db.collection('irrigation_schedules').document()
        doc_ref.set(schedule_data)
        
        return {"status": "success", "schedule_id": doc_ref.id}
    
    async def get_active_irrigation_schedule(self, farm_id: str) -> Optional[Dict[str, Any]]:
        """Get the current active irrigation schedule."""
        docs = (
            self.db.collection('irrigation_schedules')
            .where('farm_id', '==', farm_id)
            .where('active', '==', True)
            .limit(1)
            .stream()
        )
        
        for doc in docs:
            schedule = doc.to_dict()
            schedule['id'] = doc.id
            return schedule
        
        return None
    
    # ===== ALERTS =====
    
    async def create_alert(self, farm_id: str, alert_data: Dict[str, Any]) -> Dict[str, Any]:
        """Create a new alert."""
        alert_data['farm_id'] = farm_id
        alert_data['created_at'] = datetime.utcnow()
        alert_data['read'] = False
        
        doc_ref = self.db.collection('alerts').document()
        doc_ref.set(alert_data)
        
        return {"status": "success", "alert_id": doc_ref.id}
    
    async def get_alerts(self, farm_id: str, unread_only: bool = False) -> List[Dict[str, Any]]:
        """Get alerts for a farm."""
        query = self.db.collection('alerts').where('farm_id', '==', farm_id)
        
        if unread_only:
            query = query.where('read', '==', False)
        
        query = query.order_by('created_at', direction=firestore.Query.DESCENDING)
        
        docs = query.stream()
        
        alerts = []
        for doc in docs:
            alert_data = doc.to_dict()
            alert_data['id'] = doc.id
            alerts.append(alert_data)
        
        return alerts
    
    async def mark_alert_read(self, alert_id: str) -> Dict[str, Any]:
        """Mark an alert as read."""
        self.db.collection('alerts').document(alert_id).update({
            'read': True,
            'read_at': datetime.utcnow()
        })
        
        return {"status": "success", "alert_id": alert_id}

