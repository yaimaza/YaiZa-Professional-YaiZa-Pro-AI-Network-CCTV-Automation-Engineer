#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Network Health Check (Ping)
Performs initial network connectivity and health checks
"""

import logging
import subprocess
import platform
from typing import Dict, List, Tuple

logger = logging.getLogger(__name__)

class NetworkPing:
    """Network ping and health check"""
    
    def __init__(self):
        self.results = {}
        self.os_type = platform.system()
        
    def ping_host(self, host: str, count: int = 4) -> Tuple[bool, Dict]:
        """
        Ping a host
        
        Args:
            host: Target host IP or domain
            count: Number of ping packets
            
        Returns:
            Tuple of (success, statistics)
        """
        try:
            logger.info(f"Pinging {host}...")
            
            if self.os_type == "Windows":
                cmd = ["ping", "-n", str(count), host]
            else:
                cmd = ["ping", "-c", str(count), host]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            
            if result.returncode == 0:
                logger.info(f"✓ Host {host} is online")
                return True, {'host': host, 'status': 'online', 'output': result.stdout}
            else:
                logger.warning(f"✗ Host {host} is offline")
                return False, {'host': host, 'status': 'offline', 'output': result.stderr}
                
        except Exception as e:
            logger.error(f"Ping failed for {host}: {str(e)}")
            return False, {'host': host, 'status': 'error', 'error': str(e)}
            
    def ping_multiple(self, hosts: List[str]) -> Dict:
        """
        Ping multiple hosts
        
        Args:
            hosts: List of hosts to ping
            
        Returns:
            Dictionary of ping results
        """
        results = {}
        for host in hosts:
            success, data = self.ping_host(host)
            results[host] = {'success': success, 'data': data}
        return results
        
    def check_network_interfaces(self) -> List[Dict]:
        """Check network interfaces"""
        try:
            if self.os_type == "Windows":
                cmd = ["ipconfig"]
            else:
                cmd = ["ifconfig"]
                
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            logger.info("Network interfaces checked")
            return [{'output': result.stdout}]
            
        except Exception as e:
            logger.error(f"Failed to check interfaces: {str(e)}")
            return []
            
    def check_dns(self, domain: str = "8.8.8.8") -> bool:
        """Check DNS resolution"""
        try:
            logger.info(f"Checking DNS resolution for {domain}")
            success, _ = self.ping_host(domain)
            return success
        except Exception as e:
            logger.error(f"DNS check failed: {str(e)}")
            return False
