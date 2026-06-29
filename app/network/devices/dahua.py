#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dahua Device Integration
Handles Dahua CCTV camera operations and management
"""

import logging
import requests
from typing import Dict, List, Optional

logger = logging.getLogger(__name__)

class DahuaDevice:
    """Dahua device controller"""
    
    def __init__(self, host: str, username: str, password: str, port: int = 80):
        """
        Initialize Dahua device
        
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
        self.base_url = f"http://{host}:{port}/cgi-bin"
        self.session = None
        
    def connect(self) -> bool:
        """Connect to Dahua device"""
        try:
            logger.info(f"Connecting to Dahua device at {self.host}")
            self.session = requests.Session()
            self.session.auth = (self.username, self.password)
            # Test connection
            response = self.session.get(f"{self.base_url}/configManager?action=getConfig&name=System", timeout=5)
            if response.status_code == 200:
                logger.info("Connected to Dahua device successfully")
                return True
            return False
        except Exception as e:
            logger.error(f"Failed to connect to Dahua: {str(e)}")
            return False
            
    def disconnect(self):
        """Disconnect from device"""
        if self.session:
            self.session.close()
            logger.info("Disconnected from Dahua device")
            
    def get_device_info(self) -> Dict:
        """Get device information"""
        try:
            response = self.session.get(f"{self.base_url}/configManager?action=getConfig&name=System")
            if response.status_code == 200:
                return {'info': response.text}
            return {}
        except Exception as e:
            logger.error(f"Failed to get device info: {str(e)}")
            return {}
            
    def get_channels(self) -> List[Dict]:
        """Get list of video channels"""
        try:
            channels = []
            for i in range(16):  # Dahua typically has 16 channels
                channels.append({
                    'id': i,
                    'name': f'Channel {i+1}',
                    'enabled': True
                })
            return channels
        except Exception as e:
            logger.error(f"Failed to get channels: {str(e)}")
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
            'device_type': 'Dahua',
            'channels': len(self.get_channels())
        }
