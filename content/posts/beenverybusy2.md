---
title: "From WordPress to Hugo: My Website Migration Journey & Tech Upgrades"
date: 2022-06-15T11:25:52-05:00
tags: ["hugo", "wordpress", "syncthing", "proxmox", "self-hosting", "homelab", "server-migration"]
description: "Discover my journey of migrating from WordPress to Hugo, setting up Syncthing for file synchronization, and upgrading my homelab with a 1U server and HP ProCurve switch."
type: post
weight: 25
showTableOfContents: true
featuredImage: "/images/server-rack-upgrade.jpg"
featuredImageAlt: "Homelab server rack with new 1U server and network switch"
canonicalURL: "https://chrisallen.us/posts/beenverybusy2/"
---

*Last updated: June 15, 2022 | Reading time: 4 minutes*

# My Homelab Evolution: Website Migration & Infrastructure Upgrades

Balancing a full-time job with content creation and homelab projects is always challenging, but I'm excited to share some significant updates on my recent tech endeavors. In this post, I'll walk you through my website migration from WordPress to Hugo, upcoming Syncthing tutorial, and the latest additions to my homelab setup.

## Why I'm Moving from WordPress to Hugo

After years of using WordPress, I've decided to migrate to [Hugo](https://gohugo.io/), a static site generator. Here's why:

- **Blazing Fast Performance**: Static sites load significantly faster than dynamic WordPress sites
- **Enhanced Security**: No database means fewer vulnerabilities to exploit
- **Simplified Maintenance**: No more worrying about PHP updates or database optimization
- **Version Control Friendly**: All content is stored in Markdown files, making it easier to track changes

## Upcoming Content: Syncthing Deep Dive

I'm working on an in-depth Syncthing tutorial that will cover:

- **Getting Started**: Installation and initial setup
- **Configuration**: Advanced sync options and best practices
- **Use Cases**: Real-world applications for personal and professional use
- **Troubleshooting**: Common issues and how to resolve them

[Syncthing](https://syncthing.net) has been a game-changer for my workflow, especially for keeping files in sync across multiple devices securely without relying on third-party cloud services.

## The Migration Process: WordPress to Hugo

Migrating from WordPress to Hugo involves several key steps:

1. **Content Export**: Converting WordPress posts to Markdown format
2. **Theme Selection**: Choosing a responsive, SEO-friendly Hugo theme
3. **URL Structure**: Setting up proper redirects to maintain SEO rankings
4. **Deployment**: Moving from PHP/MySQL to static file hosting

## Homelab Upgrades: Better Performance & Networking

### 1U Server Case Upgrade

I've transitioned my Proxmox server into a new 1U rackmount case, which required some careful planning:

- **Cooling Solution**: Installed low-profile Noctua heat sinks to handle the thermal challenges of 1U form factor
- **Cable Management**: Optimized airflow with custom-length cables and proper routing
- **Power Efficiency**: The compact design reduces power consumption while maintaining performance

### Network Infrastructure: HP ProCurve 24-Port Switch

The new HP ProCurve 24-Port 1GB switch brings several advantages:

- **VLAN Support**: Better network segmentation for security and performance
- **Link Aggregation**: Combining multiple ports for higher bandwidth
- **Enterprise Features**: Advanced QoS and traffic monitoring capabilities
- **Reliability**: HP's lifetime warranty ensures long-term value

## Looking Ahead

These upgrades are just the beginning. Future plans include:

- **TP-Link Archer C9 Router Upgrade**: Currently running DD-WRT firmware, with plans for a more powerful solution
- **Storage Expansion**: Adding 4x 500GB hard drives to create a ZFS pool for better data management
- **Backup Strategy**: Implementing a robust solution using [Restic](https://restic.net/) and Backblaze B2
- **Monitoring**: Setting up Grafana and Prometheus for system monitoring
- **Documentation**: Creating detailed guides on the entire migration process

## Final Thoughts

Migrating from WordPress to Hugo and upgrading my homelab infrastructure has been challenging but incredibly rewarding. The performance improvements and reduced maintenance overhead make these changes well worth the effort.

*Have you migrated from WordPress to a static site generator? Or do you have experience with Syncthing in your homelab? I'd love to hear about your experiences in the comments below!*

---
*For more tech insights and homelab updates, consider [subscribing to my YouTube channel](https://www.youtube.com/@computerhacking101) for the latest content and tutorials.*
