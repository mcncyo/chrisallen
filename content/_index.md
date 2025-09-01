---
title: "Home"
date: 2025-08-31
draft: false
description: "Welcome to my personal website where I share my projects, tutorials, and updates on my journey in technology and DIY electronics."
---

# 👋 Welcome to My Digital Space

I'm Chris Allen, a technology enthusiast passionate about DIY electronics, home automation, and sharing knowledge through tutorials and project updates.

## 🚀 Featured Projects

### Zigbee Motion Sensor
Currently developing a custom Zigbee motion sensor with 4-layer PCB design and optimized power management. [Read the latest update](/posts/aug-2025-update)

### Home Server Optimization
Documenting my journey of optimizing my TrueNAS setup with Docker and implementing efficient backup solutions with Backblaze B2.

## 📝 Latest Blog Posts

{{ range first 5 (where .Site.RegularPages "Type" "posts") }}
- [{{ .Title }}]({{ .RelPermalink }}) - {{ .Date.Format "January 2, 2006" }}
{{ end }}

[View all posts →](/posts/)

## 📬 Get in Touch

Have questions or want to collaborate? Feel free to reach out!

[View All Projects](/projects) | [Read More Posts](/posts)