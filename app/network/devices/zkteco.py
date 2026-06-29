#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ZKTeco Access Control Integration
Handles ZKTeco access control and time attendance operations
"""

import logging
import requests
from typing import Dict, List, Optional

logger = logging.getLogger(__name__)

class ZKTecoDevice:
    """ZKTeco device controller"""
    
    def __init__(self, host: str, username: str, password: str, port: int = 80):
        """
        Initialize ZKTeco device
        
        Args:
            host: Device IP address
            username: Authentication username
            password: Authentication password
            port: Device port (default: 80)
        """
        self.host = host
        self.username = username
        self.password = password
        self.port = port
        self.base_url = f"http://{host}:{port}"
        self.session = None
        
    def connect(self) -> bool:
        """Connect to ZKTeco device"""
        try:
            logger.info(f"Connecting to ZKTeco device at {self.host}")
            self.session = requests.Session()
            self.session.auth = (self.username, self.password)
            # Test connection
            response = self.session.get(f"{self.base_url}/system?action=get", timeout=5)
            if response.status_code == 200:
                logger.info("Connected to ZKTeco device successfully")
                return True
            return False
        except Exception as e:
            logger.error(f"Failed to connect to ZKTeco: {str(e)}")
            return False
            
    def disconnect(self):
        """Disconnect from device"""
        if self.session:
            self.session.close()
            logger.info("Disconnected from ZKTeco device")
            
    def get_device_info(self) -> Dict:
        """Get device information"""
        try:
            response = self.session.get(f"{self.base_url}/system?action=get")
            if response.status_code == 200:
                return response.json()
            return {}
        except Exception as e:
            logger.error(f"Failed to get device info: {str(e)}")
            return {}
            
    def get_users(self) -> List[Dict]:
        """Get list of users"""
        try:
            response = self.session.get(f"{self.base_url}/user?action=get")
            if response.status_code == 200:
                return response.json().get('data', [])
            return []
        except Exception as e:
            logger.error(f"Failed to get users: {str(e)}")
            return []
            
    def get_attendance_logs(self, limit: int = 100) -> List[Dict]:
        """Get attendance logs"""
        try:
            response = self.session.get(f"{self.base_url}/attendance?action=get&limit={limit}")
            if response.status_code == 200:
                return response.json().get('data', [])
            return []
        except Exception as e:
            logger.error(f"Failed to get attendance logs: {str(e)}")
            return []
            
    def get_door_status(self) -> Dict:
        """Get door status"""
        try:
            response = self.session.get(f"{self.base_url}/door?action=status")
            if response.status_code == 200:
                return response.json()
            return {}
        except Exception as e:
            logger.error(f"Failed to get door status: {str(e)}")
            return {}
            
    def unlock_door(self, door_id: int) -> bool:
        """Unlock door"""
        try:
            logger.info(f"Unlocking door {door_id}")
            response = self.session.post(f"{self.base_url}/door?action=unlock&door_id={door_id}")
            return response.status_code == 200
        except Exception as e:
            logger.error(f"Failed to unlock door: {str(e)}")
            return False
            
    def get_status(self) -> Dict:
        """Get device status"""
        return {
            'online': True,
            'host': self.host,
            'device_type': 'ZKTeco',
            'users': len(self.get_users())
        }
