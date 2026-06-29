#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Network Problem Analyzer
Analyzes network issues and identifies problems
"""

import logging
from typing import Dict, List

logger = logging.getLogger(__name__)

class NetworkAnalyzer:
    """Network problem analyzer"""
    
    def __init__(self):
        self.issues = []
        self.severity_levels = ['critical', 'high', 'medium', 'low']
        
    def analyze_ping_results(self, ping_results: Dict) -> List[Dict]:
        """
        Analyze ping results to identify issues
        
        Args:
            ping_results: Results from ping tests
            
        Returns:
            List of identified issues
        """
        issues = []
        
        for host, result in ping_results.items():
            if not result['success']:
                issues.append({
                    'host': host,
                    'issue': 'Host unreachable',
                    'severity': 'high',
                    'timestamp': None
                })
                logger.warning(f"Issue detected: {host} is unreachable")
                
        return issues
        
    def analyze_network_latency(self, latency_data: Dict) -> List[Dict]:
        """Analyze network latency issues"""
        issues = []
        threshold_ms = 100  # 100ms threshold
        
        for host, latency in latency_data.items():
            if latency > threshold_ms:
                issues.append({
                    'host': host,
                    'issue': f'High latency: {latency}ms',
                    'severity': 'medium',
                    'latency': latency
                })
                logger.warning(f"High latency detected on {host}: {latency}ms")
                
        return issues
        
    def analyze_bandwidth(self, bandwidth_data: Dict) -> List[Dict]:
        """Analyze bandwidth issues"""
        issues = []
        threshold_percent = 85  # 85% threshold
        
        for interface, usage in bandwidth_data.items():
            if usage > threshold_percent:
                issues.append({
                    'interface': interface,
                    'issue': f'High bandwidth usage: {usage}%',
                    'severity': 'medium',
                    'usage': usage
                })
                logger.warning(f"High bandwidth usage on {interface}: {usage}%")
                
        return issues
        
    def analyze_device_status(self, device_status: Dict) -> List[Dict]:
        """Analyze device status"""
        issues = []
        
        for device, status in device_status.items():
            if status['state'] == 'down':
                issues.append({
                    'device': device,
                    'issue': 'Device is down',
                    'severity': 'critical',
                    'uptime': status.get('uptime')
                })
                logger.error(f"Critical: Device {device} is down")
                
        return issues
        
    def generate_analysis_report(self, all_issues: List[Dict]) -> Dict:
        """Generate analysis report"""
        report = {
            'total_issues': len(all_issues),
            'critical': len([i for i in all_issues if i.get('severity') == 'critical']),
            'high': len([i for i in all_issues if i.get('severity') == 'high']),
            'medium': len([i for i in all_issues if i.get('severity') == 'medium']),
            'low': len([i for i in all_issues if i.get('severity') == 'low']),
            'issues': all_issues
        }
        
        logger.info(f"Analysis Report: {report['total_issues']} issues found")
        return report
