#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ubiquiti Device Integration
Handles Ubiquiti wireless and network device operations
"""

import logging
import requests
from typing import Dict, List, Optional

logger = logging.getLogger(__name__)

class UbiquitiDevice:
    """Ubiquiti device controller"""
    
    def __init__(self, host: str, username: str, password: str, port: int = 443):
        """
        Initialize Ubiquiti device
        
        Args:
            host: Device IP address
            username: Authentication username
            password: Authentication password
            port: Device port (default: 443)
        """
        self.host = host
        self.username = username
        self.password = password
        self.port = port
        self.base_url = f"https://{host}:{port}/api"
        self.session = None
        self.token = None
        
    def connect(self) -> bool:
        """Connect to Ubiquiti device"""
        try:
            logger.info(f"Connecting to Ubiquiti device at {self.host}")
            self.session = requests.Session()
            self.session.verify = False  # Skip SSL verification for local devices
            
            # Authenticate
            auth_data = {
                'username': self.username,
                'password': self.password
            }
            response = self.session.post(f"{self.base_url}/auth/login", json=auth_data, timeout=5)
            if response.status_code == 200:
                self.token = response.json().get('meta', {}).get('token')
                logger.info("Connected to Ubiquiti device successfully")
                return True
            return False
        except Exception as e:
            logger.error(f"Failed to connect to Ubiquiti: {str(e)}")
            return False
            
    def disconnect(self):
        """Disconnect from device"""
        if self.session:
            self.session.close()
            logger.info("Disconnected from Ubiquiti device")
            
    def get_devices(self) -> List[Dict]:
        """Get connected devices"""
        try:
            headers = {'X-CSRF-Token': self.token} if self.token else {}
            response = self.session.get(f"{self.base_url}/s/default/stat/device", headers=headers)
            if response.status_code == 200:
                return response.json().get('data', [])
            return []
        except Exception as e:
            logger.error(f"Failed to get devices: {str(e)}")
            return []
            
    def get_access_points(self) -> List[Dict]:
        """Get access points"""
        try:
            headers = {'X-CSRF-Token': self.token} if self.token else {}
            response = self.session.get(f"{self.base_url}/s/default/stat/uap", headers=headers)
            if response.status_code == 200:
                return response.json().get('data', [])
            return []
        except Exception as e:
            logger.error(f"Failed to get access points: {str(e)}")
            return []
            
    def get_network_stats(self) -> Dict:
        """Get network statistics"""
        try:
            headers = {'X-CSRF-Token': self.token} if self.token else {}
            response = self.session.get(f"{self.base_url}/s/default/stat/sites", headers=headers)
            if response.status_code == 200:
                return response.json().get('data', [{}])[0]
            return {}
        except Exception as e:
            logger.error(f"Failed to get network stats: {str(e)}")
            return {}
            
    def get_status(self) -> Dict:
        """Get device status"""
        return {
            'online': True,
            'host': self.host,
            'device_type': 'Ubiquiti',
            'devices': len(self.get_devices()),
            'access_points': len(self.get_access_points())
        }
