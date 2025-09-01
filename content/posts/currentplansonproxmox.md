---
title: "Proxmox Backup Strategy: Local Windows Share & Backblaze B2 Cloud Sync"
date: 2022-07-16T00:00:00-05:00
tags: ["proxmox", "backup", "self-hosting", "backblaze", "windows", "data-protection", "homelab"]
description: "A comprehensive guide to setting up an efficient Proxmox backup system using local Windows 10 storage and Backblaze B2 for secure offsite protection. Learn about my 4x500GB SSD setup and automated backup workflow."
type: post
weight: 25
showTableOfContents: true
featuredImage: "/images/proxmox-backup-setup.jpg"
featuredImageAlt: "Proxmox backup setup with local storage and cloud sync"
canonicalURL: "https://chrisallen.us/posts/currentplansonproxmox/"
---

*Last updated: July 16, 2022 | Reading time: 5 minutes*
# My Proxmox Backup Strategy: Local + Cloud Protection

*Table of Contents*
- [Hardware Configuration](#hardware-configuration)
- [Local Backup Setup](#local-backup-setup)
- [Cloud Sync with Backblaze B2](#cloud-sync-with-backblaze-b2)
- [Automation & Scheduling](#automation--scheduling)
- [Restoration Process](#restoration-process)
- [Cost Analysis](#cost-analysis)
- [Lessons Learned](#lessons-learned)

In this post, I'll walk you through my Proxmox backup strategy that combines local storage with cloud backup for maximum data protection. This setup ensures quick recovery from local storage while maintaining an offsite copy for disaster recovery.

## Hardware Configuration

### Primary Storage
- **4 x 500GB SSDs** in ZFS RAID-10 configuration
  - Total usable space: ~930GB
  - Excellent read/write performance for VM operations
  - Data redundancy with mirroring

### Backup Storage
- **Windows 10 PC** with 4TB HDD
  - Dedicated share for Proxmox backups
  - Additional storage for ISO files and templates
  - Scheduled maintenance windows for backup operations

## Local Backup Setup

### Windows Share Configuration
1. Created a dedicated user account for Proxmox backups
2. Set up SMB share with appropriate permissions
3. Configured Proxmox to use the share for:
   - Daily VM/CT backups
   - ISO storage
   - Template storage

### Backup Retention Policy
- **Daily Backups**: Kept for 7 days
- **Weekly Backups**: Kept for 4 weeks
- **Monthly Backups**: Kept for 3 months

## Cloud Sync with Backblaze B2

### Why Backblaze B2?
- Cost-effective cloud storage ($0.005/GB/month)
- No minimum storage duration fees
- Free egress (data download) up to 3x monthly average storage
- Reliable infrastructure with 99.9% uptime

### Sync Configuration
- Using `rclone` for encrypted backup sync
- Client-side encryption for sensitive data
- Bandwidth throttling to prevent network congestion
- Email notifications for sync status

## Automation & Scheduling

### Proxmox Backup Jobs
```bash
# Example backup job for all VMs
vzdump 100 101 102 --compress zstd --mode snapshot --storage win10_backup --mailto admin@example.com
```

### Windows Task Scheduler
- Runs `rclone sync` command nightly
- Logs all operations to a dedicated file
- Sends email notifications on completion/failure

## Restoration Process

### Local Restoration
1. Access Proxmox web interface
2. Navigate to local storage
3. Select backup and click "Restore"
4. Configure VM settings as needed

### Cloud Restoration
1. Download backup from Backblaze B2
2. Decrypt if using client-side encryption
3. Upload to Proxmox storage
4. Restore using web interface

## Cost Analysis

| Component | Cost | Notes |
|-----------|------|-------|
| 4x 500GB SSDs | $300 | One-time cost |
| Backblaze B2 | ~$5/month | Based on 1TB storage |
| Windows 10 PC | $0 | Existing hardware |
| **Total First Year** | **$360** | ~$30/month |
| **Subsequent Years** | **$60/year** | Storage costs only |

## Lessons Learned

### What Worked Well
- ZFS RAID-10 provides excellent performance
- Local backups are fast for quick recovery
- Backblaze B2 is cost-effective for offsite storage
- Automation reduces manual intervention

### Challenges & Solutions
1. **Initial sync was slow**
   - Solution: Performed initial backup locally, then moved offsite

2. **Permission issues with Windows share**
   - Solution: Created dedicated backup user with appropriate permissions

3. **Storage space management**
   - Solution: Implemented strict retention policies

4. **Bandwidth usage**
   - Solution: Scheduled backups during off-peak hours

## Future Improvements
- Implement backup verification scripts
- Add monitoring for backup success/failure
- Consider using Proxmox Backup Server
- Explore incremental backup options

---

*Have questions about my setup or want to share your own backup strategy? Leave a comment below!*

*For more homelab and self-hosting content, consider [subscribing to my newsletter](#) or following me on [Twitter](#).*
