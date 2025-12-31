#!/usr/bin/env python3
"""
Version Manager Script for Docker Services
Manages versions and builds Docker images based on version configuration
"""

import yaml
import os
import sys
import subprocess
import argparse
from pathlib import Path

class VersionManager:
    def __init__(self, service_name=None):
        self.base_dir = Path(__file__).parent.parent
        self.service_name = service_name
        
    def get_available_services(self):
        """Get list of available services"""
        services_dir = self.base_dir / "services"
        return [d.name for d in services_dir.iterdir() if d.is_dir()]
    
    def load_version_config(self, service_name):
        """Load version configuration for a service"""
        version_file = self.base_dir / "services" / service_name / "versions" / "version.yml"
        if not version_file.exists():
            raise FileNotFoundError(f"Version file not found: {version_file}")
        
        with open(version_file, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    
    def get_current_version(self, service_name):
        """Get current version for a service"""
        config = self.load_version_config(service_name)
        return config.get('current', 'latest')
    
    def get_version_info(self, service_name, version=None):
        """Get information about a specific version"""
        config = self.load_version_config(service_name)
        if version is None:
            version = config.get('current', 'latest')
        
        for v in config.get('available', []):
            if v['version'] == version:
                return v
        return None
    
    def list_versions(self, service_name):
        """List all available versions for a service"""
        config = self.load_version_config(service_name)
        print(f"\n📦 Available versions for {service_name}:")
        print("=" * 50)
        
        for version_info in config.get('available', []):
            status = "🟢 CURRENT" if version_info['version'] == config.get('current') else ""
            experimental = "⚠️  EXPERIMENTAL" if version_info.get('experimental') else ""
            
            print(f"Version: {version_info['version']} {status} {experimental}")
            print(f"Image: {version_info['image']}")
            print(f"Description: {version_info['description']}")
            print(f"Features: {', '.join(version_info.get('features', []))}")
            print("-" * 30)
    
    def set_version(self, service_name, version):
        """Set current version for a service"""
        version_file = self.base_dir / "services" / service_name / "versions" / "version.yml"
        config = self.load_version_config(service_name)
        
        # Check if version exists
        version_info = self.get_version_info(service_name, version)
        if not version_info:
            print(f"❌ Version {version} not found for {service_name}")
            return False
        
        # Update current version
        config['current'] = version
        
        # Write back to file
        with open(version_file, 'w', encoding='utf-8') as f:
            yaml.dump(config, f, default_flow_style=False, allow_unicode=True)
        
        print(f"✅ Set {service_name} to version {version}")
        return True
    
    def build_service(self, service_name, version=None):
        """Build Docker image for a service with specific version"""
        if version is None:
            version = self.get_current_version(service_name)
        
        version_info = self.get_version_info(service_name, version)
        if not version_info:
            print(f"❌ Version {version} not found for {service_name}")
            return False
        
        service_dir = self.base_dir / "services" / service_name
        
        # Update Dockerfile with version
        self.update_dockerfile(service_name, version_info)
        
        # Build Docker image
        print(f"🔨 Building {service_name}:{version}...")
        try:
            cmd = ["docker", "build", "-t", f"{service_name}:{version}", "."]
            result = subprocess.run(cmd, cwd=service_dir, check=True, capture_output=True, text=True)
            print(f"✅ Successfully built {service_name}:{version}")
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ Build failed: {e}")
            print(f"Error output: {e.stderr}")
            return False
    
    def update_dockerfile(self, service_name, version_info):
        """Update Dockerfile with version-specific configuration"""
        dockerfile_path = self.base_dir / "services" / service_name / "Dockerfile"
        
        # Read current Dockerfile
        with open(dockerfile_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Update FROM line with version-specific image
        lines = content.split('\n')
        for i, line in enumerate(lines):
            if line.startswith('FROM '):
                lines[i] = f"FROM {version_info['image']}"
                break
        
        # Write updated Dockerfile
        with open(dockerfile_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))
        
        print(f"📝 Updated Dockerfile for {service_name} with {version_info['image']}")

def main():
    parser = argparse.ArgumentParser(description='Docker Service Version Manager')
    parser.add_argument('action', choices=['list', 'set', 'build', 'current'], 
                       help='Action to perform')
    parser.add_argument('--service', '-s', help='Service name')
    parser.add_argument('--version', '-v', help='Version to set or build')
    
    args = parser.parse_args()
    
    manager = VersionManager()
    
    if args.action == 'list':
        if args.service:
            manager.list_versions(args.service)
        else:
            services = manager.get_available_services()
            print("Available services:")
            for service in services:
                print(f"  - {service}")
    
    elif args.action == 'current':
        if not args.service:
            print("❌ Service name required for 'current' action")
            sys.exit(1)
        version = manager.get_current_version(args.service)
        print(f"Current version for {args.service}: {version}")
    
    elif args.action == 'set':
        if not args.service or not args.version:
            print("❌ Service name and version required for 'set' action")
            sys.exit(1)
        manager.set_version(args.service, args.version)
    
    elif args.action == 'build':
        if not args.service:
            print("❌ Service name required for 'build' action")
            sys.exit(1)
        manager.build_service(args.service, args.version)

if __name__ == "__main__":
    main()
