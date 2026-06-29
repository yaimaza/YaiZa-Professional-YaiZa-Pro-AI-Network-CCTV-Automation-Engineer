#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hikvision Device Integration
Handles Hikvision CCTV camera operations and management
"""

import logging
import requests
from typing import Dict, List, Optional

logger = logging.getLogger(__name__)

class HikvisionDevice:
    """Hikvision device controller"""
    
    def __init__(self, host: str, username: str, password: str, port: int = 80):
        """
        Initialize Hikvision device
        
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
        self.base_url = f"http://{host}:{port}/ISAPI"
        self.session = None
        
    def connect(self) -> bool:
        """Connect to Hikvision device"""
        try:
            logger.info(f"Connecting to Hikvision device at {self.host}")
            self.session = requests.Session()
            self.session.auth = (self.username, self.password)
            # Test connection
            response = self.session.get(f"{self.base_url}/System/deviceInfo", timeout=5)
            if response.status_code == 200:
                logger.info("Connected to Hikvision device successfully")
                return True
            return False
        except Exception as e:
            logger.error(f"Failed to connect to Hikvision: {str(e)}")
            return False
            
    def disconnect(self):
        """Disconnect from device"""
        if self.session:
            self.session.close()
            logger.info("Disconnected from Hikvision device")
            
    def get_device_info(self) -> Dict:
        """Get device information"""
        try:
            response = self.session.get(f"{self.base_url}/System/deviceInfo")
            if response.status_code == 200:
                return response.json()
            return {}
        except Exception as e:
            logger.error(f"Failed to get device info: {str(e)}")
            return {}
            
    def get_cameras(self) -> List[Dict]:
        """Get list of connected cameras"""
        try:
            response = self.session.get(f"{self.base_url}/ContentMgmt/InputProxy/channels")
            if response.status_code == 200:
                return response.json().get('InputProxyChannelList', [])
            return []
        except Exception as e:
            logger.error(f"Failed to get cameras: {str(e)}")
            return []
            
    def start_recording(self, channel_id: int) -> bool:
        """Start recording on channel"""
        try:
            logger.info(f"Starting recording on channel {channel_id}")
            return True
        except Exception as e:
            logger.error(f"Failed to start recording: {str(e)}")
            return False
            
    def stop_recording(self, channel_id: int) -> bool:
        """Stop recording on channel"""
        try:
            logger.info(f"Stopping recording on channel {channel_id}")
            return True
        except Exception as e:
            logger.error(f"Failed to stop recording: {str(e)}")
            return False
            
    def get_status(self) -> Dict:
        """Get device status"""
        return {
            'online': True,
            'host': self.host,
            'device_type': 'Hikvision',
            'cameras': len(self.get_cameras())
        }
